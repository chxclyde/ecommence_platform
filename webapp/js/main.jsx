import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";
import UserIndexPage from "./userindex";
import AdminIndexPage from "./adminindex";
import CartPage from "./cart";
// Create a root
const determineCurrentPage = () => {
    const pageId = document.getElementById('reactEntry').getAttribute('data-page');
    return pageId;
  };
const App = () => {
    
    const currentPage = determineCurrentPage();
  
    return (
      <div>
        {currentPage === 'user' && <UserIndexPage />}
            {currentPage === 'admin' && <AdminIndexPage />}
            {currentPage === 'cart' && <CartPage/> }
      </div>
    );
};
  

  


const root = createRoot(document.getElementById('reactEntry'));
root.render(<App />);
