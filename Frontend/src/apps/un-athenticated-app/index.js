import { Route, Switch, Redirect } from "react-router-dom";
import { LoginPage, SignupPage } from "../../Pages";
import { observer } from "mobx-react";
export const UnAuthenticatedApp = observer(() => {
  return (
    <Switch>
      <Route path="/" exact component={LoginPage} />
      <Route path="/signup" exact component={SignupPage} />
      <Redirect to="/" />
    </Switch>
  );
});
