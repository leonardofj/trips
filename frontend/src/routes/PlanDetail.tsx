import { Box } from "@chakra-ui/react";
import Header from "../components/Header";
import { useParams } from "react-router-dom";

const PlanDetail = () => {
  const { id } = useParams();
  return (
    <div>
      <Header title={"Plan"}></Header>
      <Box p={4} boxSize="sm">
        <p>ID: {id}</p>
      </Box>
    </div>
  );
};

export default PlanDetail;
