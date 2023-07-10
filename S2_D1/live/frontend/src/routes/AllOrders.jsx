import React from "react";
import { Box, Container, Button, Text, Flex, Select } from "@chakra-ui/react";
import axios from "axios";

const AllOrders = () => {
  // display all orders
  // update order status
  const [orders, setOrders] = React.useState([]);

  const handleStatusChange = async (elem, event) => {
    // console.log(elem)
    let obj = { ...elem };
    obj["status"] = event.target.value;
    console.log(obj);
    try {
      let res = await axios.put(
        `${process.env.REACT_APP_BACKEND_URL}/update_order/${elem.id}`,
        {
          ...obj,
        }
      );
      setOrders(res.data)
    } catch (error) {
      console.log(error);
    }
  };

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
            <Box key={elem.id}>
              <Text as="b" fontSize={"lg"}>
                {" "}
                Customer's Name: {elem.customerName}{" "}
              </Text>
              <Box>
                {elem?.orderedItems?.map((el) => {
                  return (
                    <Flex justifyContent={"space-between"} key={el.id}>
                      <Text as="b">Dish : {el.name} </Text>
                      <Text as="b">Price : {el.price} </Text>
                    </Flex>
                  );
                })}
              </Box>
              <Text as="b"> Total Price : {elem.totalPrice} </Text>
              <br />
              <Flex gap="5" alignItems={"center"} mb="3">
                <Text as="b"> Status: </Text>
                <Select
                  onChange={(e) => handleStatusChange(elem, e)}
                  defaultValue={elem.status}
                >
                  <option value="Order Recieved"> Order Recieved</option>
                  <option value="Prepairing">Prepairing</option>
                  <option value="Ready for pickup">Ready for pickup</option>
                  <option value="Delivered">Delivered</option>
                </Select>
              </Flex>
              <hr />
            </Box>
          );
        })}
      </Box>
    </Container>
  );
};

export default AllOrders;
