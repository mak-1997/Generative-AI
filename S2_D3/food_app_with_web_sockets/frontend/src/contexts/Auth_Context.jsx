import React from "react";

export const Auth_context = React.createContext();

export const Auth_context_provider = ({ children }) => {
  const [token, setToken] = React.useState("");
  return (
    <Auth_context.Provider value={{token,setToken}}>
      {children}
    </Auth_context.Provider>
  );
};
