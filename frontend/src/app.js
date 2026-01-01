import { useState } from "react";
import ReviewList from "./ReviewList";
import ReviewDetail from "./ReviewDetail";
import "./styles.css";

function App() {
  const [selectedReview, setSelectedReview] = useState(null);

  return (
    <div className="container">
      <h1>PR Review Dashboard</h1>
      <p className="role">Logged in as Instructor</p>

      {!selectedReview ? (
        <ReviewList onSelect={setSelectedReview} />
      ) : (
        <ReviewDetail
          reviewId={selectedReview}
          onBack={() => setSelectedReview(null)}
        />
      )}
    </div>
  );
}

export default App;
