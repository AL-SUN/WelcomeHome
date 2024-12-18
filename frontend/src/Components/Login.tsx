import React, { useState } from "react";
import { Form, Input, Button, notification } from "antd";
import axios from "axios";
import config from "../config"; // Import the config file

import { useNavigate } from "react-router-dom";

const Login = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const navigate = useNavigate();

  const handleLogin = async (values: any) => {
    setLoading(true);
    try {
      const response = await axios.post(
        `${config.apiUrl}/login`,
        {
          userName: values.userName,
          password: values.password,
        },
        {
          headers: {
            'Content-Type': 'application/json',
          },
          withCredentials: true, // This line is important to send cookies
        }
      );
      notification.success({
        message: "Login Success",
        description: response.data.message,
      });
      navigate("/dashboard");
    } catch (error: any) {
      notification.error({
        message: "Login Failed",
        description:
          error.response?.data?.error || "Invalid username or password",
      });
    }
    setLoading(false);
  };

  return (
    <div style={{ width: 400, margin: "auto", paddingTop: "50px" }}>
      <h2>Login</h2>
      <Form onFinish={handleLogin} layout="vertical">
        <Form.Item
          label="Username"
          name="userName"
          rules={[{ required: true, message: "Please input your username!" }]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          label="Password"
          name="password"
          rules={[{ required: true, message: "Please input your password!" }]}
        >
          <Input.Password />
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit" block loading={loading}>
            Log in
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default Login;
