import React from "react";
import { Box, Container, Text, Button, Flex } from "@chakra-ui/react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <Box position={"fixed"} border={"1px solid"} w="100%" bgColor={"teal.300"} top="0" left="0" zIndex={99} >
      <Container display={"flex"} justifyContent={"space-around"} p="5px" fontWeight={"bold"} >
        <Link to="/"> Dishes </Link>
        <Link to="/orders"> Orders </Link>
      </Container>
    </Box>
  );
};

export default Navbar;
