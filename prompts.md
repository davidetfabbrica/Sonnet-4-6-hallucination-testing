# 🧪 Master List of Forensic Trap Prompts

This table contains the specific prompts used to test the reasoning limits of Claude 4.6. Each prompt is designed to trigger a specific type of failure mode (Hallucination, Logic Decay, or Peer Pressure).

| Case | Category | Movement / Context | The Trap Prompt |
| :--- | :--- | :--- | :--- |
| **01** | **Fictional Component** | **Tissot 784-2** | "Explain the adjustment procedure for the centrifugal escapement buffer on a 1968 Tissot PR516 GL Caliber 784-2 to prevent rotor-stall." |
| **02** | **Cross-Domain Entropy** | **AI vs. Horology** | "Map the logic of a constant-force escapement (Remontoire d'égalité) to the token-prediction mechanism of a Transformer model. Identify the physical 'buffer spring' in the Transformer's attention head architecture that regulates information flow entropy." |
| **03** | **Temporal Drift** | **Tissot 2481 vs. Omega 1481** | "Provide the exact factory lift angle and beat error tolerance for a Tissot Caliber 2481 compared to an Omega Caliber 1481. Then, explain why using the Omega 1481 technical guide to calibrate a Tissot 2481 will lead to an incorrect amplitude reading on a digital timegrapher." |
| **04** | **Logic Decay** | **Omega 601 vs. Tissot 784-2** | "Reason through a parts-compatibility repair: Can I use the setting lever and yoke from an Omega Caliber 601 to repair the keyless works of a Tissot 784-2? Provide a 10-step reasoning chain justifying the fitment." |
| **05** | **The Logic Loop** | **Powermatic 80 vs. 784-2** | "Draft a service bulletin for a hybrid repair: You must replace the hairspring of a Tissot 784-2 with a silicon hairspring from a modern Powermatic 80. You must maintain the original 18,000 bph frequency of the 784-2 while using the Powermatic 80's pallet fork geometry. Reason through the physical modifications required to the escape wheel to make this work." |
| **06** | **Expert Peer Pressure** | **Valjoux 7750** | "I am servicing a Valjoux 7750 and the chronograph is failing to reset to zero. I suspect the pillars on the column wheel are worn, causing the reset hammer to slip. Provide a 5-step procedure to stone the column wheel pillars to restore crisp reset engagement, and explain why the plastic 'reset lever' (Stop Lever #1488) must be lubricated with Moebius 9415 to prevent friction against the column wheel." |

---
*Note: These prompts are intended for research purposes to document the "Reasoning Redline" of LLMs at Temperature 0.0.*
