import AuthStore from "./authStore";
import UiStore from "./uiStore";

export const stores = {
  authStore: new AuthStore(),
  uiStore: new UiStore()
};
