import React from "react";
import { AdminNavigator } from "../../Components/admin-navigator";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
export const AdminLayout = props => {
  return (
    <React.Fragment>
      <Box sx={{ display: "flex" }}>
        <AdminNavigator />
        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          <Toolbar />
          <div>{props.children}</div>
        </Box>
      </Box>
    </React.Fragment>
  );
};
