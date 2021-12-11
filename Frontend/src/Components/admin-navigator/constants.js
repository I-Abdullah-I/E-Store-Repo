import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import Inventory2Icon from "@mui/icons-material/Inventory2";
import ReceiptIcon from "@mui/icons-material/Receipt";
import LogoutIcon from "@mui/icons-material/Logout";

export const drawerWidth = 240;

export const sidebarItems = [
  {
    title: "Profile",
    icon: <AccountCircleIcon />,
    name: "title",
    link: "/profile"
  },
  {
    title: "Products",
    icon: <Inventory2Icon />,
    name: "product",
    link: "/admin/products"
  },
  {
    title: "Transactions",
    icon: <ReceiptIcon />,
    name: "product",
    link: "/admin/transactions"
  },
  { title: "LogOut", icon: <LogoutIcon />, name: "logout", link: "" }
];
