import React from "react";
import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
  Select,
  Button,
  Box,
  Text,
  Input,
} from "@chakra-ui/react";
import axios from "axios";

function AddNewDishModal({ setDishes }) {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [Name, setName] = React.useState("");
  const [Price, setPrice] = React.useState("");
  const [Availability, setAvailability] = React.useState("Yes");

  

  const handleNewDish = async () => {
    try {
      let res = await axios.post(
        `${process.env.REACT_APP_BACKEND_URL}/add_dish`,
        {
          name: Name,
          price: Price,
          availability: Availability,
        }
      );
      setDishes(res.data);
      onClose();
    } catch (error) {
      console.log(error);
    }
  };

//   React.useEffect(() => {
//     setName((prev) => (prev = ""));
//     setPrice((prev) => (prev = 0));
//     setAvailability((prev) => (prev = "Yes"));
//   }, []);

  return (
    <>
      <Button onClick={onOpen} colorScheme="green">
        Add a new dish
      </Button>

      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Add a new dish</ModalHeader>
          <ModalCloseButton />
          <ModalBody display="flex" flexDir={"column"} gap="5">
            <Box>
              <Text as="b">Name : </Text>
              <Input
                type="text"
                value={Name}
                placeholder="Name..."
                onChange={(e) => setName(e.target.value)}
              />
            </Box>
            <Box>
              <Text as="b">Price : </Text>
              <Input
                type="number"
                value={Price}
                placeholder="Price..."
                onChange={(e) => setPrice(e.target.value)}
              />
            </Box>
            <Box>
              <Text as="b">Availability : </Text>
              <Select
                value={Availability}
                onChange={(e) => setAvailability(e.target.value)}
              >
                <option value="Yes">Yes</option>
                <option value="No">No</option>
              </Select>
            </Box>
          </ModalBody>

          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={onClose}>
              Close
            </Button>
            <Button  colorScheme="green" onClick={handleNewDish}>
              Add
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}

export default AddNewDishModal;
