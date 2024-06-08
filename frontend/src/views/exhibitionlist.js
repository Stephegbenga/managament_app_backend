import React, { useState, useEffect } from 'react';
import { get_product, get_product_names } from "../api";
import { convertTimestampToDate } from "../util";
import './ExhibitionList.css';

const ExhibitionList = () => {
  const [products, setProducts] = useState([]);
  const [product_names, setProduct_names] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState('');
  const [filtered_products, setFiltered_products] = useState([]);

  const handleProductChange = (event) => {
    setSelectedProduct(event.target.value);
  };

  useEffect(() => {
    async function load_product_names() {
      let response = await get_product_names();
      if (response) {
        setProduct_names(response.data);
      }
    }

    load_product_names();
  }, []);

  useEffect(() => {
    const filteredProducts = products
    .filter(product => product.name === selectedProduct)
    .map(product => {
      const productNameObj = product_names.find(pn => pn.name === product.name);
      return {
        ...product,
        selling_price: productNameObj ? productNameObj.selling_price : ""
      };
    });
  setFiltered_products(filteredProducts);
  }, [selectedProduct, products, product_names]);

  useEffect(() => {
    async function load_products() {
      let response = await get_product("exhibition");
      if (response) {
        setProducts(response.data);
      }
    }

    load_products();
  }, []);


  const calculateTotals = () => {
    const totalPurchasePrice = filtered_products.reduce((total, product) => total + Number(product.purchase_price), 0);
    const totalSellingPrice = filtered_products.reduce((total, product) => total + Number(product.selling_price), 0);
    const totalSold = filtered_products.length;
    return { totalPurchasePrice, totalSellingPrice, totalSold };
  };

  const get_selling_price = (product_name) => {
    console.log(product_name)
    const product = product_names.find((product) => product.name === product_name);
    console.log(product)
    return product ? product.selling_price : "";
  };


  const { totalPurchasePrice, totalSellingPrice, totalSold } = calculateTotals();

  return (
    <div className="exhibition-list-page">
      <label htmlFor="product-select">Product name</label>
      <select id="product-select" value={selectedProduct} style={{ marginBottom: 20 }} onChange={handleProductChange}>
        <option value="" disabled>Select product</option>
        {product_names.map((product, index) => (
          <option key={index} value={product.name}>{product.name}</option>
        ))}
      </select>

      <h1>Exhibition list</h1>
      <table className="product-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Product number</th>
            <th>Registration date</th>
            <th>Sold date</th>
            <th>Purchase price</th>
            <th>Selling price</th>
            <th>Sold</th>
          </tr>
        </thead>
        <tbody>
          {filtered_products.map(product => (
            <tr key={product.product_no} className={product.sold ? 'sold' : ''}>
              <td>{product.name}</td>
              <td>{product.product_no}</td>
              <td>{convertTimestampToDate(product.registration_date)}</td>
              <td>{product.soldDate ? convertTimestampToDate(product.soldDate) : ''}</td>
              <td>{product.purchase_price}</td>
              <td>{get_selling_price(product.name)}</td>
              <td>
              1
              </td>
            </tr>
          ))}
        </tbody>
        <tfoot>
          <tr>
            <td colSpan="4">Total</td>
            <td>{totalPurchasePrice}</td>
            <td>{isNaN(totalSellingPrice) ? '' : totalSellingPrice}</td>
            <td>{totalSold}</td>
          </tr>
        </tfoot>
      </table>
    </div>
  );
};

export default ExhibitionList;
