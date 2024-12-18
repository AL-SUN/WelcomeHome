import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom"; 
import { Button, Divider } from "antd";

import CustomLayout from "./Components/Layout/CustomLayout"; 

import Login from "./Components/Login";
import Register from "./Components/Register";
import FindItemLocations from "./Components/FindItem";
import Dashboard from "./Components/Dashboard";
import FindOrderItems from "./Components/FindOrder";
import RankSystem from "./Components/Rank";
import DonationForm from "./Components/DonationForm";
import StartOrder from "./Components/StartOrder";
import ShopPage from "./Components/ShopPage";


import ProtectedRoute from "./Components/Routes/ProtectedRoute";
import RoleRoute from "./Components/Routes/RoleRoute";

import axios from "axios";

import OrderManagement from "./Components/OrderStatus";
import OrderUpdate from "./Components/OrderUpdate";
import UserOrders from "./Components/Orders";


const App = () => {
  axios.defaults.withCredentials = true; // Send cookies with every request

  return (
    <BrowserRouter>
      <CustomLayout>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />



          <Route path="/findItem" element={<ProtectedRoute element={<FindItemLocations />} />} />
          <Route path="/findOrder" element={<ProtectedRoute element={<FindOrderItems />} />} />
          <Route path="/donateForm" element={<ProtectedRoute element={<RoleRoute element={<DonationForm />} requiredRoles={["staff"]} />} />} />
          <Route path="/startOrder" element={<ProtectedRoute element={<RoleRoute element={<StartOrder />} requiredRoles={["staff"]} />} />} />
          <Route path="/shop/:orderId" element={<ProtectedRoute element={<RoleRoute element={<ShopPage />} requiredRoles={["staff"]} />} />} />
          <Route path="/dashboard" element={<ProtectedRoute element={<Dashboard />} />} />
          <Route path="/rankSystem" element={<ProtectedRoute element={<RankSystem />} />} />
          {/* <Route path="/prepareOrder" element={<ProtectedRoute element={<OrderUpdate />} />} /> */}
          <Route path="/prepareOrder" element={<ProtectedRoute element={<RoleRoute element={<OrderUpdate />} requiredRoles={["staff","volunteer"]} />} />} />
          <Route path="/userTasks" element={<ProtectedRoute element={<UserOrders />} />} />
          <Route path="/OrderUpdate" element={<ProtectedRoute element={<RoleRoute element={<OrderManagement />} requiredRoles={["staff","volunteer"]} />} />} />
          
          <Route
            path="/"
            element={
              <div style={{ width: 400, margin: "auto", paddingTop: "50px" }}>
                <h2>Welcome</h2>
                <Button type="primary" block href="/login">
                  Login
                </Button>
                <Divider>Or</Divider>
                <Button type="primary" block href="/register">
                  Register
                </Button>
              </div>
            }
          />
        </Routes>
      </CustomLayout>
    </BrowserRouter>
  );
};

export default App;
