import { useEffect, useState } from "react";
import api from "./api";

export default function ReviewList({ onSelect }) {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    api.get("/reviews").then((res) => setReviews(res.data));
  }, []);

  return (
    <div className="card">
      <h2>Pull Request Reviews</h2>

      {reviews.length === 0 && <p>No reviews available</p>}

      {reviews.map((review) => (
        <div
          key={review.id}
          className="review-item"
          onClick={() => onSelect(review.id)}
        >
          <div>
            <strong>{review.pr_title}</strong>
            <p className="branch">{review.branch}</p>
          </div>
          <span className={`status ${review.status.toLowerCase()}`}>
            {review.status}
          </span>
        </div>
      ))}
    </div>
  );
}
