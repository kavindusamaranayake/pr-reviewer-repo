import { useEffect, useState } from "react";
import api from "./api";

export default function ReviewDetail({ reviewId, onBack }) {
  const [review, setReview] = useState(null);

  useEffect(() => {
    api.get(`/reviews/${reviewId}`).then((res) => setReview(res.data));
  }, [reviewId]);

  if (!review) return <p>Loading...</p>;

  const checks = review.review_data.checks;

  const updateStatus = (status) => {
    api.post(`/reviews/${reviewId}/${status}`).then(() => {
      setReview({ ...review, status: status.toUpperCase() });
    });
  };

  return (
    <div className="card">
      <button className="back" onClick={onBack}>
        ← Back
      </button>

      <h2>{review.pr_title}</h2>
      <p className="branch">Branch: {review.branch}</p>
      <p>
        <strong>Reviewer:</strong> Automated System
      </p>
      <p>
        <strong>Instructor:</strong> You
      </p>

      <h3>Rule Checks</h3>

      <table>
        <thead>
          <tr>
            <th>Rule</th>
            <th>Result</th>
          </tr>
        </thead>
        <tbody>
          {checks.map((c, index) => (
            <tr key={index}>
              <td>{c.rule}</td>
              <td className={c.result === "PASS" ? "pass" : "fail"}>
                {c.result}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="actions">
        <button className="approve" onClick={() => updateStatus("approve")}>
          Approve Review
        </button>
        <button className="reject" onClick={() => updateStatus("reject")}>
          Reject Review
        </button>
      </div>
    </div>
  );
}
