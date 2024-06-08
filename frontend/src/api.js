import {message as toast} from "antd";
import {base_url} from "./config"


const upload_file = async (files) => {
  const formData = new FormData();
  Array.from(files).forEach(file => {
    formData.append("files", file);
  });

  try {
    const response = await fetch(base_url + "/upload", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorResponse = await response.json();
      const errorMessage = errorResponse.message;
      toast.error(errorMessage);
      return;
    }

    const result = await response.json();
    return result;
  } catch (error) {
    toast.error(error.message);
  }
};





const get_product_names = async () => {
    try {
      const response = await fetch(`${base_url}/product_name`, {
        method: "get",
        headers: {
          "Content-Type": "application/json",
        },
      });
  
      if (!response.ok) {
        const errorResponse = await response.json();
        const errorMessage = errorResponse.message;
        toast.error(errorMessage);
        return
      }
  
      const result = await response.json();
      return result;
    } catch (error) {
      toast.error(error.message);
      return null;
    }
  };


  const save_new_product_name = async (product_name) => {
    try {
      const response = await fetch(`${base_url}/product_name`, {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({name: product_name}),
      });
  
      if (!response.ok) {
        const errorResponse = await response.json();
        const errorMessage = errorResponse.message;
        toast.error(errorMessage);
        return 
      }
  
      const result = await response.json();
      return result;
    } catch (error) {
      toast.error(error.message);
      return null;
    }
  }


  const save_new_product = async (data) => {
    try {
      const response = await fetch(`${base_url}/product`, {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: data,
      });
  
      if (!response.ok) {
        const errorResponse = await response.json();
        const errorMessage = errorResponse.message;
        toast.error(errorMessage);
        return 
      }
  
      const result = await response.json();
      return result;
    } catch (error) {
      toast.error(error.message);
      return null;
    }
  }


  const get_product = async (type) => {
    try {
      const response = await fetch(`${base_url}/product?type=${type}`, {
        method: "get",
        headers: {
          "Content-Type": "application/json",
        },
      });
  
      if (!response.ok) {
        const errorResponse = await response.json();
        const errorMessage = errorResponse.message;
        toast.error(errorMessage);
        return 
      }
  
      const result = await response.json();
      return result;
    } catch (error) {
      toast.error(error.message);
      return null;
    }
  }
  

  



export {upload_file, get_product_names, save_new_product_name, save_new_product, get_product};
