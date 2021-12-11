import * as React from "react";
import {
  Avatar,
  Button,
  CssBaseline,
  TextField,
  Link,
  Box,
  Grid,
  FormControlLabel,
  Typography,
  Container,
  Radio,
  RadioGroup
} from "@mui/material";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
// import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { useStores } from "../../hooks/useStores";
import { observer } from "mobx-react";

function Copyright(props) {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      {"Copyright © "}
      <span color="inherit">Disturbuted System Team 2021</span>
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

const theme = createTheme();

export const SignupPage = observer(() => {
  const { authStore } = useStores();
  const { signUp } = authStore;

  const handleSubmit = event => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const formData = {
      full_name: data.get("full-name"),
      email: data.get("email"),
      password: data.get("password"),
      type: data.get("radio-buttons-group")
    };
    signUp(formData);
    console.log("formData", formData);
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center"
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          <Box
            component="form"
            noValidate
            onSubmit={handleSubmit}
            sx={{ mt: 3 }}
          >
            <Grid container spacing={2}>
              <Grid item xs={12} sm={12}>
                <TextField
                  autoComplete="given-name"
                  name="full-name"
                  required
                  fullWidth
                  id="full-name"
                  label="Full Name"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                />
              </Grid>
              <Grid item xs={12}>
                <Typography component="h1" variant="h6">
                  Acccount Type
                </Typography>
                <RadioGroup
                  row
                  aria-label="user_type"
                  defaultValue="E"
                  name="radio-buttons-group"
                >
                  <FormControlLabel
                    value="E"
                    control={<Radio />}
                    label="Customer"
                  />
                  <FormControlLabel
                    value="V"
                    control={<Radio />}
                    label="Vendor"
                  />
                </RadioGroup>
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign Up
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link href="login" variant="body2">
                  Already have an account? Sign in
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
    </ThemeProvider>
  );
});
