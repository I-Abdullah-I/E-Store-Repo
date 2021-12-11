import React from "react";
import { MarketNavigator } from "../../Components/market-navigator";

export const MarketLayout = props => {
  return (
    <React.Fragment>
      <MarketNavigator />
      <main>{props.children}</main>
    </React.Fragment>
  );
};
