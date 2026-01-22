class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        max_energy = float("-inf")

        for i in range(n-1, -1, -1):
            if i+k < n:
                energy[i] += energy[i+k]
            max_energy = energy[i] if energy[i] > max_energy else max_energy               
        return max_energy