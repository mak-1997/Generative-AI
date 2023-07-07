import React from "react";
import {
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
  Box,
  Container,
  Text,
  Button,
  Modal,
} from "@chakra-ui/react";
import axios from "axios";
import InputModal from "./InputModal";
const Home = () => {
  const [students, setStudents] = React.useState([]);

  const getData = async () => {
    try {
      let res = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/read`);
      console.log(res.data);
      setStudents(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  const handleDelete = async (id) => {
    try {
      let res = await axios.delete(
        `${process.env.REACT_APP_BACKEND_URL}/delete/${id}`
      );
      console.log(res.data);
      setStudents(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  React.useEffect(() => {
    getData();
  }, []);
  return (
    <Box>
      <Container>
        <Text as="b" fontSize={"5xl"}>
          Student Details
        </Text>
      </Container>
      <InputModal text="Add New Student" setStudents={setStudents} />
      <TableContainer>
        <Table variant="striped" colorScheme="teal">
          <Thead>
            <Tr>
              <Th>Name</Th>
              <Th>Email</Th>
              <Th isNumeric>Age</Th>
              <Th>Course</Th>
              <Th>Edit</Th>
              <Th>Course</Th>
            </Tr>
          </Thead>
          <Tbody>
            {students?.map((elem) => {
              return (
                <Tr key={elem.id}>
                  <Td>{elem.name}</Td>
                  <Td>{elem.email}</Td>
                  <Td isNumeric>{elem.age}</Td>
                  <Td>{elem.course}</Td>
                  <Td>
                    {" "}
                    <InputModal
                      text="Edit"
                      name={elem.name}
                      email={elem.email}
                      age={elem.age}
                      course={elem.course}
                      id={elem.id}
                      setStudents={setStudents}
                    />
                  </Td>
                  <Td>
                    {" "}
                    <Button onClick={() => handleDelete(elem.id)}>
                      {" "}
                      Delete{" "}
                    </Button>{" "}
                  </Td>
                </Tr>
              );
            })}
          </Tbody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default Home;
