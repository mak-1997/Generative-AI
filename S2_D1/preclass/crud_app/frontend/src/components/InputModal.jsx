import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
  Button,
  Input,
} from "@chakra-ui/react";
import axios from "axios";
import React from "react";

function InputModal({
  text,
  name = "",
  email = "",
  age = "",
  course = "",
  id = "",
  setStudents,
}) {
  const { isOpen, onOpen, onClose } = useDisclosure();

  const [Name, setName] = React.useState("");
  const [Email, setEmail] = React.useState("");
  const [Age, setAge] = React.useState(0);
  const [Course, setCourse] = React.useState("");

  const handleAdd = async () => {
    let res = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/create`, {
      name: Name,
      email: Email,
      age: Age,
      course: Course,
    });
    console.log(res.data);
    setStudents(res.data);
    handleClose()
  };
  const handleEdit = async (id) => {
    let res = await axios.put(`${process.env.REACT_APP_BACKEND_URL}/update/${id}`, {
      name: Name,
      email: Email,
      age: Age,
      course: Course,
    });
    console.log(res.data);
    setStudents(res.data);
    handleClose()
  };

  React.useEffect(() => {
    setName((prev) => (prev = name));
    setEmail((prev) => (prev = email));
    setAge((prev) => (prev = age));
    setCourse((prev) => (prev = course));
  }, []);

  const handleClose = () => {
    setName((prev) => (prev = ""));
    setEmail((prev) => (prev = ""));
    setAge((prev) => (prev = ""));
    setCourse((prev) => (prev = ""));

    onClose();
  };

  // React.useEffect(() => {}, [onclose]);

  return (
    <>
      <Button onClick={onOpen}>{text}</Button>

      <Modal isOpen={isOpen} onClose={handleClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Enter Student Details</ModalHeader>
          <ModalCloseButton />
          <ModalBody display={"flex"} flexDir={"column"} gap="5">
            <Input
              type="text"
              placeholder="Name..."
              value={Name}
              onChange={(e) => setName(e.target.value)}
            />
            <Input
              type="email"
              placeholder="Email..."
              value={Email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <Input
              type="number"
              placeholder="Age..."
              value={Age}
              onChange={(e) => setAge(e.target.value)}
            />
            <Input
              type="text"
              placeholder="Course..."
              value={Course}
              onChange={(e) => setCourse(e.target.value)}
            />
          </ModalBody>

          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={handleClose}>
              Close
            </Button>
            <Button
              variant="ghost"
              onClick={text === "Edit" ? ()=>handleEdit(id) : handleAdd}
            >
              Submit
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}

export default InputModal;
