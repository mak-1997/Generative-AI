import React from "react";
import { Box, Container, Button, Text, Flex } from "@chakra-ui/react";
import axios from "axios";

const AllOrders = () => {
  // display all orders
  // update order status
  const [orders, setOrders] = React.useState([]);

  const getOrders = async () => {
    try {
      let res = await axios.get(
        `${process.env.REACT_APP_BACKEND_URL}/get_orders`
      );
      console.log(res.data);
      setOrders(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  React.useEffect(() => {
    getOrders();
  }, []);

  return (
    <Container>
      <Text as="b" fontSize={"3xl"}>
        {" "}
        All Orders{" "}
      </Text>
      <Box>
        {orders?.map((elem) => {
          return (
            <Box>
              <Text as="b" fontSize={"lg"}>
                {" "}
                Customer's Name: {elem.customerName}{" "}
              </Text>
              <Box>
                {elem?.orderedItems?.map((el) => {
                  return (
                    <Flex justifyContent={"space-between"} >
                      <Text as="b" >Dish :  {el.name} </Text>
                      <Text as="b">Price : {el.price} </Text>
                    </Flex>
                  );
                })}
              </Box>
              <hr />
            </Box>
          );
        })}
      </Box>
    </Container>
  );
};

export default AllOrders;
