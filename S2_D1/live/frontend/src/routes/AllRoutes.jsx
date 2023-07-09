import React from 'react'
import {Routes, Route} from 'react-router-dom';
import AllOrders from './AllOrders';
import Dishes from './Dishes';
const AllRoutes = () => {
  return (
    <div>
        <Routes>
            <Route path="/" element={<Dishes />}  />
            <Route path="/orders" element={<AllOrders />}  />
            
        </Routes>
      
    </div>
  )
}

export default AllRoutes
