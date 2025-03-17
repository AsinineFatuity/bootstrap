APP_TSX_CONTENT = """
import React from "react";
import { Route, Routes, BrowserRouter, Navigate } from "react-router-dom";
import Home from "./src/pages/home";
import { APP_URLS } from "./helpers/utils";

function App() {
  return (
      <BrowserRouter>
        <Routes>
          <Route path={APP_URLS.home} element={<Home />} />
          <Route path="*" element={<Navigate to={APP_URLS.home} />} />
        </Routes>
      </BrowserRouter>
  );
}
export default App;
"""

INDEX_TSX_CONTENT = """
import App from "./App";
import { LoadingIndicator, FeedbackToast } from "./components";
import reduxStore from "./redux/store";

const rootElement = document.getElementById("root");

if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <React.StrictMode>
      <Provider store={reduxStore}>
        <LoadingIndicator />
        <App />
        <ToastContainer newestOnTop={true} />
        <FeedbackToast />
      </Provider>
    </React.StrictMode>,
  );
}
"""
