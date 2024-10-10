SELECT department, COUNT(*) AS patient_count
FROM appointments
WHERE appointment_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY department
ORDER BY patient_count DESC;
