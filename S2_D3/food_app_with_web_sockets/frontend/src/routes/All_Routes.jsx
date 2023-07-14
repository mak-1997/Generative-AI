import React from 'react'
import {Routes, Route} from 'react-router-dom'
import Dishes from './Dishes'
import User_Login from './User_Login'
import User_Signup from './User_Signup'
import Admin_Login from './Admin_Login'
import Admin_Signup from './Admin_Signup'
import My_Orders from './My_Orders'
import All_Orders from './All_Orders'

const All_Routes = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Dishes />}  />
        <Route path="/user/login" element={<User_Login />}  />
        <Route path="/user/signup" element={<User_Signup />}  />
        <Route path="/user/orders" element={<My_Orders />}  />
        <Route path="/admin/login" element={<Admin_Login />}  />
        <Route path="/admin/signup" element={<Admin_Signup />}  />
        <Route path="/admin/orders" element={<All_Orders />}  />
      </Routes>
    </div>
  )
}

export default All_Routes
