import {
  Box,
  Center,
  useColorModeValue,
  Heading,
  Text,
  Stack,
  Image,
  Button,
} from "@chakra-ui/react";
import axios from "axios";
import DishEditModal from "./EditDishModal";

const IMAGE =
  "https://www.gousto.co.uk/build/141790/856bca25c1c2cbaf608d598f844c1a05.jpg";

export default function Card({
  name,
  price,
  availability,
  id,
  setDishes,
  setOrderedDishes,
}) {
  const handleDelete = async (id) => {
    try {
      let res = await axios.delete(
        `${process.env.REACT_APP_BACKEND_URL}/remove_dish/${id}`
      );
      setDishes(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  const handleOrder = () => {
    let obj = {
      name,
      price,
      id,
      availability,
    };
    setOrderedDishes(prev => [...prev, obj]);
  };

  return (
    <Center py={12}>
      <Box
        role={"group"}
        p={6}
        maxW={"330px"}
        w={"full"}
        bg={useColorModeValue("white", "gray.800")}
        boxShadow={"2xl"}
        rounded={"lg"}
        pos={"relative"}
        zIndex={1}
      >
        <Box
          rounded={"lg"}
          mt={-12}
          pos={"relative"}
          height={"230px"}
          _after={{
            transition: "all .3s ease",
            content: '""',
            w: "full",
            h: "full",
            pos: "absolute",
            top: 5,
            left: 0,
            backgroundImage: `url(${IMAGE})`,
            filter: "blur(15px)",
            zIndex: -1,
          }}
          _groupHover={{
            _after: {
              filter: "blur(20px)",
            },
          }}
        >
          <Image
            rounded={"lg"}
            height={230}
            width={282}
            objectFit={"cover"}
            src={IMAGE}
          />
        </Box>
        <Stack pt={10} align={"center"}>
          <Text color={"gray.500"} fontSize={"sm"} textTransform={"uppercase"}>
            Heaven's Kitchen
          </Text>
          <Heading fontSize={"2xl"} fontFamily={"body"} fontWeight={500}>
            {name}
          </Heading>
          <Stack direction={"row"} align={"center"}>
            <Text fontWeight={800} fontSize={"xl"}>
              ₹{price}
            </Text>
          </Stack>
          <Stack direction={"row"} align={"center"}>
            <Button
              isDisabled={availability === "Yes" ? false : true}
              colorScheme="blue"
              onClick={() => handleOrder()}
            >
              Order
            </Button>
            <DishEditModal
              name={name}
              price={price}
              availability={availability}
              id={id}
              setDishes={setDishes}
            />
            <Button onClick={() => handleDelete(id)} colorScheme="red">
              Delete
            </Button>
          </Stack>
        </Stack>
      </Box>
    </Center>
  );
}
