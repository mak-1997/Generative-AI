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

function DishEditModal({ name, price, availability, id, setDishes }) {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [Name, setName] = React.useState("");
  const [Price, setPrice] = React.useState(0);
  const [Availability, setAvailability] = React.useState("");

  const handleEdit = async () => {
    try {
      let res = await axios.put(
        `${process.env.REACT_APP_BACKEND_URL}/update_dish/${id}`,
        {
          name: Name,
          price: Price,
          availability: Availability,
          id: id,
        }
      );
      setDishes(res.data);
      onClose();
    } catch (error) {
      console.log(error);
    }
  };

  React.useEffect(() => {
    setName((prev) => (prev = name));
    setPrice((prev) => (prev = price));
    setAvailability((prev) => (prev = availability));
  }, []);

  return (
    <>
      <Button onClick={onOpen} colorScheme="green">
        Edit
      </Button>

      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Edit Dish Details</ModalHeader>
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
            <Button variant="ghost" colorScheme="green" onClick={handleEdit}>
              Update
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}

export default DishEditModal;
