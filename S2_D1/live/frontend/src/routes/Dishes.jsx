import React from "react";
import axios from "axios";
import Card from "../components/Card";
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

const Dishes = () => {
  // Display all dishes
  // Add new Dish
  // Update Dish
  // Delete Dish
  // Take Order

  const [dishes, setDishes] = React.useState([]);
  const [customerName, setCustomerName] = React.useState("");
  const [orderedDishes, setOrderedDishes] = React.useState([]);
  const [totalPrice, setTotalPrice] = React.useState(0);

  const getData = async () => {
    try {
      let res = await axios.get(
        `${process.env.REACT_APP_BACKEND_URL}/get_dishes`
      );
      // console.log(res.data);
      setDishes(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  const placeOrder = async () => {
    if (customerName === "") {
      alert("Customer's Name required !!");
      return;
    }
    try {
      let res = await axios.post(
        `${process.env.REACT_APP_BACKEND_URL}/add_order`,
        {
          customerName,
          orderedItems: orderedDishes,
          totalPrice,
        }
      );
      console.log(res.data);
      alert("order placed.");
      setOrderedDishes([])
      setCustomerName("")
      setTotalPrice(0)
    } catch (error) {
      console.log(error);
    }
  };

  const handleOrderDelete = (id) => {
    const neworder = orderedDishes.filter((elem) => elem.id !== id);
    console.log(neworder);
    setOrderedDishes(neworder);
  };

  const calculateTotal = () => {
    let total = orderedDishes.reduce((sum, elem) => sum + +elem.price, 0);
    console.log(total);
    setTotalPrice(total);
  };

  React.useEffect(() => {
    getData();
  }, []);

  React.useEffect(() => {
    calculateTotal();
  }, [orderedDishes]);

  return (
    <Container
      marginTop={"2rem"}
      display={"flex"}
      maxW={"100%"}
      justifyContent={"space-between"}
    >
      <Box
        width={"70%"}
        display={"grid"}
        gridTemplateColumns={"repeat(3, 1fr)"}
        columnGap={"5"}
        padding={"10px"}
      >
        {dishes?.map((elem) => {
          return (
            <Card
              setDishes={setDishes}
              name={elem.name}
              price={elem.price}
              availability={elem.availability}
              key={elem.id}
              id={elem.id}
              setOrderedDishes={setOrderedDishes}
            />
          );
        })}
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
        <Text as="b">Customer's name :</Text>
        <Input
          required
          variant="filled"
          value={customerName}
          onChange={(e) => setCustomerName(e.target.value)}
        />
        <Button alignSelf={"end"} onClick={placeOrder}>
          {" "}
          Place order{" "}
        </Button>

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
                {orderedDishes.map((elem) => {
                  return (
                    <Tr fontWeight={"bold"} key={elem.id}>
                      <Td>{elem.name}</Td>
                      <Td isNumeric>{elem.price}</Td>
                      <Td display={"flex"} justifyContent={"center"}>
                        {" "}
                        <Button
                          colorScheme="red"
                          size="sm"
                          onClick={() => handleOrderDelete(elem.id)}
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
      </Box>
    </Container>
  );
};

export default Dishes;
