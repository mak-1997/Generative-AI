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

const IMAGE =
  "https://images.unsplash.com/photo-1615719413546-198b25453f85?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Zm9vZCUyMGRlbGl2ZXJ5fGVufDB8fDB8fHww&w=1000&q=80";

export default function Card({
  dish_name,
  dish_price,
  dish_availability,
  _id,
  setDishes,
  setOrderedDishes,
}) {

  const handleOrder = () => {
    let obj = {
      dish_name,
      dish_price,
      _id,
      dish_availability,
    };
    setOrderedDishes(prev => [...prev, obj]);
  };

  return (
    <Center py={12}  >
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
            {dish_name}
          </Heading>
          <Stack direction={"row"} align={"center"}>
            <Text fontWeight={800} fontSize={"xl"}>
              ₹{dish_price}
            </Text>
          </Stack>
          <Stack direction={"row"} align={"center"}>
            <Button
              isDisabled={dish_availability === true ? false : true}
              colorScheme="blue"
              onClick={() => handleOrder()}
            >
              Add To Order
            </Button>
           
          </Stack>
        </Stack>
      </Box>
    </Center>
  );
}
