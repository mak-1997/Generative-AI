import React from "react";
import { Auth_context } from "../contexts/Auth_Context";
import axios from "axios";
import {
  Box,
  Container,
  Text,
  Input,
  Button,
  Flex,
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
} from "@chakra-ui/react";
import Card from "../components/Card";

const Dishes = () => {
  const url = process.env.REACT_APP_BACKEND_URL;
  const { token, setToken } = React.useContext(Auth_context);

  const [dishes, setDishes] = React.useState([]);
  const [customerName, setCustomerName] = React.useState("");
  const [orderedDishes, setOrderedDishes] = React.useState([]);
  const [totalPrice, setTotalPrice] = React.useState(0);

  const get_data = async () => {
    try {
      const res = await axios.get(`${url}/dishes`);
      console.log(res.data);
      setDishes(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  const get_dish_ids = () => {
    const dish_ids = orderedDishes?.map((elem) => elem._id);
    return dish_ids;
  };

  const placeOrder = async () => {
    if (token === "") {
      alert("Login required !!");
      return;
    }
    try {
      let res = await axios.post(
        `${process.env.REACT_APP_BACKEND_URL}/orders`,
        {
          dish_ids: get_dish_ids(),
        },
        {
          headers: {
            Authorization: token,
          },
        }
      );
      console.log(res.data);
      alert("Order placed.");
      setOrderedDishes([]);
      setCustomerName("");
      setTotalPrice(0);
    } catch (error) {
      console.log(error);
    }
  };
  
  const handleOrderDelete = (id) => {
    const neworder = orderedDishes.filter((elem) => elem._id !== id);
    console.log(neworder);
    setOrderedDishes(neworder);
  };

  React.useEffect(() => {
    get_data();
  }, []);

  return (
    <Container
      marginTop={"2rem"}
      display={"flex"}
      maxW={"100%"}
      justifyContent={"space-between"}
    >
      <Box width={"70%"} paddingTop={"1rem"}>
        <Box
          display={"grid"}
          gridTemplateColumns={"repeat(3, 1fr)"}
          columnGap={"5"}
          padding={"10px"}
        >
          {dishes?.map((elem) => {
            return (
              <Card
                setDishes={setDishes}
                dish_name={elem.dish_name}
                dish_price={elem.dish_price}
                dish_availability={elem.dish_availability}
                key={elem._id["$oid"]}
                _id={elem._id}
                setOrderedDishes={setOrderedDishes}
              />
            );
          })}
        </Box>
      </Box>
      <Box
        // w="25%"
        textAlign={"left"}
        padding={"10px"}
        display={"flex"}
        flexDir={"column"}
        gap="2"
        position={"fixed"}
        right={0}
        height={"100vh"}
        borderLeft={"2px solid"}
      >
        <Text as="b">Your Orders :</Text>

        <Text as="b">Total Items : {orderedDishes.length}</Text>
        <Text as="b">Order total : {totalPrice}</Text>
        <Box>
          <TableContainer>
            <Table variant="striped" colorScheme="teal">
              <Thead>
                <Tr>
                  <Th>Name</Th>
                  <Th isNumeric>Price</Th>
                  <Th>Remove</Th>
                </Tr>
              </Thead>
              <Tbody>
                {orderedDishes?.map((elem) => {
                  return (
                    <Tr fontWeight={"bold"} key={elem._id["$oid"]}>
                      <Td>{elem.dish_name}</Td>
                      <Td isNumeric>{elem.dish_price}</Td>
                      <Td display={"flex"} justifyContent={"center"}>
                        {" "}
                        <Button
                          colorScheme="red"
                          size="sm"
                          onClick={() => handleOrderDelete(elem._id)}
                        >
                          x
                        </Button>{" "}
                      </Td>
                    </Tr>
                  );
                })}
              </Tbody>
            </Table>
          </TableContainer>
        </Box>
        <Button alignSelf={"end"} onClick={placeOrder} colorScheme="blue">
          {" "}
          Place order{" "}
        </Button>
      </Box>
    </Container>
  );
};

export default Dishes;
