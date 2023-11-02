function rotate(matrix, direction) {
  const numCols = matrix[0].length;

  if (direction === 'clockwise') {
    return Array.from({ length: numCols }, (_, i) =>
      matrix.map(row => row[i]).reverse()
    );
  } else if (direction === 'counter-clockwise') {
    return Array.from({ length: numCols }, (_, i) =>
      matrix.map(row => row[numCols - 1 - i])
    );
  }
}

module.exports = rotate