import "./CustomizedButton.css";
import { Button } from "@material-ui/core";
export default function CustomizedButton({
  customStyle,
  onClick,
  children,
  className
}) {
  return (
    <button
      className={`basic-button ${
        customStyle ? customStyle : "main-primary"
      } ${className}`}
      onClick={onClick ? onClick : () => console.log(children, "clicked")}
    >
      {children}
    </button>
  );
}
