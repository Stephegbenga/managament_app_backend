import React from "react";
import { Spin } from "antd";
import { LoadingOutlined } from "@ant-design/icons";

const antIcon = <LoadingOutlined style={{ fontSize: 24 }} spin />;

const Loading = ({ type = "default", size = "large", isVisible = false, message = "" }) => {
  if (!isVisible) {
    return null;
  }

  return (
    <div
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        width: "100%",
        height: "100%",
        backgroundColor: "rgba(0, 0, 0, 0.7)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        zIndex: 9999,
        color: "#fff",
        fontSize: "16px",
      }}
    >
      {type === "circle" ? (
        <Spin indicator={antIcon} size={size} />
      ) : (
        <Spin size={size} />
      )}
      {message && (
        <div
          style={{
            marginTop: "20px",
            textAlign: "center",
            fontSize: "18px",
          }}
        >
          {message}
        </div>
      )}
    </div>
  );
};

export default Loading;
