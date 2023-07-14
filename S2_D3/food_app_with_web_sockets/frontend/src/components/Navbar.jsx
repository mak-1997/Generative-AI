import React from "react";
import { Link } from "react-router-dom";
import { Box, Container, Text, Button, Flex } from "@chakra-ui/react";
const Navbar = () => {
  return (
    <Flex
      w="100%"
      position={"fixed"}
      border={"1px solid"}
      zIndex={9}
      justify={"space-around"}
      fontWeight={"bold"}
      padding={"5px"}
      top={0}
    >
      <Link to="/">Home</Link>
      <Link to="/user/login">Login </Link>
      <Link to="/user/signup">Signup </Link>
      <Link to="/user/orders">My Orders</Link>
      <Link to="/admin/login">Admin Login</Link>
      <Link to="/admin/orders">All orders</Link>
    </Flex>
  );
};

export default Navbar;
