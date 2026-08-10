class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for value in operations:
            if value == "+":
                record.append(record[-1] + record[-2])
            elif value == "D":
                record.append(record[-1]*2)
            elif value == "C":
                if record:
                    record.pop()
            else:
                record.append(int(value))

        return sum(record)

        