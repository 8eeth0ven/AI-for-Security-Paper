# Paper Tag Taxonomy and Index

Multi-axis tags for all papers in this repository. Tags were assigned per paper from title+abstract; see the Tags column in the master table.

## Tag Taxonomy (Four Axes)

| Axis | Tag (EN) | Tag (ZH) |
|---|---|---|
| 方法 | multi-agent | 多智能体 |
| 方法 | single-agent pipeline | 单Agent流水线 |
| 方法 | fine-tuning / training | 微调训练 |
| 方法 | RAG / knowledge base | RAG知识库 |
| 方法 | neuro-symbolic (LLM + program analysis) | 神经符号 |
| 方法 | prompting-only | 纯提示 |
| 方法 | benchmark / dataset | 基准数据集 |
| 方法 | empirical study / survey | 实证研究 |
| 任务 | detection | 检测 |
| 任务 | localization | 定位 |
| 任务 | repair | 修复 |
| 任务 | fuzzing | 模糊测试 |
| 任务 | exploit / PoC verification | 利用验证 |
| 任务 | audit / code review | 审计评审 |
| 任务 | evaluation | 评测 |
| 对象 | C/C++ | C/C++ |
| 对象 | Java | Java |
| 对象 | Python | Python |
| 对象 | JavaScript / TypeScript | JS/TS |
| 对象 | Go / Rust | Go/Rust |
| 对象 | smart contracts / EVM | 智能合约 |
| 对象 | binary / firmware | 二进制固件 |
| 对象 | web | Web |
| 对象 | mobile / Android | 移动端 |
| 对象 | package ecosystem | 包生态 |
| 对象 | cross-language | 跨语言 |
| 证据 | real CVEs | 真实CVE |
| 证据 | real disclosure / maintainer-confirmed | 真实披露 |
| 证据 | wild / production data | 真实生态数据 |
| 证据 | synthetic / self-built | 合成自建 |
| 证据 | open artifacts | 开源工件 |

## Tag Distribution

| Tag | Papers |
|---|---:|
| detection | 366 |
| empirical study / survey | 216 |
| wild / production data | 194 |
| evaluation | 180 |
| neuro-symbolic (LLM + program analysis) | 152 |
| synthetic / self-built | 140 |
| real CVEs | 140 |
| fine-tuning / training | 132 |
| benchmark / dataset | 116 |
| single-agent pipeline | 96 |
| exploit / PoC verification | 84 |
| repair | 83 |
| open artifacts | 80 |
| multi-agent | 78 |
| prompting-only | 78 |
| smart contracts / EVM | 74 |
| RAG / knowledge base | 67 |
| cross-language | 67 |
| audit / code review | 65 |
| binary / firmware | 58 |
| C/C++ | 53 |
| fuzzing | 50 |
| real disclosure / maintainer-confirmed | 42 |
| package ecosystem | 33 |
| Python | 30 |
| localization | 30 |
| Java | 24 |
| web | 21 |
| mobile / Android | 17 |
| JavaScript / TypeScript | 11 |
| Go / Rust | 10 |

## Tag Index (by overall rank)

### 方法 Axis

#### multi-agent (78 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 2 | [CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability](https://arxiv.org/abs/2602.03012) | A / 76 |
| 10 | [Does Teaming-Up LLMs Improve Secure Code Generation? A Comprehensive Evaluation with Multi-LLMSecCodeEval](https://arxiv.org/abs/2603.22717) | B / 74 |
| 11 | [ABSENTIA: Detecting Broken Access Control Vulnerabilities in Web Applications](https://arxiv.org/abs/2610.00977) | B / 74 |
| 13 | [VCAO: Verifier-Centered Agentic Orchestration for Strategic OS Vulnerability Discovery](https://arxiv.org/abs/2604.08291) | B / 73 |
| 23 | [AVIATOR: Towards AI-Agentic Vulnerability Injection Workflow for High-Fidelity, Large-Scale Code Security Dataset](https://arxiv.org/abs/2508.20866) | B / 71 |
| 24 | [Multi-Agent End-to-End Vulnerability Management for Mitigating Recurring Vulnerabilities](https://arxiv.org/abs/2601.17762) | B / 71 |
| 34 | [VulnAgent-R2: Evidence-Calibrated Multi-Agent Auditing for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2603.13384) | B / 70 |
| 41 | [SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing](https://arxiv.org/abs/2602.04418) | B / 69 |
| 43 | [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/abs/2604.01645) | B / 69 |
| 44 | [Security Is Relative: Training-Free Vulnerability Detection via Multi-Agent Behavioral Contract Synthesis](https://arxiv.org/abs/2604.19012) | B / 69 |
| 51 | [From CVE Entries to Verifiable Exploits: An Automated Multi-Agent Framework for Reproducing CVEs](https://arxiv.org/abs/2509.01835) | B / 68 |
| 64 | [VulnResolver: A Hybrid Agent Framework for LLM-Based Automated Vulnerability Issue Resolution](https://arxiv.org/abs/2601.13933) | B / 67 |
| 68 | [FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction](https://arxiv.org/abs/2605.21779) | B / 67 |
| 70 | [PrimSynth: An Agentic Approach to Discover, Validate, and Synthesize Exploit Primitives for Linux Kernel Vulnerabilities](https://arxiv.org/abs/2609.02647) | B / 67 |
| 78 | [Co-RedTeam: Orchestrated Security Discovery and Exploitation with LLM Agents](https://arxiv.org/abs/2602.02164) | B / 66 |
| 80 | [AXE: Grey-Box Exploitability Confirmation for Localized Vulnerability Reports](https://arxiv.org/abs/2602.14345) | B / 66 |
| 81 | [MultiVer: Zero-Shot Multi-Agent Vulnerability Detection](https://arxiv.org/abs/2602.17875) | B / 66 |
| 82 | [Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization](https://arxiv.org/abs/2603.26270) | B / 66 |
| 84 | [Three Heads Are Better Than One: A Multi-perspective Reasoning Framework for Enhanced Vulnerability Detection](https://arxiv.org/abs/2605.18153) | B / 66 |
| 89 | [DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2607.13439) | B / 66 |
| 100 | [Multi-LLM Energy Reasoning for Binary-Free Zero-Day IoT Detection](https://arxiv.org/abs/2512.19945) | B / 65 |
| 104 | [Security in a Workflow: Exploring Role-Based Agentic Architectures for Vulnerability Handling](https://arxiv.org/abs/2606.14261) | B / 65 |
| 106 | [Beyond Detection: Agentic Attack Synthesis and Simulation for Smart Contracts](https://arxiv.org/abs/2607.15673) | B / 65 |
| 108 | [AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair](https://arxiv.org/abs/2607.29422) | B / 65 |
| 135 | [CyberDual: AI Attackers versus AI Code Reviewers in Real Software Maintenance](https://arxiv.org/abs/2610.34435) | B / 64 |
| 136 | [VulAgent: Hypothesis-Validation based Multi-Agent Vulnerability Detection](https://arxiv.org/abs/2509.11523) | B / 63 |
| 137 | [SLEAN: Simple Lightweight Ensemble Analysis Network for Multi-Provider LLM Coordination: Design, Implementation, and Vibe Coding Bug Investigation Case Study](https://arxiv.org/abs/2510.10010) | B / 63 |
| 142 | [AEGIS: From Clues to Verdicts -- Graph-Guided Deep Vulnerability Reasoning via Dialectics and Meta-Auditing](https://arxiv.org/abs/2603.20637) | B / 63 |
| 144 | [A Multi-Agent Framework for Automated Exploit Generation with Constraint-Guided Comprehension and Reflection](https://arxiv.org/abs/2604.05130) | B / 63 |
| 145 | [Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection](https://arxiv.org/abs/2604.21282) | B / 63 |
| 147 | [Veritas: Grounding LLM Agents for Reliable Vulnerability Reasoning over Stripped Binaries](https://arxiv.org/abs/2605.15097) | B / 63 |
| 159 | [RegoMender: A Multi-agent Framework for Automated Rego Policy Repair](https://arxiv.org/abs/2610.29456) | B / 63 |
| 160 | [Multi-Agent Penetration Testing AI for the Web](https://arxiv.org/abs/2508.20816) | B / 62 |
| 170 | [HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation](https://arxiv.org/abs/2601.13864) | B / 62 |
| 179 | [Detecting Vulnerability-Inducing Commits via Multi-Stage Reasoning with LLM-Based Agents](https://arxiv.org/abs/2607.05772) | B / 62 |
| 182 | [One Pipeline Does Not Fit All: TAILOR, a Type- and State-Aware Framework for CVE Reproduction](https://arxiv.org/abs/2609.37006) | B / 62 |
| 185 | [P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245) | B / 62 |
| 193 | [SolAgent: A Specialized Multi-Agent Framework for Solidity Code Generation](https://arxiv.org/abs/2601.23009) | B / 61 |
| 194 | [QRS: A Rule-Synthesizing Neuro-Symbolic Triad for Autonomous Vulnerability Discovery](https://arxiv.org/abs/2602.09774) | B / 61 |
| 199 | [Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection](https://arxiv.org/abs/2604.06633) | B / 61 |
| 212 | [SEEK: Agentic Knowledge Graph Retrieval for Secure Code Generation](https://arxiv.org/abs/2610.14968) | B / 61 |
| 216 | [MAVUL: Multi-Agent Vulnerability Detection via Contextual Reasoning and Interactive Refinement](https://arxiv.org/abs/2510.00317) | B / 60 |
| 219 | [LLMs as Firmware Experts: A Runtime-Grown Tree-of-Agents Framework](https://arxiv.org/abs/2511.18438) | B / 60 |
| 227 | [Transferable Self-Evolving Playbooks for Agentic Security Auditing](https://arxiv.org/abs/2606.16420) | B / 60 |
| 236 | [Multi-Agent Collaborative Fuzzing with Continuous Reflection for Smart Contracts Vulnerability Detection](https://arxiv.org/abs/2511.12164) | C / 59 |
| 239 | [PatchIsland: Orchestration of LLM Agents for Continuous Vulnerability Repair](https://arxiv.org/abs/2601.17471) | C / 59 |
| 245 | [Synthesizing Multi-Agent Harnesses for Vulnerability Discovery](https://arxiv.org/abs/2604.20801) | C / 59 |
| 246 | [AgenticVM: Agentic AI for Adaptive Software Vulnerability Management](https://arxiv.org/abs/2605.01739) | C / 59 |
| 248 | [CHAINTRIX: A multi-pipeline LLM-augmented framework for automated smart-contract security auditing](https://arxiv.org/abs/2605.09350) | C / 59 |
| 253 | [Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs](https://arxiv.org/abs/2607.00555) | C / 59 |
| 257 | [MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing](https://arxiv.org/abs/2608.14216) | C / 59 |
| 268 | [Scalable Weak-to-Strong Verifier Hardening for Agent Environments](https://arxiv.org/abs/2610.15924) | C / 59 |
| 269 | [Trojan Horse: Automated Repository Poisoning against Coding Agents](https://arxiv.org/abs/2610.23109) | C / 59 |
| 270 | [Ulysses: A Security Harness For Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831) | C / 59 |
| 281 | [MulVul: Retrieval-augmented Multi-Agent Code Vulnerability Detection via Cross-Model Prompt Evolution](https://arxiv.org/abs/2601.18847) | C / 58 |
| 283 | [SecureRAG-RTL: A Retrieval-Augmented, Multi-Agent, Zero-Shot LLM-Driven Framework for Hardware Vulnerability Detection](https://arxiv.org/abs/2603.05689) | C / 58 |
| 284 | [SCAFFOLD-CEGIS: Preventing Latent Security Degradation in LLM-Driven Iterative Code Refinement](https://arxiv.org/abs/2603.08520) | C / 58 |
| 311 | [MALF: A Multi-Agent LLM Framework for Intelligent Fuzzing of Industrial Control Protocols](https://arxiv.org/abs/2510.02694) | C / 57 |
| 332 | [Securing LLM-Generated Embedded Firmware through AI Agent-Driven Validation and Patching](https://arxiv.org/abs/2509.09970) | C / 56 |
| 344 | [Symbolic Execution Meets Multi-LLM Orchestration: Detecting Memory Vulnerabilities in Incomplete Rust CVE Snippets](https://arxiv.org/abs/2605.00034) | C / 56 |
| 352 | [ProfMalPlus: Agent-Coordinated Detection of Malicious NPM Packages via Static-Dynamic Analysis Synergy](https://arxiv.org/abs/2607.13965) | C / 56 |
| 357 | [Moirae: A Multimodal Agent Collaborative Framework for Dynamic Android Malware Detection](https://arxiv.org/abs/2608.27994) | C / 56 |
| 379 | [TitanCA: Lessons from Orchestrating LLM Agents to Discover 100+ CVEs](https://arxiv.org/abs/2604.17860) | C / 55 |
| 398 | [MAS-SZZ: Multi-Agentic SZZ Algorithm for Vulnerability-Inducing Commit Identification](https://arxiv.org/abs/2604.24398) | C / 54 |
| 423 | [Agentic AI for Autonomous Defense in Software Supply Chain Security: Beyond Provenance to Vulnerability Mitigation](https://arxiv.org/abs/2512.23480) | C / 53 |
| 436 | [MARD: A Multi-Agent Framework for Robust Android Malware Detection](https://arxiv.org/abs/2604.25264) | C / 53 |
| 439 | [Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection](https://arxiv.org/abs/2605.20051) | C / 53 |
| 446 | [MAGS: Multi-agent Auto-formalization Guarantees Safety for Agentic Outputs](https://arxiv.org/abs/2609.19391) | C / 53 |
| 480 | [Feedback-Driven Execution for LLM-Based Binary Analysis](https://arxiv.org/abs/2604.15136) | C / 51 |
| 505 | [FORGE: Multi-Agent Graduated Exploitation and Detection Engineering](https://arxiv.org/abs/2606.03453) | C / 50 |
| 509 | [When Context Gets Root: Privilege Escalation in LLM Harnesses](https://arxiv.org/abs/2608.27299) | C / 50 |
| 521 | [Towards Personalizing Secure Programming Education with LLM-Injected Vulnerabilities](https://arxiv.org/abs/2604.13955) | C / 49 |
| 529 | [From Requirements to Attack Trees: Grounded LLM Agents for Design-Time Security Review](https://arxiv.org/abs/2610.03820) | C / 49 |
| 555 | [Multi-Agent Taint Specification Extraction for Vulnerability Detection](https://arxiv.org/abs/2601.10865) | C / 47 |
| 587 | [FalseCrashReducer: Mitigating False Positive Crashes in OSS-Fuzz-Gen Using Agentic AI](https://arxiv.org/abs/2510.02185) | D / 44 |
| 621 | [AdverMCTS: Combating Pseudo-Correctness in Code Generation via Adversarial Monte Carlo Tree Search](https://arxiv.org/abs/2604.10449) | D / 42 |
| 643 | [VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents](https://arxiv.org/abs/2607.09653) | D / 40 |
| 665 | [RAVEN: Retrieval-Augmented Vulnerability Exploration Network for Memory Corruption Analysis in User Code and Binary Programs](https://arxiv.org/abs/2604.17948) | D / 36 |

#### single-agent pipeline (96 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 3 | [MemRepair: Hierarchical Memory for Agentic Repository-Level Vulnerability Repair](https://arxiv.org/abs/2605.17444) | A / 76 |
| 4 | [Antaeus: Hunting Repository-Level Logic Vulnerabilities via Context-Grounded LLM Reasoning](https://arxiv.org/abs/2607.01138) | A / 76 |
| 6 | [OpenAnt: LLM-Powered Vulnerability Discovery Through Code Decomposition, Adversarial Verification, and Dynamic Testing](https://arxiv.org/abs/2606.19149) | A / 75 |
| 7 | [JANUS: Agentic Cross-Language Fuzzing Harness Generation for Android Native Libraries](https://arxiv.org/abs/2610.30218) | A / 75 |
| 9 | [An Effective and Cost-Efficient Agentic Framework for Ethereum Smart Contract Auditing](https://arxiv.org/abs/2601.17833) | B / 74 |
| 20 | [ARQ: Agentic CodeQL Query Refinement for C/C++ Vulnerability Detection](https://arxiv.org/abs/2608.20637) | B / 72 |
| 26 | [RAVEN: Agentic RAG for Automated Vulnerability Repair](https://arxiv.org/abs/2606.22647) | B / 71 |
| 28 | [AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration](https://arxiv.org/abs/2607.12058) | B / 71 |
| 30 | [The History Is the Detector: Executing CVE Patch History, End-to-End](https://arxiv.org/abs/2609.05335) | B / 71 |
| 40 | [LogicScan: An LLM-driven Framework for Detecting Business Logic Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2602.03271) | B / 69 |
| 45 | [ContraFix: Skill-Enhanced Contrastive Runtime Analysis for Vulnerability Repair](https://arxiv.org/abs/2605.17450) | B / 69 |
| 52 | [RuleForge: Automated Generation and Validation for Web Vulnerability Detection at Scale](https://arxiv.org/abs/2604.01977) | B / 68 |
| 53 | [Quality-Assured Fuzz Harness Generation via the Four Principles Framework](https://arxiv.org/abs/2605.21824) | B / 68 |
| 58 | [Proving the Wrong Program: Miscompilations as a Threat to zkVM Guarantees](https://arxiv.org/abs/2611.04701) | B / 68 |
| 60 | [From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localization](https://arxiv.org/abs/2510.02389) | B / 67 |
| 62 | [SmartPoC: Generating Executable and Validated PoCs for Smart Contract Bug Reports](https://arxiv.org/abs/2511.12993) | B / 67 |
| 63 | [VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection](https://arxiv.org/abs/2512.07533) | B / 67 |
| 65 | [AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection](https://arxiv.org/abs/2601.19138) | B / 67 |
| 67 | [Agentic Vulnerability Reasoning on COTS Binaries](https://arxiv.org/abs/2605.05000) | B / 67 |
| 94 | [SmartMemory: Detecting On-chain-off-chain Communication Inconsistency for Smart Contract via Memory-based Agent](https://arxiv.org/abs/2609.34983) | B / 66 |
| 115 | [Keeping Fuzzers on Duty: Repairing Fuzzing Build Breakages in Continuous Open-Source Fuzzing](https://arxiv.org/abs/2611.06358) | B / 65 |
| 125 | [EvoRepair: Enhancing Vulnerability Repair Agents Through Experience-Based Self-Evolution](https://arxiv.org/abs/2605.30105) | B / 64 |
| 129 | [CoSA: Context-Aware Severity Assessment via Context Analysis with Large Language Models](https://arxiv.org/abs/2608.13928) | B / 64 |
| 130 | [From Component Snapshots to Lifecycle Traces: Agent-Based Software Composition Analysis](https://arxiv.org/abs/2609.18391) | B / 64 |
| 150 | [Code-Augur: Agentic Vulnerability Detection via Specification Inference](https://arxiv.org/abs/2606.18619) | B / 63 |
| 155 | [PatchHolmes: Agentic Patch Retrieval via Listwise Selection](https://arxiv.org/abs/2609.38807) | B / 63 |
| 158 | [RELAY: Scaling Historical Build Restoration through Rule Reuse and Agentic Repair](https://arxiv.org/abs/2610.27784) | B / 63 |
| 164 | [Red Teaming Program Repair Agents: When Correct Patches can Hide Vulnerabilities](https://arxiv.org/abs/2509.25894) | B / 62 |
| 167 | [Diffploit: Facilitating Cross-Version Exploit Migration for Open Source Library Vulnerabilities](https://arxiv.org/abs/2511.12950) | B / 62 |
| 177 | [SCARA: A Semantics-Constrained Autonomous Remediation Agent for Opaque Industrial Software Vulnerabilities](https://arxiv.org/abs/2605.19668) | B / 62 |
| 188 | [Agentic Discovery and Validation of Android App Vulnerabilities](https://arxiv.org/abs/2508.21579) | B / 61 |
| 189 | [SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair](https://arxiv.org/abs/2509.16275) | B / 61 |
| 192 | [Exposing Hidden Interfaces: LLM-Guided Type Inference for Reverse Engineering macOS Private Frameworks](https://arxiv.org/abs/2601.01673) | B / 61 |
| 205 | [Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases](https://arxiv.org/abs/2606.22263) | B / 61 |
| 206 | [SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing](https://arxiv.org/abs/2607.08949) | B / 61 |
| 210 | [COMPASS: Predicting the Relationship of Multiple Patches for Vulnerabilities with LLMs](https://arxiv.org/abs/2609.39783) | B / 61 |
| 220 | [Execution-State-Aware LLM Reasoning for Automated Proof-of-Vulnerability Generation](https://arxiv.org/abs/2602.13574) | B / 60 |
| 228 | [Knowledge-Enhanced Agentic Vulnerability Repair](https://arxiv.org/abs/2607.00820) | B / 60 |
| 231 | [FlowArk: Boosting Agentic Data-flow Analysis for Android Apps via Context-Aware Knowledge Reuse](https://arxiv.org/abs/2607.11308) | B / 60 |
| 232 | [RuleAutoPilot: Synthesizing Deployable Suricata Rules from Network Traffic](https://arxiv.org/abs/2609.16231) | B / 60 |
| 244 | [AgentSZZ: Teaching the LLM Agent to Play Detective with Bug-Inducing Commits](https://arxiv.org/abs/2604.02665) | C / 59 |
| 247 | [VulKey: Automated Vulnerability Repair Guided by Domain-Specific Repair Patterns](https://arxiv.org/abs/2605.01769) | C / 59 |
| 255 | [RECEIPT: Deterministic, Reward-Hacking-Resistant Verification for White-Box Agentic XSS Discovery](https://arxiv.org/abs/2607.18575) | C / 59 |
| 256 | [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](https://arxiv.org/abs/2607.24964) | C / 59 |
| 262 | [PentestChain: A Cost-Aware, MCP-Orchestrated Framework for Automated Penetration Testing with Free-Tier LLMs](https://arxiv.org/abs/2609.18120) | C / 59 |
| 264 | [SelfOp: An Optimization Algorithm for Self-Improving Security Agents](https://arxiv.org/abs/2609.22792) | C / 59 |
| 267 | [Aletheia: Permission-Minimality Testing for Coding-Agent Rules](https://arxiv.org/abs/2609.39678) | C / 59 |
| 273 | [A Gingerbread House for LLM Agents: Source-Planned Honeypots That Lure Autonomous Attackers into an Isolated Shadow](https://arxiv.org/abs/2611.07611) | C / 59 |
| 280 | [CoTDeceptor:Adversarial Code Obfuscation Against CoT-Enhanced LLM Code Agents](https://arxiv.org/abs/2512.21250) | C / 58 |
| 288 | [Program Analysis Guided LLM Agent for Proof-of-Concept Generation](https://arxiv.org/abs/2604.07624) | C / 58 |
| 292 | [DIG: Oracle-Guided Directed Input Generation for One-Day Vulnerabilities](https://arxiv.org/abs/2606.13037) | C / 58 |
| 298 | [Antares: Foundation Models for Agentic Vulnerability Localization](https://arxiv.org/abs/2608.02407) | C / 58 |
| 306 | [Post-SQLFix: Property-Guided Repair of LLM-Generated SQL with Runtime Verification](https://arxiv.org/abs/2610.41472) | C / 58 |
| 308 | [CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion](https://arxiv.org/abs/2611.04356) | C / 58 |
| 334 | [PBFuzz: Agentic Directed Fuzzing for PoV Generation](https://arxiv.org/abs/2512.04611) | C / 56 |
| 343 | [Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis](https://arxiv.org/abs/2604.10800) | C / 56 |
| 355 | [Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems](https://arxiv.org/abs/2608.21095) | C / 56 |
| 361 | [Secure Agentic Coding through Counterexample-Grounded Feedback](https://arxiv.org/abs/2610.25916) | C / 56 |
| 367 | [PoCo: Agentic Proof-of-Concept Exploit Generation for Smart Contracts](https://arxiv.org/abs/2511.02780) | C / 55 |
| 370 | [HarnessAgent: Scaling Automatic Fuzzing Harness Construction with Tool-Augmented LLM Pipelines](https://arxiv.org/abs/2512.03420) | C / 55 |
| 373 | [Okara: Detection and Attribution of TLS Man-in-the-Middle Vulnerabilities in Android Apps with Foundation Models](https://arxiv.org/abs/2601.22770) | C / 55 |
| 378 | [PCodeTrans: Translate Decompiled Pseudocode to Compilable and Executable Equivalent](https://arxiv.org/abs/2603.14855) | C / 55 |
| 390 | [Secure and Functional Code Generation with Self-Evaluation](https://arxiv.org/abs/2610.33450) | C / 55 |
| 417 | [Orion: Fuzzing Workflow Automation](https://arxiv.org/abs/2509.15195) | C / 53 |
| 418 | [Hound: Relation-First Knowledge Graphs for Complex-System Reasoning in Security Audits](https://arxiv.org/abs/2510.09633) | C / 53 |
| 433 | [Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning](https://arxiv.org/abs/2604.20179) | C / 53 |
| 444 | [PYPILINE: Malicious PyPI Package Detection via Suspicious API Knowledge and Agent Workflow](https://arxiv.org/abs/2606.19063) | C / 53 |
| 449 | [CAT-RAG: Improving Secure Code Generation with Category-Aware Agentic Retrieval](https://arxiv.org/abs/2610.24907) | C / 53 |
| 450 | [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253) | C / 53 |
| 454 | [CodeCureAgent: Automatic Classification and Repair of Static Analysis Warnings](https://arxiv.org/abs/2509.11787) | C / 52 |
| 456 | [PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting](https://arxiv.org/abs/2511.20555) | C / 52 |
| 460 | [SPECA: Specification-to-Checklist Agentic Auditing for Multi-Implementation Systems -- A Case Study on Ethereum Clients](https://arxiv.org/abs/2602.07513) | C / 52 |
| 463 | [V2E: Validating Smart Contract Vulnerabilities through Profit-driven Exploit Generation and Execution](https://arxiv.org/abs/2604.13611) | C / 52 |
| 466 | [EntailLLM: Verifying LLM-Generated Vulnerability Discovery Paths with Domain Knowledge via Logic Programming](https://arxiv.org/abs/2608.01763) | C / 52 |
| 468 | [Beyond Static Guarantees: Measuring the Static-Pass Dynamic-Fail Gap in Security-Sensitive and LLM-Generated Python Code](https://arxiv.org/abs/2609.10762) | C / 52 |
| 472 | [KubeGuard: LLM-Assisted Kubernetes Hardening via Configuration Files and Runtime Logs Analysis](https://arxiv.org/abs/2509.04191) | C / 51 |
| 485 | [Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities](https://arxiv.org/abs/2606.26933) | C / 51 |
| 493 | [Locus: Agentic Predicate Synthesis for Directed Fuzzing](https://arxiv.org/abs/2508.21302) | C / 50 |
| 496 | [QLCoder: A Query Synthesizer For Static Analysis of Security Vulnerabilities](https://arxiv.org/abs/2511.08462) | C / 50 |
| 500 | [Well Begun is Half Done: Location-Aware and Trace-Guided Iterative Automated Vulnerability Repair](https://arxiv.org/abs/2512.20203) | C / 50 |
| 506 | [FirmCure:Towards Autonomous and Adaptive Rehosting of Linux-Based Firmware](https://arxiv.org/abs/2606.24549) | C / 50 |
| 508 | [Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline](https://arxiv.org/abs/2608.16187) | C / 50 |
| 516 | [Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback](https://arxiv.org/abs/2601.00509) | C / 49 |
| 518 | [Favia: Forensic Agent for Vulnerability-fix Identification and Analysis](https://arxiv.org/abs/2602.12500) | C / 49 |
| 553 | [Automated Vulnerability Validation and Verification: A Large Language Model Approach](https://arxiv.org/abs/2509.24037) | C / 47 |
| 556 | [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/abs/2605.04251) | C / 47 |
| 563 | [Revisiting Vulnerability Patch Localization: An Empirical Study and LLM-Based Solution](https://arxiv.org/abs/2509.15777) | C / 46 |
| 565 | [TypePilot: Leveraging the Scala Type System for Secure LLM-generated Code](https://arxiv.org/abs/2510.11151) | C / 46 |
| 567 | [Domain-constrained Synthesis of Inconsistent Key Aspects in Textual Vulnerability Descriptions](https://arxiv.org/abs/2511.16123) | C / 46 |
| 593 | [ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code](https://arxiv.org/abs/2603.06365) | D / 44 |
| 596 | [Towards LLM-Enhanced Android Taint Analysis](https://arxiv.org/abs/2608.24269) | D / 44 |
| 598 | [Evaluating Context Segmentation in Locally Deployable SLMs for Cybersecurity CTF Tasks](https://arxiv.org/abs/2609.12839) | D / 44 |
| 602 | [Thinking in Graphs: Neo4j-Backed Exploit-Chain Reasoning for LLM Penetration-Testing Agents](https://arxiv.org/abs/2610.20902) | D / 44 |
| 631 | [From LLMs to Agents: A Comparative Evaluation of LLMs and LLM-based Agents in Security Patch Detection](https://arxiv.org/abs/2511.08060) | D / 41 |
| 639 | [AutoBaxBuilder: Bootstrapping Code Security Benchmarking](https://arxiv.org/abs/2512.21132) | D / 40 |
| 650 | [LLM-Based Static Verification of Code Against Natural-Language Requirements: An Industrial Experience Report](https://arxiv.org/abs/2605.17926) | D / 39 |

#### fine-tuning / training (132 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 2 | [CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability](https://arxiv.org/abs/2602.03012) | A / 76 |
| 8 | [SecureCode: A Production-Grade Multi-Turn Dataset for Training Security-Aware Code Generation Models](https://arxiv.org/abs/2512.18542) | B / 74 |
| 18 | [Secure Code Generation via Online Reinforcement Learning with Vulnerability Reward Model](https://arxiv.org/abs/2602.07422) | B / 72 |
| 23 | [AVIATOR: Towards AI-Agentic Vulnerability Injection Workflow for High-Fidelity, Large-Scale Code Security Dataset](https://arxiv.org/abs/2508.20866) | B / 71 |
| 33 | [Enhancing Continual Learning for Software Vulnerability Prediction: Addressing Catastrophic Forgetting via Hybrid-Confidence-Aware Selective Replay for Temporal LLM Fine-Tuning](https://arxiv.org/abs/2602.23834) | B / 70 |
| 36 | [Defusing Explosive Prompts: Understanding and Preventing Trigger-Based Prompt Injections in LLM Agents](https://arxiv.org/abs/2609.22510) | B / 70 |
| 42 | [Automated Vulnerability Detection in Source Code Using Deep Representation Learning](https://arxiv.org/abs/2602.23121) | B / 69 |
| 56 | [Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security](https://arxiv.org/abs/2610.24896) | B / 68 |
| 61 | [FLAMES: Fine-tuning LLMs to Synthesize Invariants for Smart Contract Security](https://arxiv.org/abs/2510.21401) | B / 67 |
| 63 | [VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection](https://arxiv.org/abs/2512.07533) | B / 67 |
| 66 | [VulnScout-C: A Lightweight Transformer for C Code Vulnerability Detection](https://arxiv.org/abs/2603.28309) | B / 67 |
| 69 | [CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training](https://arxiv.org/abs/2608.06471) | B / 67 |
| 79 | [Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection](https://arxiv.org/abs/2602.06751) | B / 66 |
| 85 | [Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software](https://arxiv.org/abs/2606.20502) | B / 66 |
| 96 | [Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models](https://arxiv.org/abs/2610.35829) | B / 66 |
| 97 | [Rethinking Neural Decompilation: Candidate Selection as the Hidden Bottleneck](https://arxiv.org/abs/2611.02788) | B / 66 |
| 99 | [Taught by the Flawed: How Dataset Insecurity Breeds Vulnerable AI Code](https://arxiv.org/abs/2511.09879) | B / 65 |
| 102 | [VulReaD: Knowledge-Graph-guided Software Vulnerability Reasoning and Detection](https://arxiv.org/abs/2602.10787) | B / 65 |
| 105 | [Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction](https://arxiv.org/abs/2607.01764) | B / 65 |
| 111 | [Function Name Is All You Need to Detect Blockchain Application Attacks](https://arxiv.org/abs/2609.12315) | B / 65 |
| 118 | [SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-aware Fine-tuning](https://arxiv.org/abs/2510.26457) | B / 64 |
| 123 | [Synergistic Directed Execution and LLM-Driven Analysis for Zero-Day AI-Generated Malware Detection](https://arxiv.org/abs/2603.09044) | B / 64 |
| 143 | [Software Vulnerability Detection Using a Lightweight Graph Neural Network](https://arxiv.org/abs/2603.29216) | B / 63 |
| 168 | [Retrieval-Augmented Few-Shot Prompting Versus Fine-Tuning for Code Vulnerability Detection](https://arxiv.org/abs/2512.04106) | B / 62 |
| 174 | [How Code Representation Shapes False-Positive Dynamics in Cross-Language LLM Vulnerability Detection](https://arxiv.org/abs/2604.27714) | B / 62 |
| 180 | [Checked-In Secret Detection: Strings Are All You Need](https://arxiv.org/abs/2608.04523) | B / 62 |
| 189 | [SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair](https://arxiv.org/abs/2509.16275) | B / 61 |
| 191 | [Leveraging Self-Paced Learning for Software Vulnerability Detection](https://arxiv.org/abs/2511.09212) | B / 61 |
| 192 | [Exposing Hidden Interfaces: LLM-Guided Type Inference for Reverse Engineering macOS Private Frameworks](https://arxiv.org/abs/2601.01673) | B / 61 |
| 200 | [Secret Stealing Attacks on Local LLM Fine-Tuning through Supply-Chain Model Code Backdoors](https://arxiv.org/abs/2604.27426) | B / 61 |
| 203 | [Decoupled Smart Contract Audits: Lightweight LLM Framework via Distillation and Aggregation](https://arxiv.org/abs/2606.03128) | B / 61 |
| 209 | [DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation](https://arxiv.org/abs/2609.28996) | B / 61 |
| 214 | [Code Vulnerability Detection Across Different Programming Languages with AI Models](https://arxiv.org/abs/2508.11710) | B / 60 |
| 218 | [VULPO: Context-Aware Vulnerability Detection via On-Policy LLM Optimization](https://arxiv.org/abs/2511.11896) | B / 60 |
| 223 | [VulStyle: A Multi-Modal Pre-Training for Code Stylometry-Augmented Vulnerability Detection](https://arxiv.org/abs/2604.26313) | B / 60 |
| 225 | [MARGIN: Margin-Aware Regularized Geometry for Imbalanced Vulnerability Detection](https://arxiv.org/abs/2605.10240) | B / 60 |
| 247 | [VulKey: Automated Vulnerability Repair Guided by Domain-Specific Repair Patterns](https://arxiv.org/abs/2605.01769) | C / 59 |
| 266 | [SecureVibe: Making Vibe Coding More Secure](https://arxiv.org/abs/2609.38606) | C / 59 |
| 271 | [Kerkoporta: Injecting Structured-Output Backdoors in Reasoning Coding Agents](https://arxiv.org/abs/2611.00138) | C / 59 |
| 276 | [Detection of security smells in IaC scripts through semantics-aware code and language processing](https://arxiv.org/abs/2509.18790) | C / 58 |
| 279 | [Towards Classifying Benign And Malicious Packages Using Machine Learning](https://arxiv.org/abs/2511.15033) | C / 58 |
| 285 | [SecPI: Secure Code Generation with Reasoning Models via Security Reasoning Internalization](https://arxiv.org/abs/2604.03587) | C / 58 |
| 286 | [LiquiLM: Bridging the Semantic Gap in Liquidity Flaw Audit via DCN and LLMs](https://arxiv.org/abs/2604.03860) | C / 58 |
| 289 | [Learning Generalizable Multimodal Representations for Software Vulnerability Detection](https://arxiv.org/abs/2604.25711) | C / 58 |
| 298 | [Antares: Foundation Models for Agentic Vulnerability Localization](https://arxiv.org/abs/2608.02407) | C / 58 |
| 302 | [Hieronym: Leveraging Hierarchical Multi-Source Information for Function Renaming in Stripped Binary](https://arxiv.org/abs/2609.12457) | C / 58 |
| 311 | [MALF: A Multi-Agent LLM Framework for Intelligent Fuzzing of Industrial Control Protocols](https://arxiv.org/abs/2510.02694) | C / 57 |
| 314 | [From SFT to RL: Demystifying the Post-Training Pipeline for LLM-based Vulnerability Detection](https://arxiv.org/abs/2602.14012) | C / 57 |
| 316 | [ORACAL: A Robust and Explainable Multimodal Framework for Smart Contract Vulnerability Detection with Causal Graph Enrichment](https://arxiv.org/abs/2603.28128) | C / 57 |
| 320 | [Graph Is the Verifier: Agentic Reinforcement Learning for Interprocedural Vulnerability Detection](https://arxiv.org/abs/2607.26656) | C / 57 |
| 328 | [VulDec: Vulnerability Detection in Binaries via Neural Decompilation](https://arxiv.org/abs/2610.33716) | C / 57 |
| 333 | [Esim: EVM Bytecode Similarity Detection Based on Stable-Semantic Graph](https://arxiv.org/abs/2511.12971) | C / 56 |
| 335 | [BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks](https://arxiv.org/abs/2512.09385) | C / 56 |
| 340 | [LLMs in Code Vulnerability Analysis: A Proof of Concept](https://arxiv.org/abs/2601.08691) | C / 56 |
| 361 | [Secure Agentic Coding through Counterexample-Grounded Feedback](https://arxiv.org/abs/2610.25916) | C / 56 |
| 363 | [PatchCon: Patch-aware Weighted Supervised Contrastive Learning for Vulnerability Detection](https://arxiv.org/abs/2611.06583) | C / 56 |
| 371 | [An Empirical Evaluation of LLM-Based Approaches for Code Vulnerability Detection: RAG, SFT, and Dual-Agent Systems](https://arxiv.org/abs/2601.00254) | C / 55 |
| 381 | [Athena: Vulnerability-Affected Library Identification via Knowledge Graph Completion](https://arxiv.org/abs/2609.01187) | C / 55 |
| 382 | [DeFiFusion: Combining Transaction Events with Smart Contracts to Detect Price Manipulation Attacks](https://arxiv.org/abs/2609.11008) | C / 55 |
| 384 | [HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning](https://arxiv.org/abs/2609.26352) | C / 55 |
| 386 | [JevVibe: Efficient Classification-Guided Secure Code Generation](https://arxiv.org/abs/2609.34963) | C / 55 |
| 391 | [VISION: Robust and Interpretable Code Vulnerability Detection Leveraging Counterfactual Augmentation](https://arxiv.org/abs/2508.18933) | C / 54 |
| 401 | [Binary Decompilation LLM with Feedback-Driven Multi-Turn Refinement](https://arxiv.org/abs/2606.16162) | C / 54 |
| 403 | [From Evaluation to Optimisation: Hierarchy-Aware Training Signals for CWE Prediction in Python](https://arxiv.org/abs/2607.21069) | C / 54 |
| 412 | [Making Small Code LLMs More Efficient for Secure Code Review with Neuro-Symbolic Fine-Tuning](https://arxiv.org/abs/2610.35477) | C / 54 |
| 415 | [Cross-Domain Evaluation of Transformer-Based Vulnerability Detection on Open & Industry Data](https://arxiv.org/abs/2509.09313) | C / 53 |
| 416 | [Towards Secure and Explainable Smart Contract Generation with Security-Aware Group Relative Policy Optimization](https://arxiv.org/abs/2509.09942) | C / 53 |
| 419 | [MulVuln: Enhancing Pre-trained LMs with Shared and Language-Specific Knowledge for Multilingual Vulnerability Detection](https://arxiv.org/abs/2510.04397) | C / 53 |
| 420 | [ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contract Vulnerability Detection](https://arxiv.org/abs/2510.17919) | C / 53 |
| 421 | [HYDRA: A Hybrid Heuristic-Guided Deep Representation Architecture for Predicting Latent Zero-Day Vulnerabilities in Patched Functions](https://arxiv.org/abs/2511.06220) | C / 53 |
| 422 | [Llama-based source code vulnerability detection: Prompt engineering vs Fine tuning](https://arxiv.org/abs/2512.09006) | C / 53 |
| 425 | [Lightweight Yet Secure: Secure Scripting Language Generation via Lightweight LLMs](https://arxiv.org/abs/2601.06419) | C / 53 |
| 427 | [Do Fine-Tuned LLMs Understand Vulnerabilities? An Investigation into the Semantic Trap](https://arxiv.org/abs/2601.22655) | C / 53 |
| 428 | [Code Fingerprints: Disentangled Attribution of LLM-Generated Code](https://arxiv.org/abs/2603.04212) | C / 53 |
| 431 | [SynthFix: Adaptive Neuro-Symbolic Code Vulnerability Repair](https://arxiv.org/abs/2604.17184) | C / 53 |
| 432 | [SAGE: Signal-Amplified Guided Embeddings for LLM-based Vulnerability Detection](https://arxiv.org/abs/2604.19031) | C / 53 |
| 442 | [FusionVul: A Multimodal Feature Fusion Framework for Source Code Vulnerability Detection](https://arxiv.org/abs/2606.08553) | C / 53 |
| 455 | [Vul-R2: A Reasoning LLM for Automated Vulnerability Repair](https://arxiv.org/abs/2510.05480) | C / 52 |
| 457 | [Towards Compositional Generalization in LLMs for Smart Contract Security: A Case Study on Reentrancy Vulnerabilities](https://arxiv.org/abs/2601.06914) | C / 52 |
| 458 | [Cascaded Vulnerability Attacks in Software Supply Chains](https://arxiv.org/abs/2601.20158) | C / 52 |
| 459 | [Evaluating and Enhancing the Vulnerability Reasoning Capabilities of Large Language Models](https://arxiv.org/abs/2602.06687) | C / 52 |
| 470 | [ContractLens: Latent Security Knowledge for Malicious Smart Contract Detection](https://arxiv.org/abs/2610.04992) | C / 52 |
| 475 | [Large Language Model based Smart Contract Auditing with LLMBugScanner](https://arxiv.org/abs/2512.02069) | C / 51 |
| 476 | [SHERLOCK: A Deep Learning Approach To Detect Software Vulnerabilities](https://arxiv.org/abs/2512.12593) | C / 51 |
| 477 | [ReSIM: Re-ranking Binary Similarity Embeddings to Improve Function Search Performance](https://arxiv.org/abs/2602.09548) | C / 51 |
| 488 | [When Label Noise Meets Class Imbalance: A Robust Framework for Android Malware Family Classification](https://arxiv.org/abs/2609.22835) | C / 51 |
| 494 | [LLaVul: A Multimodal LLM for Interpretable Vulnerability Reasoning about Source Code](https://arxiv.org/abs/2509.17337) | C / 50 |
| 495 | [Clutch Control: An Attention-based Combinatorial Bandit for Efficient Mutation in JavaScript Engine Fuzzing](https://arxiv.org/abs/2510.12732) | C / 50 |
| 497 | [Can LLMs Recover Program Semantics? A Systematic Evaluation with Symbolic Execution](https://arxiv.org/abs/2511.19130) | C / 50 |
| 512 | [Backdooring Sparse Autoencoders](https://arxiv.org/abs/2610.06049) | C / 50 |
| 513 | [InterType: Breaking the Single-Function Barrier in Neural Binary Type Inference](https://arxiv.org/abs/2610.26906) | C / 50 |
| 522 | [PLMGH: What Matters in PLM-GNN Hybrids for Code Classification and Vulnerability Detection](https://arxiv.org/abs/2604.25599) | C / 49 |
| 524 | [AttackPathGNN: Cross-function vulnerability detection in smart contracts using state interference graphs and conjunction pooling](https://arxiv.org/abs/2606.05986) | C / 49 |
| 525 | [Data-Centric Benchmarking of Exploit Generation in LLMs: Understanding the Impact of Fine-Tuning](https://arxiv.org/abs/2606.15123) | C / 49 |
| 527 | [VulnGym: Evaluating Vulnerability Management Strategies against Advanced Persistent Threats](https://arxiv.org/abs/2607.24552) | C / 49 |
| 528 | [N2NMatcher: Towards Inlining-Resilient Binary Decomposition and Module Matching](https://arxiv.org/abs/2608.10043) | C / 49 |
| 530 | [Predicting CVSS and CWE from CVE Descriptions with Fine-Tuned Small Language Models](https://arxiv.org/abs/2610.24297) | C / 49 |
| 533 | [LLM-based Vulnerability Discovery through the Lens of Code Metrics](https://arxiv.org/abs/2509.19117) | C / 48 |
| 534 | [Distilling Lightweight Language Models for C/C++ Vulnerabilities](https://arxiv.org/abs/2510.06645) | C / 48 |
| 537 | [Focus on What Matters: Fisher-Guided Adaptive Multimodal Fusion for Vulnerability Detection](https://arxiv.org/abs/2601.02438) | C / 48 |
| 538 | [SecCodePRM: A Process Reward Model for Code Security](https://arxiv.org/abs/2602.10418) | C / 48 |
| 540 | [Walma: Learning to See Memory Corruption in WebAssembly](https://arxiv.org/abs/2603.24167) | C / 48 |
| 541 | [Robust Smart Contract Vulnerability Detection via Contrastive Learning-Enhanced Granular-ball Training](https://arxiv.org/abs/2603.27734) | C / 48 |
| 545 | [Malformer: A Multi-Modal Malware Detector Using Transformers](https://arxiv.org/abs/2608.19052) | C / 48 |
| 551 | [Federated Learning for Malware Image Classification under Data Heterogeneity](https://arxiv.org/abs/2610.25264) | C / 48 |
| 559 | [RAMP: Reversing Adversarial Perturbations to Strengthen Clean-Label Backdoor Attacks against Malware Detectors](https://arxiv.org/abs/2609.27422) | C / 47 |
| 562 | [Optimizing Code Embeddings and ML Classifiers for Python Source Code Vulnerability Detection](https://arxiv.org/abs/2509.13134) | C / 46 |
| 568 | [Examining the Effectiveness of Transformer-Based Smart Contract Vulnerability Scan](https://arxiv.org/abs/2601.07334) | C / 46 |
| 570 | [Mitigating False Positives in Static Memory Safety Analysis of Rust Programs via Reinforcement Learning](https://arxiv.org/abs/2605.04000) | C / 46 |
| 574 | [MalFlows: Context-aware Fusion of Heterogeneous Flow Semantics for Android Malware Detection](https://arxiv.org/abs/2508.03588) | C / 45 |
| 577 | [Detecting Vulnerabilities from Issue Reports for Internet-of-Things](https://arxiv.org/abs/2511.01941) | C / 45 |
| 581 | [Efficient Software Vulnerability Detection Using Transformer-based Models](https://arxiv.org/abs/2604.00112) | C / 45 |
| 582 | [Towards Robust Personalized Federated Learning: Vulnerability Assessment and Defense Co-Design](https://arxiv.org/abs/2606.22782) | C / 45 |
| 585 | [Name2Pkg: Lightweight One-Class Android Malware Screening via Name-Package Correspondence Modeling](https://arxiv.org/abs/2609.24389) | C / 45 |
| 599 | [Exploring Automated Vulnerability Identification in JavaScript Code Using Large Language Models](https://arxiv.org/abs/2609.13816) | D / 44 |
| 600 | [Behavior-Centric Malware Classification with Fine-Grained Malicious Logic Localization](https://arxiv.org/abs/2609.38390) | D / 44 |
| 608 | [SecureCodeRL: Security-Aware Reinforcement Learning for Code Generation with Partial-Credit Rewards](https://arxiv.org/abs/2601.01184) | D / 43 |
| 609 | [Deep Learning-based Binary Analysis for Vulnerability Detection in x86-64 Machine Code](https://arxiv.org/abs/2601.09157) | D / 43 |
| 613 | [A Comparison of Malware Image Transformations Using Grad-CAM and Hybrid Learning Models](https://arxiv.org/abs/2608.12077) | D / 43 |
| 614 | [RTLGuard: A Lightweight Teacher-Student Defense for Poisoned RTL Code Generation Models](https://arxiv.org/abs/2608.26049) | D / 43 |
| 619 | [On the Effectiveness of Instruction-Tuning Local LLMs for Identifying Software Vulnerabilities](https://arxiv.org/abs/2512.20062) | D / 42 |
| 622 | [LCC-LLM: Leveraging Code-Centric Large Language Models for Malware Attribution](https://arxiv.org/abs/2605.05807) | D / 42 |
| 626 | [SemVul: Semantic-Enhanced Graph Neural Networks for Code Property Graph-based Vulnerability Detection](https://arxiv.org/abs/2609.06035) | D / 42 |
| 628 | [OPBackdoor: Opportunistic Backdoors via Alibi-Aligned Reasoning](https://arxiv.org/abs/2609.24826) | D / 42 |
| 630 | [ScamDetect: Towards a Robust, Agnostic Framework to Uncover Threats in Smart Contracts](https://arxiv.org/abs/2508.07094) | D / 41 |
| 633 | [Learn from Your Mistakes: Tree-like Self-Play for Secure Code LLMs](https://arxiv.org/abs/2606.03489) | D / 41 |
| 637 | [SEMA-GUARD: Semantic and Graph-Based Vulnerability Detection in Assembly Code](https://arxiv.org/abs/2609.17254) | D / 41 |
| 645 | [Enhancing Multiclass Malware Classification in Resource-Constrained Environments](https://arxiv.org/abs/2609.27950) | D / 40 |
| 648 | [Prompt Engineering vs. Fine-Tuning for LLM-Based Vulnerability Detection in Solana and Algorand Smart Contracts](https://arxiv.org/abs/2511.11250) | D / 39 |
| 652 | [C-ing Clearly: Enhanced Binary Code Explanations using C code](https://arxiv.org/abs/2512.14500) | D / 38 |
| 657 | [Cross-modal Retrieval Models for Stripped Binary Analysis](https://arxiv.org/abs/2512.10393) | D / 37 |
| 674 | [Pretraining on Call Graphs: When Binary Analysis Tasks Profit From Context](https://arxiv.org/abs/2608.02084) | D / 31 |

#### RAG / knowledge base (67 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 3 | [MemRepair: Hierarchical Memory for Agentic Repository-Level Vulnerability Repair](https://arxiv.org/abs/2605.17444) | A / 76 |
| 23 | [AVIATOR: Towards AI-Agentic Vulnerability Injection Workflow for High-Fidelity, Large-Scale Code Security Dataset](https://arxiv.org/abs/2508.20866) | B / 71 |
| 24 | [Multi-Agent End-to-End Vulnerability Management for Mitigating Recurring Vulnerabilities](https://arxiv.org/abs/2601.17762) | B / 71 |
| 26 | [RAVEN: Agentic RAG for Automated Vulnerability Repair](https://arxiv.org/abs/2606.22647) | B / 71 |
| 65 | [AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection](https://arxiv.org/abs/2601.19138) | B / 67 |
| 75 | [CKG-LLM: LLM-Assisted Detection of Smart Contract Access Control Vulnerabilities Based on Knowledge Graphs](https://arxiv.org/abs/2512.06846) | B / 66 |
| 82 | [Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization](https://arxiv.org/abs/2603.26270) | B / 66 |
| 94 | [SmartMemory: Detecting On-chain-off-chain Communication Inconsistency for Smart Contract via Memory-based Agent](https://arxiv.org/abs/2609.34983) | B / 66 |
| 98 | [CryptoScope: Utilizing Large Language Models for Automated Cryptographic Logic Vulnerability Detection](https://arxiv.org/abs/2508.11599) | B / 65 |
| 102 | [VulReaD: Knowledge-Graph-guided Software Vulnerability Reasoning and Detection](https://arxiv.org/abs/2602.10787) | B / 65 |
| 103 | [Securing the Dark Matter: A Semantic-Enhanced Neuro-Symbolic Framework for Supply Chain Analysis of Opaque Industrial Software](https://arxiv.org/abs/2605.07737) | B / 65 |
| 106 | [Beyond Detection: Agentic Attack Synthesis and Simulation for Smart Contracts](https://arxiv.org/abs/2607.15673) | B / 65 |
| 116 | [VulRTex: A Reasoning-Guided Approach to Identify Vulnerabilities from Rich-Text Issue Report](https://arxiv.org/abs/2509.03875) | B / 64 |
| 118 | [SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-aware Fine-tuning](https://arxiv.org/abs/2510.26457) | B / 64 |
| 120 | [VulInstruct: Teaching LLMs Root-Cause Reasoning for Vulnerability Detection via Security Specifications](https://arxiv.org/abs/2511.04014) | B / 64 |
| 124 | [EvoPoC: Automated Exploit Synthesis for DeFi Smart Contracts via Hierarchical Knowledge Graphs](https://arxiv.org/abs/2605.02868) | B / 64 |
| 125 | [EvoRepair: Enhancing Vulnerability Repair Agents Through Experience-Based Self-Evolution](https://arxiv.org/abs/2605.30105) | B / 64 |
| 128 | [Memoir: Learning, Verifying, and Evolving False-Positive Memories for Static Application Security Testing Tools](https://arxiv.org/abs/2608.09181) | B / 64 |
| 146 | [VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.09461) | B / 63 |
| 163 | [LISA Technical Report: An Agentic Framework for Smart Contract Auditing](https://arxiv.org/abs/2509.24698) | B / 62 |
| 165 | [QuiLL: An LLM-Based Vulnerability Assessment Framework for the Wild](https://arxiv.org/abs/2510.04056) | B / 62 |
| 168 | [Retrieval-Augmented Few-Shot Prompting Versus Fine-Tuning for Code Vulnerability Detection](https://arxiv.org/abs/2512.04106) | B / 62 |
| 199 | [Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection](https://arxiv.org/abs/2604.06633) | B / 61 |
| 212 | [SEEK: Agentic Knowledge Graph Retrieval for Secure Code Generation](https://arxiv.org/abs/2610.14968) | B / 61 |
| 217 | [SCRUTINEER: Detecting Logic-Level Usage Violations of Reusable Components in Smart Contracts](https://arxiv.org/abs/2511.11411) | B / 60 |
| 228 | [Knowledge-Enhanced Agentic Vulnerability Repair](https://arxiv.org/abs/2607.00820) | B / 60 |
| 231 | [FlowArk: Boosting Agentic Data-flow Analysis for Android Apps via Context-Aware Knowledge Reuse](https://arxiv.org/abs/2607.11308) | B / 60 |
| 243 | [SCPatcher: Automated Smart Contract Code Repair via Retrieval-Augmented Generation and Knowledge Graph](https://arxiv.org/abs/2604.00687) | C / 59 |
| 247 | [VulKey: Automated Vulnerability Repair Guided by Domain-Specific Repair Patterns](https://arxiv.org/abs/2605.01769) | C / 59 |
| 278 | [Fortifying LLM-Based Code Generation with Graph-Based Reasoning on Secure Coding Practices](https://arxiv.org/abs/2510.09682) | C / 58 |
| 281 | [MulVul: Retrieval-augmented Multi-Agent Code Vulnerability Detection via Cross-Model Prompt Evolution](https://arxiv.org/abs/2601.18847) | C / 58 |
| 283 | [SecureRAG-RTL: A Retrieval-Augmented, Multi-Agent, Zero-Shot LLM-Driven Framework for Hardware Vulnerability Detection](https://arxiv.org/abs/2603.05689) | C / 58 |
| 295 | [Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing](https://arxiv.org/abs/2607.21983) | C / 58 |
| 311 | [MALF: A Multi-Agent LLM Framework for Intelligent Fuzzing of Industrial Control Protocols](https://arxiv.org/abs/2510.02694) | C / 57 |
| 316 | [ORACAL: A Robust and Explainable Multimodal Framework for Smart Contract Vulnerability Detection with Causal Graph Enrichment](https://arxiv.org/abs/2603.28128) | C / 57 |
| 319 | [Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code](https://arxiv.org/abs/2607.21641) | C / 57 |
| 323 | [DBcover: A White-box SQL Test Generation Framework for Coverage Improvement](https://arxiv.org/abs/2608.25573) | C / 57 |
| 325 | [A Queryable Graph-Based Security Analysis Framework for O-RAN](https://arxiv.org/abs/2609.06855) | C / 57 |
| 346 | [KVerus: Scalable and Resilient Formal Verification Proof Generation for Rust Code](https://arxiv.org/abs/2605.03822) | C / 56 |
| 353 | [DeFiScreener: Efficient DeFi Attack Pre-screening in Smart Contracts via Historical Case Matching](https://arxiv.org/abs/2607.22184) | C / 56 |
| 358 | [Self-Evolving Defense: Continual Security Policy Learning for LLM Agents](https://arxiv.org/abs/2609.36603) | C / 56 |
| 371 | [An Empirical Evaluation of LLM-Based Approaches for Code Vulnerability Detection: RAG, SFT, and Dual-Agent Systems](https://arxiv.org/abs/2601.00254) | C / 55 |
| 381 | [Athena: Vulnerability-Affected Library Identification via Knowledge Graph Completion](https://arxiv.org/abs/2609.01187) | C / 55 |
| 390 | [Secure and Functional Code Generation with Self-Evaluation](https://arxiv.org/abs/2610.33450) | C / 55 |
| 392 | [PatchSeeker: Mapping NVD Records to their Vulnerability-fixing Commits with LLM Generated Commits and Embeddings](https://arxiv.org/abs/2509.07540) | C / 54 |
| 409 | [ORCAGen: Orchestrating Context-Aware Malware Deception with RAG-Guided Generative AI](https://arxiv.org/abs/2610.12415) | C / 54 |
| 418 | [Hound: Relation-First Knowledge Graphs for Complex-System Reasoning in Security Audits](https://arxiv.org/abs/2510.09633) | C / 53 |
| 420 | [ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contract Vulnerability Detection](https://arxiv.org/abs/2510.17919) | C / 53 |
| 422 | [Llama-based source code vulnerability detection: Prompt engineering vs Fine tuning](https://arxiv.org/abs/2512.09006) | C / 53 |
| 441 | [R+R: Reassessing Java Security API Misuse in Current LLMs: A Replication on JCA and JSSE APIs with External Security Knowledge](https://arxiv.org/abs/2605.31135) | C / 53 |
| 444 | [PYPILINE: Malicious PyPI Package Detection via Suspicious API Knowledge and Agent Workflow](https://arxiv.org/abs/2606.19063) | C / 53 |
| 449 | [CAT-RAG: Improving Secure Code Generation with Category-Aware Agentic Retrieval](https://arxiv.org/abs/2610.24907) | C / 53 |
| 474 | [ReVul-CoT: Towards Effective Software Vulnerability Assessment with Retrieval-Augmented Generation and Chain-of-Thought Prompting](https://arxiv.org/abs/2511.17027) | C / 51 |
| 491 | [CVE-to-ATT&CK Mapping via Evidence-Constrained Ranking](https://arxiv.org/abs/2610.33924) | C / 51 |
| 516 | [Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback](https://arxiv.org/abs/2601.00509) | C / 49 |
| 523 | [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](https://arxiv.org/abs/2606.04739) | C / 49 |
| 546 | [HARP: Hierarchical Adaptive Ranking with Preference-Adaptive Fusion for Query-Based CVE Prioritization](https://arxiv.org/abs/2608.19430) | C / 48 |
| 552 | [When Code Crosses Borders: A Security-Centric Study of LLM-based Code Translation](https://arxiv.org/abs/2509.06504) | C / 47 |
| 553 | [Automated Vulnerability Validation and Verification: A Large Language Model Approach](https://arxiv.org/abs/2509.24037) | C / 47 |
| 566 | [MalCVE: Malware Detection and CVE Association Using Large Language Models](https://arxiv.org/abs/2510.15567) | C / 46 |
| 580 | [Persistent Human Feedback, LLMs, and Static Analyzers for Secure Code Generation and Vulnerability Detection](https://arxiv.org/abs/2602.05868) | C / 45 |
| 602 | [Thinking in Graphs: Neo4j-Backed Exploit-Chain Reasoning for LLM Penetration-Testing Agents](https://arxiv.org/abs/2610.20902) | D / 44 |
| 617 | [MirrorFuzz: Leveraging LLM and Shared Bugs for Deep Learning Framework APIs Fuzzing](https://arxiv.org/abs/2510.15690) | D / 42 |
| 622 | [LCC-LLM: Leveraging Code-Centric Large Language Models for Malware Attribution](https://arxiv.org/abs/2605.05807) | D / 42 |
| 640 | [LLM-Powered Silent Bug Fuzzing in Deep Learning Libraries via Versatile and Controlled Bug Transfer](https://arxiv.org/abs/2602.23065) | D / 40 |
| 665 | [RAVEN: Retrieval-Augmented Vulnerability Exploration Network for Memory Corruption Analysis in User Code and Binary Programs](https://arxiv.org/abs/2604.17948) | D / 36 |
| 666 | [FT-Pilot: Automated Fault-Tolerant RTL Rewriting via Vulnerability-Guided LLMs](https://arxiv.org/abs/2605.28169) | D / 36 |

#### neuro-symbolic (LLM + program analysis) (152 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 6 | [OpenAnt: LLM-Powered Vulnerability Discovery Through Code Decomposition, Adversarial Verification, and Dynamic Testing](https://arxiv.org/abs/2606.19149) | A / 75 |
| 13 | [VCAO: Verifier-Centered Agentic Orchestration for Strategic OS Vulnerability Discovery](https://arxiv.org/abs/2604.08291) | B / 73 |
| 20 | [ARQ: Agentic CodeQL Query Refinement for C/C++ Vulnerability Detection](https://arxiv.org/abs/2608.20637) | B / 72 |
| 25 | [VulWeaver: Weaving Broken Semantics for Grounded Vulnerability Detection](https://arxiv.org/abs/2604.10767) | B / 71 |
| 28 | [AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration](https://arxiv.org/abs/2607.12058) | B / 71 |
| 30 | [The History Is the Detector: Executing CVE Patch History, End-to-End](https://arxiv.org/abs/2609.05335) | B / 71 |
| 35 | [Agent Audit: A Security AnalS System for LLM Agent Applications](https://arxiv.org/abs/2603.22853) | B / 70 |
| 38 | [VULSOLVER: Vulnerability Detection via LLM-Driven Constraint Solving](https://arxiv.org/abs/2509.00882) | B / 69 |
| 43 | [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/abs/2604.01645) | B / 69 |
| 46 | [PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance](https://arxiv.org/abs/2608.17220) | B / 69 |
| 55 | [IntentFuzz: A Protocol-Aware Fuzzer for Automated Invariant Violation Detection in Intent-Based Cross-Chain Bridges](https://arxiv.org/abs/2609.13004) | B / 68 |
| 57 | [Towards Effective Fuzzing of EDK2 Components](https://arxiv.org/abs/2611.03854) | B / 68 |
| 68 | [FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction](https://arxiv.org/abs/2605.21779) | B / 67 |
| 72 | [An Empirical Analysis of CodeQL False Positives and Query Refinements for Java Vulnerabilities](https://arxiv.org/abs/2609.04535) | B / 67 |
| 73 | [From Instructions to Exploits: Applying Program Analysis to Malicious Agent Skills Across Natural Language and Code](https://arxiv.org/abs/2610.33489) | B / 67 |
| 75 | [CKG-LLM: LLM-Assisted Detection of Smart Contract Access Control Vulnerabilities Based on Knowledge Graphs](https://arxiv.org/abs/2512.06846) | B / 66 |
| 79 | [Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection](https://arxiv.org/abs/2602.06751) | B / 66 |
| 88 | [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](https://arxiv.org/abs/2607.12316) | B / 66 |
| 96 | [Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models](https://arxiv.org/abs/2610.35829) | B / 66 |
| 97 | [Rethinking Neural Decompilation: Candidate Selection as the Hidden Bottleneck](https://arxiv.org/abs/2611.02788) | B / 66 |
| 103 | [Securing the Dark Matter: A Semantic-Enhanced Neuro-Symbolic Framework for Supply Chain Analysis of Opaque Industrial Software](https://arxiv.org/abs/2605.07737) | B / 65 |
| 104 | [Security in a Workflow: Exploring Role-Based Agentic Architectures for Vulnerability Handling](https://arxiv.org/abs/2606.14261) | B / 65 |
| 114 | [SEMPRE: Semantic-Aware Protocol Reverse Engineering via Consistency-Driven Joint Optimization](https://arxiv.org/abs/2610.31844) | B / 65 |
| 119 | [Hybrid Fuzzing with LLM-Guided Input Mutation and Semantic Feedback](https://arxiv.org/abs/2511.03995) | B / 64 |
| 123 | [Synergistic Directed Execution and LLM-Driven Analysis for Zero-Day AI-Generated Malware Detection](https://arxiv.org/abs/2603.09044) | B / 64 |
| 124 | [EvoPoC: Automated Exploit Synthesis for DeFi Smart Contracts via Hierarchical Knowledge Graphs](https://arxiv.org/abs/2605.02868) | B / 64 |
| 129 | [CoSA: Context-Aware Severity Assessment via Context Analysis with Large Language Models](https://arxiv.org/abs/2608.13928) | B / 64 |
| 133 | [ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary](https://arxiv.org/abs/2610.13651) | B / 64 |
| 138 | [LLM-Powered Detection of Price Manipulation in DeFi](https://arxiv.org/abs/2510.21272) | B / 63 |
| 139 | [LLM-Driven Adaptive Source-Sink Identification and False Positive Mitigation for Static Analysis](https://arxiv.org/abs/2511.04023) | B / 63 |
| 141 | [Attention Distance: A Novel Metric for Directed Fuzzing with Large Language Models](https://arxiv.org/abs/2512.19758) | B / 63 |
| 142 | [AEGIS: From Clues to Verdicts -- Graph-Guided Deep Vulnerability Reasoning via Dialectics and Meta-Auditing](https://arxiv.org/abs/2603.20637) | B / 63 |
| 144 | [A Multi-Agent Framework for Automated Exploit Generation with Constraint-Guided Comprehension and Reflection](https://arxiv.org/abs/2604.05130) | B / 63 |
| 147 | [Veritas: Grounding LLM Agents for Reliable Vulnerability Reasoning over Stripped Binaries](https://arxiv.org/abs/2605.15097) | B / 63 |
| 148 | [Automated Repair of TEE Partitioning Issues via DSL-Guided and LLM-Assisted Patching](https://arxiv.org/abs/2605.22087) | B / 63 |
| 150 | [Code-Augur: Agentic Vulnerability Detection via Specification Inference](https://arxiv.org/abs/2606.18619) | B / 63 |
| 151 | [ShadowProbe: Language-Extensible Detection of Hidden Algorithmic Complexity Vulnerabilities](https://arxiv.org/abs/2607.05474) | B / 63 |
| 152 | [Unsaid, Unsafe? Implicit Security Obligations in LLM-Based RTL Code Generation](https://arxiv.org/abs/2608.26588) | B / 63 |
| 153 | [Echo: Learning-based Matching Decompilation using Trusted Back Translation](https://arxiv.org/abs/2609.18706) | B / 63 |
| 156 | [Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents](https://arxiv.org/abs/2609.39065) | B / 63 |
| 162 | [LLM-Driven SAST-Genius: A Hybrid Static Analysis Framework for Comprehensive and Actionable Security](https://arxiv.org/abs/2509.15433) | B / 62 |
| 163 | [LISA Technical Report: An Agentic Framework for Smart Contract Auditing](https://arxiv.org/abs/2509.24698) | B / 62 |
| 166 | [Trace: Securing Smart Contract Repository Against Access Control Vulnerability](https://arxiv.org/abs/2510.19254) | B / 62 |
| 172 | [Detecting Data Poisoning in Code Generation LLMs via Black-Box, Vulnerability-Oriented Scanning](https://arxiv.org/abs/2603.17174) | B / 62 |
| 184 | [LLM-based Code Auditing by Inferring and Evaluating Developer Assumptions](https://arxiv.org/abs/2610.15729) | B / 62 |
| 188 | [Agentic Discovery and Validation of Android App Vulnerabilities](https://arxiv.org/abs/2508.21579) | B / 61 |
| 193 | [SolAgent: A Specialized Multi-Agent Framework for Solidity Code Generation](https://arxiv.org/abs/2601.23009) | B / 61 |
| 194 | [QRS: A Rule-Synthesizing Neuro-Symbolic Triad for Autonomous Vulnerability Discovery](https://arxiv.org/abs/2602.09774) | B / 61 |
| 198 | [Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/abs/2604.05292) | B / 61 |
| 204 | [Local LLM Agents as Vulnerable Runtimes:A Source-Code Audit of the Agent Runtime Layer](https://arxiv.org/abs/2606.21071) | B / 61 |
| 205 | [Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases](https://arxiv.org/abs/2606.22263) | B / 61 |
| 207 | [Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities](https://arxiv.org/abs/2607.12723) | B / 61 |
| 209 | [DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation](https://arxiv.org/abs/2609.28996) | B / 61 |
| 217 | [SCRUTINEER: Detecting Logic-Level Usage Violations of Reusable Components in Smart Contracts](https://arxiv.org/abs/2511.11411) | B / 60 |
| 221 | [LibScan: Smart Contract Library Misuse Detection with Iterative Feedback and Static Verification](https://arxiv.org/abs/2604.00657) | B / 60 |
| 233 | [Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail](https://arxiv.org/abs/2609.39086) | B / 60 |
| 237 | [GAPS: Targeted Execution of Android Apps via Static Path Reconstruction](https://arxiv.org/abs/2511.23213) | C / 59 |
| 241 | [Bridging Code Property Graphs and Language Models for Program Analysis](https://arxiv.org/abs/2603.24837) | C / 59 |
| 248 | [CHAINTRIX: A multi-pipeline LLM-augmented framework for automated smart-contract security auditing](https://arxiv.org/abs/2605.09350) | C / 59 |
| 249 | [NeuroLog: Reasoning You Can Audit -- Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT](https://arxiv.org/abs/2606.00669) | C / 59 |
| 258 | [KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference](https://arxiv.org/abs/2608.26699) | C / 59 |
| 261 | [BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure](https://arxiv.org/abs/2609.11028) | C / 59 |
| 262 | [PentestChain: A Cost-Aware, MCP-Orchestrated Framework for Automated Penetration Testing with Free-Tier LLMs](https://arxiv.org/abs/2609.18120) | C / 59 |
| 263 | [CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection](https://arxiv.org/abs/2609.18862) | C / 59 |
| 284 | [SCAFFOLD-CEGIS: Preventing Latent Security Degradation in LLM-Driven Iterative Code Refinement](https://arxiv.org/abs/2603.08520) | C / 58 |
| 287 | [Guiding Symbolic Execution with Static Analysis and LLMs for Vulnerability Discovery](https://arxiv.org/abs/2604.06506) | C / 58 |
| 288 | [Program Analysis Guided LLM Agent for Proof-of-Concept Generation](https://arxiv.org/abs/2604.07624) | C / 58 |
| 292 | [DIG: Oracle-Guided Directed Input Generation for One-Day Vulnerabilities](https://arxiv.org/abs/2606.13037) | C / 58 |
| 294 | [Directed Symbolic Execution for Vulnerability Discovery: An LLM-Guided Approach in KLEE](https://arxiv.org/abs/2607.21676) | C / 58 |
| 295 | [Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing](https://arxiv.org/abs/2607.21983) | C / 58 |
| 299 | [Generics-Aware Fuzz Target Generation for Rust Libraries via Structured API Analysis](https://arxiv.org/abs/2608.08637) | C / 58 |
| 300 | [LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles](https://arxiv.org/abs/2608.13450) | C / 58 |
| 306 | [Post-SQLFix: Property-Guided Repair of LLM-Generated SQL with Runtime Verification](https://arxiv.org/abs/2610.41472) | C / 58 |
| 308 | [CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion](https://arxiv.org/abs/2611.04356) | C / 58 |
| 310 | [TraceLLM: Security Diagnosis Through Traces and Smart Contracts in Ethereum](https://arxiv.org/abs/2509.03037) | C / 57 |
| 312 | [Bridging Semantics & Structure for Software Vulnerability Detection using Hybrid Network Models](https://arxiv.org/abs/2510.10321) | C / 57 |
| 317 | [Reachability Across the NL/PL Boundary: A Taxonomy-Driven Dataflow Model for LLM-Integrated Applications](https://arxiv.org/abs/2603.28345) | C / 57 |
| 319 | [Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code](https://arxiv.org/abs/2607.21641) | C / 57 |
| 320 | [Graph Is the Verifier: Agentic Reinforcement Learning for Interprocedural Vulnerability Detection](https://arxiv.org/abs/2607.26656) | C / 57 |
| 321 | [CWEEP: A Lexical Static Analysis Framework for CWE Early Prevention](https://arxiv.org/abs/2607.29604) | C / 57 |
| 323 | [DBcover: A White-box SQL Test Generation Framework for Coverage Improvement](https://arxiv.org/abs/2608.25573) | C / 57 |
| 331 | [All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching](https://arxiv.org/abs/2509.07225) | C / 56 |
| 336 | [Taint-Based Code Slicing for LLMs-based Malicious NPM Package Detection](https://arxiv.org/abs/2512.12313) | C / 56 |
| 339 | [STELP: Secure Transpilation and Execution of LLM-Generated Programs](https://arxiv.org/abs/2601.05467) | C / 56 |
| 343 | [Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis](https://arxiv.org/abs/2604.10800) | C / 56 |
| 344 | [Symbolic Execution Meets Multi-LLM Orchestration: Detecting Memory Vulnerabilities in Incomplete Rust CVE Snippets](https://arxiv.org/abs/2605.00034) | C / 56 |
| 346 | [KVerus: Scalable and Resilient Formal Verification Proof Generation for Rust Code](https://arxiv.org/abs/2605.03822) | C / 56 |
| 347 | [VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers](https://arxiv.org/abs/2605.21392) | C / 56 |
| 350 | [Knowledge Over Parameters: Evolving Smart Contract Vulnerability Detection](https://arxiv.org/abs/2607.01742) | C / 56 |
| 352 | [ProfMalPlus: Agent-Coordinated Detection of Malicious NPM Packages via Static-Dynamic Analysis Synergy](https://arxiv.org/abs/2607.13965) | C / 56 |
| 364 | [ZeroFalse: Improving Precision in Static Analysis with LLMs](https://arxiv.org/abs/2510.02534) | C / 55 |
| 366 | [ConneX: Automatically Resolving Transaction Opacity of Cross-Chain Bridges for Security Analysis](https://arxiv.org/abs/2511.01393) | C / 55 |
| 369 | [RampoNN: A Reachability-Guided System Falsification for Efficient Cyber-Kinetic Vulnerability Detection](https://arxiv.org/abs/2511.16765) | C / 55 |
| 372 | [SSR: Safeguarding Staking Rewards by Defining and Detecting Logical Defects in DeFi Staking](https://arxiv.org/abs/2601.05827) | C / 55 |
| 375 | [FuzzySQL: Uncovering Hidden Vulnerabilities in DBMS Special Features with LLM-Driven Fuzzing](https://arxiv.org/abs/2602.19490) | C / 55 |
| 376 | [NeuroSCA: Neuro-Symbolic Constraint Abstraction for Smart Contract Hybrid Fuzzing](https://arxiv.org/abs/2603.01272) | C / 55 |
| 378 | [PCodeTrans: Translate Decompiled Pseudocode to Compilable and Executable Equivalent](https://arxiv.org/abs/2603.14855) | C / 55 |
| 380 | [Aray: Deterministic-First Synthesis of Benign Artifacts for YARA Validation](https://arxiv.org/abs/2608.19387) | C / 55 |
| 393 | [TaintSentinel: Path-Level Randomness Vulnerability Detection for Ethereum Smart Contracts](https://arxiv.org/abs/2510.18192) | C / 54 |
| 394 | [One Signature, Multiple Payments: Demystifying and Detecting Signature Replay Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2511.09134) | C / 54 |
| 397 | [SDLLMFuzz: Dynamic-static LLM-assisted greybox fuzzing for structured input programs](https://arxiv.org/abs/2604.17750) | C / 54 |
| 412 | [Making Small Code LLMs More Efficient for Secure Code Review with Neuro-Symbolic Fine-Tuning](https://arxiv.org/abs/2610.35477) | C / 54 |
| 417 | [Orion: Fuzzing Workflow Automation](https://arxiv.org/abs/2509.15195) | C / 53 |
| 424 | [AutoVulnPHP: LLM-Powered Two-Stage PHP Vulnerability Detection and Automated Localization](https://arxiv.org/abs/2601.06177) | C / 53 |
| 425 | [Lightweight Yet Secure: Secure Scripting Language Generation via Lightweight LLMs](https://arxiv.org/abs/2601.06419) | C / 53 |
| 429 | [Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities](https://arxiv.org/abs/2603.10163) | C / 53 |
| 430 | [COBALT-TLA: A Neuro-Symbolic Verification Loop for Cross-Chain Bridge Vulnerability Discovery](https://arxiv.org/abs/2604.12172) | C / 53 |
| 431 | [SynthFix: Adaptive Neuro-Symbolic Code Vulnerability Repair](https://arxiv.org/abs/2604.17184) | C / 53 |
| 434 | [GoAT-X: A Graph of Auditing Thoughts for Securing Token Transactions in Cross-Chain Contracts](https://arxiv.org/abs/2604.24341) | C / 53 |
| 436 | [MARD: A Multi-Agent Framework for Robust Android Malware Detection](https://arxiv.org/abs/2604.25264) | C / 53 |
| 446 | [MAGS: Multi-agent Auto-formalization Guarantees Safety for Agentic Outputs](https://arxiv.org/abs/2609.19391) | C / 53 |
| 453 | [Guided Reasoning in LLM-Driven Penetration Testing Using Structured Attack Trees](https://arxiv.org/abs/2509.07939) | C / 52 |
| 457 | [Towards Compositional Generalization in LLMs for Smart Contract Security: A Case Study on Reentrancy Vulnerabilities](https://arxiv.org/abs/2601.06914) | C / 52 |
| 461 | [ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents](https://arxiv.org/abs/2603.12614) | C / 52 |
| 462 | [The Code Whisperer: LLM and Graph-Based AI for Smell and Vulnerability Resolution](https://arxiv.org/abs/2604.13114) | C / 52 |
| 466 | [EntailLLM: Verifying LLM-Generated Vulnerability Discovery Paths with Domain Knowledge via Logic Programming](https://arxiv.org/abs/2608.01763) | C / 52 |
| 468 | [Beyond Static Guarantees: Measuring the Static-Pass Dynamic-Fail Gap in Security-Sensitive and LLM-Generated Python Code](https://arxiv.org/abs/2609.10762) | C / 52 |
| 485 | [Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities](https://arxiv.org/abs/2606.26933) | C / 51 |
| 492 | [VerilogLAVD: LLM-Aided Rule Generation for Vulnerability Detection in Verilog](https://arxiv.org/abs/2508.13092) | C / 50 |
| 493 | [Locus: Agentic Predicate Synthesis for Directed Fuzzing](https://arxiv.org/abs/2508.21302) | C / 50 |
| 496 | [QLCoder: A Query Synthesizer For Static Analysis of Security Vulnerabilities](https://arxiv.org/abs/2511.08462) | C / 50 |
| 497 | [Can LLMs Recover Program Semantics? A Systematic Evaluation with Symbolic Execution](https://arxiv.org/abs/2511.19130) | C / 50 |
| 506 | [FirmCure:Towards Autonomous and Adaptive Rehosting of Linux-Based Firmware](https://arxiv.org/abs/2606.24549) | C / 50 |
| 508 | [Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline](https://arxiv.org/abs/2608.16187) | C / 50 |
| 511 | [Post-Hoc Attention Steering of Large Language Models for Robust Code Understanding under Obfuscation](https://arxiv.org/abs/2609.26102) | C / 50 |
| 515 | [Beyond Imprecise Distance Metrics: Trace-Guided Directed Greybox Fuzzing via LLM-Predicted Call Stacks](https://arxiv.org/abs/2510.23101) | C / 49 |
| 516 | [Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback](https://arxiv.org/abs/2601.00509) | C / 49 |
| 519 | [Quantum-Safe Code Auditing: LLM-Assisted Static Analysis and Quantum-Aware Risk Scoring for Post-Quantum Cryptography Migration](https://arxiv.org/abs/2604.00560) | C / 49 |
| 520 | [VibeGuard: A Security Gate Framework for AI-Generated Code](https://arxiv.org/abs/2604.01052) | C / 49 |
| 526 | [Neuro-Symbolic Reasoning for Vulnerability Detection](https://arxiv.org/abs/2607.03963) | C / 49 |
| 531 | [Static Analysis as a Feedback Loop: Enhancing LLM-Generated Code Beyond Correctness](https://arxiv.org/abs/2508.14419) | C / 48 |
| 539 | [Following Dragons: Code Review-Guided Fuzzing](https://arxiv.org/abs/2602.10487) | C / 48 |
| 542 | [MASFuzzer: Fuzz Driver Generation and Adaptive Scheduling via Multidimensional API Sequences](https://arxiv.org/abs/2604.17977) | C / 48 |
| 543 | [AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs](https://arxiv.org/abs/2607.01640) | C / 48 |
| 554 | [From Obfuscated to Obvious: A Comprehensive JavaScript Deobfuscation Tool for Security Analysis](https://arxiv.org/abs/2512.14070) | C / 47 |
| 555 | [Multi-Agent Taint Specification Extraction for Vulnerability Detection](https://arxiv.org/abs/2601.10865) | C / 47 |
| 556 | [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/abs/2605.04251) | C / 47 |
| 560 | [CITADEL: CWE-Guided Insertion of Hardware Trojans via Analysis of DFG-Enabled LLMs](https://arxiv.org/abs/2610.02544) | C / 47 |
| 565 | [TypePilot: Leveraging the Scala Type System for Secure LLM-generated Code](https://arxiv.org/abs/2510.11151) | C / 46 |
| 570 | [Mitigating False Positives in Static Memory Safety Analysis of Rust Programs via Reinforcement Learning](https://arxiv.org/abs/2605.04000) | C / 46 |
| 573 | [Chiral Analysis of Smart Contracts: Detecting Vulnerabilities from Relational Inconsistencies Across Business Paths](https://arxiv.org/abs/2607.17987) | C / 46 |
| 576 | [RustAssure: Differential Symbolic Testing for LLM-Transpiled C-to-Rust Code](https://arxiv.org/abs/2510.07604) | C / 45 |
| 578 | [USCSA: Evolution-Aware Security Analysis for Proxy-Based Upgradeable Smart Contracts](https://arxiv.org/abs/2512.08372) | C / 45 |
| 592 | [GPU-Fuzz: Finding Memory Errors in Deep Learning Frameworks](https://arxiv.org/abs/2602.10478) | D / 44 |
| 596 | [Towards LLM-Enhanced Android Taint Analysis](https://arxiv.org/abs/2608.24269) | D / 44 |
| 616 | [Validating Solidity Code Defects using Symbolic and Concrete Execution powered by Large Language Models](https://arxiv.org/abs/2509.13023) | D / 42 |
| 626 | [SemVul: Semantic-Enhanced Graph Neural Networks for Code Property Graph-based Vulnerability Detection](https://arxiv.org/abs/2609.06035) | D / 42 |
| 635 | [CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs](https://arxiv.org/abs/2606.29124) | D / 41 |
| 636 | [Comprendia: AI-Augmented Code Comprehension](https://arxiv.org/abs/2608.10290) | D / 41 |
| 666 | [FT-Pilot: Automated Fault-Tolerant RTL Rewriting via Vulnerability-Guided LLMs](https://arxiv.org/abs/2605.28169) | D / 36 |
| 668 | [What You Code Is What We Prove: Translating BLE App Logic into Formal Models with LLMs for Vulnerability Detection](https://arxiv.org/abs/2509.09291) | D / 35 |
| 672 | [Agentic Interpretation: Lattice-Structured Evidence for LLM-Based Program Analysis](https://arxiv.org/abs/2605.12694) | D / 31 |

#### prompting-only (78 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 22 | [Autonomous OSS Threat Detection via Taxonomy-Aligned LLMs](https://arxiv.org/abs/2610.01263) | B / 72 |
| 25 | [VulWeaver: Weaving Broken Semantics for Grounded Vulnerability Detection](https://arxiv.org/abs/2604.10767) | B / 71 |
| 44 | [Security Is Relative: Training-Free Vulnerability Detection via Multi-Agent Behavioral Contract Synthesis](https://arxiv.org/abs/2604.19012) | B / 69 |
| 77 | [Constitutional Spec-Driven Development: Enforcing Security by Construction in AI-Assisted Code Generation](https://arxiv.org/abs/2602.02584) | B / 66 |
| 81 | [MultiVer: Zero-Shot Multi-Agent Vulnerability Detection](https://arxiv.org/abs/2602.17875) | B / 66 |
| 112 | [Mind the Gap: Detecting Description-Execution Mismatch Attacks in DAO Governance](https://arxiv.org/abs/2609.13601) | B / 65 |
| 122 | [From Coverage to Causes: Data-Centric Fuzzing for JavaScript Engines](https://arxiv.org/abs/2512.18102) | B / 64 |
| 127 | [Using LLMs to Adjudicate Static-Analysis Alerts with Error Reduction Techniques](https://arxiv.org/abs/2607.09979) | B / 64 |
| 165 | [QuiLL: An LLM-Based Vulnerability Assessment Framework for the Wild](https://arxiv.org/abs/2510.04056) | B / 62 |
| 168 | [Retrieval-Augmented Few-Shot Prompting Versus Fine-Tuning for Code Vulnerability Detection](https://arxiv.org/abs/2512.04106) | B / 62 |
| 190 | [iCodeReviewer: Improving Secure Code Review with Mixture of Prompts](https://arxiv.org/abs/2510.12186) | B / 61 |
| 195 | [SAFuzz: Semantic-Guided Adaptive Fuzzing for LLM-Generated Code](https://arxiv.org/abs/2602.11209) | B / 61 |
| 201 | [SecureForge: Finding and Preventing Vulnerabilities in LLM-Generated Code via Prompt Optimization](https://arxiv.org/abs/2605.08382) | B / 61 |
| 234 | [Revealing Adversarial Smart Contracts through Semantic Interpretation and Uncertainty Estimation](https://arxiv.org/abs/2509.18934) | C / 59 |
| 235 | [LLMs as verification oracles for Solidity](https://arxiv.org/abs/2509.19153) | C / 59 |
| 254 | [The Language of Security: How Prompt Syntax Shapes Secure Code Generation in Open LLMs](https://arxiv.org/abs/2607.15937) | C / 59 |
| 259 | [SpiderSapien: Client-Centric Web Crawler and Security Scanner](https://arxiv.org/abs/2609.02532) | C / 59 |
| 260 | [LLMSec-AV: A Vulnerability Taxonomy and LLM-Driven Software Weakness Discovery Framework for Autonomous Vehicles](https://arxiv.org/abs/2609.09386) | C / 59 |
| 278 | [Fortifying LLM-Based Code Generation with Graph-Based Reasoning on Secure Coding Practices](https://arxiv.org/abs/2510.09682) | C / 58 |
| 283 | [SecureRAG-RTL: A Retrieval-Augmented, Multi-Agent, Zero-Shot LLM-Driven Framework for Hardware Vulnerability Detection](https://arxiv.org/abs/2603.05689) | C / 58 |
| 290 | [PromptAudit: Auditing Prompt Sensitivity in LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.24171) | C / 58 |
| 293 | [Routing Ceilings Are Domain-Independent: Structural Prior Injection in Code Security Vulnerability Detection](https://arxiv.org/abs/2607.14628) | C / 58 |
| 301 | [AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs](https://arxiv.org/abs/2609.01023) | C / 58 |
| 337 | [Diverse LLMs vs. Vulnerabilities: Who Detects and Fixes Them Better?](https://arxiv.org/abs/2512.12536) | C / 56 |
| 345 | [Tailored Prompts, Targeted Protection: Vulnerability-Specific LLM Analysis for Smart Contracts](https://arxiv.org/abs/2605.03697) | C / 56 |
| 358 | [Self-Evolving Defense: Continual Security Policy Learning for LLM Agents](https://arxiv.org/abs/2609.36603) | C / 56 |
| 362 | [SPLASH: Contrastive Audit Pressure for Detecting and Localizing Security Hallucinations in Generated Code](https://arxiv.org/abs/2610.26001) | C / 56 |
| 365 | [Evaluating Large Language Models in detecting Secrets in Android Apps](https://arxiv.org/abs/2510.18601) | C / 55 |
| 368 | [Secure Code Generation at Scale with Reflexion](https://arxiv.org/abs/2511.03898) | C / 55 |
| 389 | [SpecCloak: Probing Harmful Code Generation through Engineering Specifications](https://arxiv.org/abs/2610.17907) | C / 55 |
| 395 | [Benchmarking Zero-Shot Reasoning Approaches for Error Detection in Solidity Smart Contracts](https://arxiv.org/abs/2603.13239) | C / 54 |
| 396 | [From Theory to Practice: Code Generation Using LLMs for CAPEC and CWE Frameworks](https://arxiv.org/abs/2604.02548) | C / 54 |
| 411 | [Spoofing the Toolbox: Optimizing Tool Descriptions to Deceive LLM Agents](https://arxiv.org/abs/2610.33182) | C / 54 |
| 422 | [Llama-based source code vulnerability detection: Prompt engineering vs Fine tuning](https://arxiv.org/abs/2512.09006) | C / 53 |
| 443 | [Evaluating LLMs for Obfuscation Detection and Classification in Android Apps](https://arxiv.org/abs/2606.14233) | C / 53 |
| 447 | [Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files](https://arxiv.org/abs/2610.09264) | C / 53 |
| 471 | [LLM-HyPZ: Hardware Vulnerability Discovery using an LLM-Assisted Hybrid Platform for Zero-Shot Knowledge Extraction and Refinement](https://arxiv.org/abs/2509.00647) | C / 51 |
| 472 | [KubeGuard: LLM-Assisted Kubernetes Hardening via Configuration Files and Runtime Logs Analysis](https://arxiv.org/abs/2509.04191) | C / 51 |
| 474 | [ReVul-CoT: Towards Effective Software Vulnerability Assessment with Retrieval-Augmented Generation and Chain-of-Thought Prompting](https://arxiv.org/abs/2511.17027) | C / 51 |
| 481 | [An Empirical Security Evaluation of LLM-Generated Cryptographic Rust Code](https://arxiv.org/abs/2604.27001) | C / 51 |
| 482 | [An Empirical Evaluation of LLM-Generated Code Security Across Prompting Methods](https://arxiv.org/abs/2605.24298) | C / 51 |
| 490 | [CodeMimicry: Exploiting Safety Generalization Lag in Large Language Models via Structured Code Completion](https://arxiv.org/abs/2609.39902) | C / 51 |
| 498 | [Sift or Get Off the PoC: Applying Information Retrieval to Vulnerability Research with SiftRank](https://arxiv.org/abs/2512.06155) | C / 50 |
| 503 | [AFL-ICP: Enhancing Industrial Control Protocol Reliability via Specification-Guided Fuzzing](https://arxiv.org/abs/2605.04760) | C / 50 |
| 510 | [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](https://arxiv.org/abs/2609.02774) | C / 50 |
| 514 | [Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation](https://arxiv.org/abs/2509.19533) | C / 49 |
| 517 | [Cracking IoT Security: Can LLMs Outsmart Static Analysis Tools?](https://arxiv.org/abs/2601.00559) | C / 49 |
| 531 | [Static Analysis as a Feedback Loop: Enhancing LLM-Generated Code Beyond Correctness](https://arxiv.org/abs/2508.14419) | C / 48 |
| 532 | [PromptGuard: An Orchestrated Prompting Framework for Principled Synthetic Text Generation for Vulnerable Populations using LLMs with Enhanced Safety, Fairness, and Controllability](https://arxiv.org/abs/2509.08910) | C / 48 |
| 539 | [Following Dragons: Code Review-Guided Fuzzing](https://arxiv.org/abs/2602.10487) | C / 48 |
| 549 | [Reasoning Topology Matters: A Controlled Study of LLM-Based Cybersecurity Analysis](https://arxiv.org/abs/2609.24710) | C / 48 |
| 557 | [Enhancing Reliability in LLM-Based Secure Code Generation](https://arxiv.org/abs/2605.24300) | C / 47 |
| 558 | [Evaluating LLMs for Real-World Web Vulnerability Detection](https://arxiv.org/abs/2606.21397) | C / 47 |
| 561 | [Beware EviLLM: Enabling Vulnerability Injection via Large Language Models](https://arxiv.org/abs/2610.03857) | C / 47 |
| 575 | [Can LLMs Find Bugs in Code? An Evaluation from Beginner Errors to Security Vulnerabilities in Python and C++](https://arxiv.org/abs/2508.16419) | C / 45 |
| 576 | [RustAssure: Differential Symbolic Testing for LLM-Transpiled C-to-Rust Code](https://arxiv.org/abs/2510.07604) | C / 45 |
| 584 | [Automated Vulnerability Injection in Smart Contracts Using Large Language Models](https://arxiv.org/abs/2609.02624) | C / 45 |
| 589 | [On the Difficulty of Selecting Few-Shot Examples for Effective LLM-based Vulnerability Detection](https://arxiv.org/abs/2510.27675) | D / 44 |
| 590 | [An LLM-based Quantitative Framework for Evaluating High-Stealthy Backdoor Risks in OSS Supply Chains](https://arxiv.org/abs/2511.13341) | D / 44 |
| 599 | [Exploring Automated Vulnerability Identification in JavaScript Code Using Large Language Models](https://arxiv.org/abs/2609.13816) | D / 44 |
| 601 | [Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents](https://arxiv.org/abs/2609.39607) | D / 44 |
| 606 | [Explaining Software Vulnerabilities with Large Language Models](https://arxiv.org/abs/2511.04179) | D / 43 |
| 607 | [Evaluating LLMs for One-Shot Patching of Real and Artificial Vulnerabilities](https://arxiv.org/abs/2511.23408) | D / 43 |
| 610 | [Human in the Loop for Fuzz Testing: Literature Review and the Road Ahead](https://arxiv.org/abs/2603.13411) | D / 43 |
| 618 | [GPTrace: Effective Crash Deduplication Using LLM Embeddings](https://arxiv.org/abs/2512.01609) | D / 42 |
| 629 | [Learning from Failures: A Failure-Driven Prompt Refinement for LLM-Based Vulnerability Analysis](https://arxiv.org/abs/2610.08405) | D / 42 |
| 631 | [From LLMs to Agents: A Comparative Evaluation of LLMs and LLM-based Agents in Security Patch Detection](https://arxiv.org/abs/2511.08060) | D / 41 |
| 634 | [Investigating Metamorphic Fuzz Oracle Enhancement via Large Language Models](https://arxiv.org/abs/2606.14164) | D / 41 |
| 648 | [Prompt Engineering vs. Fine-Tuning for LLM-Based Vulnerability Detection in Solana and Algorand Smart Contracts](https://arxiv.org/abs/2511.11250) | D / 39 |
| 651 | [LLM-Assisted Detection and Repair of Hardware Security Vulnerabilities in Verilog Designs](https://arxiv.org/abs/2608.04907) | D / 39 |
| 653 | [Security of LLM-generated Code: A Comparative Analysis](https://arxiv.org/abs/2605.23091) | D / 38 |
| 656 | [Poster: Rethinking Security in LLM Code Generation through Real-World Risk Scenarios](https://arxiv.org/abs/2607.23088) | D / 38 |
| 658 | [A Prompt-Based Framework for Loop Vulnerability Detection Using Local LLMs](https://arxiv.org/abs/2601.15352) | D / 37 |
| 660 | [Secure Coding Drift in LLM-Assisted Post-Quantum Cryptography Development: A Gamified Fix](https://arxiv.org/abs/2606.19474) | D / 37 |
| 661 | [Transformer-Assisted LLM-Based Source Code Summarisation: to Enable More Secure Software Development](https://arxiv.org/abs/2607.20933) | D / 37 |
| 667 | [Towards LLM-assisted High-Quality Property Generation for Solidity Smart Contracts](https://arxiv.org/abs/2607.23308) | D / 36 |
| 670 | [From Model to Breach: Towards Actionable LLM-Generated Vulnerabilities Reporting](https://arxiv.org/abs/2511.04538) | D / 34 |
| 675 | [Investigating Security Implications of Automatically Generated Code on the Software Supply Chain](https://arxiv.org/abs/2509.20277) | D / 30 |

#### benchmark / dataset (116 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 2 | [CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability](https://arxiv.org/abs/2602.03012) | A / 76 |
| 5 | [LLMVul: A Vulnerability-Labeled Dataset of LLM-Generated C/C++ Functions from Real Production Repositories](https://arxiv.org/abs/2609.10945) | A / 76 |
| 8 | [SecureCode: A Production-Grade Multi-Turn Dataset for Training Security-Aware Code Generation Models](https://arxiv.org/abs/2512.18542) | B / 74 |
| 10 | [Does Teaming-Up LLMs Improve Secure Code Generation? A Comprehensive Evaluation with Multi-LLMSecCodeEval](https://arxiv.org/abs/2603.22717) | B / 74 |
| 11 | [ABSENTIA: Detecting Broken Access Control Vulnerabilities in Web Applications](https://arxiv.org/abs/2610.00977) | B / 74 |
| 14 | [The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark](https://arxiv.org/abs/2608.11469) | B / 73 |
| 15 | [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](https://arxiv.org/abs/2608.26882) | B / 73 |
| 16 | [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](https://arxiv.org/abs/2609.15939) | B / 73 |
| 17 | [CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices](https://arxiv.org/abs/2609.21344) | B / 73 |
| 19 | [Towards a Risk Assessment of Malicious Skill Files in Coding Agents](https://arxiv.org/abs/2608.05223) | B / 72 |
| 21 | [VEX-Bench: Benchmarking LLM Agents for Assessing Exploitability of Software Supply Chain Vulnerabilities](https://arxiv.org/abs/2609.08040) | B / 72 |
| 23 | [AVIATOR: Towards AI-Agentic Vulnerability Injection Workflow for High-Fidelity, Large-Scale Code Security Dataset](https://arxiv.org/abs/2508.20866) | B / 71 |
| 27 | [CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?](https://arxiv.org/abs/2606.26216) | B / 71 |
| 28 | [AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration](https://arxiv.org/abs/2607.12058) | B / 71 |
| 32 | [LLM Agents for Automated Web Vulnerability Reproduction: Are We There Yet?](https://arxiv.org/abs/2510.14700) | B / 70 |
| 37 | [HarnessSecurity-Bench: Do Security Mechanisms Really Protect Coding Agent Harnesses?](https://arxiv.org/abs/2610.07639) | B / 70 |
| 47 | [CS-Guard: Benchmarking LLM Guardrails for Code Generation Security](https://arxiv.org/abs/2609.09798) | B / 69 |
| 48 | [What is the Difference Between Me and You? Benchmarking the Quality Gap Between Human-Written and AI-Generated Code](https://arxiv.org/abs/2609.12708) | B / 69 |
| 49 | [MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes](https://arxiv.org/abs/2609.23980) | B / 69 |
| 50 | [A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code](https://arxiv.org/abs/2611.06294) | B / 69 |
| 54 | [The Illusion of Safety: Multi-Tier Verification of AI vs. Human C++ Code](https://arxiv.org/abs/2607.00107) | B / 68 |
| 59 | [SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios](https://arxiv.org/abs/2509.22097) | B / 67 |
| 60 | [From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localization](https://arxiv.org/abs/2510.02389) | B / 67 |
| 66 | [VulnScout-C: A Lightweight Transformer for C Code Vulnerability Detection](https://arxiv.org/abs/2603.28309) | B / 67 |
| 69 | [CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training](https://arxiv.org/abs/2608.06471) | B / 67 |
| 71 | [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075) | B / 67 |
| 74 | [Large Language Models Cannot Reliably Detect Vulnerabilities in JavaScript: The First Systematic Benchmark and Evaluation](https://arxiv.org/abs/2512.01255) | B / 66 |
| 76 | [RealSec-bench: A Benchmark for Evaluating Secure Code Generation in Real-World Repositories](https://arxiv.org/abs/2601.22706) | B / 66 |
| 87 | [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](https://arxiv.org/abs/2607.04729) | B / 66 |
| 89 | [DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2607.13439) | B / 66 |
| 90 | [Vul4Py: Benchmarking Automated Vulnerability Repair in Python with Paired Exploit and Functional Oracles](https://arxiv.org/abs/2608.00692) | B / 66 |
| 91 | [GraftyVul: Synthesising Insecure Programs Through Real-World Vulnerability Grafting](https://arxiv.org/abs/2608.27928) | B / 66 |
| 93 | [ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure?](https://arxiv.org/abs/2609.30325) | B / 66 |
| 95 | [INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems](https://arxiv.org/abs/2610.20776) | B / 66 |
| 101 | [Beyond Single Bugs: Benchmarking Large Language Models for Multi-Vulnerability Detection](https://arxiv.org/abs/2512.22306) | B / 65 |
| 107 | [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](https://arxiv.org/abs/2607.25225) | B / 65 |
| 109 | [VICBench: A Multi-Language Benchmark for Code Vulnerability Detection](https://arxiv.org/abs/2608.12246) | B / 65 |
| 126 | [ARVO: Atlas of Reproducible Vulnerabilities for Open-Source Software](https://arxiv.org/abs/2606.17283) | B / 64 |
| 131 | [SecProbe: Adaptive Evaluation of Coding Agents on Cybersecurity Vulnerabilities](https://arxiv.org/abs/2609.33763) | B / 64 |
| 135 | [CyberDual: AI Attackers versus AI Code Reviewers in Real Software Maintenance](https://arxiv.org/abs/2610.34435) | B / 64 |
| 140 | [PATCHEVAL: A New Benchmark for Evaluating LLMs on Patching Real-World Vulnerabilities](https://arxiv.org/abs/2511.11019) | B / 63 |
| 149 | [Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks](https://arxiv.org/abs/2605.23243) | B / 63 |
| 152 | [Unsaid, Unsafe? Implicit Security Obligations in LLM-Based RTL Code Generation](https://arxiv.org/abs/2608.26588) | B / 63 |
| 154 | [ReproBench: Benchmarking LLM Agents on Reproducing Vulnerability From Scratch](https://arxiv.org/abs/2609.34450) | B / 63 |
| 159 | [RegoMender: A Multi-agent Framework for Automated Rego Policy Repair](https://arxiv.org/abs/2610.29456) | B / 63 |
| 161 | [An Empirical Study of Vulnerabilities in Python Packages and Their Detection](https://arxiv.org/abs/2509.04260) | B / 62 |
| 169 | [Adaptive Hierarchical Evaluation of LLMs and SAST tools for CWE Prediction in Python](https://arxiv.org/abs/2601.01320) | B / 62 |
| 170 | [HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation](https://arxiv.org/abs/2601.13864) | B / 62 |
| 175 | [SmartEval: A Benchmark for Evaluating LLM-Generated Smart Contracts from Natural Language Specifications](https://arxiv.org/abs/2605.09610) | B / 62 |
| 176 | [From Controlled to the Wild: Evaluation of Pentesting Agents for the Real-World](https://arxiv.org/abs/2605.10834) | B / 62 |
| 178 | [CyberGym-E2E: Scalable Real-World Benchmark for AI Agents' End-to-End Cybersecurity Capabilities](https://arxiv.org/abs/2606.04460) | B / 62 |
| 181 | [SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs](https://arxiv.org/abs/2609.06149) | B / 62 |
| 183 | [Adaptive Code Revision Attacks on AI Pull Request Reviewers](https://arxiv.org/abs/2610.05399) | B / 62 |
| 186 | [Do Coding Agents Understand Why Systems Crash---and Why They Don't?](https://arxiv.org/abs/2610.29332) | B / 62 |
| 187 | [Simple Features Beat Most AI Control Monitors](https://arxiv.org/abs/2610.41713) | B / 62 |
| 196 | [Toward Scalable Automated Repository-Level Datasets for Software Vulnerability Detection](https://arxiv.org/abs/2603.17974) | B / 61 |
| 204 | [Local LLM Agents as Vulnerable Runtimes:A Source-Code Audit of the Agent Runtime Layer](https://arxiv.org/abs/2606.21071) | B / 61 |
| 229 | [JavaVulBench: A Java Vulnerability Benchmark with Realistic Splits, a Unified Multi-Backend Harness, and a Leakage-Aware Evaluation Mode](https://arxiv.org/abs/2607.02825) | B / 60 |
| 233 | [Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail](https://arxiv.org/abs/2609.39086) | B / 60 |
| 238 | [CFCEval: Evaluating Security Aspects in Code Generated by Large Language Models](https://arxiv.org/abs/2512.06248) | C / 59 |
| 240 | [Patch Validation in Automated Vulnerability Repair](https://arxiv.org/abs/2603.06858) | C / 59 |
| 242 | [Detecting Protracted Vulnerabilities in Open Source Projects](https://arxiv.org/abs/2603.27067) | C / 59 |
| 251 | [MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation](https://arxiv.org/abs/2606.11416) | C / 59 |
| 252 | [Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning](https://arxiv.org/abs/2606.25356) | C / 59 |
| 261 | [BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure](https://arxiv.org/abs/2609.11028) | C / 59 |
| 269 | [Trojan Horse: Automated Repository Poisoning against Coding Agents](https://arxiv.org/abs/2610.23109) | C / 59 |
| 274 | [Large Language Models Versus Static Code Analysis Tools: A Systematic Benchmark for Vulnerability Detection](https://arxiv.org/abs/2508.04448) | C / 58 |
| 275 | [Revisiting Third-Party Library Detection: A Ground Truth Dataset and Its Implications Across Security Tasks](https://arxiv.org/abs/2509.04091) | C / 58 |
| 277 | [Library Hallucinations in LLM-Generated Code: A Risk Analysis Grounded in Developer Queries](https://arxiv.org/abs/2509.22202) | C / 58 |
| 282 | [SecCodeBench-V2 Technical Report](https://arxiv.org/abs/2602.15485) | C / 58 |
| 291 | [Bastet: A Fine-Grained Expert-Labeled Dataset for DeFi Smart Contract Vulnerability Detection](https://arxiv.org/abs/2606.03387) | C / 58 |
| 296 | [HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models](https://arxiv.org/abs/2607.27030) | C / 58 |
| 297 | [EduPluginBench: Executable Assurance for AI-Generated Educational Plugins](https://arxiv.org/abs/2608.00739) | C / 58 |
| 303 | [AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination](https://arxiv.org/abs/2609.19140) | C / 58 |
| 309 | [A.S.E: A Repository-Level Benchmark for Evaluating Security in AI-Generated Code](https://arxiv.org/abs/2508.18106) | C / 57 |
| 318 | [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494) | C / 57 |
| 326 | [Understanding and Mitigating Cross-Session Attacks via Persistent Artifacts in Agent Skill Composition](https://arxiv.org/abs/2610.13227) | C / 57 |
| 327 | [CWE-bench: Refocusing Agentic Security from Exploitation to Defense](https://arxiv.org/abs/2610.17020) | C / 57 |
| 328 | [VulDec: Vulnerability Detection in Binaries via Neural Decompilation](https://arxiv.org/abs/2610.33716) | C / 57 |
| 338 | [Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming](https://arxiv.org/abs/2601.02060) | C / 56 |
| 339 | [STELP: Secure Transpilation and Execution of LLM-Generated Programs](https://arxiv.org/abs/2601.05467) | C / 56 |
| 342 | [Re-Evaluating EVMBench: Are AI Agents Ready for Smart Contract Security?](https://arxiv.org/abs/2603.10795) | C / 56 |
| 348 | [ASSEMBLAGE-DEEPHISTORY: A Cross-Build Binary Dataset with Temporal Coverage](https://arxiv.org/abs/2605.21615) | C / 56 |
| 349 | [On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus](https://arxiv.org/abs/2606.07363) | C / 56 |
| 360 | [CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat](https://arxiv.org/abs/2610.19005) | C / 56 |
| 377 | [EVMbench: Evaluating AI Agents on Smart Contract Security](https://arxiv.org/abs/2603.04915) | C / 55 |
| 387 | [SINGED: Correct Outputs Do Not Certify Safe Execution in LLM Agents](https://arxiv.org/abs/2609.35889) | C / 55 |
| 396 | [From Theory to Practice: Code Generation Using LLMs for CAPEC and CWE Frameworks](https://arxiv.org/abs/2604.02548) | C / 54 |
| 400 | [SEC-bench Pro: Can Language Models Solve Long-Horizon Software Security Tasks?](https://arxiv.org/abs/2605.26548) | C / 54 |
| 404 | [VulnGym: Benchmarking Coding Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2608.02001) | C / 54 |
| 406 | [Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning](https://arxiv.org/abs/2608.30686) | C / 54 |
| 408 | [Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities](https://arxiv.org/abs/2609.15963) | C / 54 |
| 410 | [ProtoArena: Can AI Agents Discover and Exploit Real-World Cross-Component Protocol Vulnerabilities?](https://arxiv.org/abs/2610.17837) | C / 54 |
| 424 | [AutoVulnPHP: LLM-Powered Two-Stage PHP Vulnerability Detection and Automated Localization](https://arxiv.org/abs/2601.06177) | C / 53 |
| 425 | [Lightweight Yet Secure: Secure Scripting Language Generation via Lightweight LLMs](https://arxiv.org/abs/2601.06419) | C / 53 |
| 438 | [MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents](https://arxiv.org/abs/2605.03952) | C / 53 |
| 440 | [Refusal Evaluation in Coding LLMs and Code Agents: A Systematic Review of Thirteen Malicious-Code Prompt Corpora (2023-2025)](https://arxiv.org/abs/2605.20351) | C / 53 |
| 452 | [VulnRepairEval: An Exploit-Based Evaluation Framework for Assessing Large Language Model Vulnerability Repair Capabilities](https://arxiv.org/abs/2509.03331) | C / 52 |
| 459 | [Evaluating and Enhancing the Vulnerability Reasoning Capabilities of Large Language Models](https://arxiv.org/abs/2602.06687) | C / 52 |
| 464 | [Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities](https://arxiv.org/abs/2605.28893) | C / 52 |
| 478 | [CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering](https://arxiv.org/abs/2604.03750) | C / 51 |
| 483 | [REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange](https://arxiv.org/abs/2606.05493) | C / 51 |
| 499 | [From Lab to Reality: A Practical Evaluation of Deep Learning Models and LLMs for Vulnerability Detection](https://arxiv.org/abs/2512.10485) | C / 50 |
| 525 | [Data-Centric Benchmarking of Exploit Generation in LLMs: Understanding the Impact of Fine-Tuning](https://arxiv.org/abs/2606.15123) | C / 49 |
| 527 | [VulnGym: Evaluating Vulnerability Management Strategies against Advanced Persistent Threats](https://arxiv.org/abs/2607.24552) | C / 49 |
| 543 | [AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs](https://arxiv.org/abs/2607.01640) | C / 48 |
| 560 | [CITADEL: CWE-Guided Insertion of Hardware Trojans via Analysis of DFG-Enabled LLMs](https://arxiv.org/abs/2610.02544) | C / 47 |
| 571 | [TUANDROMD-X: Advanced Entropy and Visual Analytics Dataset for Enhanced Malware Detection and Classification](https://arxiv.org/abs/2605.06718) | C / 46 |
| 583 | [AI Slop and Hallucinations in Vulnerability Assessment: A Survey on Reasoning Failures and Trustworthy Mitigation](https://arxiv.org/abs/2608.25667) | C / 45 |
| 584 | [Automated Vulnerability Injection in Smart Contracts Using Large Language Models](https://arxiv.org/abs/2609.02624) | C / 45 |
| 594 | [Detect--Repair--Verify for LLM-Generated Code: A Multi-Language, Multi-Granularity Empirical Study](https://arxiv.org/abs/2603.23633) | D / 44 |
| 595 | [Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions](https://arxiv.org/abs/2605.06279) | D / 44 |
| 623 | [Repository-Level Solidity Code Generation with Large Language Models: From Prompting to Fine-Tuning](https://arxiv.org/abs/2606.19988) | D / 42 |
| 638 | [RiskyPy: Toward Model-Calibrated Prompt Generation for Joint Security and Functionality Evaluation of LLM-Generated Code](https://arxiv.org/abs/2610.40735) | D / 41 |
| 639 | [AutoBaxBuilder: Bootstrapping Code Security Benchmarking](https://arxiv.org/abs/2512.21132) | D / 40 |
| 656 | [Poster: Rethinking Security in LLM Code Generation through Real-World Risk Scenarios](https://arxiv.org/abs/2607.23088) | D / 38 |

#### empirical study / survey (216 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 1 | [LLM-based Vulnerability Detection at Project Scale: An Empirical Study](https://arxiv.org/abs/2601.19239) | A / 77 |
| 10 | [Does Teaming-Up LLMs Improve Secure Code Generation? A Comprehensive Evaluation with Multi-LLMSecCodeEval](https://arxiv.org/abs/2603.22717) | B / 74 |
| 12 | [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](https://arxiv.org/abs/2611.03555) | B / 74 |
| 19 | [Towards a Risk Assessment of Malicious Skill Files in Coding Agents](https://arxiv.org/abs/2608.05223) | B / 72 |
| 29 | [From Runnable to Verifiable: An Independent Reproducibility Study of LLM/Agent-Driven Vulnerability Validation Artifacts](https://arxiv.org/abs/2608.09567) | B / 71 |
| 31 | [Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub](https://arxiv.org/abs/2610.11169) | B / 71 |
| 32 | [LLM Agents for Automated Web Vulnerability Reproduction: Are We There Yet?](https://arxiv.org/abs/2510.14700) | B / 70 |
| 36 | [Defusing Explosive Prompts: Understanding and Preventing Trigger-Based Prompt Injections in LLM Agents](https://arxiv.org/abs/2609.22510) | B / 70 |
| 37 | [HarnessSecurity-Bench: Do Security Mechanisms Really Protect Coding Agent Harnesses?](https://arxiv.org/abs/2610.07639) | B / 70 |
| 39 | [Sifting the Noise: A Comparative Study of LLM Agents in Vulnerability False Positive Filtering](https://arxiv.org/abs/2601.22952) | B / 69 |
| 47 | [CS-Guard: Benchmarking LLM Guardrails for Code Generation Security](https://arxiv.org/abs/2609.09798) | B / 69 |
| 48 | [What is the Difference Between Me and You? Benchmarking the Quality Gap Between Human-Written and AI-Generated Code](https://arxiv.org/abs/2609.12708) | B / 69 |
| 50 | [A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code](https://arxiv.org/abs/2611.06294) | B / 69 |
| 54 | [The Illusion of Safety: Multi-Tier Verification of AI vs. Human C++ Code](https://arxiv.org/abs/2607.00107) | B / 68 |
| 58 | [Proving the Wrong Program: Miscompilations as a Threat to zkVM Guarantees](https://arxiv.org/abs/2611.04701) | B / 68 |
| 71 | [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075) | B / 67 |
| 72 | [An Empirical Analysis of CodeQL False Positives and Query Refinements for Java Vulnerabilities](https://arxiv.org/abs/2609.04535) | B / 67 |
| 74 | [Large Language Models Cannot Reliably Detect Vulnerabilities in JavaScript: The First Systematic Benchmark and Evaluation](https://arxiv.org/abs/2512.01255) | B / 66 |
| 76 | [RealSec-bench: A Benchmark for Evaluating Secure Code Generation in Real-World Repositories](https://arxiv.org/abs/2601.22706) | B / 66 |
| 83 | [Seclens: Role-specific Evaluation of LLM's for security vulnerablity detection](https://arxiv.org/abs/2604.01637) | B / 66 |
| 85 | [Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software](https://arxiv.org/abs/2606.20502) | B / 66 |
| 86 | [Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection](https://arxiv.org/abs/2606.30587) | B / 66 |
| 90 | [Vul4Py: Benchmarking Automated Vulnerability Repair in Python with Paired Exploit and Functional Oracles](https://arxiv.org/abs/2608.00692) | B / 66 |
| 92 | [Reveree: Diagnosing LLM Reverse-Engineering Agents](https://arxiv.org/abs/2609.01185) | B / 66 |
| 107 | [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](https://arxiv.org/abs/2607.25225) | B / 65 |
| 110 | [When LLM Decompilers Recompile More and Preserve Less](https://arxiv.org/abs/2609.05370) | B / 65 |
| 113 | [Humans vs. Machines: A Comparison With AI Agents in Software Reverse Engineering](https://arxiv.org/abs/2610.14960) | B / 65 |
| 117 | [Ensembling Large Language Models for Code Vulnerability Detection: An Empirical Evaluation](https://arxiv.org/abs/2509.12629) | B / 64 |
| 121 | [A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection](https://arxiv.org/abs/2512.16538) | B / 64 |
| 127 | [Using LLMs to Adjudicate Static-Analysis Alerts with Error Reduction Techniques](https://arxiv.org/abs/2607.09979) | B / 64 |
| 132 | [SoK: Are LLMs Reliable at Source Code Recovery? A Taxonomy and Empirical Evaluation](https://arxiv.org/abs/2610.11556) | B / 64 |
| 134 | [Names Are Not Objects: Object-Bound Confinement for Compromised AI Coding Agents](https://arxiv.org/abs/2610.14488) | B / 64 |
| 149 | [Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks](https://arxiv.org/abs/2605.23243) | B / 63 |
| 157 | [Narratives Mislead: An Empirical Study of How LLMs Misjudge CVSS Severity in Bug Bounty Reports](https://arxiv.org/abs/2610.24623) | B / 63 |
| 161 | [An Empirical Study of Vulnerabilities in Python Packages and Their Detection](https://arxiv.org/abs/2509.04260) | B / 62 |
| 164 | [Red Teaming Program Repair Agents: When Correct Patches can Hide Vulnerabilities](https://arxiv.org/abs/2509.25894) | B / 62 |
| 168 | [Retrieval-Augmented Few-Shot Prompting Versus Fine-Tuning for Code Vulnerability Detection](https://arxiv.org/abs/2512.04106) | B / 62 |
| 169 | [Adaptive Hierarchical Evaluation of LLMs and SAST tools for CWE Prediction in Python](https://arxiv.org/abs/2601.01320) | B / 62 |
| 171 | [Formal Analysis and Supply Chain Security for Agentic AI Skills](https://arxiv.org/abs/2603.00195) | B / 62 |
| 173 | [Revisiting and Expanding the IPv6 Periphery: Global-Scale Measurement and Security Analysis](https://arxiv.org/abs/2604.19487) | B / 62 |
| 174 | [How Code Representation Shapes False-Positive Dynamics in Cross-Language LLM Vulnerability Detection](https://arxiv.org/abs/2604.27714) | B / 62 |
| 176 | [From Controlled to the Wild: Evaluation of Pentesting Agents for the Real-World](https://arxiv.org/abs/2605.10834) | B / 62 |
| 181 | [SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs](https://arxiv.org/abs/2609.06149) | B / 62 |
| 183 | [Adaptive Code Revision Attacks on AI Pull Request Reviewers](https://arxiv.org/abs/2610.05399) | B / 62 |
| 186 | [Do Coding Agents Understand Why Systems Crash---and Why They Don't?](https://arxiv.org/abs/2610.29332) | B / 62 |
| 187 | [Simple Features Beat Most AI Control Monitors](https://arxiv.org/abs/2610.41713) | B / 62 |
| 197 | [Implicit Patterns in LLM-Based Binary Analysis](https://arxiv.org/abs/2603.19138) | B / 61 |
| 198 | [Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/abs/2604.05292) | B / 61 |
| 202 | [Quality and Security Signals in AI-Generated Python Refactoring Pull Requests](https://arxiv.org/abs/2605.21453) | B / 61 |
| 208 | [When Verified Source Becomes Attack Input: Defending Smart Contracts Against LLM-Based Vulnerability Scanning](https://arxiv.org/abs/2608.28400) | B / 61 |
| 211 | [Newer and Bigger, but Safer? A Longitudinal Study of the Functionality-Security Gap in LLM-Generated Code](https://arxiv.org/abs/2610.08240) | B / 61 |
| 213 | [When File Ingestion Misleads Language Models: Measuring and Mitigating Divergences in Office Documents](https://arxiv.org/abs/2611.05806) | B / 61 |
| 215 | [Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity](https://arxiv.org/abs/2508.21634) | B / 60 |
| 222 | [Adaptive and AI-Augmented Security Testing: A Systematic Survey of Program Analysis, Feedback-Driven Testing, and Hybrid Learning-Based Approaches](https://arxiv.org/abs/2604.27000) | B / 60 |
| 224 | [Lightweight Vulnerability Detection from Code Metrics and Token Features](https://arxiv.org/abs/2605.04260) | B / 60 |
| 226 | [Dissecting the Black Box: Circuit-Level Analysis of LLM Vulnerability Detection](https://arxiv.org/abs/2605.29901) | B / 60 |
| 230 | [The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities](https://arxiv.org/abs/2607.05743) | B / 60 |
| 235 | [LLMs as verification oracles for Solidity](https://arxiv.org/abs/2509.19153) | C / 59 |
| 240 | [Patch Validation in Automated Vulnerability Repair](https://arxiv.org/abs/2603.06858) | C / 59 |
| 242 | [Detecting Protracted Vulnerabilities in Open Source Projects](https://arxiv.org/abs/2603.27067) | C / 59 |
| 250 | [Context-Based Adversarial Attacks on AI Code Generators: Vulnerability Analysis and Implications](https://arxiv.org/abs/2606.10945) | C / 59 |
| 252 | [Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning](https://arxiv.org/abs/2606.25356) | C / 59 |
| 254 | [The Language of Security: How Prompt Syntax Shapes Secure Code Generation in Open LLMs](https://arxiv.org/abs/2607.15937) | C / 59 |
| 265 | [Cheap to Hypothesize, Costly to Verify: The Defense Surface of Agentic Vulnerability Discovery](https://arxiv.org/abs/2609.35909) | C / 59 |
| 266 | [SecureVibe: Making Vibe Coding More Secure](https://arxiv.org/abs/2609.38606) | C / 59 |
| 272 | [Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains](https://arxiv.org/abs/2611.06585) | C / 59 |
| 274 | [Large Language Models Versus Static Code Analysis Tools: A Systematic Benchmark for Vulnerability Detection](https://arxiv.org/abs/2508.04448) | C / 58 |
| 275 | [Revisiting Third-Party Library Detection: A Ground Truth Dataset and Its Implications Across Security Tasks](https://arxiv.org/abs/2509.04091) | C / 58 |
| 277 | [Library Hallucinations in LLM-Generated Code: A Risk Analysis Grounded in Developer Queries](https://arxiv.org/abs/2509.22202) | C / 58 |
| 290 | [PromptAudit: Auditing Prompt Sensitivity in LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.24171) | C / 58 |
| 293 | [Routing Ceilings Are Domain-Independent: Structural Prior Injection in Code Security Vulnerability Detection](https://arxiv.org/abs/2607.14628) | C / 58 |
| 304 | [Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities](https://arxiv.org/abs/2610.29379) | C / 58 |
| 305 | [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](https://arxiv.org/abs/2610.29869) | C / 58 |
| 307 | [The Long Con on the Web: Earn-then-Exploit Fraud Attacks against Coding Agents](https://arxiv.org/abs/2611.00725) | C / 58 |
| 313 | [AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software](https://arxiv.org/abs/2512.18567) | C / 57 |
| 314 | [From SFT to RL: Demystifying the Post-Training Pipeline for LLM-based Vulnerability Detection](https://arxiv.org/abs/2602.14012) | C / 57 |
| 315 | [Reentrancy Detection in the Age of LLMs](https://arxiv.org/abs/2603.26497) | C / 57 |
| 318 | [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494) | C / 57 |
| 322 | [Evaluating Inference-Time Defenses Against Package Hallucination in LLM-Generated Code](https://arxiv.org/abs/2608.22652) | C / 57 |
| 324 | [Can escalation channels redirect reward hacking toward defect disclosure?](https://arxiv.org/abs/2608.29460) | C / 57 |
| 329 | [Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products](https://arxiv.org/abs/2610.42032) | C / 57 |
| 330 | [Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security](https://arxiv.org/abs/2611.01976) | C / 57 |
| 337 | [Diverse LLMs vs. Vulnerabilities: Who Detects and Fixes Them Better?](https://arxiv.org/abs/2512.12536) | C / 56 |
| 338 | [Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming](https://arxiv.org/abs/2601.02060) | C / 56 |
| 340 | [LLMs in Code Vulnerability Analysis: A Proof of Concept](https://arxiv.org/abs/2601.08691) | C / 56 |
| 341 | [Who Said CVE? How Vulnerability Identifiers Are Mentioned by Humans, Bots, and Agents in Pull Requests](https://arxiv.org/abs/2601.19636) | C / 56 |
| 342 | [Re-Evaluating EVMBench: Are AI Agents Ready for Smart Contract Security?](https://arxiv.org/abs/2603.10795) | C / 56 |
| 351 | [Open-Source Intelligence for Code Provenance and the Security Patterns that Separate Human and Large-Language-Model Implementations of Common Programming Tasks](https://arxiv.org/abs/2607.12524) | C / 56 |
| 354 | [Security Tests as Executable Specifications for LLM Code Generation: Benefits, Trade-offs, and Coverage Limits](https://arxiv.org/abs/2608.09740) | C / 56 |
| 356 | [How Do LLM Agents Actually Get the Flag? Trace-Level Provenance for Agentic Offensive Security Evaluation](https://arxiv.org/abs/2608.26237) | C / 56 |
| 359 | [When Talk Isn't Code: Comparing LLM Agents That Simulate and Develop Software](https://arxiv.org/abs/2610.04639) | C / 56 |
| 368 | [Secure Code Generation at Scale with Reflexion](https://arxiv.org/abs/2511.03898) | C / 55 |
| 370 | [HarnessAgent: Scaling Automatic Fuzzing Harness Construction with Tool-Augmented LLM Pipelines](https://arxiv.org/abs/2512.03420) | C / 55 |
| 371 | [An Empirical Evaluation of LLM-Based Approaches for Code Vulnerability Detection: RAG, SFT, and Dual-Agent Systems](https://arxiv.org/abs/2601.00254) | C / 55 |
| 372 | [SSR: Safeguarding Staking Rewards by Defining and Detecting Logical Defects in DeFi Staking](https://arxiv.org/abs/2601.05827) | C / 55 |
| 374 | [Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation](https://arxiv.org/abs/2602.04195) | C / 55 |
| 383 | [ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers](https://arxiv.org/abs/2609.19722) | C / 55 |
| 385 | [LLM Agents Can Easily Tamper With Their Own Traces](https://arxiv.org/abs/2609.30266) | C / 55 |
| 388 | [The Innocent Courier: Covert Exfiltration Through Legitimate LLM Web Fetching](https://arxiv.org/abs/2610.01768) | C / 55 |
| 389 | [SpecCloak: Probing Harmful Code Generation through Engineering Specifications](https://arxiv.org/abs/2610.17907) | C / 55 |
| 394 | [One Signature, Multiple Payments: Demystifying and Detecting Signature Replay Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2511.09134) | C / 54 |
| 395 | [Benchmarking Zero-Shot Reasoning Approaches for Error Detection in Solidity Smart Contracts](https://arxiv.org/abs/2603.13239) | C / 54 |
| 399 | [Benchmarking LLM-Based Static Analysis for Secure Smart Contract Development: Reliability, Limitations, and Potential Hybrid Solutions](https://arxiv.org/abs/2605.11163) | C / 54 |
| 402 | [Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform](https://arxiv.org/abs/2606.26590) | C / 54 |
| 404 | [VulnGym: Benchmarking Coding Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2608.02001) | C / 54 |
| 405 | [SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills](https://arxiv.org/abs/2608.08468) | C / 54 |
| 406 | [Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning](https://arxiv.org/abs/2608.30686) | C / 54 |
| 407 | [Why Is SHAP Not a Reliable Standalone Explanation Framework for Malware Detection?](https://arxiv.org/abs/2609.04626) | C / 54 |
| 408 | [Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities](https://arxiv.org/abs/2609.15963) | C / 54 |
| 413 | [On the Evaluation of Large Language Models in Multilingual Vulnerability Repair](https://arxiv.org/abs/2508.03470) | C / 53 |
| 414 | [From Attack Descriptions to Vulnerabilities: A Sentence Transformer-Based Approach](https://arxiv.org/abs/2509.02077) | C / 53 |
| 415 | [Cross-Domain Evaluation of Transformer-Based Vulnerability Detection on Open & Industry Data](https://arxiv.org/abs/2509.09313) | C / 53 |
| 426 | [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/abs/2601.10338) | C / 53 |
| 427 | [Do Fine-Tuned LLMs Understand Vulnerabilities? An Investigation into the Semantic Trap](https://arxiv.org/abs/2601.22655) | C / 53 |
| 435 | [A systematic literature Review for Transformer-based Software Vulnerability detection](https://arxiv.org/abs/2604.24822) | C / 53 |
| 437 | [Identifying and Characterizing Semantic Clones of Solidity Functions](https://arxiv.org/abs/2604.26526) | C / 53 |
| 439 | [Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection](https://arxiv.org/abs/2605.20051) | C / 53 |
| 440 | [Refusal Evaluation in Coding LLMs and Code Agents: A Systematic Review of Thirteen Malicious-Code Prompt Corpora (2023-2025)](https://arxiv.org/abs/2605.20351) | C / 53 |
| 441 | [R+R: Reassessing Java Security API Misuse in Current LLMs: A Replication on JCA and JSSE APIs with External Security Knowledge](https://arxiv.org/abs/2605.31135) | C / 53 |
| 443 | [Evaluating LLMs for Obfuscation Detection and Classification in Android Apps](https://arxiv.org/abs/2606.14233) | C / 53 |
| 445 | [Large Language Models at the Intersection of Software Engineering and Software Security: An Evidence-Centered Structured Survey and Research Agenda](https://arxiv.org/abs/2608.21107) | C / 53 |
| 448 | [Natural Code Transformation Confuses Agents in Vulnerability Analysis](https://arxiv.org/abs/2610.14350) | C / 53 |
| 451 | [Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis](https://arxiv.org/abs/2508.14727) | C / 52 |
| 459 | [Evaluating and Enhancing the Vulnerability Reasoning Capabilities of Large Language Models](https://arxiv.org/abs/2602.06687) | C / 52 |
| 464 | [Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities](https://arxiv.org/abs/2605.28893) | C / 52 |
| 465 | [An Empirical Study of Security Calibration in Large Language Models for Code](https://arxiv.org/abs/2606.31159) | C / 52 |
| 467 | [Shortcutting the Fix: Identifying and Categorizing Agentic Exploits in Software Engineering Benchmarks](https://arxiv.org/abs/2609.06780) | C / 52 |
| 469 | [Trajectory-Level Security Debt in LLM Coding Agents](https://arxiv.org/abs/2609.35199) | C / 52 |
| 473 | [Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories](https://arxiv.org/abs/2510.26103) | C / 51 |
| 479 | [Vulnerability Detection with Interprocedural Context in Multiple Languages: Assessing Effectiveness and Cost of Modern LLMs](https://arxiv.org/abs/2604.08417) | C / 51 |
| 481 | [An Empirical Security Evaluation of LLM-Generated Cryptographic Rust Code](https://arxiv.org/abs/2604.27001) | C / 51 |
| 482 | [An Empirical Evaluation of LLM-Generated Code Security Across Prompting Methods](https://arxiv.org/abs/2605.24298) | C / 51 |
| 483 | [REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange](https://arxiv.org/abs/2606.05493) | C / 51 |
| 484 | [Reinforcement Learning for Software Vulnerability Analysis: A Systematic Review with Emphasis on C/C++ Source Code and Static Analysis](https://arxiv.org/abs/2606.28403) | C / 51 |
| 486 | [Prompt Structure Redistributes, Not Reduces: An Empirical Analysis of Security-Weaknesses in LLM-Generated Python Code](https://arxiv.org/abs/2608.24857) | C / 51 |
| 487 | [Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape](https://arxiv.org/abs/2609.20614) | C / 51 |
| 489 | [API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary](https://arxiv.org/abs/2609.33371) | C / 51 |
| 497 | [Can LLMs Recover Program Semantics? A Systematic Evaluation with Symbolic Execution](https://arxiv.org/abs/2511.19130) | C / 50 |
| 499 | [From Lab to Reality: A Practical Evaluation of Deep Learning Models and LLMs for Vulnerability Detection](https://arxiv.org/abs/2512.10485) | C / 50 |
| 501 | [Can Adversarial Code Comments Fool AI Security Reviewers -- Large-Scale Empirical Study of Comment-Based Attacks and Defenses Against LLM Code Analysis](https://arxiv.org/abs/2602.16741) | C / 50 |
| 502 | [Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review](https://arxiv.org/abs/2603.18740) | C / 50 |
| 504 | [PickleFuzzer: A Case Study in Fuzzing for Discrepancies Between Python Pickle Implementations](https://arxiv.org/abs/2605.15084) | C / 50 |
| 507 | [Beyond Refusal: A Same-Lineage Study of Aligned and Abliterated LLMs for Vulnerability Analysis](https://arxiv.org/abs/2607.05842) | C / 50 |
| 509 | [When Context Gets Root: Privilege Escalation in LLM Harnesses](https://arxiv.org/abs/2608.27299) | C / 50 |
| 517 | [Cracking IoT Security: Can LLMs Outsmart Static Analysis Tools?](https://arxiv.org/abs/2601.00559) | C / 49 |
| 522 | [PLMGH: What Matters in PLM-GNN Hybrids for Code Classification and Vulnerability Detection](https://arxiv.org/abs/2604.25599) | C / 49 |
| 523 | [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](https://arxiv.org/abs/2606.04739) | C / 49 |
| 533 | [LLM-based Vulnerability Discovery through the Lens of Code Metrics](https://arxiv.org/abs/2509.19117) | C / 48 |
| 535 | [Supporting Students in Navigating LLM-Generated Insecure Code](https://arxiv.org/abs/2511.20878) | C / 48 |
| 536 | [UncertaintyZoo: A Unified Toolkit for Quantifying Predictive Uncertainty in Deep Learning Systems](https://arxiv.org/abs/2512.06406) | C / 48 |
| 544 | [Understanding the Impact of AI Code Assistants on Security API Usage: An Empirical Study](https://arxiv.org/abs/2607.11348) | C / 48 |
| 547 | [Authority Is Not a String: A Capability-Scoped Harness for Prompt-Injection-Resistant Coding Agents](https://arxiv.org/abs/2609.08371) | C / 48 |
| 548 | [Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks](https://arxiv.org/abs/2609.17817) | C / 48 |
| 549 | [Reasoning Topology Matters: A Controlled Study of LLM-Based Cybersecurity Analysis](https://arxiv.org/abs/2609.24710) | C / 48 |
| 550 | [From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)](https://arxiv.org/abs/2610.20437) | C / 48 |
| 551 | [Federated Learning for Malware Image Classification under Data Heterogeneity](https://arxiv.org/abs/2610.25264) | C / 48 |
| 552 | [When Code Crosses Borders: A Security-Centric Study of LLM-based Code Translation](https://arxiv.org/abs/2509.06504) | C / 47 |
| 557 | [Enhancing Reliability in LLM-Based Secure Code Generation](https://arxiv.org/abs/2605.24300) | C / 47 |
| 558 | [Evaluating LLMs for Real-World Web Vulnerability Detection](https://arxiv.org/abs/2606.21397) | C / 47 |
| 562 | [Optimizing Code Embeddings and ML Classifiers for Python Source Code Vulnerability Detection](https://arxiv.org/abs/2509.13134) | C / 46 |
| 563 | [Revisiting Vulnerability Patch Localization: An Empirical Study and LLM-Based Solution](https://arxiv.org/abs/2509.15777) | C / 46 |
| 564 | [SoK: Potentials and Challenges of Large Language Models for Reverse Engineering](https://arxiv.org/abs/2509.21821) | C / 46 |
| 569 | [An Empirical Study of the Imbalance Issue in Software Vulnerability Detection](https://arxiv.org/abs/2602.12038) | C / 46 |
| 572 | [Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge](https://arxiv.org/abs/2607.10221) | C / 46 |
| 575 | [Can LLMs Find Bugs in Code? An Evaluation from Beginner Errors to Security Vulnerabilities in Python and C++](https://arxiv.org/abs/2508.16419) | C / 45 |
| 579 | [The Role of AI in Modern Penetration Testing](https://arxiv.org/abs/2512.12326) | C / 45 |
| 580 | [Persistent Human Feedback, LLMs, and Static Analyzers for Secure Code Generation and Vulnerability Detection](https://arxiv.org/abs/2602.05868) | C / 45 |
| 582 | [Towards Robust Personalized Federated Learning: Vulnerability Assessment and Defense Co-Design](https://arxiv.org/abs/2606.22782) | C / 45 |
| 583 | [AI Slop and Hallucinations in Vulnerability Assessment: A Survey on Reasoning Failures and Trustworthy Mitigation](https://arxiv.org/abs/2608.25667) | C / 45 |
| 586 | [Can We Trust the AI Pair Programmer? Copilot for API Misuse Detection and Correction](https://arxiv.org/abs/2509.16795) | D / 44 |
| 588 | [Evaluating Line-level Localization Ability of Learning-based Code Vulnerability Detection Models](https://arxiv.org/abs/2510.11202) | D / 44 |
| 590 | [An LLM-based Quantitative Framework for Evaluating High-Stealthy Backdoor Risks in OSS Supply Chains](https://arxiv.org/abs/2511.13341) | D / 44 |
| 591 | [WildCode Revisited: A Comprehensive Empirical Study on the Security of LLM-Generated Code](https://arxiv.org/abs/2512.04259) | D / 44 |
| 594 | [Detect--Repair--Verify for LLM-Generated Code: A Multi-Language, Multi-Granularity Empirical Study](https://arxiv.org/abs/2603.23633) | D / 44 |
| 595 | [Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions](https://arxiv.org/abs/2605.06279) | D / 44 |
| 597 | [Vulnerable Code Search: Transferable Attack for Code Language Models](https://arxiv.org/abs/2608.26031) | D / 44 |
| 599 | [Exploring Automated Vulnerability Identification in JavaScript Code Using Large Language Models](https://arxiv.org/abs/2609.13816) | D / 44 |
| 603 | [Web3 x AI Agents: Landscape, Integrations, and Foundational Challenges](https://arxiv.org/abs/2508.02773) | D / 43 |
| 604 | [Detecting Stealthy Data Poisoning Attacks in AI Code Generators](https://arxiv.org/abs/2508.21636) | D / 43 |
| 605 | [HFuzzer: Testing Large Language Models for Package Hallucinations via Phrase-based Fuzzing](https://arxiv.org/abs/2509.23835) | D / 43 |
| 606 | [Explaining Software Vulnerabilities with Large Language Models](https://arxiv.org/abs/2511.04179) | D / 43 |
| 607 | [Evaluating LLMs for One-Shot Patching of Real and Artificial Vulnerabilities](https://arxiv.org/abs/2511.23408) | D / 43 |
| 609 | [Deep Learning-based Binary Analysis for Vulnerability Detection in x86-64 Machine Code](https://arxiv.org/abs/2601.09157) | D / 43 |
| 610 | [Human in the Loop for Fuzz Testing: Literature Review and the Road Ahead](https://arxiv.org/abs/2603.13411) | D / 43 |
| 611 | [Minimal Prompt Perturbations Lead to Code Vulnerabilities: Prompt Fragility and Hidden-State Signals in Coding LLMs](https://arxiv.org/abs/2605.29737) | D / 43 |
| 612 | [Acoda: Adversarial Code Obfuscation for Defending against LLM-based Analysis](https://arxiv.org/abs/2606.11755) | D / 43 |
| 613 | [A Comparison of Malware Image Transformations Using Grad-CAM and Hybrid Learning Models](https://arxiv.org/abs/2608.12077) | D / 43 |
| 615 | [A Study of the Reliability of Agentic AI-Generated Programs](https://arxiv.org/abs/2609.18298) | D / 43 |
| 619 | [On the Effectiveness of Instruction-Tuning Local LLMs for Identifying Software Vulnerabilities](https://arxiv.org/abs/2512.20062) | D / 42 |
| 620 | [When Labels Are Scarce: A Systematic Mapping of Label-Efficient Code Vulnerability Detection](https://arxiv.org/abs/2604.00079) | D / 42 |
| 623 | [Repository-Level Solidity Code Generation with Large Language Models: From Prompting to Fine-Tuning](https://arxiv.org/abs/2606.19988) | D / 42 |
| 624 | [Understanding the (In)Security of Vibe-Coded Applications](https://arxiv.org/abs/2606.23130) | D / 42 |
| 625 | [Security Vulnerability Patterns in AI-Generated Code: A Cross-Model Comparative Study](https://arxiv.org/abs/2607.20713) | D / 42 |
| 627 | [Evaluating the NIST Bugs Framework Against CWE as a Successor for Automated Vulnerability Classification](https://arxiv.org/abs/2609.16433) | D / 42 |
| 631 | [From LLMs to Agents: A Comparative Evaluation of LLMs and LLM-based Agents in Security Patch Detection](https://arxiv.org/abs/2511.08060) | D / 41 |
| 632 | [LLM-CSEC: Empirical Evaluation of Security in C/C++ Code Generated by Large Language Models](https://arxiv.org/abs/2511.18966) | D / 41 |
| 641 | [From Preventive to Reactive: How AI Coding Assistants Transform Developers' Security Awareness](https://arxiv.org/abs/2605.23130) | D / 40 |
| 642 | [Helpful or Harmful? Evaluating LLM-Assisted Vulnerability Patching via a Human Study](https://arxiv.org/abs/2606.25973) | D / 40 |
| 644 | [Cross-Cutting Security Analysis of LLM-Generated Code via Metamorphic Testing and Association Rule Mining](https://arxiv.org/abs/2607.12089) | D / 40 |
| 646 | [Vibe Coding in Practice: Motivations, Challenges, and a Future Outlook -- a Grey Literature Review](https://arxiv.org/abs/2510.00328) | D / 39 |
| 647 | [Death by a Thousand Prompts: Open Model Vulnerability Analysis](https://arxiv.org/abs/2511.03247) | D / 39 |
| 649 | [Evaluating the Vulnerability Landscape of LLM-Generated Smart Contracts](https://arxiv.org/abs/2602.04039) | D / 39 |
| 653 | [Security of LLM-generated Code: A Comparative Analysis](https://arxiv.org/abs/2605.23091) | D / 38 |
| 654 | [SoK: AI-Augmented Binary Reversing](https://arxiv.org/abs/2606.17398) | D / 38 |
| 655 | [Advanced Topic Modeling Techniques for Categorizing Software Vulnerabilities](https://arxiv.org/abs/2607.03887) | D / 38 |
| 659 | [A Quasi-Experimental Developer Study of Security Training in LLM-Assisted Web Application Development](https://arxiv.org/abs/2604.17763) | D / 37 |
| 661 | [Transformer-Assisted LLM-Based Source Code Summarisation: to Enable More Secure Software Development](https://arxiv.org/abs/2607.20933) | D / 37 |
| 662 | [When Machine Learning Meets Vulnerability Discovery: Challenges and Lessons Learned](https://arxiv.org/abs/2508.15042) | D / 36 |
| 663 | [Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias](https://arxiv.org/abs/2508.17361) | D / 36 |
| 664 | [Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation](https://arxiv.org/abs/2603.10072) | D / 36 |
| 669 | [An Empirical Study on Remote Code Execution in Machine Learning Model Hosting Ecosystems](https://arxiv.org/abs/2601.14163) | D / 35 |
| 670 | [From Model to Breach: Towards Actionable LLM-Generated Vulnerabilities Reporting](https://arxiv.org/abs/2511.04538) | D / 34 |
| 671 | [Measuring the Security of the Evolving Software Supply Chain: a Research Agenda](https://arxiv.org/abs/2609.08810) | D / 32 |
| 673 | [Compile-time Security Analysis and Optimization of Sensitive String Producers](https://arxiv.org/abs/2605.16561) | D / 31 |
| 675 | [Investigating Security Implications of Automatically Generated Code on the Software Supply Chain](https://arxiv.org/abs/2509.20277) | D / 30 |
| 676 | [Automatically Attacking Software Reverse Engineering AI Agents](https://arxiv.org/abs/2605.30667) | D / 29 |

### 任务 Axis

#### detection (366 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 1 | [LLM-based Vulnerability Detection at Project Scale: An Empirical Study](https://arxiv.org/abs/2601.19239) | A / 77 |
| 4 | [Antaeus: Hunting Repository-Level Logic Vulnerabilities via Context-Grounded LLM Reasoning](https://arxiv.org/abs/2607.01138) | A / 76 |
| 5 | [LLMVul: A Vulnerability-Labeled Dataset of LLM-Generated C/C++ Functions from Real Production Repositories](https://arxiv.org/abs/2609.10945) | A / 76 |
| 6 | [OpenAnt: LLM-Powered Vulnerability Discovery Through Code Decomposition, Adversarial Verification, and Dynamic Testing](https://arxiv.org/abs/2606.19149) | A / 75 |
| 11 | [ABSENTIA: Detecting Broken Access Control Vulnerabilities in Web Applications](https://arxiv.org/abs/2610.00977) | B / 74 |
| 13 | [VCAO: Verifier-Centered Agentic Orchestration for Strategic OS Vulnerability Discovery](https://arxiv.org/abs/2604.08291) | B / 73 |
| 18 | [Secure Code Generation via Online Reinforcement Learning with Vulnerability Reward Model](https://arxiv.org/abs/2602.07422) | B / 72 |
| 20 | [ARQ: Agentic CodeQL Query Refinement for C/C++ Vulnerability Detection](https://arxiv.org/abs/2608.20637) | B / 72 |
| 22 | [Autonomous OSS Threat Detection via Taxonomy-Aligned LLMs](https://arxiv.org/abs/2610.01263) | B / 72 |
| 23 | [AVIATOR: Towards AI-Agentic Vulnerability Injection Workflow for High-Fidelity, Large-Scale Code Security Dataset](https://arxiv.org/abs/2508.20866) | B / 71 |
| 24 | [Multi-Agent End-to-End Vulnerability Management for Mitigating Recurring Vulnerabilities](https://arxiv.org/abs/2601.17762) | B / 71 |
| 25 | [VulWeaver: Weaving Broken Semantics for Grounded Vulnerability Detection](https://arxiv.org/abs/2604.10767) | B / 71 |
| 30 | [The History Is the Detector: Executing CVE Patch History, End-to-End](https://arxiv.org/abs/2609.05335) | B / 71 |
| 33 | [Enhancing Continual Learning for Software Vulnerability Prediction: Addressing Catastrophic Forgetting via Hybrid-Confidence-Aware Selective Replay for Temporal LLM Fine-Tuning](https://arxiv.org/abs/2602.23834) | B / 70 |
| 34 | [VulnAgent-R2: Evidence-Calibrated Multi-Agent Auditing for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2603.13384) | B / 70 |
| 35 | [Agent Audit: A Security AnalS System for LLM Agent Applications](https://arxiv.org/abs/2603.22853) | B / 70 |
| 36 | [Defusing Explosive Prompts: Understanding and Preventing Trigger-Based Prompt Injections in LLM Agents](https://arxiv.org/abs/2609.22510) | B / 70 |
| 38 | [VULSOLVER: Vulnerability Detection via LLM-Driven Constraint Solving](https://arxiv.org/abs/2509.00882) | B / 69 |
| 39 | [Sifting the Noise: A Comparative Study of LLM Agents in Vulnerability False Positive Filtering](https://arxiv.org/abs/2601.22952) | B / 69 |
| 40 | [LogicScan: An LLM-driven Framework for Detecting Business Logic Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2602.03271) | B / 69 |
| 42 | [Automated Vulnerability Detection in Source Code Using Deep Representation Learning](https://arxiv.org/abs/2602.23121) | B / 69 |
| 44 | [Security Is Relative: Training-Free Vulnerability Detection via Multi-Agent Behavioral Contract Synthesis](https://arxiv.org/abs/2604.19012) | B / 69 |
| 49 | [MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes](https://arxiv.org/abs/2609.23980) | B / 69 |
| 52 | [RuleForge: Automated Generation and Validation for Web Vulnerability Detection at Scale](https://arxiv.org/abs/2604.01977) | B / 68 |
| 55 | [IntentFuzz: A Protocol-Aware Fuzzer for Automated Invariant Violation Detection in Intent-Based Cross-Chain Bridges](https://arxiv.org/abs/2609.13004) | B / 68 |
| 56 | [Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security](https://arxiv.org/abs/2610.24896) | B / 68 |
| 60 | [From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localization](https://arxiv.org/abs/2510.02389) | B / 67 |
| 63 | [VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection](https://arxiv.org/abs/2512.07533) | B / 67 |
| 65 | [AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection](https://arxiv.org/abs/2601.19138) | B / 67 |
| 66 | [VulnScout-C: A Lightweight Transformer for C Code Vulnerability Detection](https://arxiv.org/abs/2603.28309) | B / 67 |
| 67 | [Agentic Vulnerability Reasoning on COTS Binaries](https://arxiv.org/abs/2605.05000) | B / 67 |
| 68 | [FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction](https://arxiv.org/abs/2605.21779) | B / 67 |
| 72 | [An Empirical Analysis of CodeQL False Positives and Query Refinements for Java Vulnerabilities](https://arxiv.org/abs/2609.04535) | B / 67 |
| 73 | [From Instructions to Exploits: Applying Program Analysis to Malicious Agent Skills Across Natural Language and Code](https://arxiv.org/abs/2610.33489) | B / 67 |
| 74 | [Large Language Models Cannot Reliably Detect Vulnerabilities in JavaScript: The First Systematic Benchmark and Evaluation](https://arxiv.org/abs/2512.01255) | B / 66 |
| 75 | [CKG-LLM: LLM-Assisted Detection of Smart Contract Access Control Vulnerabilities Based on Knowledge Graphs](https://arxiv.org/abs/2512.06846) | B / 66 |
| 78 | [Co-RedTeam: Orchestrated Security Discovery and Exploitation with LLM Agents](https://arxiv.org/abs/2602.02164) | B / 66 |
| 79 | [Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection](https://arxiv.org/abs/2602.06751) | B / 66 |
| 81 | [MultiVer: Zero-Shot Multi-Agent Vulnerability Detection](https://arxiv.org/abs/2602.17875) | B / 66 |
| 82 | [Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization](https://arxiv.org/abs/2603.26270) | B / 66 |
| 83 | [Seclens: Role-specific Evaluation of LLM's for security vulnerablity detection](https://arxiv.org/abs/2604.01637) | B / 66 |
| 84 | [Three Heads Are Better Than One: A Multi-perspective Reasoning Framework for Enhanced Vulnerability Detection](https://arxiv.org/abs/2605.18153) | B / 66 |
| 85 | [Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software](https://arxiv.org/abs/2606.20502) | B / 66 |
| 86 | [Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection](https://arxiv.org/abs/2606.30587) | B / 66 |
| 87 | [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](https://arxiv.org/abs/2607.04729) | B / 66 |
| 88 | [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](https://arxiv.org/abs/2607.12316) | B / 66 |
| 89 | [DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2607.13439) | B / 66 |
| 94 | [SmartMemory: Detecting On-chain-off-chain Communication Inconsistency for Smart Contract via Memory-based Agent](https://arxiv.org/abs/2609.34983) | B / 66 |
| 96 | [Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models](https://arxiv.org/abs/2610.35829) | B / 66 |
| 98 | [CryptoScope: Utilizing Large Language Models for Automated Cryptographic Logic Vulnerability Detection](https://arxiv.org/abs/2508.11599) | B / 65 |
| 100 | [Multi-LLM Energy Reasoning for Binary-Free Zero-Day IoT Detection](https://arxiv.org/abs/2512.19945) | B / 65 |
| 101 | [Beyond Single Bugs: Benchmarking Large Language Models for Multi-Vulnerability Detection](https://arxiv.org/abs/2512.22306) | B / 65 |
| 102 | [VulReaD: Knowledge-Graph-guided Software Vulnerability Reasoning and Detection](https://arxiv.org/abs/2602.10787) | B / 65 |
| 103 | [Securing the Dark Matter: A Semantic-Enhanced Neuro-Symbolic Framework for Supply Chain Analysis of Opaque Industrial Software](https://arxiv.org/abs/2605.07737) | B / 65 |
| 104 | [Security in a Workflow: Exploring Role-Based Agentic Architectures for Vulnerability Handling](https://arxiv.org/abs/2606.14261) | B / 65 |
| 109 | [VICBench: A Multi-Language Benchmark for Code Vulnerability Detection](https://arxiv.org/abs/2608.12246) | B / 65 |
| 111 | [Function Name Is All You Need to Detect Blockchain Application Attacks](https://arxiv.org/abs/2609.12315) | B / 65 |
| 112 | [Mind the Gap: Detecting Description-Execution Mismatch Attacks in DAO Governance](https://arxiv.org/abs/2609.13601) | B / 65 |
| 114 | [SEMPRE: Semantic-Aware Protocol Reverse Engineering via Consistency-Driven Joint Optimization](https://arxiv.org/abs/2610.31844) | B / 65 |
| 116 | [VulRTex: A Reasoning-Guided Approach to Identify Vulnerabilities from Rich-Text Issue Report](https://arxiv.org/abs/2509.03875) | B / 64 |
| 117 | [Ensembling Large Language Models for Code Vulnerability Detection: An Empirical Evaluation](https://arxiv.org/abs/2509.12629) | B / 64 |
| 119 | [Hybrid Fuzzing with LLM-Guided Input Mutation and Semantic Feedback](https://arxiv.org/abs/2511.03995) | B / 64 |
| 120 | [VulInstruct: Teaching LLMs Root-Cause Reasoning for Vulnerability Detection via Security Specifications](https://arxiv.org/abs/2511.04014) | B / 64 |
| 121 | [A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection](https://arxiv.org/abs/2512.16538) | B / 64 |
| 123 | [Synergistic Directed Execution and LLM-Driven Analysis for Zero-Day AI-Generated Malware Detection](https://arxiv.org/abs/2603.09044) | B / 64 |
| 124 | [EvoPoC: Automated Exploit Synthesis for DeFi Smart Contracts via Hierarchical Knowledge Graphs](https://arxiv.org/abs/2605.02868) | B / 64 |
| 128 | [Memoir: Learning, Verifying, and Evolving False-Positive Memories for Static Application Security Testing Tools](https://arxiv.org/abs/2608.09181) | B / 64 |
| 130 | [From Component Snapshots to Lifecycle Traces: Agent-Based Software Composition Analysis](https://arxiv.org/abs/2609.18391) | B / 64 |
| 133 | [ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary](https://arxiv.org/abs/2610.13651) | B / 64 |
| 136 | [VulAgent: Hypothesis-Validation based Multi-Agent Vulnerability Detection](https://arxiv.org/abs/2509.11523) | B / 63 |
| 138 | [LLM-Powered Detection of Price Manipulation in DeFi](https://arxiv.org/abs/2510.21272) | B / 63 |
| 139 | [LLM-Driven Adaptive Source-Sink Identification and False Positive Mitigation for Static Analysis](https://arxiv.org/abs/2511.04023) | B / 63 |
| 142 | [AEGIS: From Clues to Verdicts -- Graph-Guided Deep Vulnerability Reasoning via Dialectics and Meta-Auditing](https://arxiv.org/abs/2603.20637) | B / 63 |
| 143 | [Software Vulnerability Detection Using a Lightweight Graph Neural Network](https://arxiv.org/abs/2603.29216) | B / 63 |
| 144 | [A Multi-Agent Framework for Automated Exploit Generation with Constraint-Guided Comprehension and Reflection](https://arxiv.org/abs/2604.05130) | B / 63 |
| 145 | [Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection](https://arxiv.org/abs/2604.21282) | B / 63 |
| 146 | [VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.09461) | B / 63 |
| 147 | [Veritas: Grounding LLM Agents for Reliable Vulnerability Reasoning over Stripped Binaries](https://arxiv.org/abs/2605.15097) | B / 63 |
| 149 | [Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks](https://arxiv.org/abs/2605.23243) | B / 63 |
| 150 | [Code-Augur: Agentic Vulnerability Detection via Specification Inference](https://arxiv.org/abs/2606.18619) | B / 63 |
| 151 | [ShadowProbe: Language-Extensible Detection of Hidden Algorithmic Complexity Vulnerabilities](https://arxiv.org/abs/2607.05474) | B / 63 |
| 156 | [Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents](https://arxiv.org/abs/2609.39065) | B / 63 |
| 161 | [An Empirical Study of Vulnerabilities in Python Packages and Their Detection](https://arxiv.org/abs/2509.04260) | B / 62 |
| 162 | [LLM-Driven SAST-Genius: A Hybrid Static Analysis Framework for Comprehensive and Actionable Security](https://arxiv.org/abs/2509.15433) | B / 62 |
| 163 | [LISA Technical Report: An Agentic Framework for Smart Contract Auditing](https://arxiv.org/abs/2509.24698) | B / 62 |
| 165 | [QuiLL: An LLM-Based Vulnerability Assessment Framework for the Wild](https://arxiv.org/abs/2510.04056) | B / 62 |
| 166 | [Trace: Securing Smart Contract Repository Against Access Control Vulnerability](https://arxiv.org/abs/2510.19254) | B / 62 |
| 168 | [Retrieval-Augmented Few-Shot Prompting Versus Fine-Tuning for Code Vulnerability Detection](https://arxiv.org/abs/2512.04106) | B / 62 |
| 169 | [Adaptive Hierarchical Evaluation of LLMs and SAST tools for CWE Prediction in Python](https://arxiv.org/abs/2601.01320) | B / 62 |
| 171 | [Formal Analysis and Supply Chain Security for Agentic AI Skills](https://arxiv.org/abs/2603.00195) | B / 62 |
| 172 | [Detecting Data Poisoning in Code Generation LLMs via Black-Box, Vulnerability-Oriented Scanning](https://arxiv.org/abs/2603.17174) | B / 62 |
| 173 | [Revisiting and Expanding the IPv6 Periphery: Global-Scale Measurement and Security Analysis](https://arxiv.org/abs/2604.19487) | B / 62 |
| 174 | [How Code Representation Shapes False-Positive Dynamics in Cross-Language LLM Vulnerability Detection](https://arxiv.org/abs/2604.27714) | B / 62 |
| 179 | [Detecting Vulnerability-Inducing Commits via Multi-Stage Reasoning with LLM-Based Agents](https://arxiv.org/abs/2607.05772) | B / 62 |
| 180 | [Checked-In Secret Detection: Strings Are All You Need](https://arxiv.org/abs/2608.04523) | B / 62 |
| 181 | [SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs](https://arxiv.org/abs/2609.06149) | B / 62 |
| 184 | [LLM-based Code Auditing by Inferring and Evaluating Developer Assumptions](https://arxiv.org/abs/2610.15729) | B / 62 |
| 187 | [Simple Features Beat Most AI Control Monitors](https://arxiv.org/abs/2610.41713) | B / 62 |
| 188 | [Agentic Discovery and Validation of Android App Vulnerabilities](https://arxiv.org/abs/2508.21579) | B / 61 |
| 191 | [Leveraging Self-Paced Learning for Software Vulnerability Detection](https://arxiv.org/abs/2511.09212) | B / 61 |
| 194 | [QRS: A Rule-Synthesizing Neuro-Symbolic Triad for Autonomous Vulnerability Discovery](https://arxiv.org/abs/2602.09774) | B / 61 |
| 196 | [Toward Scalable Automated Repository-Level Datasets for Software Vulnerability Detection](https://arxiv.org/abs/2603.17974) | B / 61 |
| 197 | [Implicit Patterns in LLM-Based Binary Analysis](https://arxiv.org/abs/2603.19138) | B / 61 |
| 198 | [Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/abs/2604.05292) | B / 61 |
| 199 | [Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection](https://arxiv.org/abs/2604.06633) | B / 61 |
| 201 | [SecureForge: Finding and Preventing Vulnerabilities in LLM-Generated Code via Prompt Optimization](https://arxiv.org/abs/2605.08382) | B / 61 |
| 203 | [Decoupled Smart Contract Audits: Lightweight LLM Framework via Distillation and Aggregation](https://arxiv.org/abs/2606.03128) | B / 61 |
| 204 | [Local LLM Agents as Vulnerable Runtimes:A Source-Code Audit of the Agent Runtime Layer](https://arxiv.org/abs/2606.21071) | B / 61 |
| 205 | [Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases](https://arxiv.org/abs/2606.22263) | B / 61 |
| 207 | [Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities](https://arxiv.org/abs/2607.12723) | B / 61 |
| 208 | [When Verified Source Becomes Attack Input: Defending Smart Contracts Against LLM-Based Vulnerability Scanning](https://arxiv.org/abs/2608.28400) | B / 61 |
| 209 | [DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation](https://arxiv.org/abs/2609.28996) | B / 61 |
| 212 | [SEEK: Agentic Knowledge Graph Retrieval for Secure Code Generation](https://arxiv.org/abs/2610.14968) | B / 61 |
| 214 | [Code Vulnerability Detection Across Different Programming Languages with AI Models](https://arxiv.org/abs/2508.11710) | B / 60 |
| 216 | [MAVUL: Multi-Agent Vulnerability Detection via Contextual Reasoning and Interactive Refinement](https://arxiv.org/abs/2510.00317) | B / 60 |
| 217 | [SCRUTINEER: Detecting Logic-Level Usage Violations of Reusable Components in Smart Contracts](https://arxiv.org/abs/2511.11411) | B / 60 |
| 218 | [VULPO: Context-Aware Vulnerability Detection via On-Policy LLM Optimization](https://arxiv.org/abs/2511.11896) | B / 60 |
| 219 | [LLMs as Firmware Experts: A Runtime-Grown Tree-of-Agents Framework](https://arxiv.org/abs/2511.18438) | B / 60 |
| 221 | [LibScan: Smart Contract Library Misuse Detection with Iterative Feedback and Static Verification](https://arxiv.org/abs/2604.00657) | B / 60 |
| 222 | [Adaptive and AI-Augmented Security Testing: A Systematic Survey of Program Analysis, Feedback-Driven Testing, and Hybrid Learning-Based Approaches](https://arxiv.org/abs/2604.27000) | B / 60 |
| 223 | [VulStyle: A Multi-Modal Pre-Training for Code Stylometry-Augmented Vulnerability Detection](https://arxiv.org/abs/2604.26313) | B / 60 |
| 224 | [Lightweight Vulnerability Detection from Code Metrics and Token Features](https://arxiv.org/abs/2605.04260) | B / 60 |
| 225 | [MARGIN: Margin-Aware Regularized Geometry for Imbalanced Vulnerability Detection](https://arxiv.org/abs/2605.10240) | B / 60 |
| 226 | [Dissecting the Black Box: Circuit-Level Analysis of LLM Vulnerability Detection](https://arxiv.org/abs/2605.29901) | B / 60 |
| 229 | [JavaVulBench: A Java Vulnerability Benchmark with Realistic Splits, a Unified Multi-Backend Harness, and a Leakage-Aware Evaluation Mode](https://arxiv.org/abs/2607.02825) | B / 60 |
| 232 | [RuleAutoPilot: Synthesizing Deployable Suricata Rules from Network Traffic](https://arxiv.org/abs/2609.16231) | B / 60 |
| 234 | [Revealing Adversarial Smart Contracts through Semantic Interpretation and Uncertainty Estimation](https://arxiv.org/abs/2509.18934) | C / 59 |
| 236 | [Multi-Agent Collaborative Fuzzing with Continuous Reflection for Smart Contracts Vulnerability Detection](https://arxiv.org/abs/2511.12164) | C / 59 |
| 237 | [GAPS: Targeted Execution of Android Apps via Static Path Reconstruction](https://arxiv.org/abs/2511.23213) | C / 59 |
| 241 | [Bridging Code Property Graphs and Language Models for Program Analysis](https://arxiv.org/abs/2603.24837) | C / 59 |
| 242 | [Detecting Protracted Vulnerabilities in Open Source Projects](https://arxiv.org/abs/2603.27067) | C / 59 |
| 245 | [Synthesizing Multi-Agent Harnesses for Vulnerability Discovery](https://arxiv.org/abs/2604.20801) | C / 59 |
| 246 | [AgenticVM: Agentic AI for Adaptive Software Vulnerability Management](https://arxiv.org/abs/2605.01739) | C / 59 |
| 249 | [NeuroLog: Reasoning You Can Audit -- Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT](https://arxiv.org/abs/2606.00669) | C / 59 |
| 252 | [Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning](https://arxiv.org/abs/2606.25356) | C / 59 |
| 253 | [Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs](https://arxiv.org/abs/2607.00555) | C / 59 |
| 255 | [RECEIPT: Deterministic, Reward-Hacking-Resistant Verification for White-Box Agentic XSS Discovery](https://arxiv.org/abs/2607.18575) | C / 59 |
| 256 | [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](https://arxiv.org/abs/2607.24964) | C / 59 |
| 258 | [KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference](https://arxiv.org/abs/2608.26699) | C / 59 |
| 259 | [SpiderSapien: Client-Centric Web Crawler and Security Scanner](https://arxiv.org/abs/2609.02532) | C / 59 |
| 260 | [LLMSec-AV: A Vulnerability Taxonomy and LLM-Driven Software Weakness Discovery Framework for Autonomous Vehicles](https://arxiv.org/abs/2609.09386) | C / 59 |
| 263 | [CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection](https://arxiv.org/abs/2609.18862) | C / 59 |
| 265 | [Cheap to Hypothesize, Costly to Verify: The Defense Surface of Agentic Vulnerability Discovery](https://arxiv.org/abs/2609.35909) | C / 59 |
| 267 | [Aletheia: Permission-Minimality Testing for Coding-Agent Rules](https://arxiv.org/abs/2609.39678) | C / 59 |
| 274 | [Large Language Models Versus Static Code Analysis Tools: A Systematic Benchmark for Vulnerability Detection](https://arxiv.org/abs/2508.04448) | C / 58 |
| 275 | [Revisiting Third-Party Library Detection: A Ground Truth Dataset and Its Implications Across Security Tasks](https://arxiv.org/abs/2509.04091) | C / 58 |
| 276 | [Detection of security smells in IaC scripts through semantics-aware code and language processing](https://arxiv.org/abs/2509.18790) | C / 58 |
| 279 | [Towards Classifying Benign And Malicious Packages Using Machine Learning](https://arxiv.org/abs/2511.15033) | C / 58 |
| 280 | [CoTDeceptor:Adversarial Code Obfuscation Against CoT-Enhanced LLM Code Agents](https://arxiv.org/abs/2512.21250) | C / 58 |
| 281 | [MulVul: Retrieval-augmented Multi-Agent Code Vulnerability Detection via Cross-Model Prompt Evolution](https://arxiv.org/abs/2601.18847) | C / 58 |
| 283 | [SecureRAG-RTL: A Retrieval-Augmented, Multi-Agent, Zero-Shot LLM-Driven Framework for Hardware Vulnerability Detection](https://arxiv.org/abs/2603.05689) | C / 58 |
| 287 | [Guiding Symbolic Execution with Static Analysis and LLMs for Vulnerability Discovery](https://arxiv.org/abs/2604.06506) | C / 58 |
| 289 | [Learning Generalizable Multimodal Representations for Software Vulnerability Detection](https://arxiv.org/abs/2604.25711) | C / 58 |
| 290 | [PromptAudit: Auditing Prompt Sensitivity in LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.24171) | C / 58 |
| 291 | [Bastet: A Fine-Grained Expert-Labeled Dataset for DeFi Smart Contract Vulnerability Detection](https://arxiv.org/abs/2606.03387) | C / 58 |
| 293 | [Routing Ceilings Are Domain-Independent: Structural Prior Injection in Code Security Vulnerability Detection](https://arxiv.org/abs/2607.14628) | C / 58 |
| 294 | [Directed Symbolic Execution for Vulnerability Discovery: An LLM-Guided Approach in KLEE](https://arxiv.org/abs/2607.21676) | C / 58 |
| 295 | [Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing](https://arxiv.org/abs/2607.21983) | C / 58 |
| 296 | [HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models](https://arxiv.org/abs/2607.27030) | C / 58 |
| 304 | [Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities](https://arxiv.org/abs/2610.29379) | C / 58 |
| 310 | [TraceLLM: Security Diagnosis Through Traces and Smart Contracts in Ethereum](https://arxiv.org/abs/2509.03037) | C / 57 |
| 312 | [Bridging Semantics & Structure for Software Vulnerability Detection using Hybrid Network Models](https://arxiv.org/abs/2510.10321) | C / 57 |
| 313 | [AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software](https://arxiv.org/abs/2512.18567) | C / 57 |
| 314 | [From SFT to RL: Demystifying the Post-Training Pipeline for LLM-based Vulnerability Detection](https://arxiv.org/abs/2602.14012) | C / 57 |
| 315 | [Reentrancy Detection in the Age of LLMs](https://arxiv.org/abs/2603.26497) | C / 57 |
| 316 | [ORACAL: A Robust and Explainable Multimodal Framework for Smart Contract Vulnerability Detection with Causal Graph Enrichment](https://arxiv.org/abs/2603.28128) | C / 57 |
| 317 | [Reachability Across the NL/PL Boundary: A Taxonomy-Driven Dataflow Model for LLM-Integrated Applications](https://arxiv.org/abs/2603.28345) | C / 57 |
| 320 | [Graph Is the Verifier: Agentic Reinforcement Learning for Interprocedural Vulnerability Detection](https://arxiv.org/abs/2607.26656) | C / 57 |
| 321 | [CWEEP: A Lexical Static Analysis Framework for CWE Early Prevention](https://arxiv.org/abs/2607.29604) | C / 57 |
| 324 | [Can escalation channels redirect reward hacking toward defect disclosure?](https://arxiv.org/abs/2608.29460) | C / 57 |
| 328 | [VulDec: Vulnerability Detection in Binaries via Neural Decompilation](https://arxiv.org/abs/2610.33716) | C / 57 |
| 329 | [Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products](https://arxiv.org/abs/2610.42032) | C / 57 |
| 332 | [Securing LLM-Generated Embedded Firmware through AI Agent-Driven Validation and Patching](https://arxiv.org/abs/2509.09970) | C / 56 |
| 333 | [Esim: EVM Bytecode Similarity Detection Based on Stable-Semantic Graph](https://arxiv.org/abs/2511.12971) | C / 56 |
| 335 | [BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks](https://arxiv.org/abs/2512.09385) | C / 56 |
| 336 | [Taint-Based Code Slicing for LLMs-based Malicious NPM Package Detection](https://arxiv.org/abs/2512.12313) | C / 56 |
| 337 | [Diverse LLMs vs. Vulnerabilities: Who Detects and Fixes Them Better?](https://arxiv.org/abs/2512.12536) | C / 56 |
| 340 | [LLMs in Code Vulnerability Analysis: A Proof of Concept](https://arxiv.org/abs/2601.08691) | C / 56 |
| 343 | [Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis](https://arxiv.org/abs/2604.10800) | C / 56 |
| 344 | [Symbolic Execution Meets Multi-LLM Orchestration: Detecting Memory Vulnerabilities in Incomplete Rust CVE Snippets](https://arxiv.org/abs/2605.00034) | C / 56 |
| 345 | [Tailored Prompts, Targeted Protection: Vulnerability-Specific LLM Analysis for Smart Contracts](https://arxiv.org/abs/2605.03697) | C / 56 |
| 346 | [KVerus: Scalable and Resilient Formal Verification Proof Generation for Rust Code](https://arxiv.org/abs/2605.03822) | C / 56 |
| 347 | [VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers](https://arxiv.org/abs/2605.21392) | C / 56 |
| 348 | [ASSEMBLAGE-DEEPHISTORY: A Cross-Build Binary Dataset with Temporal Coverage](https://arxiv.org/abs/2605.21615) | C / 56 |
| 349 | [On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus](https://arxiv.org/abs/2606.07363) | C / 56 |
| 350 | [Knowledge Over Parameters: Evolving Smart Contract Vulnerability Detection](https://arxiv.org/abs/2607.01742) | C / 56 |
| 351 | [Open-Source Intelligence for Code Provenance and the Security Patterns that Separate Human and Large-Language-Model Implementations of Common Programming Tasks](https://arxiv.org/abs/2607.12524) | C / 56 |
| 352 | [ProfMalPlus: Agent-Coordinated Detection of Malicious NPM Packages via Static-Dynamic Analysis Synergy](https://arxiv.org/abs/2607.13965) | C / 56 |
| 353 | [DeFiScreener: Efficient DeFi Attack Pre-screening in Smart Contracts via Historical Case Matching](https://arxiv.org/abs/2607.22184) | C / 56 |
| 355 | [Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems](https://arxiv.org/abs/2608.21095) | C / 56 |
| 357 | [Moirae: A Multimodal Agent Collaborative Framework for Dynamic Android Malware Detection](https://arxiv.org/abs/2608.27994) | C / 56 |
| 362 | [SPLASH: Contrastive Audit Pressure for Detecting and Localizing Security Hallucinations in Generated Code](https://arxiv.org/abs/2610.26001) | C / 56 |
| 363 | [PatchCon: Patch-aware Weighted Supervised Contrastive Learning for Vulnerability Detection](https://arxiv.org/abs/2611.06583) | C / 56 |
| 364 | [ZeroFalse: Improving Precision in Static Analysis with LLMs](https://arxiv.org/abs/2510.02534) | C / 55 |
| 365 | [Evaluating Large Language Models in detecting Secrets in Android Apps](https://arxiv.org/abs/2510.18601) | C / 55 |
| 366 | [ConneX: Automatically Resolving Transaction Opacity of Cross-Chain Bridges for Security Analysis](https://arxiv.org/abs/2511.01393) | C / 55 |
| 369 | [RampoNN: A Reachability-Guided System Falsification for Efficient Cyber-Kinetic Vulnerability Detection](https://arxiv.org/abs/2511.16765) | C / 55 |
| 371 | [An Empirical Evaluation of LLM-Based Approaches for Code Vulnerability Detection: RAG, SFT, and Dual-Agent Systems](https://arxiv.org/abs/2601.00254) | C / 55 |
| 372 | [SSR: Safeguarding Staking Rewards by Defining and Detecting Logical Defects in DeFi Staking](https://arxiv.org/abs/2601.05827) | C / 55 |
| 373 | [Okara: Detection and Attribution of TLS Man-in-the-Middle Vulnerabilities in Android Apps with Foundation Models](https://arxiv.org/abs/2601.22770) | C / 55 |
| 374 | [Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation](https://arxiv.org/abs/2602.04195) | C / 55 |
| 379 | [TitanCA: Lessons from Orchestrating LLM Agents to Discover 100+ CVEs](https://arxiv.org/abs/2604.17860) | C / 55 |
| 381 | [Athena: Vulnerability-Affected Library Identification via Knowledge Graph Completion](https://arxiv.org/abs/2609.01187) | C / 55 |
| 382 | [DeFiFusion: Combining Transaction Events with Smart Contracts to Detect Price Manipulation Attacks](https://arxiv.org/abs/2609.11008) | C / 55 |
| 383 | [ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers](https://arxiv.org/abs/2609.19722) | C / 55 |
| 384 | [HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning](https://arxiv.org/abs/2609.26352) | C / 55 |
| 386 | [JevVibe: Efficient Classification-Guided Secure Code Generation](https://arxiv.org/abs/2609.34963) | C / 55 |
| 391 | [VISION: Robust and Interpretable Code Vulnerability Detection Leveraging Counterfactual Augmentation](https://arxiv.org/abs/2508.18933) | C / 54 |
| 393 | [TaintSentinel: Path-Level Randomness Vulnerability Detection for Ethereum Smart Contracts](https://arxiv.org/abs/2510.18192) | C / 54 |
| 394 | [One Signature, Multiple Payments: Demystifying and Detecting Signature Replay Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2511.09134) | C / 54 |
| 395 | [Benchmarking Zero-Shot Reasoning Approaches for Error Detection in Solidity Smart Contracts](https://arxiv.org/abs/2603.13239) | C / 54 |
| 396 | [From Theory to Practice: Code Generation Using LLMs for CAPEC and CWE Frameworks](https://arxiv.org/abs/2604.02548) | C / 54 |
| 401 | [Binary Decompilation LLM with Feedback-Driven Multi-Turn Refinement](https://arxiv.org/abs/2606.16162) | C / 54 |
| 402 | [Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform](https://arxiv.org/abs/2606.26590) | C / 54 |
| 403 | [From Evaluation to Optimisation: Hierarchy-Aware Training Signals for CWE Prediction in Python](https://arxiv.org/abs/2607.21069) | C / 54 |
| 404 | [VulnGym: Benchmarking Coding Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2608.02001) | C / 54 |
| 405 | [SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills](https://arxiv.org/abs/2608.08468) | C / 54 |
| 414 | [From Attack Descriptions to Vulnerabilities: A Sentence Transformer-Based Approach](https://arxiv.org/abs/2509.02077) | C / 53 |
| 415 | [Cross-Domain Evaluation of Transformer-Based Vulnerability Detection on Open & Industry Data](https://arxiv.org/abs/2509.09313) | C / 53 |
| 419 | [MulVuln: Enhancing Pre-trained LMs with Shared and Language-Specific Knowledge for Multilingual Vulnerability Detection](https://arxiv.org/abs/2510.04397) | C / 53 |
| 420 | [ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contract Vulnerability Detection](https://arxiv.org/abs/2510.17919) | C / 53 |
| 421 | [HYDRA: A Hybrid Heuristic-Guided Deep Representation Architecture for Predicting Latent Zero-Day Vulnerabilities in Patched Functions](https://arxiv.org/abs/2511.06220) | C / 53 |
| 422 | [Llama-based source code vulnerability detection: Prompt engineering vs Fine tuning](https://arxiv.org/abs/2512.09006) | C / 53 |
| 423 | [Agentic AI for Autonomous Defense in Software Supply Chain Security: Beyond Provenance to Vulnerability Mitigation](https://arxiv.org/abs/2512.23480) | C / 53 |
| 424 | [AutoVulnPHP: LLM-Powered Two-Stage PHP Vulnerability Detection and Automated Localization](https://arxiv.org/abs/2601.06177) | C / 53 |
| 425 | [Lightweight Yet Secure: Secure Scripting Language Generation via Lightweight LLMs](https://arxiv.org/abs/2601.06419) | C / 53 |
| 426 | [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/abs/2601.10338) | C / 53 |
| 427 | [Do Fine-Tuned LLMs Understand Vulnerabilities? An Investigation into the Semantic Trap](https://arxiv.org/abs/2601.22655) | C / 53 |
| 428 | [Code Fingerprints: Disentangled Attribution of LLM-Generated Code](https://arxiv.org/abs/2603.04212) | C / 53 |
| 429 | [Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities](https://arxiv.org/abs/2603.10163) | C / 53 |
| 430 | [COBALT-TLA: A Neuro-Symbolic Verification Loop for Cross-Chain Bridge Vulnerability Discovery](https://arxiv.org/abs/2604.12172) | C / 53 |
| 432 | [SAGE: Signal-Amplified Guided Embeddings for LLM-based Vulnerability Detection](https://arxiv.org/abs/2604.19031) | C / 53 |
| 433 | [Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning](https://arxiv.org/abs/2604.20179) | C / 53 |
| 434 | [GoAT-X: A Graph of Auditing Thoughts for Securing Token Transactions in Cross-Chain Contracts](https://arxiv.org/abs/2604.24341) | C / 53 |
| 435 | [A systematic literature Review for Transformer-based Software Vulnerability detection](https://arxiv.org/abs/2604.24822) | C / 53 |
| 436 | [MARD: A Multi-Agent Framework for Robust Android Malware Detection](https://arxiv.org/abs/2604.25264) | C / 53 |
| 437 | [Identifying and Characterizing Semantic Clones of Solidity Functions](https://arxiv.org/abs/2604.26526) | C / 53 |
| 439 | [Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection](https://arxiv.org/abs/2605.20051) | C / 53 |
| 441 | [R+R: Reassessing Java Security API Misuse in Current LLMs: A Replication on JCA and JSSE APIs with External Security Knowledge](https://arxiv.org/abs/2605.31135) | C / 53 |
| 442 | [FusionVul: A Multimodal Feature Fusion Framework for Source Code Vulnerability Detection](https://arxiv.org/abs/2606.08553) | C / 53 |
| 443 | [Evaluating LLMs for Obfuscation Detection and Classification in Android Apps](https://arxiv.org/abs/2606.14233) | C / 53 |
| 444 | [PYPILINE: Malicious PyPI Package Detection via Suspicious API Knowledge and Agent Workflow](https://arxiv.org/abs/2606.19063) | C / 53 |
| 445 | [Large Language Models at the Intersection of Software Engineering and Software Security: An Evidence-Centered Structured Survey and Research Agenda](https://arxiv.org/abs/2608.21107) | C / 53 |
| 454 | [CodeCureAgent: Automatic Classification and Repair of Static Analysis Warnings](https://arxiv.org/abs/2509.11787) | C / 52 |
| 457 | [Towards Compositional Generalization in LLMs for Smart Contract Security: A Case Study on Reentrancy Vulnerabilities](https://arxiv.org/abs/2601.06914) | C / 52 |
| 458 | [Cascaded Vulnerability Attacks in Software Supply Chains](https://arxiv.org/abs/2601.20158) | C / 52 |
| 459 | [Evaluating and Enhancing the Vulnerability Reasoning Capabilities of Large Language Models](https://arxiv.org/abs/2602.06687) | C / 52 |
| 461 | [ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents](https://arxiv.org/abs/2603.12614) | C / 52 |
| 462 | [The Code Whisperer: LLM and Graph-Based AI for Smell and Vulnerability Resolution](https://arxiv.org/abs/2604.13114) | C / 52 |
| 466 | [EntailLLM: Verifying LLM-Generated Vulnerability Discovery Paths with Domain Knowledge via Logic Programming](https://arxiv.org/abs/2608.01763) | C / 52 |
| 467 | [Shortcutting the Fix: Identifying and Categorizing Agentic Exploits in Software Engineering Benchmarks](https://arxiv.org/abs/2609.06780) | C / 52 |
| 468 | [Beyond Static Guarantees: Measuring the Static-Pass Dynamic-Fail Gap in Security-Sensitive and LLM-Generated Python Code](https://arxiv.org/abs/2609.10762) | C / 52 |
| 470 | [ContractLens: Latent Security Knowledge for Malicious Smart Contract Detection](https://arxiv.org/abs/2610.04992) | C / 52 |
| 471 | [LLM-HyPZ: Hardware Vulnerability Discovery using an LLM-Assisted Hybrid Platform for Zero-Shot Knowledge Extraction and Refinement](https://arxiv.org/abs/2509.00647) | C / 51 |
| 473 | [Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories](https://arxiv.org/abs/2510.26103) | C / 51 |
| 474 | [ReVul-CoT: Towards Effective Software Vulnerability Assessment with Retrieval-Augmented Generation and Chain-of-Thought Prompting](https://arxiv.org/abs/2511.17027) | C / 51 |
| 475 | [Large Language Model based Smart Contract Auditing with LLMBugScanner](https://arxiv.org/abs/2512.02069) | C / 51 |
| 476 | [SHERLOCK: A Deep Learning Approach To Detect Software Vulnerabilities](https://arxiv.org/abs/2512.12593) | C / 51 |
| 477 | [ReSIM: Re-ranking Binary Similarity Embeddings to Improve Function Search Performance](https://arxiv.org/abs/2602.09548) | C / 51 |
| 479 | [Vulnerability Detection with Interprocedural Context in Multiple Languages: Assessing Effectiveness and Cost of Modern LLMs](https://arxiv.org/abs/2604.08417) | C / 51 |
| 480 | [Feedback-Driven Execution for LLM-Based Binary Analysis](https://arxiv.org/abs/2604.15136) | C / 51 |
| 484 | [Reinforcement Learning for Software Vulnerability Analysis: A Systematic Review with Emphasis on C/C++ Source Code and Static Analysis](https://arxiv.org/abs/2606.28403) | C / 51 |
| 485 | [Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities](https://arxiv.org/abs/2606.26933) | C / 51 |
| 488 | [When Label Noise Meets Class Imbalance: A Robust Framework for Android Malware Family Classification](https://arxiv.org/abs/2609.22835) | C / 51 |
| 491 | [CVE-to-ATT&CK Mapping via Evidence-Constrained Ranking](https://arxiv.org/abs/2610.33924) | C / 51 |
| 492 | [VerilogLAVD: LLM-Aided Rule Generation for Vulnerability Detection in Verilog](https://arxiv.org/abs/2508.13092) | C / 50 |
| 494 | [LLaVul: A Multimodal LLM for Interpretable Vulnerability Reasoning about Source Code](https://arxiv.org/abs/2509.17337) | C / 50 |
| 496 | [QLCoder: A Query Synthesizer For Static Analysis of Security Vulnerabilities](https://arxiv.org/abs/2511.08462) | C / 50 |
| 498 | [Sift or Get Off the PoC: Applying Information Retrieval to Vulnerability Research with SiftRank](https://arxiv.org/abs/2512.06155) | C / 50 |
| 499 | [From Lab to Reality: A Practical Evaluation of Deep Learning Models and LLMs for Vulnerability Detection](https://arxiv.org/abs/2512.10485) | C / 50 |
| 501 | [Can Adversarial Code Comments Fool AI Security Reviewers -- Large-Scale Empirical Study of Comment-Based Attacks and Defenses Against LLM Code Analysis](https://arxiv.org/abs/2602.16741) | C / 50 |
| 502 | [Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review](https://arxiv.org/abs/2603.18740) | C / 50 |
| 505 | [FORGE: Multi-Agent Graduated Exploitation and Detection Engineering](https://arxiv.org/abs/2606.03453) | C / 50 |
| 506 | [FirmCure:Towards Autonomous and Adaptive Rehosting of Linux-Based Firmware](https://arxiv.org/abs/2606.24549) | C / 50 |
| 508 | [Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline](https://arxiv.org/abs/2608.16187) | C / 50 |
| 511 | [Post-Hoc Attention Steering of Large Language Models for Robust Code Understanding under Obfuscation](https://arxiv.org/abs/2609.26102) | C / 50 |
| 513 | [InterType: Breaking the Single-Function Barrier in Neural Binary Type Inference](https://arxiv.org/abs/2610.26906) | C / 50 |
| 517 | [Cracking IoT Security: Can LLMs Outsmart Static Analysis Tools?](https://arxiv.org/abs/2601.00559) | C / 49 |
| 520 | [VibeGuard: A Security Gate Framework for AI-Generated Code](https://arxiv.org/abs/2604.01052) | C / 49 |
| 521 | [Towards Personalizing Secure Programming Education with LLM-Injected Vulnerabilities](https://arxiv.org/abs/2604.13955) | C / 49 |
| 522 | [PLMGH: What Matters in PLM-GNN Hybrids for Code Classification and Vulnerability Detection](https://arxiv.org/abs/2604.25599) | C / 49 |
| 523 | [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](https://arxiv.org/abs/2606.04739) | C / 49 |
| 524 | [AttackPathGNN: Cross-function vulnerability detection in smart contracts using state interference graphs and conjunction pooling](https://arxiv.org/abs/2606.05986) | C / 49 |
| 526 | [Neuro-Symbolic Reasoning for Vulnerability Detection](https://arxiv.org/abs/2607.03963) | C / 49 |
| 528 | [N2NMatcher: Towards Inlining-Resilient Binary Decomposition and Module Matching](https://arxiv.org/abs/2608.10043) | C / 49 |
| 530 | [Predicting CVSS and CWE from CVE Descriptions with Fine-Tuned Small Language Models](https://arxiv.org/abs/2610.24297) | C / 49 |
| 532 | [PromptGuard: An Orchestrated Prompting Framework for Principled Synthetic Text Generation for Vulnerable Populations using LLMs with Enhanced Safety, Fairness, and Controllability](https://arxiv.org/abs/2509.08910) | C / 48 |
| 533 | [LLM-based Vulnerability Discovery through the Lens of Code Metrics](https://arxiv.org/abs/2509.19117) | C / 48 |
| 534 | [Distilling Lightweight Language Models for C/C++ Vulnerabilities](https://arxiv.org/abs/2510.06645) | C / 48 |
| 536 | [UncertaintyZoo: A Unified Toolkit for Quantifying Predictive Uncertainty in Deep Learning Systems](https://arxiv.org/abs/2512.06406) | C / 48 |
| 537 | [Focus on What Matters: Fisher-Guided Adaptive Multimodal Fusion for Vulnerability Detection](https://arxiv.org/abs/2601.02438) | C / 48 |
| 538 | [SecCodePRM: A Process Reward Model for Code Security](https://arxiv.org/abs/2602.10418) | C / 48 |
| 540 | [Walma: Learning to See Memory Corruption in WebAssembly](https://arxiv.org/abs/2603.24167) | C / 48 |
| 541 | [Robust Smart Contract Vulnerability Detection via Contrastive Learning-Enhanced Granular-ball Training](https://arxiv.org/abs/2603.27734) | C / 48 |
| 543 | [AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs](https://arxiv.org/abs/2607.01640) | C / 48 |
| 545 | [Malformer: A Multi-Modal Malware Detector Using Transformers](https://arxiv.org/abs/2608.19052) | C / 48 |
| 551 | [Federated Learning for Malware Image Classification under Data Heterogeneity](https://arxiv.org/abs/2610.25264) | C / 48 |
| 555 | [Multi-Agent Taint Specification Extraction for Vulnerability Detection](https://arxiv.org/abs/2601.10865) | C / 47 |
| 558 | [Evaluating LLMs for Real-World Web Vulnerability Detection](https://arxiv.org/abs/2606.21397) | C / 47 |
| 559 | [RAMP: Reversing Adversarial Perturbations to Strengthen Clean-Label Backdoor Attacks against Malware Detectors](https://arxiv.org/abs/2609.27422) | C / 47 |
| 562 | [Optimizing Code Embeddings and ML Classifiers for Python Source Code Vulnerability Detection](https://arxiv.org/abs/2509.13134) | C / 46 |
| 563 | [Revisiting Vulnerability Patch Localization: An Empirical Study and LLM-Based Solution](https://arxiv.org/abs/2509.15777) | C / 46 |
| 564 | [SoK: Potentials and Challenges of Large Language Models for Reverse Engineering](https://arxiv.org/abs/2509.21821) | C / 46 |
| 566 | [MalCVE: Malware Detection and CVE Association Using Large Language Models](https://arxiv.org/abs/2510.15567) | C / 46 |
| 568 | [Examining the Effectiveness of Transformer-Based Smart Contract Vulnerability Scan](https://arxiv.org/abs/2601.07334) | C / 46 |
| 569 | [An Empirical Study of the Imbalance Issue in Software Vulnerability Detection](https://arxiv.org/abs/2602.12038) | C / 46 |
| 570 | [Mitigating False Positives in Static Memory Safety Analysis of Rust Programs via Reinforcement Learning](https://arxiv.org/abs/2605.04000) | C / 46 |
| 571 | [TUANDROMD-X: Advanced Entropy and Visual Analytics Dataset for Enhanced Malware Detection and Classification](https://arxiv.org/abs/2605.06718) | C / 46 |
| 572 | [Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge](https://arxiv.org/abs/2607.10221) | C / 46 |
| 573 | [Chiral Analysis of Smart Contracts: Detecting Vulnerabilities from Relational Inconsistencies Across Business Paths](https://arxiv.org/abs/2607.17987) | C / 46 |
| 574 | [MalFlows: Context-aware Fusion of Heterogeneous Flow Semantics for Android Malware Detection](https://arxiv.org/abs/2508.03588) | C / 45 |
| 575 | [Can LLMs Find Bugs in Code? An Evaluation from Beginner Errors to Security Vulnerabilities in Python and C++](https://arxiv.org/abs/2508.16419) | C / 45 |
| 576 | [RustAssure: Differential Symbolic Testing for LLM-Transpiled C-to-Rust Code](https://arxiv.org/abs/2510.07604) | C / 45 |
| 577 | [Detecting Vulnerabilities from Issue Reports for Internet-of-Things](https://arxiv.org/abs/2511.01941) | C / 45 |
| 578 | [USCSA: Evolution-Aware Security Analysis for Proxy-Based Upgradeable Smart Contracts](https://arxiv.org/abs/2512.08372) | C / 45 |
| 579 | [The Role of AI in Modern Penetration Testing](https://arxiv.org/abs/2512.12326) | C / 45 |
| 580 | [Persistent Human Feedback, LLMs, and Static Analyzers for Secure Code Generation and Vulnerability Detection](https://arxiv.org/abs/2602.05868) | C / 45 |
| 581 | [Efficient Software Vulnerability Detection Using Transformer-based Models](https://arxiv.org/abs/2604.00112) | C / 45 |
| 582 | [Towards Robust Personalized Federated Learning: Vulnerability Assessment and Defense Co-Design](https://arxiv.org/abs/2606.22782) | C / 45 |
| 584 | [Automated Vulnerability Injection in Smart Contracts Using Large Language Models](https://arxiv.org/abs/2609.02624) | C / 45 |
| 585 | [Name2Pkg: Lightweight One-Class Android Malware Screening via Name-Package Correspondence Modeling](https://arxiv.org/abs/2609.24389) | C / 45 |
| 586 | [Can We Trust the AI Pair Programmer? Copilot for API Misuse Detection and Correction](https://arxiv.org/abs/2509.16795) | D / 44 |
| 589 | [On the Difficulty of Selecting Few-Shot Examples for Effective LLM-based Vulnerability Detection](https://arxiv.org/abs/2510.27675) | D / 44 |
| 592 | [GPU-Fuzz: Finding Memory Errors in Deep Learning Frameworks](https://arxiv.org/abs/2602.10478) | D / 44 |
| 593 | [ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code](https://arxiv.org/abs/2603.06365) | D / 44 |
| 594 | [Detect--Repair--Verify for LLM-Generated Code: A Multi-Language, Multi-Granularity Empirical Study](https://arxiv.org/abs/2603.23633) | D / 44 |
| 596 | [Towards LLM-Enhanced Android Taint Analysis](https://arxiv.org/abs/2608.24269) | D / 44 |
| 599 | [Exploring Automated Vulnerability Identification in JavaScript Code Using Large Language Models](https://arxiv.org/abs/2609.13816) | D / 44 |
| 600 | [Behavior-Centric Malware Classification with Fine-Grained Malicious Logic Localization](https://arxiv.org/abs/2609.38390) | D / 44 |
| 601 | [Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents](https://arxiv.org/abs/2609.39607) | D / 44 |
| 604 | [Detecting Stealthy Data Poisoning Attacks in AI Code Generators](https://arxiv.org/abs/2508.21636) | D / 43 |
| 605 | [HFuzzer: Testing Large Language Models for Package Hallucinations via Phrase-based Fuzzing](https://arxiv.org/abs/2509.23835) | D / 43 |
| 609 | [Deep Learning-based Binary Analysis for Vulnerability Detection in x86-64 Machine Code](https://arxiv.org/abs/2601.09157) | D / 43 |
| 613 | [A Comparison of Malware Image Transformations Using Grad-CAM and Hybrid Learning Models](https://arxiv.org/abs/2608.12077) | D / 43 |
| 616 | [Validating Solidity Code Defects using Symbolic and Concrete Execution powered by Large Language Models](https://arxiv.org/abs/2509.13023) | D / 42 |
| 619 | [On the Effectiveness of Instruction-Tuning Local LLMs for Identifying Software Vulnerabilities](https://arxiv.org/abs/2512.20062) | D / 42 |
| 620 | [When Labels Are Scarce: A Systematic Mapping of Label-Efficient Code Vulnerability Detection](https://arxiv.org/abs/2604.00079) | D / 42 |
| 621 | [AdverMCTS: Combating Pseudo-Correctness in Code Generation via Adversarial Monte Carlo Tree Search](https://arxiv.org/abs/2604.10449) | D / 42 |
| 622 | [LCC-LLM: Leveraging Code-Centric Large Language Models for Malware Attribution](https://arxiv.org/abs/2605.05807) | D / 42 |
| 624 | [Understanding the (In)Security of Vibe-Coded Applications](https://arxiv.org/abs/2606.23130) | D / 42 |
| 626 | [SemVul: Semantic-Enhanced Graph Neural Networks for Code Property Graph-based Vulnerability Detection](https://arxiv.org/abs/2609.06035) | D / 42 |
| 627 | [Evaluating the NIST Bugs Framework Against CWE as a Successor for Automated Vulnerability Classification](https://arxiv.org/abs/2609.16433) | D / 42 |
| 628 | [OPBackdoor: Opportunistic Backdoors via Alibi-Aligned Reasoning](https://arxiv.org/abs/2609.24826) | D / 42 |
| 629 | [Learning from Failures: A Failure-Driven Prompt Refinement for LLM-Based Vulnerability Analysis](https://arxiv.org/abs/2610.08405) | D / 42 |
| 630 | [ScamDetect: Towards a Robust, Agnostic Framework to Uncover Threats in Smart Contracts](https://arxiv.org/abs/2508.07094) | D / 41 |
| 631 | [From LLMs to Agents: A Comparative Evaluation of LLMs and LLM-based Agents in Security Patch Detection](https://arxiv.org/abs/2511.08060) | D / 41 |
| 637 | [SEMA-GUARD: Semantic and Graph-Based Vulnerability Detection in Assembly Code](https://arxiv.org/abs/2609.17254) | D / 41 |
| 643 | [VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents](https://arxiv.org/abs/2607.09653) | D / 40 |
| 644 | [Cross-Cutting Security Analysis of LLM-Generated Code via Metamorphic Testing and Association Rule Mining](https://arxiv.org/abs/2607.12089) | D / 40 |
| 645 | [Enhancing Multiclass Malware Classification in Resource-Constrained Environments](https://arxiv.org/abs/2609.27950) | D / 40 |
| 648 | [Prompt Engineering vs. Fine-Tuning for LLM-Based Vulnerability Detection in Solana and Algorand Smart Contracts](https://arxiv.org/abs/2511.11250) | D / 39 |
| 651 | [LLM-Assisted Detection and Repair of Hardware Security Vulnerabilities in Verilog Designs](https://arxiv.org/abs/2608.04907) | D / 39 |
| 652 | [C-ing Clearly: Enhanced Binary Code Explanations using C code](https://arxiv.org/abs/2512.14500) | D / 38 |
| 653 | [Security of LLM-generated Code: A Comparative Analysis](https://arxiv.org/abs/2605.23091) | D / 38 |
| 654 | [SoK: AI-Augmented Binary Reversing](https://arxiv.org/abs/2606.17398) | D / 38 |
| 655 | [Advanced Topic Modeling Techniques for Categorizing Software Vulnerabilities](https://arxiv.org/abs/2607.03887) | D / 38 |
| 657 | [Cross-modal Retrieval Models for Stripped Binary Analysis](https://arxiv.org/abs/2512.10393) | D / 37 |
| 658 | [A Prompt-Based Framework for Loop Vulnerability Detection Using Local LLMs](https://arxiv.org/abs/2601.15352) | D / 37 |
| 662 | [When Machine Learning Meets Vulnerability Discovery: Challenges and Lessons Learned](https://arxiv.org/abs/2508.15042) | D / 36 |
| 663 | [Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias](https://arxiv.org/abs/2508.17361) | D / 36 |
| 668 | [What You Code Is What We Prove: Translating BLE App Logic into Formal Models with LLMs for Vulnerability Detection](https://arxiv.org/abs/2509.09291) | D / 35 |
| 669 | [An Empirical Study on Remote Code Execution in Machine Learning Model Hosting Ecosystems](https://arxiv.org/abs/2601.14163) | D / 35 |
| 671 | [Measuring the Security of the Evolving Software Supply Chain: a Research Agenda](https://arxiv.org/abs/2609.08810) | D / 32 |
| 673 | [Compile-time Security Analysis and Optimization of Sensitive String Producers](https://arxiv.org/abs/2605.16561) | D / 31 |
| 674 | [Pretraining on Call Graphs: When Binary Analysis Tasks Profit From Context](https://arxiv.org/abs/2608.02084) | D / 31 |
| 675 | [Investigating Security Implications of Automatically Generated Code on the Software Supply Chain](https://arxiv.org/abs/2509.20277) | D / 30 |

#### localization (30 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 16 | [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](https://arxiv.org/abs/2609.15939) | B / 73 |
| 28 | [AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration](https://arxiv.org/abs/2607.12058) | B / 71 |
| 34 | [VulnAgent-R2: Evidence-Calibrated Multi-Agent Auditing for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2603.13384) | B / 70 |
| 60 | [From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localization](https://arxiv.org/abs/2510.02389) | B / 67 |
| 64 | [VulnResolver: A Hybrid Agent Framework for LLM-Based Automated Vulnerability Issue Resolution](https://arxiv.org/abs/2601.13933) | B / 67 |
| 65 | [AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection](https://arxiv.org/abs/2601.19138) | B / 67 |
| 75 | [CKG-LLM: LLM-Assisted Detection of Smart Contract Access Control Vulnerabilities Based on Knowledge Graphs](https://arxiv.org/abs/2512.06846) | B / 66 |
| 87 | [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](https://arxiv.org/abs/2607.04729) | B / 66 |
| 136 | [VulAgent: Hypothesis-Validation based Multi-Agent Vulnerability Detection](https://arxiv.org/abs/2509.11523) | B / 63 |
| 147 | [Veritas: Grounding LLM Agents for Reliable Vulnerability Reasoning over Stripped Binaries](https://arxiv.org/abs/2605.15097) | B / 63 |
| 155 | [PatchHolmes: Agentic Patch Retrieval via Listwise Selection](https://arxiv.org/abs/2609.38807) | B / 63 |
| 190 | [iCodeReviewer: Improving Secure Code Review with Mixture of Prompts](https://arxiv.org/abs/2510.12186) | B / 61 |
| 244 | [AgentSZZ: Teaching the LLM Agent to Play Detective with Bug-Inducing Commits](https://arxiv.org/abs/2604.02665) | C / 59 |
| 298 | [Antares: Foundation Models for Agentic Vulnerability Localization](https://arxiv.org/abs/2608.02407) | C / 58 |
| 321 | [CWEEP: A Lexical Static Analysis Framework for CWE Early Prevention](https://arxiv.org/abs/2607.29604) | C / 57 |
| 350 | [Knowledge Over Parameters: Evolving Smart Contract Vulnerability Detection](https://arxiv.org/abs/2607.01742) | C / 56 |
| 362 | [SPLASH: Contrastive Audit Pressure for Detecting and Localizing Security Hallucinations in Generated Code](https://arxiv.org/abs/2610.26001) | C / 56 |
| 373 | [Okara: Detection and Attribution of TLS Man-in-the-Middle Vulnerabilities in Android Apps with Foundation Models](https://arxiv.org/abs/2601.22770) | C / 55 |
| 392 | [PatchSeeker: Mapping NVD Records to their Vulnerability-fixing Commits with LLM Generated Commits and Embeddings](https://arxiv.org/abs/2509.07540) | C / 54 |
| 398 | [MAS-SZZ: Multi-Agentic SZZ Algorithm for Vulnerability-Inducing Commit Identification](https://arxiv.org/abs/2604.24398) | C / 54 |
| 404 | [VulnGym: Benchmarking Coding Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2608.02001) | C / 54 |
| 415 | [Cross-Domain Evaluation of Transformer-Based Vulnerability Detection on Open & Industry Data](https://arxiv.org/abs/2509.09313) | C / 53 |
| 424 | [AutoVulnPHP: LLM-Powered Two-Stage PHP Vulnerability Detection and Automated Localization](https://arxiv.org/abs/2601.06177) | C / 53 |
| 498 | [Sift or Get Off the PoC: Applying Information Retrieval to Vulnerability Research with SiftRank](https://arxiv.org/abs/2512.06155) | C / 50 |
| 500 | [Well Begun is Half Done: Location-Aware and Trace-Guided Iterative Automated Vulnerability Repair](https://arxiv.org/abs/2512.20203) | C / 50 |
| 518 | [Favia: Forensic Agent for Vulnerability-fix Identification and Analysis](https://arxiv.org/abs/2602.12500) | C / 49 |
| 556 | [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/abs/2605.04251) | C / 47 |
| 563 | [Revisiting Vulnerability Patch Localization: An Empirical Study and LLM-Based Solution](https://arxiv.org/abs/2509.15777) | C / 46 |
| 588 | [Evaluating Line-level Localization Ability of Learning-based Code Vulnerability Detection Models](https://arxiv.org/abs/2510.11202) | D / 44 |
| 600 | [Behavior-Centric Malware Classification with Fine-Grained Malicious Logic Localization](https://arxiv.org/abs/2609.38390) | D / 44 |

#### repair (83 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 3 | [MemRepair: Hierarchical Memory for Agentic Repository-Level Vulnerability Repair](https://arxiv.org/abs/2605.17444) | A / 76 |
| 24 | [Multi-Agent End-to-End Vulnerability Management for Mitigating Recurring Vulnerabilities](https://arxiv.org/abs/2601.17762) | B / 71 |
| 26 | [RAVEN: Agentic RAG for Automated Vulnerability Repair](https://arxiv.org/abs/2606.22647) | B / 71 |
| 30 | [The History Is the Detector: Executing CVE Patch History, End-to-End](https://arxiv.org/abs/2609.05335) | B / 71 |
| 45 | [ContraFix: Skill-Enhanced Contrastive Runtime Analysis for Vulnerability Repair](https://arxiv.org/abs/2605.17450) | B / 69 |
| 61 | [FLAMES: Fine-tuning LLMs to Synthesize Invariants for Smart Contract Security](https://arxiv.org/abs/2510.21401) | B / 67 |
| 64 | [VulnResolver: A Hybrid Agent Framework for LLM-Based Automated Vulnerability Issue Resolution](https://arxiv.org/abs/2601.13933) | B / 67 |
| 69 | [CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training](https://arxiv.org/abs/2608.06471) | B / 67 |
| 71 | [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075) | B / 67 |
| 90 | [Vul4Py: Benchmarking Automated Vulnerability Repair in Python with Paired Exploit and Functional Oracles](https://arxiv.org/abs/2608.00692) | B / 66 |
| 104 | [Security in a Workflow: Exploring Role-Based Agentic Architectures for Vulnerability Handling](https://arxiv.org/abs/2606.14261) | B / 65 |
| 108 | [AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair](https://arxiv.org/abs/2607.29422) | B / 65 |
| 115 | [Keeping Fuzzers on Duty: Repairing Fuzzing Build Breakages in Continuous Open-Source Fuzzing](https://arxiv.org/abs/2611.06358) | B / 65 |
| 125 | [EvoRepair: Enhancing Vulnerability Repair Agents Through Experience-Based Self-Evolution](https://arxiv.org/abs/2605.30105) | B / 64 |
| 131 | [SecProbe: Adaptive Evaluation of Coding Agents on Cybersecurity Vulnerabilities](https://arxiv.org/abs/2609.33763) | B / 64 |
| 140 | [PATCHEVAL: A New Benchmark for Evaluating LLMs on Patching Real-World Vulnerabilities](https://arxiv.org/abs/2511.11019) | B / 63 |
| 148 | [Automated Repair of TEE Partitioning Issues via DSL-Guided and LLM-Assisted Patching](https://arxiv.org/abs/2605.22087) | B / 63 |
| 153 | [Echo: Learning-based Matching Decompilation using Trusted Back Translation](https://arxiv.org/abs/2609.18706) | B / 63 |
| 158 | [RELAY: Scaling Historical Build Restoration through Rule Reuse and Agentic Repair](https://arxiv.org/abs/2610.27784) | B / 63 |
| 159 | [RegoMender: A Multi-agent Framework for Automated Rego Policy Repair](https://arxiv.org/abs/2610.29456) | B / 63 |
| 177 | [SCARA: A Semantics-Constrained Autonomous Remediation Agent for Opaque Industrial Software Vulnerabilities](https://arxiv.org/abs/2605.19668) | B / 62 |
| 185 | [P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245) | B / 62 |
| 189 | [SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair](https://arxiv.org/abs/2509.16275) | B / 61 |
| 193 | [SolAgent: A Specialized Multi-Agent Framework for Solidity Code Generation](https://arxiv.org/abs/2601.23009) | B / 61 |
| 201 | [SecureForge: Finding and Preventing Vulnerabilities in LLM-Generated Code via Prompt Optimization](https://arxiv.org/abs/2605.08382) | B / 61 |
| 207 | [Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities](https://arxiv.org/abs/2607.12723) | B / 61 |
| 210 | [COMPASS: Predicting the Relationship of Multiple Patches for Vulnerabilities with LLMs](https://arxiv.org/abs/2609.39783) | B / 61 |
| 228 | [Knowledge-Enhanced Agentic Vulnerability Repair](https://arxiv.org/abs/2607.00820) | B / 60 |
| 233 | [Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail](https://arxiv.org/abs/2609.39086) | B / 60 |
| 239 | [PatchIsland: Orchestration of LLM Agents for Continuous Vulnerability Repair](https://arxiv.org/abs/2601.17471) | C / 59 |
| 240 | [Patch Validation in Automated Vulnerability Repair](https://arxiv.org/abs/2603.06858) | C / 59 |
| 241 | [Bridging Code Property Graphs and Language Models for Program Analysis](https://arxiv.org/abs/2603.24837) | C / 59 |
| 243 | [SCPatcher: Automated Smart Contract Code Repair via Retrieval-Augmented Generation and Knowledge Graph](https://arxiv.org/abs/2604.00687) | C / 59 |
| 247 | [VulKey: Automated Vulnerability Repair Guided by Domain-Specific Repair Patterns](https://arxiv.org/abs/2605.01769) | C / 59 |
| 251 | [MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation](https://arxiv.org/abs/2606.11416) | C / 59 |
| 258 | [KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference](https://arxiv.org/abs/2608.26699) | C / 59 |
| 268 | [Scalable Weak-to-Strong Verifier Hardening for Agent Environments](https://arxiv.org/abs/2610.15924) | C / 59 |
| 284 | [SCAFFOLD-CEGIS: Preventing Latent Security Degradation in LLM-Driven Iterative Code Refinement](https://arxiv.org/abs/2603.08520) | C / 58 |
| 306 | [Post-SQLFix: Property-Guided Repair of LLM-Generated SQL with Runtime Verification](https://arxiv.org/abs/2610.41472) | C / 58 |
| 319 | [Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code](https://arxiv.org/abs/2607.21641) | C / 57 |
| 327 | [CWE-bench: Refocusing Agentic Security from Exploitation to Defense](https://arxiv.org/abs/2610.17020) | C / 57 |
| 331 | [All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching](https://arxiv.org/abs/2509.07225) | C / 56 |
| 332 | [Securing LLM-Generated Embedded Firmware through AI Agent-Driven Validation and Patching](https://arxiv.org/abs/2509.09970) | C / 56 |
| 337 | [Diverse LLMs vs. Vulnerabilities: Who Detects and Fixes Them Better?](https://arxiv.org/abs/2512.12536) | C / 56 |
| 339 | [STELP: Secure Transpilation and Execution of LLM-Generated Programs](https://arxiv.org/abs/2601.05467) | C / 56 |
| 340 | [LLMs in Code Vulnerability Analysis: A Proof of Concept](https://arxiv.org/abs/2601.08691) | C / 56 |
| 343 | [Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis](https://arxiv.org/abs/2604.10800) | C / 56 |
| 354 | [Security Tests as Executable Specifications for LLM Code Generation: Benefits, Trade-offs, and Coverage Limits](https://arxiv.org/abs/2608.09740) | C / 56 |
| 361 | [Secure Agentic Coding through Counterexample-Grounded Feedback](https://arxiv.org/abs/2610.25916) | C / 56 |
| 378 | [PCodeTrans: Translate Decompiled Pseudocode to Compilable and Executable Equivalent](https://arxiv.org/abs/2603.14855) | C / 55 |
| 386 | [JevVibe: Efficient Classification-Guided Secure Code Generation](https://arxiv.org/abs/2609.34963) | C / 55 |
| 390 | [Secure and Functional Code Generation with Self-Evaluation](https://arxiv.org/abs/2610.33450) | C / 55 |
| 402 | [Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform](https://arxiv.org/abs/2606.26590) | C / 54 |
| 408 | [Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities](https://arxiv.org/abs/2609.15963) | C / 54 |
| 413 | [On the Evaluation of Large Language Models in Multilingual Vulnerability Repair](https://arxiv.org/abs/2508.03470) | C / 53 |
| 416 | [Towards Secure and Explainable Smart Contract Generation with Security-Aware Group Relative Policy Optimization](https://arxiv.org/abs/2509.09942) | C / 53 |
| 425 | [Lightweight Yet Secure: Secure Scripting Language Generation via Lightweight LLMs](https://arxiv.org/abs/2601.06419) | C / 53 |
| 431 | [SynthFix: Adaptive Neuro-Symbolic Code Vulnerability Repair](https://arxiv.org/abs/2604.17184) | C / 53 |
| 446 | [MAGS: Multi-agent Auto-formalization Guarantees Safety for Agentic Outputs](https://arxiv.org/abs/2609.19391) | C / 53 |
| 449 | [CAT-RAG: Improving Secure Code Generation with Category-Aware Agentic Retrieval](https://arxiv.org/abs/2610.24907) | C / 53 |
| 452 | [VulnRepairEval: An Exploit-Based Evaluation Framework for Assessing Large Language Model Vulnerability Repair Capabilities](https://arxiv.org/abs/2509.03331) | C / 52 |
| 454 | [CodeCureAgent: Automatic Classification and Repair of Static Analysis Warnings](https://arxiv.org/abs/2509.11787) | C / 52 |
| 455 | [Vul-R2: A Reasoning LLM for Automated Vulnerability Repair](https://arxiv.org/abs/2510.05480) | C / 52 |
| 462 | [The Code Whisperer: LLM and Graph-Based AI for Smell and Vulnerability Resolution](https://arxiv.org/abs/2604.13114) | C / 52 |
| 464 | [Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities](https://arxiv.org/abs/2605.28893) | C / 52 |
| 465 | [An Empirical Study of Security Calibration in Large Language Models for Code](https://arxiv.org/abs/2606.31159) | C / 52 |
| 472 | [KubeGuard: LLM-Assisted Kubernetes Hardening via Configuration Files and Runtime Logs Analysis](https://arxiv.org/abs/2509.04191) | C / 51 |
| 500 | [Well Begun is Half Done: Location-Aware and Trace-Guided Iterative Automated Vulnerability Repair](https://arxiv.org/abs/2512.20203) | C / 50 |
| 508 | [Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline](https://arxiv.org/abs/2608.16187) | C / 50 |
| 516 | [Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback](https://arxiv.org/abs/2601.00509) | C / 49 |
| 531 | [Static Analysis as a Feedback Loop: Enhancing LLM-Generated Code Beyond Correctness](https://arxiv.org/abs/2508.14419) | C / 48 |
| 547 | [Authority Is Not a String: A Capability-Scoped Harness for Prompt-Injection-Resistant Coding Agents](https://arxiv.org/abs/2609.08371) | C / 48 |
| 556 | [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/abs/2605.04251) | C / 47 |
| 565 | [TypePilot: Leveraging the Scala Type System for Secure LLM-generated Code](https://arxiv.org/abs/2510.11151) | C / 46 |
| 586 | [Can We Trust the AI Pair Programmer? Copilot for API Misuse Detection and Correction](https://arxiv.org/abs/2509.16795) | D / 44 |
| 594 | [Detect--Repair--Verify for LLM-Generated Code: A Multi-Language, Multi-Granularity Empirical Study](https://arxiv.org/abs/2603.23633) | D / 44 |
| 607 | [Evaluating LLMs for One-Shot Patching of Real and Artificial Vulnerabilities](https://arxiv.org/abs/2511.23408) | D / 43 |
| 614 | [RTLGuard: A Lightweight Teacher-Student Defense for Poisoned RTL Code Generation Models](https://arxiv.org/abs/2608.26049) | D / 43 |
| 633 | [Learn from Your Mistakes: Tree-like Self-Play for Secure Code LLMs](https://arxiv.org/abs/2606.03489) | D / 41 |
| 642 | [Helpful or Harmful? Evaluating LLM-Assisted Vulnerability Patching via a Human Study](https://arxiv.org/abs/2606.25973) | D / 40 |
| 660 | [Secure Coding Drift in LLM-Assisted Post-Quantum Cryptography Development: A Gamified Fix](https://arxiv.org/abs/2606.19474) | D / 37 |
| 664 | [Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation](https://arxiv.org/abs/2603.10072) | D / 36 |
| 666 | [FT-Pilot: Automated Fault-Tolerant RTL Rewriting via Vulnerability-Guided LLMs](https://arxiv.org/abs/2605.28169) | D / 36 |

#### fuzzing (50 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 7 | [JANUS: Agentic Cross-Language Fuzzing Harness Generation for Android Native Libraries](https://arxiv.org/abs/2610.30218) | A / 75 |
| 43 | [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/abs/2604.01645) | B / 69 |
| 53 | [Quality-Assured Fuzz Harness Generation via the Four Principles Framework](https://arxiv.org/abs/2605.21824) | B / 68 |
| 55 | [IntentFuzz: A Protocol-Aware Fuzzer for Automated Invariant Violation Detection in Intent-Based Cross-Chain Bridges](https://arxiv.org/abs/2609.13004) | B / 68 |
| 57 | [Towards Effective Fuzzing of EDK2 Components](https://arxiv.org/abs/2611.03854) | B / 68 |
| 68 | [FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction](https://arxiv.org/abs/2605.21779) | B / 67 |
| 115 | [Keeping Fuzzers on Duty: Repairing Fuzzing Build Breakages in Continuous Open-Source Fuzzing](https://arxiv.org/abs/2611.06358) | B / 65 |
| 119 | [Hybrid Fuzzing with LLM-Guided Input Mutation and Semantic Feedback](https://arxiv.org/abs/2511.03995) | B / 64 |
| 122 | [From Coverage to Causes: Data-Centric Fuzzing for JavaScript Engines](https://arxiv.org/abs/2512.18102) | B / 64 |
| 133 | [ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary](https://arxiv.org/abs/2610.13651) | B / 64 |
| 141 | [Attention Distance: A Novel Metric for Directed Fuzzing with Large Language Models](https://arxiv.org/abs/2512.19758) | B / 63 |
| 195 | [SAFuzz: Semantic-Guided Adaptive Fuzzing for LLM-Generated Code](https://arxiv.org/abs/2602.11209) | B / 61 |
| 206 | [SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing](https://arxiv.org/abs/2607.08949) | B / 61 |
| 222 | [Adaptive and AI-Augmented Security Testing: A Systematic Survey of Program Analysis, Feedback-Driven Testing, and Hybrid Learning-Based Approaches](https://arxiv.org/abs/2604.27000) | B / 60 |
| 236 | [Multi-Agent Collaborative Fuzzing with Continuous Reflection for Smart Contracts Vulnerability Detection](https://arxiv.org/abs/2511.12164) | C / 59 |
| 292 | [DIG: Oracle-Guided Directed Input Generation for One-Day Vulnerabilities](https://arxiv.org/abs/2606.13037) | C / 58 |
| 299 | [Generics-Aware Fuzz Target Generation for Rust Libraries via Structured API Analysis](https://arxiv.org/abs/2608.08637) | C / 58 |
| 300 | [LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles](https://arxiv.org/abs/2608.13450) | C / 58 |
| 311 | [MALF: A Multi-Agent LLM Framework for Intelligent Fuzzing of Industrial Control Protocols](https://arxiv.org/abs/2510.02694) | C / 57 |
| 323 | [DBcover: A White-box SQL Test Generation Framework for Coverage Improvement](https://arxiv.org/abs/2608.25573) | C / 57 |
| 331 | [All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching](https://arxiv.org/abs/2509.07225) | C / 56 |
| 334 | [PBFuzz: Agentic Directed Fuzzing for PoV Generation](https://arxiv.org/abs/2512.04611) | C / 56 |
| 370 | [HarnessAgent: Scaling Automatic Fuzzing Harness Construction with Tool-Augmented LLM Pipelines](https://arxiv.org/abs/2512.03420) | C / 55 |
| 375 | [FuzzySQL: Uncovering Hidden Vulnerabilities in DBMS Special Features with LLM-Driven Fuzzing](https://arxiv.org/abs/2602.19490) | C / 55 |
| 376 | [NeuroSCA: Neuro-Symbolic Constraint Abstraction for Smart Contract Hybrid Fuzzing](https://arxiv.org/abs/2603.01272) | C / 55 |
| 397 | [SDLLMFuzz: Dynamic-static LLM-assisted greybox fuzzing for structured input programs](https://arxiv.org/abs/2604.17750) | C / 54 |
| 417 | [Orion: Fuzzing Workflow Automation](https://arxiv.org/abs/2509.15195) | C / 53 |
| 456 | [PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting](https://arxiv.org/abs/2511.20555) | C / 52 |
| 461 | [ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents](https://arxiv.org/abs/2603.12614) | C / 52 |
| 484 | [Reinforcement Learning for Software Vulnerability Analysis: A Systematic Review with Emphasis on C/C++ Source Code and Static Analysis](https://arxiv.org/abs/2606.28403) | C / 51 |
| 493 | [Locus: Agentic Predicate Synthesis for Directed Fuzzing](https://arxiv.org/abs/2508.21302) | C / 50 |
| 495 | [Clutch Control: An Attention-based Combinatorial Bandit for Efficient Mutation in JavaScript Engine Fuzzing](https://arxiv.org/abs/2510.12732) | C / 50 |
| 503 | [AFL-ICP: Enhancing Industrial Control Protocol Reliability via Specification-Guided Fuzzing](https://arxiv.org/abs/2605.04760) | C / 50 |
| 504 | [PickleFuzzer: A Case Study in Fuzzing for Discrepancies Between Python Pickle Implementations](https://arxiv.org/abs/2605.15084) | C / 50 |
| 514 | [Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation](https://arxiv.org/abs/2509.19533) | C / 49 |
| 515 | [Beyond Imprecise Distance Metrics: Trace-Guided Directed Greybox Fuzzing via LLM-Predicted Call Stacks](https://arxiv.org/abs/2510.23101) | C / 49 |
| 539 | [Following Dragons: Code Review-Guided Fuzzing](https://arxiv.org/abs/2602.10487) | C / 48 |
| 542 | [MASFuzzer: Fuzz Driver Generation and Adaptive Scheduling via Multidimensional API Sequences](https://arxiv.org/abs/2604.17977) | C / 48 |
| 587 | [FalseCrashReducer: Mitigating False Positive Crashes in OSS-Fuzz-Gen Using Agentic AI](https://arxiv.org/abs/2510.02185) | D / 44 |
| 592 | [GPU-Fuzz: Finding Memory Errors in Deep Learning Frameworks](https://arxiv.org/abs/2602.10478) | D / 44 |
| 605 | [HFuzzer: Testing Large Language Models for Package Hallucinations via Phrase-based Fuzzing](https://arxiv.org/abs/2509.23835) | D / 43 |
| 610 | [Human in the Loop for Fuzz Testing: Literature Review and the Road Ahead](https://arxiv.org/abs/2603.13411) | D / 43 |
| 615 | [A Study of the Reliability of Agentic AI-Generated Programs](https://arxiv.org/abs/2609.18298) | D / 43 |
| 617 | [MirrorFuzz: Leveraging LLM and Shared Bugs for Deep Learning Framework APIs Fuzzing](https://arxiv.org/abs/2510.15690) | D / 42 |
| 618 | [GPTrace: Effective Crash Deduplication Using LLM Embeddings](https://arxiv.org/abs/2512.01609) | D / 42 |
| 621 | [AdverMCTS: Combating Pseudo-Correctness in Code Generation via Adversarial Monte Carlo Tree Search](https://arxiv.org/abs/2604.10449) | D / 42 |
| 634 | [Investigating Metamorphic Fuzz Oracle Enhancement via Large Language Models](https://arxiv.org/abs/2606.14164) | D / 41 |
| 635 | [CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs](https://arxiv.org/abs/2606.29124) | D / 41 |
| 640 | [LLM-Powered Silent Bug Fuzzing in Deep Learning Libraries via Versatile and Controlled Bug Transfer](https://arxiv.org/abs/2602.23065) | D / 40 |
| 667 | [Towards LLM-assisted High-Quality Property Generation for Solidity Smart Contracts](https://arxiv.org/abs/2607.23308) | D / 36 |

#### exploit / PoC verification (84 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 6 | [OpenAnt: LLM-Powered Vulnerability Discovery Through Code Decomposition, Adversarial Verification, and Dynamic Testing](https://arxiv.org/abs/2606.19149) | A / 75 |
| 9 | [An Effective and Cost-Efficient Agentic Framework for Ethereum Smart Contract Auditing](https://arxiv.org/abs/2601.17833) | B / 74 |
| 21 | [VEX-Bench: Benchmarking LLM Agents for Assessing Exploitability of Software Supply Chain Vulnerabilities](https://arxiv.org/abs/2609.08040) | B / 72 |
| 32 | [LLM Agents for Automated Web Vulnerability Reproduction: Are We There Yet?](https://arxiv.org/abs/2510.14700) | B / 70 |
| 43 | [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/abs/2604.01645) | B / 69 |
| 49 | [MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes](https://arxiv.org/abs/2609.23980) | B / 69 |
| 51 | [From CVE Entries to Verifiable Exploits: An Automated Multi-Agent Framework for Reproducing CVEs](https://arxiv.org/abs/2509.01835) | B / 68 |
| 56 | [Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security](https://arxiv.org/abs/2610.24896) | B / 68 |
| 58 | [Proving the Wrong Program: Miscompilations as a Threat to zkVM Guarantees](https://arxiv.org/abs/2611.04701) | B / 68 |
| 62 | [SmartPoC: Generating Executable and Validated PoCs for Smart Contract Bug Reports](https://arxiv.org/abs/2511.12993) | B / 67 |
| 67 | [Agentic Vulnerability Reasoning on COTS Binaries](https://arxiv.org/abs/2605.05000) | B / 67 |
| 70 | [PrimSynth: An Agentic Approach to Discover, Validate, and Synthesize Exploit Primitives for Linux Kernel Vulnerabilities](https://arxiv.org/abs/2609.02647) | B / 67 |
| 78 | [Co-RedTeam: Orchestrated Security Discovery and Exploitation with LLM Agents](https://arxiv.org/abs/2602.02164) | B / 66 |
| 80 | [AXE: Grey-Box Exploitability Confirmation for Localized Vulnerability Reports](https://arxiv.org/abs/2602.14345) | B / 66 |
| 82 | [Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization](https://arxiv.org/abs/2603.26270) | B / 66 |
| 88 | [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](https://arxiv.org/abs/2607.12316) | B / 66 |
| 105 | [Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction](https://arxiv.org/abs/2607.01764) | B / 65 |
| 106 | [Beyond Detection: Agentic Attack Synthesis and Simulation for Smart Contracts](https://arxiv.org/abs/2607.15673) | B / 65 |
| 124 | [EvoPoC: Automated Exploit Synthesis for DeFi Smart Contracts via Hierarchical Knowledge Graphs](https://arxiv.org/abs/2605.02868) | B / 64 |
| 126 | [ARVO: Atlas of Reproducible Vulnerabilities for Open-Source Software](https://arxiv.org/abs/2606.17283) | B / 64 |
| 134 | [Names Are Not Objects: Object-Bound Confinement for Compromised AI Coding Agents](https://arxiv.org/abs/2610.14488) | B / 64 |
| 144 | [A Multi-Agent Framework for Automated Exploit Generation with Constraint-Guided Comprehension and Reflection](https://arxiv.org/abs/2604.05130) | B / 63 |
| 154 | [ReproBench: Benchmarking LLM Agents on Reproducing Vulnerability From Scratch](https://arxiv.org/abs/2609.34450) | B / 63 |
| 160 | [Multi-Agent Penetration Testing AI for the Web](https://arxiv.org/abs/2508.20816) | B / 62 |
| 167 | [Diffploit: Facilitating Cross-Version Exploit Migration for Open Source Library Vulnerabilities](https://arxiv.org/abs/2511.12950) | B / 62 |
| 182 | [One Pipeline Does Not Fit All: TAILOR, a Type- and State-Aware Framework for CVE Reproduction](https://arxiv.org/abs/2609.37006) | B / 62 |
| 183 | [Adaptive Code Revision Attacks on AI Pull Request Reviewers](https://arxiv.org/abs/2610.05399) | B / 62 |
| 185 | [P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245) | B / 62 |
| 188 | [Agentic Discovery and Validation of Android App Vulnerabilities](https://arxiv.org/abs/2508.21579) | B / 61 |
| 194 | [QRS: A Rule-Synthesizing Neuro-Symbolic Triad for Autonomous Vulnerability Discovery](https://arxiv.org/abs/2602.09774) | B / 61 |
| 200 | [Secret Stealing Attacks on Local LLM Fine-Tuning through Supply-Chain Model Code Backdoors](https://arxiv.org/abs/2604.27426) | B / 61 |
| 205 | [Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases](https://arxiv.org/abs/2606.22263) | B / 61 |
| 213 | [When File Ingestion Misleads Language Models: Measuring and Mitigating Divergences in Office Documents](https://arxiv.org/abs/2611.05806) | B / 61 |
| 220 | [Execution-State-Aware LLM Reasoning for Automated Proof-of-Vulnerability Generation](https://arxiv.org/abs/2602.13574) | B / 60 |
| 227 | [Transferable Self-Evolving Playbooks for Agentic Security Auditing](https://arxiv.org/abs/2606.16420) | B / 60 |
| 249 | [NeuroLog: Reasoning You Can Audit -- Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT](https://arxiv.org/abs/2606.00669) | C / 59 |
| 255 | [RECEIPT: Deterministic, Reward-Hacking-Resistant Verification for White-Box Agentic XSS Discovery](https://arxiv.org/abs/2607.18575) | C / 59 |
| 257 | [MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing](https://arxiv.org/abs/2608.14216) | C / 59 |
| 262 | [PentestChain: A Cost-Aware, MCP-Orchestrated Framework for Automated Penetration Testing with Free-Tier LLMs](https://arxiv.org/abs/2609.18120) | C / 59 |
| 264 | [SelfOp: An Optimization Algorithm for Self-Improving Security Agents](https://arxiv.org/abs/2609.22792) | C / 59 |
| 270 | [Ulysses: A Security Harness For Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831) | C / 59 |
| 271 | [Kerkoporta: Injecting Structured-Output Backdoors in Reasoning Coding Agents](https://arxiv.org/abs/2611.00138) | C / 59 |
| 272 | [Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains](https://arxiv.org/abs/2611.06585) | C / 59 |
| 273 | [A Gingerbread House for LLM Agents: Source-Planned Honeypots That Lure Autonomous Attackers into an Isolated Shadow](https://arxiv.org/abs/2611.07611) | C / 59 |
| 288 | [Program Analysis Guided LLM Agent for Proof-of-Concept Generation](https://arxiv.org/abs/2604.07624) | C / 58 |
| 292 | [DIG: Oracle-Guided Directed Input Generation for One-Day Vulnerabilities](https://arxiv.org/abs/2606.13037) | C / 58 |
| 300 | [LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles](https://arxiv.org/abs/2608.13450) | C / 58 |
| 305 | [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](https://arxiv.org/abs/2610.29869) | C / 58 |
| 307 | [The Long Con on the Web: Earn-then-Exploit Fraud Attacks against Coding Agents](https://arxiv.org/abs/2611.00725) | C / 58 |
| 308 | [CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion](https://arxiv.org/abs/2611.04356) | C / 58 |
| 330 | [Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security](https://arxiv.org/abs/2611.01976) | C / 57 |
| 334 | [PBFuzz: Agentic Directed Fuzzing for PoV Generation](https://arxiv.org/abs/2512.04611) | C / 56 |
| 343 | [Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis](https://arxiv.org/abs/2604.10800) | C / 56 |
| 347 | [VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers](https://arxiv.org/abs/2605.21392) | C / 56 |
| 356 | [How Do LLM Agents Actually Get the Flag? Trace-Level Provenance for Agentic Offensive Security Evaluation](https://arxiv.org/abs/2608.26237) | C / 56 |
| 360 | [CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat](https://arxiv.org/abs/2610.19005) | C / 56 |
| 367 | [PoCo: Agentic Proof-of-Concept Exploit Generation for Smart Contracts](https://arxiv.org/abs/2511.02780) | C / 55 |
| 385 | [LLM Agents Can Easily Tamper With Their Own Traces](https://arxiv.org/abs/2609.30266) | C / 55 |
| 388 | [The Innocent Courier: Covert Exfiltration Through Legitimate LLM Web Fetching](https://arxiv.org/abs/2610.01768) | C / 55 |
| 400 | [SEC-bench Pro: Can Language Models Solve Long-Horizon Software Security Tasks?](https://arxiv.org/abs/2605.26548) | C / 54 |
| 409 | [ORCAGen: Orchestrating Context-Aware Malware Deception with RAG-Guided Generative AI](https://arxiv.org/abs/2610.12415) | C / 54 |
| 410 | [ProtoArena: Can AI Agents Discover and Exploit Real-World Cross-Component Protocol Vulnerabilities?](https://arxiv.org/abs/2610.17837) | C / 54 |
| 429 | [Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities](https://arxiv.org/abs/2603.10163) | C / 53 |
| 433 | [Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning](https://arxiv.org/abs/2604.20179) | C / 53 |
| 453 | [Guided Reasoning in LLM-Driven Penetration Testing Using Structured Attack Trees](https://arxiv.org/abs/2509.07939) | C / 52 |
| 463 | [V2E: Validating Smart Contract Vulnerabilities through Profit-driven Exploit Generation and Execution](https://arxiv.org/abs/2604.13611) | C / 52 |
| 468 | [Beyond Static Guarantees: Measuring the Static-Pass Dynamic-Fail Gap in Security-Sensitive and LLM-Generated Python Code](https://arxiv.org/abs/2609.10762) | C / 52 |
| 485 | [Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities](https://arxiv.org/abs/2606.26933) | C / 51 |
| 487 | [Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape](https://arxiv.org/abs/2609.20614) | C / 51 |
| 505 | [FORGE: Multi-Agent Graduated Exploitation and Detection Engineering](https://arxiv.org/abs/2606.03453) | C / 50 |
| 506 | [FirmCure:Towards Autonomous and Adaptive Rehosting of Linux-Based Firmware](https://arxiv.org/abs/2606.24549) | C / 50 |
| 509 | [When Context Gets Root: Privilege Escalation in LLM Harnesses](https://arxiv.org/abs/2608.27299) | C / 50 |
| 512 | [Backdooring Sparse Autoencoders](https://arxiv.org/abs/2610.06049) | C / 50 |
| 525 | [Data-Centric Benchmarking of Exploit Generation in LLMs: Understanding the Impact of Fine-Tuning](https://arxiv.org/abs/2606.15123) | C / 49 |
| 550 | [From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)](https://arxiv.org/abs/2610.20437) | C / 48 |
| 553 | [Automated Vulnerability Validation and Verification: A Large Language Model Approach](https://arxiv.org/abs/2509.24037) | C / 47 |
| 560 | [CITADEL: CWE-Guided Insertion of Hardware Trojans via Analysis of DFG-Enabled LLMs](https://arxiv.org/abs/2610.02544) | C / 47 |
| 561 | [Beware EviLLM: Enabling Vulnerability Injection via Large Language Models](https://arxiv.org/abs/2610.03857) | C / 47 |
| 579 | [The Role of AI in Modern Penetration Testing](https://arxiv.org/abs/2512.12326) | C / 45 |
| 598 | [Evaluating Context Segmentation in Locally Deployable SLMs for Cybersecurity CTF Tasks](https://arxiv.org/abs/2609.12839) | D / 44 |
| 602 | [Thinking in Graphs: Neo4j-Backed Exploit-Chain Reasoning for LLM Penetration-Testing Agents](https://arxiv.org/abs/2610.20902) | D / 44 |
| 607 | [Evaluating LLMs for One-Shot Patching of Real and Artificial Vulnerabilities](https://arxiv.org/abs/2511.23408) | D / 43 |
| 643 | [VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents](https://arxiv.org/abs/2607.09653) | D / 40 |
| 676 | [Automatically Attacking Software Reverse Engineering AI Agents](https://arxiv.org/abs/2605.30667) | D / 29 |

#### audit / code review (65 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 9 | [An Effective and Cost-Efficient Agentic Framework for Ethereum Smart Contract Auditing](https://arxiv.org/abs/2601.17833) | B / 74 |
| 31 | [Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub](https://arxiv.org/abs/2610.11169) | B / 71 |
| 35 | [Agent Audit: A Security AnalS System for LLM Agent Applications](https://arxiv.org/abs/2603.22853) | B / 70 |
| 40 | [LogicScan: An LLM-driven Framework for Detecting Business Logic Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2602.03271) | B / 69 |
| 41 | [SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing](https://arxiv.org/abs/2602.04418) | B / 69 |
| 46 | [PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance](https://arxiv.org/abs/2608.17220) | B / 69 |
| 65 | [AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection](https://arxiv.org/abs/2601.19138) | B / 67 |
| 97 | [Rethinking Neural Decompilation: Candidate Selection as the Hidden Bottleneck](https://arxiv.org/abs/2611.02788) | B / 66 |
| 118 | [SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-aware Fine-tuning](https://arxiv.org/abs/2510.26457) | B / 64 |
| 127 | [Using LLMs to Adjudicate Static-Analysis Alerts with Error Reduction Techniques](https://arxiv.org/abs/2607.09979) | B / 64 |
| 129 | [CoSA: Context-Aware Severity Assessment via Context Analysis with Large Language Models](https://arxiv.org/abs/2608.13928) | B / 64 |
| 135 | [CyberDual: AI Attackers versus AI Code Reviewers in Real Software Maintenance](https://arxiv.org/abs/2610.34435) | B / 64 |
| 137 | [SLEAN: Simple Lightweight Ensemble Analysis Network for Multi-Provider LLM Coordination: Design, Implementation, and Vibe Coding Bug Investigation Case Study](https://arxiv.org/abs/2510.10010) | B / 63 |
| 160 | [Multi-Agent Penetration Testing AI for the Web](https://arxiv.org/abs/2508.20816) | B / 62 |
| 162 | [LLM-Driven SAST-Genius: A Hybrid Static Analysis Framework for Comprehensive and Actionable Security](https://arxiv.org/abs/2509.15433) | B / 62 |
| 183 | [Adaptive Code Revision Attacks on AI Pull Request Reviewers](https://arxiv.org/abs/2610.05399) | B / 62 |
| 184 | [LLM-based Code Auditing by Inferring and Evaluating Developer Assumptions](https://arxiv.org/abs/2610.15729) | B / 62 |
| 190 | [iCodeReviewer: Improving Secure Code Review with Mixture of Prompts](https://arxiv.org/abs/2510.12186) | B / 61 |
| 192 | [Exposing Hidden Interfaces: LLM-Guided Type Inference for Reverse Engineering macOS Private Frameworks](https://arxiv.org/abs/2601.01673) | B / 61 |
| 203 | [Decoupled Smart Contract Audits: Lightweight LLM Framework via Distillation and Aggregation](https://arxiv.org/abs/2606.03128) | B / 61 |
| 204 | [Local LLM Agents as Vulnerable Runtimes:A Source-Code Audit of the Agent Runtime Layer](https://arxiv.org/abs/2606.21071) | B / 61 |
| 227 | [Transferable Self-Evolving Playbooks for Agentic Security Auditing](https://arxiv.org/abs/2606.16420) | B / 60 |
| 230 | [The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities](https://arxiv.org/abs/2607.05743) | B / 60 |
| 231 | [FlowArk: Boosting Agentic Data-flow Analysis for Android Apps via Context-Aware Knowledge Reuse](https://arxiv.org/abs/2607.11308) | B / 60 |
| 241 | [Bridging Code Property Graphs and Language Models for Program Analysis](https://arxiv.org/abs/2603.24837) | C / 59 |
| 248 | [CHAINTRIX: A multi-pipeline LLM-augmented framework for automated smart-contract security auditing](https://arxiv.org/abs/2605.09350) | C / 59 |
| 286 | [LiquiLM: Bridging the Semantic Gap in Liquidity Flaw Audit via DCN and LLMs](https://arxiv.org/abs/2604.03860) | C / 58 |
| 302 | [Hieronym: Leveraging Hierarchical Multi-Source Information for Function Renaming in Stripped Binary](https://arxiv.org/abs/2609.12457) | C / 58 |
| 310 | [TraceLLM: Security Diagnosis Through Traces and Smart Contracts in Ethereum](https://arxiv.org/abs/2509.03037) | C / 57 |
| 325 | [A Queryable Graph-Based Security Analysis Framework for O-RAN](https://arxiv.org/abs/2609.06855) | C / 57 |
| 327 | [CWE-bench: Refocusing Agentic Security from Exploitation to Defense](https://arxiv.org/abs/2610.17020) | C / 57 |
| 341 | [Who Said CVE? How Vulnerability Identifiers Are Mentioned by Humans, Bots, and Agents in Pull Requests](https://arxiv.org/abs/2601.19636) | C / 56 |
| 399 | [Benchmarking LLM-Based Static Analysis for Secure Smart Contract Development: Reliability, Limitations, and Potential Hybrid Solutions](https://arxiv.org/abs/2605.11163) | C / 54 |
| 412 | [Making Small Code LLMs More Efficient for Secure Code Review with Neuro-Symbolic Fine-Tuning](https://arxiv.org/abs/2610.35477) | C / 54 |
| 418 | [Hound: Relation-First Knowledge Graphs for Complex-System Reasoning in Security Audits](https://arxiv.org/abs/2510.09633) | C / 53 |
| 434 | [GoAT-X: A Graph of Auditing Thoughts for Securing Token Transactions in Cross-Chain Contracts](https://arxiv.org/abs/2604.24341) | C / 53 |
| 460 | [SPECA: Specification-to-Checklist Agentic Auditing for Multi-Implementation Systems -- A Case Study on Ethereum Clients](https://arxiv.org/abs/2602.07513) | C / 52 |
| 483 | [REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange](https://arxiv.org/abs/2606.05493) | C / 51 |
| 502 | [Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review](https://arxiv.org/abs/2603.18740) | C / 50 |
| 511 | [Post-Hoc Attention Steering of Large Language Models for Robust Code Understanding under Obfuscation](https://arxiv.org/abs/2609.26102) | C / 50 |
| 519 | [Quantum-Safe Code Auditing: LLM-Assisted Static Analysis and Quantum-Aware Risk Scoring for Post-Quantum Cryptography Migration](https://arxiv.org/abs/2604.00560) | C / 49 |
| 529 | [From Requirements to Attack Trees: Grounded LLM Agents for Design-Time Security Review](https://arxiv.org/abs/2610.03820) | C / 49 |
| 535 | [Supporting Students in Navigating LLM-Generated Insecure Code](https://arxiv.org/abs/2511.20878) | C / 48 |
| 543 | [AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs](https://arxiv.org/abs/2607.01640) | C / 48 |
| 546 | [HARP: Hierarchical Adaptive Ranking with Preference-Adaptive Fusion for Query-Based CVE Prioritization](https://arxiv.org/abs/2608.19430) | C / 48 |
| 554 | [From Obfuscated to Obvious: A Comprehensive JavaScript Deobfuscation Tool for Security Analysis](https://arxiv.org/abs/2512.14070) | C / 47 |
| 567 | [Domain-constrained Synthesis of Inconsistent Key Aspects in Textual Vulnerability Descriptions](https://arxiv.org/abs/2511.16123) | C / 46 |
| 578 | [USCSA: Evolution-Aware Security Analysis for Proxy-Based Upgradeable Smart Contracts](https://arxiv.org/abs/2512.08372) | C / 45 |
| 583 | [AI Slop and Hallucinations in Vulnerability Assessment: A Survey on Reasoning Failures and Trustworthy Mitigation](https://arxiv.org/abs/2608.25667) | C / 45 |
| 590 | [An LLM-based Quantitative Framework for Evaluating High-Stealthy Backdoor Risks in OSS Supply Chains](https://arxiv.org/abs/2511.13341) | D / 44 |
| 593 | [ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code](https://arxiv.org/abs/2603.06365) | D / 44 |
| 603 | [Web3 x AI Agents: Landscape, Integrations, and Foundational Challenges](https://arxiv.org/abs/2508.02773) | D / 43 |
| 606 | [Explaining Software Vulnerabilities with Large Language Models](https://arxiv.org/abs/2511.04179) | D / 43 |
| 616 | [Validating Solidity Code Defects using Symbolic and Concrete Execution powered by Large Language Models](https://arxiv.org/abs/2509.13023) | D / 42 |
| 624 | [Understanding the (In)Security of Vibe-Coded Applications](https://arxiv.org/abs/2606.23130) | D / 42 |
| 625 | [Security Vulnerability Patterns in AI-Generated Code: A Cross-Model Comparative Study](https://arxiv.org/abs/2607.20713) | D / 42 |
| 636 | [Comprendia: AI-Augmented Code Comprehension](https://arxiv.org/abs/2608.10290) | D / 41 |
| 641 | [From Preventive to Reactive: How AI Coding Assistants Transform Developers' Security Awareness](https://arxiv.org/abs/2605.23130) | D / 40 |
| 646 | [Vibe Coding in Practice: Motivations, Challenges, and a Future Outlook -- a Grey Literature Review](https://arxiv.org/abs/2510.00328) | D / 39 |
| 650 | [LLM-Based Static Verification of Code Against Natural-Language Requirements: An Industrial Experience Report](https://arxiv.org/abs/2605.17926) | D / 39 |
| 660 | [Secure Coding Drift in LLM-Assisted Post-Quantum Cryptography Development: A Gamified Fix](https://arxiv.org/abs/2606.19474) | D / 37 |
| 661 | [Transformer-Assisted LLM-Based Source Code Summarisation: to Enable More Secure Software Development](https://arxiv.org/abs/2607.20933) | D / 37 |
| 665 | [RAVEN: Retrieval-Augmented Vulnerability Exploration Network for Memory Corruption Analysis in User Code and Binary Programs](https://arxiv.org/abs/2604.17948) | D / 36 |
| 672 | [Agentic Interpretation: Lattice-Structured Evidence for LLM-Based Program Analysis](https://arxiv.org/abs/2605.12694) | D / 31 |
| 673 | [Compile-time Security Analysis and Optimization of Sensitive String Producers](https://arxiv.org/abs/2605.16561) | D / 31 |

#### evaluation (180 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 1 | [LLM-based Vulnerability Detection at Project Scale: An Empirical Study](https://arxiv.org/abs/2601.19239) | A / 77 |
| 2 | [CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability](https://arxiv.org/abs/2602.03012) | A / 76 |
| 8 | [SecureCode: A Production-Grade Multi-Turn Dataset for Training Security-Aware Code Generation Models](https://arxiv.org/abs/2512.18542) | B / 74 |
| 10 | [Does Teaming-Up LLMs Improve Secure Code Generation? A Comprehensive Evaluation with Multi-LLMSecCodeEval](https://arxiv.org/abs/2603.22717) | B / 74 |
| 12 | [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](https://arxiv.org/abs/2611.03555) | B / 74 |
| 14 | [The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark](https://arxiv.org/abs/2608.11469) | B / 73 |
| 15 | [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](https://arxiv.org/abs/2608.26882) | B / 73 |
| 16 | [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](https://arxiv.org/abs/2609.15939) | B / 73 |
| 17 | [CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices](https://arxiv.org/abs/2609.21344) | B / 73 |
| 19 | [Towards a Risk Assessment of Malicious Skill Files in Coding Agents](https://arxiv.org/abs/2608.05223) | B / 72 |
| 21 | [VEX-Bench: Benchmarking LLM Agents for Assessing Exploitability of Software Supply Chain Vulnerabilities](https://arxiv.org/abs/2609.08040) | B / 72 |
| 27 | [CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?](https://arxiv.org/abs/2606.26216) | B / 71 |
| 29 | [From Runnable to Verifiable: An Independent Reproducibility Study of LLM/Agent-Driven Vulnerability Validation Artifacts](https://arxiv.org/abs/2608.09567) | B / 71 |
| 37 | [HarnessSecurity-Bench: Do Security Mechanisms Really Protect Coding Agent Harnesses?](https://arxiv.org/abs/2610.07639) | B / 70 |
| 47 | [CS-Guard: Benchmarking LLM Guardrails for Code Generation Security](https://arxiv.org/abs/2609.09798) | B / 69 |
| 48 | [What is the Difference Between Me and You? Benchmarking the Quality Gap Between Human-Written and AI-Generated Code](https://arxiv.org/abs/2609.12708) | B / 69 |
| 49 | [MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes](https://arxiv.org/abs/2609.23980) | B / 69 |
| 50 | [A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code](https://arxiv.org/abs/2611.06294) | B / 69 |
| 54 | [The Illusion of Safety: Multi-Tier Verification of AI vs. Human C++ Code](https://arxiv.org/abs/2607.00107) | B / 68 |
| 59 | [SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios](https://arxiv.org/abs/2509.22097) | B / 67 |
| 71 | [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075) | B / 67 |
| 74 | [Large Language Models Cannot Reliably Detect Vulnerabilities in JavaScript: The First Systematic Benchmark and Evaluation](https://arxiv.org/abs/2512.01255) | B / 66 |
| 76 | [RealSec-bench: A Benchmark for Evaluating Secure Code Generation in Real-World Repositories](https://arxiv.org/abs/2601.22706) | B / 66 |
| 77 | [Constitutional Spec-Driven Development: Enforcing Security by Construction in AI-Assisted Code Generation](https://arxiv.org/abs/2602.02584) | B / 66 |
| 83 | [Seclens: Role-specific Evaluation of LLM's for security vulnerablity detection](https://arxiv.org/abs/2604.01637) | B / 66 |
| 87 | [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](https://arxiv.org/abs/2607.04729) | B / 66 |
| 91 | [GraftyVul: Synthesising Insecure Programs Through Real-World Vulnerability Grafting](https://arxiv.org/abs/2608.27928) | B / 66 |
| 92 | [Reveree: Diagnosing LLM Reverse-Engineering Agents](https://arxiv.org/abs/2609.01185) | B / 66 |
| 93 | [ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure?](https://arxiv.org/abs/2609.30325) | B / 66 |
| 95 | [INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems](https://arxiv.org/abs/2610.20776) | B / 66 |
| 99 | [Taught by the Flawed: How Dataset Insecurity Breeds Vulnerable AI Code](https://arxiv.org/abs/2511.09879) | B / 65 |
| 101 | [Beyond Single Bugs: Benchmarking Large Language Models for Multi-Vulnerability Detection](https://arxiv.org/abs/2512.22306) | B / 65 |
| 107 | [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](https://arxiv.org/abs/2607.25225) | B / 65 |
| 109 | [VICBench: A Multi-Language Benchmark for Code Vulnerability Detection](https://arxiv.org/abs/2608.12246) | B / 65 |
| 110 | [When LLM Decompilers Recompile More and Preserve Less](https://arxiv.org/abs/2609.05370) | B / 65 |
| 113 | [Humans vs. Machines: A Comparison With AI Agents in Software Reverse Engineering](https://arxiv.org/abs/2610.14960) | B / 65 |
| 121 | [A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection](https://arxiv.org/abs/2512.16538) | B / 64 |
| 131 | [SecProbe: Adaptive Evaluation of Coding Agents on Cybersecurity Vulnerabilities](https://arxiv.org/abs/2609.33763) | B / 64 |
| 132 | [SoK: Are LLMs Reliable at Source Code Recovery? A Taxonomy and Empirical Evaluation](https://arxiv.org/abs/2610.11556) | B / 64 |
| 135 | [CyberDual: AI Attackers versus AI Code Reviewers in Real Software Maintenance](https://arxiv.org/abs/2610.34435) | B / 64 |
| 140 | [PATCHEVAL: A New Benchmark for Evaluating LLMs on Patching Real-World Vulnerabilities](https://arxiv.org/abs/2511.11019) | B / 63 |
| 149 | [Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks](https://arxiv.org/abs/2605.23243) | B / 63 |
| 152 | [Unsaid, Unsafe? Implicit Security Obligations in LLM-Based RTL Code Generation](https://arxiv.org/abs/2608.26588) | B / 63 |
| 154 | [ReproBench: Benchmarking LLM Agents on Reproducing Vulnerability From Scratch](https://arxiv.org/abs/2609.34450) | B / 63 |
| 157 | [Narratives Mislead: An Empirical Study of How LLMs Misjudge CVSS Severity in Bug Bounty Reports](https://arxiv.org/abs/2610.24623) | B / 63 |
| 164 | [Red Teaming Program Repair Agents: When Correct Patches can Hide Vulnerabilities](https://arxiv.org/abs/2509.25894) | B / 62 |
| 165 | [QuiLL: An LLM-Based Vulnerability Assessment Framework for the Wild](https://arxiv.org/abs/2510.04056) | B / 62 |
| 169 | [Adaptive Hierarchical Evaluation of LLMs and SAST tools for CWE Prediction in Python](https://arxiv.org/abs/2601.01320) | B / 62 |
| 170 | [HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation](https://arxiv.org/abs/2601.13864) | B / 62 |
| 175 | [SmartEval: A Benchmark for Evaluating LLM-Generated Smart Contracts from Natural Language Specifications](https://arxiv.org/abs/2605.09610) | B / 62 |
| 176 | [From Controlled to the Wild: Evaluation of Pentesting Agents for the Real-World](https://arxiv.org/abs/2605.10834) | B / 62 |
| 178 | [CyberGym-E2E: Scalable Real-World Benchmark for AI Agents' End-to-End Cybersecurity Capabilities](https://arxiv.org/abs/2606.04460) | B / 62 |
| 186 | [Do Coding Agents Understand Why Systems Crash---and Why They Don't?](https://arxiv.org/abs/2610.29332) | B / 62 |
| 187 | [Simple Features Beat Most AI Control Monitors](https://arxiv.org/abs/2610.41713) | B / 62 |
| 198 | [Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/abs/2604.05292) | B / 61 |
| 202 | [Quality and Security Signals in AI-Generated Python Refactoring Pull Requests](https://arxiv.org/abs/2605.21453) | B / 61 |
| 211 | [Newer and Bigger, but Safer? A Longitudinal Study of the Functionality-Security Gap in LLM-Generated Code](https://arxiv.org/abs/2610.08240) | B / 61 |
| 215 | [Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity](https://arxiv.org/abs/2508.21634) | B / 60 |
| 229 | [JavaVulBench: A Java Vulnerability Benchmark with Realistic Splits, a Unified Multi-Backend Harness, and a Leakage-Aware Evaluation Mode](https://arxiv.org/abs/2607.02825) | B / 60 |
| 233 | [Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail](https://arxiv.org/abs/2609.39086) | B / 60 |
| 235 | [LLMs as verification oracles for Solidity](https://arxiv.org/abs/2509.19153) | C / 59 |
| 238 | [CFCEval: Evaluating Security Aspects in Code Generated by Large Language Models](https://arxiv.org/abs/2512.06248) | C / 59 |
| 240 | [Patch Validation in Automated Vulnerability Repair](https://arxiv.org/abs/2603.06858) | C / 59 |
| 250 | [Context-Based Adversarial Attacks on AI Code Generators: Vulnerability Analysis and Implications](https://arxiv.org/abs/2606.10945) | C / 59 |
| 251 | [MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation](https://arxiv.org/abs/2606.11416) | C / 59 |
| 252 | [Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning](https://arxiv.org/abs/2606.25356) | C / 59 |
| 254 | [The Language of Security: How Prompt Syntax Shapes Secure Code Generation in Open LLMs](https://arxiv.org/abs/2607.15937) | C / 59 |
| 256 | [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](https://arxiv.org/abs/2607.24964) | C / 59 |
| 261 | [BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure](https://arxiv.org/abs/2609.11028) | C / 59 |
| 266 | [SecureVibe: Making Vibe Coding More Secure](https://arxiv.org/abs/2609.38606) | C / 59 |
| 268 | [Scalable Weak-to-Strong Verifier Hardening for Agent Environments](https://arxiv.org/abs/2610.15924) | C / 59 |
| 269 | [Trojan Horse: Automated Repository Poisoning against Coding Agents](https://arxiv.org/abs/2610.23109) | C / 59 |
| 274 | [Large Language Models Versus Static Code Analysis Tools: A Systematic Benchmark for Vulnerability Detection](https://arxiv.org/abs/2508.04448) | C / 58 |
| 277 | [Library Hallucinations in LLM-Generated Code: A Risk Analysis Grounded in Developer Queries](https://arxiv.org/abs/2509.22202) | C / 58 |
| 278 | [Fortifying LLM-Based Code Generation with Graph-Based Reasoning on Secure Coding Practices](https://arxiv.org/abs/2510.09682) | C / 58 |
| 280 | [CoTDeceptor:Adversarial Code Obfuscation Against CoT-Enhanced LLM Code Agents](https://arxiv.org/abs/2512.21250) | C / 58 |
| 282 | [SecCodeBench-V2 Technical Report](https://arxiv.org/abs/2602.15485) | C / 58 |
| 285 | [SecPI: Secure Code Generation with Reasoning Models via Security Reasoning Internalization](https://arxiv.org/abs/2604.03587) | C / 58 |
| 290 | [PromptAudit: Auditing Prompt Sensitivity in LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.24171) | C / 58 |
| 296 | [HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models](https://arxiv.org/abs/2607.27030) | C / 58 |
| 297 | [EduPluginBench: Executable Assurance for AI-Generated Educational Plugins](https://arxiv.org/abs/2608.00739) | C / 58 |
| 301 | [AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs](https://arxiv.org/abs/2609.01023) | C / 58 |
| 303 | [AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination](https://arxiv.org/abs/2609.19140) | C / 58 |
| 304 | [Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities](https://arxiv.org/abs/2610.29379) | C / 58 |
| 307 | [The Long Con on the Web: Earn-then-Exploit Fraud Attacks against Coding Agents](https://arxiv.org/abs/2611.00725) | C / 58 |
| 309 | [A.S.E: A Repository-Level Benchmark for Evaluating Security in AI-Generated Code](https://arxiv.org/abs/2508.18106) | C / 57 |
| 315 | [Reentrancy Detection in the Age of LLMs](https://arxiv.org/abs/2603.26497) | C / 57 |
| 318 | [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494) | C / 57 |
| 322 | [Evaluating Inference-Time Defenses Against Package Hallucination in LLM-Generated Code](https://arxiv.org/abs/2608.22652) | C / 57 |
| 324 | [Can escalation channels redirect reward hacking toward defect disclosure?](https://arxiv.org/abs/2608.29460) | C / 57 |
| 326 | [Understanding and Mitigating Cross-Session Attacks via Persistent Artifacts in Agent Skill Composition](https://arxiv.org/abs/2610.13227) | C / 57 |
| 327 | [CWE-bench: Refocusing Agentic Security from Exploitation to Defense](https://arxiv.org/abs/2610.17020) | C / 57 |
| 330 | [Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security](https://arxiv.org/abs/2611.01976) | C / 57 |
| 338 | [Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming](https://arxiv.org/abs/2601.02060) | C / 56 |
| 342 | [Re-Evaluating EVMBench: Are AI Agents Ready for Smart Contract Security?](https://arxiv.org/abs/2603.10795) | C / 56 |
| 348 | [ASSEMBLAGE-DEEPHISTORY: A Cross-Build Binary Dataset with Temporal Coverage](https://arxiv.org/abs/2605.21615) | C / 56 |
| 349 | [On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus](https://arxiv.org/abs/2606.07363) | C / 56 |
| 351 | [Open-Source Intelligence for Code Provenance and the Security Patterns that Separate Human and Large-Language-Model Implementations of Common Programming Tasks](https://arxiv.org/abs/2607.12524) | C / 56 |
| 356 | [How Do LLM Agents Actually Get the Flag? Trace-Level Provenance for Agentic Offensive Security Evaluation](https://arxiv.org/abs/2608.26237) | C / 56 |
| 358 | [Self-Evolving Defense: Continual Security Policy Learning for LLM Agents](https://arxiv.org/abs/2609.36603) | C / 56 |
| 359 | [When Talk Isn't Code: Comparing LLM Agents That Simulate and Develop Software](https://arxiv.org/abs/2610.04639) | C / 56 |
| 360 | [CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat](https://arxiv.org/abs/2610.19005) | C / 56 |
| 368 | [Secure Code Generation at Scale with Reflexion](https://arxiv.org/abs/2511.03898) | C / 55 |
| 377 | [EVMbench: Evaluating AI Agents on Smart Contract Security](https://arxiv.org/abs/2603.04915) | C / 55 |
| 380 | [Aray: Deterministic-First Synthesis of Benign Artifacts for YARA Validation](https://arxiv.org/abs/2608.19387) | C / 55 |
| 383 | [ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers](https://arxiv.org/abs/2609.19722) | C / 55 |
| 387 | [SINGED: Correct Outputs Do Not Certify Safe Execution in LLM Agents](https://arxiv.org/abs/2609.35889) | C / 55 |
| 389 | [SpecCloak: Probing Harmful Code Generation through Engineering Specifications](https://arxiv.org/abs/2610.17907) | C / 55 |
| 395 | [Benchmarking Zero-Shot Reasoning Approaches for Error Detection in Solidity Smart Contracts](https://arxiv.org/abs/2603.13239) | C / 54 |
| 399 | [Benchmarking LLM-Based Static Analysis for Secure Smart Contract Development: Reliability, Limitations, and Potential Hybrid Solutions](https://arxiv.org/abs/2605.11163) | C / 54 |
| 400 | [SEC-bench Pro: Can Language Models Solve Long-Horizon Software Security Tasks?](https://arxiv.org/abs/2605.26548) | C / 54 |
| 404 | [VulnGym: Benchmarking Coding Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2608.02001) | C / 54 |
| 406 | [Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning](https://arxiv.org/abs/2608.30686) | C / 54 |
| 407 | [Why Is SHAP Not a Reliable Standalone Explanation Framework for Malware Detection?](https://arxiv.org/abs/2609.04626) | C / 54 |
| 408 | [Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities](https://arxiv.org/abs/2609.15963) | C / 54 |
| 410 | [ProtoArena: Can AI Agents Discover and Exploit Real-World Cross-Component Protocol Vulnerabilities?](https://arxiv.org/abs/2610.17837) | C / 54 |
| 411 | [Spoofing the Toolbox: Optimizing Tool Descriptions to Deceive LLM Agents](https://arxiv.org/abs/2610.33182) | C / 54 |
| 413 | [On the Evaluation of Large Language Models in Multilingual Vulnerability Repair](https://arxiv.org/abs/2508.03470) | C / 53 |
| 438 | [MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents](https://arxiv.org/abs/2605.03952) | C / 53 |
| 440 | [Refusal Evaluation in Coding LLMs and Code Agents: A Systematic Review of Thirteen Malicious-Code Prompt Corpora (2023-2025)](https://arxiv.org/abs/2605.20351) | C / 53 |
| 445 | [Large Language Models at the Intersection of Software Engineering and Software Security: An Evidence-Centered Structured Survey and Research Agenda](https://arxiv.org/abs/2608.21107) | C / 53 |
| 447 | [Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files](https://arxiv.org/abs/2610.09264) | C / 53 |
| 448 | [Natural Code Transformation Confuses Agents in Vulnerability Analysis](https://arxiv.org/abs/2610.14350) | C / 53 |
| 450 | [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253) | C / 53 |
| 451 | [Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis](https://arxiv.org/abs/2508.14727) | C / 52 |
| 452 | [VulnRepairEval: An Exploit-Based Evaluation Framework for Assessing Large Language Model Vulnerability Repair Capabilities](https://arxiv.org/abs/2509.03331) | C / 52 |
| 459 | [Evaluating and Enhancing the Vulnerability Reasoning Capabilities of Large Language Models](https://arxiv.org/abs/2602.06687) | C / 52 |
| 465 | [An Empirical Study of Security Calibration in Large Language Models for Code](https://arxiv.org/abs/2606.31159) | C / 52 |
| 467 | [Shortcutting the Fix: Identifying and Categorizing Agentic Exploits in Software Engineering Benchmarks](https://arxiv.org/abs/2609.06780) | C / 52 |
| 469 | [Trajectory-Level Security Debt in LLM Coding Agents](https://arxiv.org/abs/2609.35199) | C / 52 |
| 478 | [CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering](https://arxiv.org/abs/2604.03750) | C / 51 |
| 479 | [Vulnerability Detection with Interprocedural Context in Multiple Languages: Assessing Effectiveness and Cost of Modern LLMs](https://arxiv.org/abs/2604.08417) | C / 51 |
| 481 | [An Empirical Security Evaluation of LLM-Generated Cryptographic Rust Code](https://arxiv.org/abs/2604.27001) | C / 51 |
| 482 | [An Empirical Evaluation of LLM-Generated Code Security Across Prompting Methods](https://arxiv.org/abs/2605.24298) | C / 51 |
| 486 | [Prompt Structure Redistributes, Not Reduces: An Empirical Analysis of Security-Weaknesses in LLM-Generated Python Code](https://arxiv.org/abs/2608.24857) | C / 51 |
| 489 | [API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary](https://arxiv.org/abs/2609.33371) | C / 51 |
| 490 | [CodeMimicry: Exploiting Safety Generalization Lag in Large Language Models via Structured Code Completion](https://arxiv.org/abs/2609.39902) | C / 51 |
| 497 | [Can LLMs Recover Program Semantics? A Systematic Evaluation with Symbolic Execution](https://arxiv.org/abs/2511.19130) | C / 50 |
| 499 | [From Lab to Reality: A Practical Evaluation of Deep Learning Models and LLMs for Vulnerability Detection](https://arxiv.org/abs/2512.10485) | C / 50 |
| 501 | [Can Adversarial Code Comments Fool AI Security Reviewers -- Large-Scale Empirical Study of Comment-Based Attacks and Defenses Against LLM Code Analysis](https://arxiv.org/abs/2602.16741) | C / 50 |
| 507 | [Beyond Refusal: A Same-Lineage Study of Aligned and Abliterated LLMs for Vulnerability Analysis](https://arxiv.org/abs/2607.05842) | C / 50 |
| 510 | [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](https://arxiv.org/abs/2609.02774) | C / 50 |
| 523 | [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](https://arxiv.org/abs/2606.04739) | C / 49 |
| 525 | [Data-Centric Benchmarking of Exploit Generation in LLMs: Understanding the Impact of Fine-Tuning](https://arxiv.org/abs/2606.15123) | C / 49 |
| 527 | [VulnGym: Evaluating Vulnerability Management Strategies against Advanced Persistent Threats](https://arxiv.org/abs/2607.24552) | C / 49 |
| 536 | [UncertaintyZoo: A Unified Toolkit for Quantifying Predictive Uncertainty in Deep Learning Systems](https://arxiv.org/abs/2512.06406) | C / 48 |
| 544 | [Understanding the Impact of AI Code Assistants on Security API Usage: An Empirical Study](https://arxiv.org/abs/2607.11348) | C / 48 |
| 548 | [Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks](https://arxiv.org/abs/2609.17817) | C / 48 |
| 549 | [Reasoning Topology Matters: A Controlled Study of LLM-Based Cybersecurity Analysis](https://arxiv.org/abs/2609.24710) | C / 48 |
| 552 | [When Code Crosses Borders: A Security-Centric Study of LLM-based Code Translation](https://arxiv.org/abs/2509.06504) | C / 47 |
| 557 | [Enhancing Reliability in LLM-Based Secure Code Generation](https://arxiv.org/abs/2605.24300) | C / 47 |
| 558 | [Evaluating LLMs for Real-World Web Vulnerability Detection](https://arxiv.org/abs/2606.21397) | C / 47 |
| 575 | [Can LLMs Find Bugs in Code? An Evaluation from Beginner Errors to Security Vulnerabilities in Python and C++](https://arxiv.org/abs/2508.16419) | C / 45 |
| 588 | [Evaluating Line-level Localization Ability of Learning-based Code Vulnerability Detection Models](https://arxiv.org/abs/2510.11202) | D / 44 |
| 589 | [On the Difficulty of Selecting Few-Shot Examples for Effective LLM-based Vulnerability Detection](https://arxiv.org/abs/2510.27675) | D / 44 |
| 591 | [WildCode Revisited: A Comprehensive Empirical Study on the Security of LLM-Generated Code](https://arxiv.org/abs/2512.04259) | D / 44 |
| 595 | [Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions](https://arxiv.org/abs/2605.06279) | D / 44 |
| 597 | [Vulnerable Code Search: Transferable Attack for Code Language Models](https://arxiv.org/abs/2608.26031) | D / 44 |
| 598 | [Evaluating Context Segmentation in Locally Deployable SLMs for Cybersecurity CTF Tasks](https://arxiv.org/abs/2609.12839) | D / 44 |
| 601 | [Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents](https://arxiv.org/abs/2609.39607) | D / 44 |
| 608 | [SecureCodeRL: Security-Aware Reinforcement Learning for Code Generation with Partial-Credit Rewards](https://arxiv.org/abs/2601.01184) | D / 43 |
| 611 | [Minimal Prompt Perturbations Lead to Code Vulnerabilities: Prompt Fragility and Hidden-State Signals in Coding LLMs](https://arxiv.org/abs/2605.29737) | D / 43 |
| 612 | [Acoda: Adversarial Code Obfuscation for Defending against LLM-based Analysis](https://arxiv.org/abs/2606.11755) | D / 43 |
| 615 | [A Study of the Reliability of Agentic AI-Generated Programs](https://arxiv.org/abs/2609.18298) | D / 43 |
| 620 | [When Labels Are Scarce: A Systematic Mapping of Label-Efficient Code Vulnerability Detection](https://arxiv.org/abs/2604.00079) | D / 42 |
| 623 | [Repository-Level Solidity Code Generation with Large Language Models: From Prompting to Fine-Tuning](https://arxiv.org/abs/2606.19988) | D / 42 |
| 625 | [Security Vulnerability Patterns in AI-Generated Code: A Cross-Model Comparative Study](https://arxiv.org/abs/2607.20713) | D / 42 |
| 627 | [Evaluating the NIST Bugs Framework Against CWE as a Successor for Automated Vulnerability Classification](https://arxiv.org/abs/2609.16433) | D / 42 |
| 631 | [From LLMs to Agents: A Comparative Evaluation of LLMs and LLM-based Agents in Security Patch Detection](https://arxiv.org/abs/2511.08060) | D / 41 |
| 632 | [LLM-CSEC: Empirical Evaluation of Security in C/C++ Code Generated by Large Language Models](https://arxiv.org/abs/2511.18966) | D / 41 |
| 638 | [RiskyPy: Toward Model-Calibrated Prompt Generation for Joint Security and Functionality Evaluation of LLM-Generated Code](https://arxiv.org/abs/2610.40735) | D / 41 |
| 639 | [AutoBaxBuilder: Bootstrapping Code Security Benchmarking](https://arxiv.org/abs/2512.21132) | D / 40 |
| 642 | [Helpful or Harmful? Evaluating LLM-Assisted Vulnerability Patching via a Human Study](https://arxiv.org/abs/2606.25973) | D / 40 |
| 647 | [Death by a Thousand Prompts: Open Model Vulnerability Analysis](https://arxiv.org/abs/2511.03247) | D / 39 |
| 649 | [Evaluating the Vulnerability Landscape of LLM-Generated Smart Contracts](https://arxiv.org/abs/2602.04039) | D / 39 |
| 653 | [Security of LLM-generated Code: A Comparative Analysis](https://arxiv.org/abs/2605.23091) | D / 38 |
| 656 | [Poster: Rethinking Security in LLM Code Generation through Real-World Risk Scenarios](https://arxiv.org/abs/2607.23088) | D / 38 |
| 659 | [A Quasi-Experimental Developer Study of Security Training in LLM-Assisted Web Application Development](https://arxiv.org/abs/2604.17763) | D / 37 |
| 670 | [From Model to Breach: Towards Actionable LLM-Generated Vulnerabilities Reporting](https://arxiv.org/abs/2511.04538) | D / 34 |
| 675 | [Investigating Security Implications of Automatically Generated Code on the Software Supply Chain](https://arxiv.org/abs/2509.20277) | D / 30 |

### 对象 Axis

#### C/C++ (53 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 1 | [LLM-based Vulnerability Detection at Project Scale: An Empirical Study](https://arxiv.org/abs/2601.19239) | A / 77 |
| 5 | [LLMVul: A Vulnerability-Labeled Dataset of LLM-Generated C/C++ Functions from Real Production Repositories](https://arxiv.org/abs/2609.10945) | A / 76 |
| 7 | [JANUS: Agentic Cross-Language Fuzzing Harness Generation for Android Native Libraries](https://arxiv.org/abs/2610.30218) | A / 75 |
| 13 | [VCAO: Verifier-Centered Agentic Orchestration for Strategic OS Vulnerability Discovery](https://arxiv.org/abs/2604.08291) | B / 73 |
| 20 | [ARQ: Agentic CodeQL Query Refinement for C/C++ Vulnerability Detection](https://arxiv.org/abs/2608.20637) | B / 72 |
| 39 | [Sifting the Noise: A Comparative Study of LLM Agents in Vulnerability False Positive Filtering](https://arxiv.org/abs/2601.22952) | B / 69 |
| 42 | [Automated Vulnerability Detection in Source Code Using Deep Representation Learning](https://arxiv.org/abs/2602.23121) | B / 69 |
| 53 | [Quality-Assured Fuzz Harness Generation via the Four Principles Framework](https://arxiv.org/abs/2605.21824) | B / 68 |
| 54 | [The Illusion of Safety: Multi-Tier Verification of AI vs. Human C++ Code](https://arxiv.org/abs/2607.00107) | B / 68 |
| 59 | [SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios](https://arxiv.org/abs/2509.22097) | B / 67 |
| 66 | [VulnScout-C: A Lightweight Transformer for C Code Vulnerability Detection](https://arxiv.org/abs/2603.28309) | B / 67 |
| 68 | [FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction](https://arxiv.org/abs/2605.21779) | B / 67 |
| 69 | [CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training](https://arxiv.org/abs/2608.06471) | B / 67 |
| 70 | [PrimSynth: An Agentic Approach to Discover, Validate, and Synthesize Exploit Primitives for Linux Kernel Vulnerabilities](https://arxiv.org/abs/2609.02647) | B / 67 |
| 71 | [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075) | B / 67 |
| 85 | [Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software](https://arxiv.org/abs/2606.20502) | B / 66 |
| 104 | [Security in a Workflow: Exploring Role-Based Agentic Architectures for Vulnerability Handling](https://arxiv.org/abs/2606.14261) | B / 65 |
| 139 | [LLM-Driven Adaptive Source-Sink Identification and False Positive Mitigation for Static Analysis](https://arxiv.org/abs/2511.04023) | B / 63 |
| 148 | [Automated Repair of TEE Partitioning Issues via DSL-Guided and LLM-Assisted Patching](https://arxiv.org/abs/2605.22087) | B / 63 |
| 185 | [P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245) | B / 62 |
| 212 | [SEEK: Agentic Knowledge Graph Retrieval for Secure Code Generation](https://arxiv.org/abs/2610.14968) | B / 61 |
| 220 | [Execution-State-Aware LLM Reasoning for Automated Proof-of-Vulnerability Generation](https://arxiv.org/abs/2602.13574) | B / 60 |
| 224 | [Lightweight Vulnerability Detection from Code Metrics and Token Features](https://arxiv.org/abs/2605.04260) | B / 60 |
| 226 | [Dissecting the Black Box: Circuit-Level Analysis of LLM Vulnerability Detection](https://arxiv.org/abs/2605.29901) | B / 60 |
| 228 | [Knowledge-Enhanced Agentic Vulnerability Repair](https://arxiv.org/abs/2607.00820) | B / 60 |
| 241 | [Bridging Code Property Graphs and Language Models for Program Analysis](https://arxiv.org/abs/2603.24837) | C / 59 |
| 249 | [NeuroLog: Reasoning You Can Audit -- Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT](https://arxiv.org/abs/2606.00669) | C / 59 |
| 252 | [Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning](https://arxiv.org/abs/2606.25356) | C / 59 |
| 287 | [Guiding Symbolic Execution with Static Analysis and LLMs for Vulnerability Discovery](https://arxiv.org/abs/2604.06506) | C / 58 |
| 294 | [Directed Symbolic Execution for Vulnerability Discovery: An LLM-Guided Approach in KLEE](https://arxiv.org/abs/2607.21676) | C / 58 |
| 296 | [HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models](https://arxiv.org/abs/2607.27030) | C / 58 |
| 319 | [Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code](https://arxiv.org/abs/2607.21641) | C / 57 |
| 331 | [All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching](https://arxiv.org/abs/2509.07225) | C / 56 |
| 334 | [PBFuzz: Agentic Directed Fuzzing for PoV Generation](https://arxiv.org/abs/2512.04611) | C / 56 |
| 340 | [LLMs in Code Vulnerability Analysis: A Proof of Concept](https://arxiv.org/abs/2601.08691) | C / 56 |
| 363 | [PatchCon: Patch-aware Weighted Supervised Contrastive Learning for Vulnerability Detection](https://arxiv.org/abs/2611.06583) | C / 56 |
| 370 | [HarnessAgent: Scaling Automatic Fuzzing Harness Construction with Tool-Augmented LLM Pipelines](https://arxiv.org/abs/2512.03420) | C / 55 |
| 397 | [SDLLMFuzz: Dynamic-static LLM-assisted greybox fuzzing for structured input programs](https://arxiv.org/abs/2604.17750) | C / 54 |
| 400 | [SEC-bench Pro: Can Language Models Solve Long-Horizon Software Security Tasks?](https://arxiv.org/abs/2605.26548) | C / 54 |
| 412 | [Making Small Code LLMs More Efficient for Secure Code Review with Neuro-Symbolic Fine-Tuning](https://arxiv.org/abs/2610.35477) | C / 54 |
| 479 | [Vulnerability Detection with Interprocedural Context in Multiple Languages: Assessing Effectiveness and Cost of Modern LLMs](https://arxiv.org/abs/2604.08417) | C / 51 |
| 484 | [Reinforcement Learning for Software Vulnerability Analysis: A Systematic Review with Emphasis on C/C++ Source Code and Static Analysis](https://arxiv.org/abs/2606.28403) | C / 51 |
| 497 | [Can LLMs Recover Program Semantics? A Systematic Evaluation with Symbolic Execution](https://arxiv.org/abs/2511.19130) | C / 50 |
| 499 | [From Lab to Reality: A Practical Evaluation of Deep Learning Models and LLMs for Vulnerability Detection](https://arxiv.org/abs/2512.10485) | C / 50 |
| 500 | [Well Begun is Half Done: Location-Aware and Trace-Guided Iterative Automated Vulnerability Repair](https://arxiv.org/abs/2512.20203) | C / 50 |
| 510 | [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](https://arxiv.org/abs/2609.02774) | C / 50 |
| 526 | [Neuro-Symbolic Reasoning for Vulnerability Detection](https://arxiv.org/abs/2607.03963) | C / 49 |
| 534 | [Distilling Lightweight Language Models for C/C++ Vulnerabilities](https://arxiv.org/abs/2510.06645) | C / 48 |
| 556 | [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/abs/2605.04251) | C / 47 |
| 576 | [RustAssure: Differential Symbolic Testing for LLM-Transpiled C-to-Rust Code](https://arxiv.org/abs/2510.07604) | C / 45 |
| 581 | [Efficient Software Vulnerability Detection Using Transformer-based Models](https://arxiv.org/abs/2604.00112) | C / 45 |
| 615 | [A Study of the Reliability of Agentic AI-Generated Programs](https://arxiv.org/abs/2609.18298) | D / 43 |
| 632 | [LLM-CSEC: Empirical Evaluation of Security in C/C++ Code Generated by Large Language Models](https://arxiv.org/abs/2511.18966) | D / 41 |

#### Java (24 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 1 | [LLM-based Vulnerability Detection at Project Scale: An Empirical Study](https://arxiv.org/abs/2601.19239) | A / 77 |
| 39 | [Sifting the Noise: A Comparative Study of LLM Agents in Vulnerability False Positive Filtering](https://arxiv.org/abs/2601.22952) | B / 69 |
| 43 | [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/abs/2604.01645) | B / 69 |
| 72 | [An Empirical Analysis of CodeQL False Positives and Query Refinements for Java Vulnerabilities](https://arxiv.org/abs/2609.04535) | B / 67 |
| 76 | [RealSec-bench: A Benchmark for Evaluating Secure Code Generation in Real-World Repositories](https://arxiv.org/abs/2601.22706) | B / 66 |
| 128 | [Memoir: Learning, Verifying, and Evolving False-Positive Memories for Static Application Security Testing Tools](https://arxiv.org/abs/2608.09181) | B / 64 |
| 167 | [Diffploit: Facilitating Cross-Version Exploit Migration for Open Source Library Vulnerabilities](https://arxiv.org/abs/2511.12950) | B / 62 |
| 185 | [P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245) | B / 62 |
| 215 | [Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity](https://arxiv.org/abs/2508.21634) | B / 60 |
| 229 | [JavaVulBench: A Java Vulnerability Benchmark with Realistic Splits, a Unified Multi-Backend Harness, and a Leakage-Aware Evaluation Mode](https://arxiv.org/abs/2607.02825) | B / 60 |
| 312 | [Bridging Semantics & Structure for Software Vulnerability Detection using Hybrid Network Models](https://arxiv.org/abs/2510.10321) | C / 57 |
| 331 | [All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching](https://arxiv.org/abs/2509.07225) | C / 56 |
| 364 | [ZeroFalse: Improving Precision in Static Analysis with LLMs](https://arxiv.org/abs/2510.02534) | C / 55 |
| 441 | [R+R: Reassessing Java Security API Misuse in Current LLMs: A Replication on JCA and JSSE APIs with External Security Knowledge](https://arxiv.org/abs/2605.31135) | C / 53 |
| 451 | [Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis](https://arxiv.org/abs/2508.14727) | C / 52 |
| 454 | [CodeCureAgent: Automatic Classification and Repair of Static Analysis Warnings](https://arxiv.org/abs/2509.11787) | C / 52 |
| 496 | [QLCoder: A Query Synthesizer For Static Analysis of Security Vulnerabilities](https://arxiv.org/abs/2511.08462) | C / 50 |
| 507 | [Beyond Refusal: A Same-Lineage Study of Aligned and Abliterated LLMs for Vulnerability Analysis](https://arxiv.org/abs/2607.05842) | C / 50 |
| 510 | [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](https://arxiv.org/abs/2609.02774) | C / 50 |
| 566 | [MalCVE: Malware Detection and CVE Association Using Large Language Models](https://arxiv.org/abs/2510.15567) | C / 46 |
| 629 | [Learning from Failures: A Failure-Driven Prompt Refinement for LLM-Based Vulnerability Analysis](https://arxiv.org/abs/2610.08405) | D / 42 |
| 636 | [Comprendia: AI-Augmented Code Comprehension](https://arxiv.org/abs/2608.10290) | D / 41 |
| 659 | [A Quasi-Experimental Developer Study of Security Training in LLM-Assisted Web Application Development](https://arxiv.org/abs/2604.17763) | D / 37 |
| 664 | [Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation](https://arxiv.org/abs/2603.10072) | D / 36 |

#### Python (30 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 35 | [Agent Audit: A Security AnalS System for LLM Agent Applications](https://arxiv.org/abs/2603.22853) | B / 70 |
| 89 | [DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2607.13439) | B / 66 |
| 90 | [Vul4Py: Benchmarking Automated Vulnerability Repair in Python with Paired Exploit and Functional Oracles](https://arxiv.org/abs/2608.00692) | B / 66 |
| 99 | [Taught by the Flawed: How Dataset Insecurity Breeds Vulnerable AI Code](https://arxiv.org/abs/2511.09879) | B / 65 |
| 161 | [An Empirical Study of Vulnerabilities in Python Packages and Their Detection](https://arxiv.org/abs/2509.04260) | B / 62 |
| 169 | [Adaptive Hierarchical Evaluation of LLMs and SAST tools for CWE Prediction in Python](https://arxiv.org/abs/2601.01320) | B / 62 |
| 189 | [SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair](https://arxiv.org/abs/2509.16275) | B / 61 |
| 202 | [Quality and Security Signals in AI-Generated Python Refactoring Pull Requests](https://arxiv.org/abs/2605.21453) | B / 61 |
| 212 | [SEEK: Agentic Knowledge Graph Retrieval for Secure Code Generation](https://arxiv.org/abs/2610.14968) | B / 61 |
| 215 | [Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity](https://arxiv.org/abs/2508.21634) | B / 60 |
| 233 | [Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail](https://arxiv.org/abs/2609.39086) | B / 60 |
| 251 | [MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation](https://arxiv.org/abs/2606.11416) | C / 59 |
| 403 | [From Evaluation to Optimisation: Hierarchy-Aware Training Signals for CWE Prediction in Python](https://arxiv.org/abs/2607.21069) | C / 54 |
| 444 | [PYPILINE: Malicious PyPI Package Detection via Suspicious API Knowledge and Agent Workflow](https://arxiv.org/abs/2606.19063) | C / 53 |
| 450 | [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253) | C / 53 |
| 452 | [VulnRepairEval: An Exploit-Based Evaluation Framework for Assessing Large Language Model Vulnerability Repair Capabilities](https://arxiv.org/abs/2509.03331) | C / 52 |
| 468 | [Beyond Static Guarantees: Measuring the Static-Pass Dynamic-Fail Gap in Security-Sensitive and LLM-Generated Python Code](https://arxiv.org/abs/2609.10762) | C / 52 |
| 479 | [Vulnerability Detection with Interprocedural Context in Multiple Languages: Assessing Effectiveness and Cost of Modern LLMs](https://arxiv.org/abs/2604.08417) | C / 51 |
| 486 | [Prompt Structure Redistributes, Not Reduces: An Empirical Analysis of Security-Weaknesses in LLM-Generated Python Code](https://arxiv.org/abs/2608.24857) | C / 51 |
| 504 | [PickleFuzzer: A Case Study in Fuzzing for Discrepancies Between Python Pickle Implementations](https://arxiv.org/abs/2605.15084) | C / 50 |
| 508 | [Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline](https://arxiv.org/abs/2608.16187) | C / 50 |
| 531 | [Static Analysis as a Feedback Loop: Enhancing LLM-Generated Code Beyond Correctness](https://arxiv.org/abs/2508.14419) | C / 48 |
| 547 | [Authority Is Not a String: A Capability-Scoped Harness for Prompt-Injection-Resistant Coding Agents](https://arxiv.org/abs/2609.08371) | C / 48 |
| 562 | [Optimizing Code Embeddings and ML Classifiers for Python Source Code Vulnerability Detection](https://arxiv.org/abs/2509.13134) | C / 46 |
| 595 | [Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions](https://arxiv.org/abs/2605.06279) | D / 44 |
| 617 | [MirrorFuzz: Leveraging LLM and Shared Bugs for Deep Learning Framework APIs Fuzzing](https://arxiv.org/abs/2510.15690) | D / 42 |
| 638 | [RiskyPy: Toward Model-Calibrated Prompt Generation for Joint Security and Functionality Evaluation of LLM-Generated Code](https://arxiv.org/abs/2610.40735) | D / 41 |
| 640 | [LLM-Powered Silent Bug Fuzzing in Deep Learning Libraries via Versatile and Controlled Bug Transfer](https://arxiv.org/abs/2602.23065) | D / 40 |
| 658 | [A Prompt-Based Framework for Loop Vulnerability Detection Using Local LLMs](https://arxiv.org/abs/2601.15352) | D / 37 |
| 669 | [An Empirical Study on Remote Code Execution in Machine Learning Model Hosting Ecosystems](https://arxiv.org/abs/2601.14163) | D / 35 |

#### JavaScript / TypeScript (11 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 74 | [Large Language Models Cannot Reliably Detect Vulnerabilities in JavaScript: The First Systematic Benchmark and Evaluation](https://arxiv.org/abs/2512.01255) | B / 66 |
| 122 | [From Coverage to Causes: Data-Centric Fuzzing for JavaScript Engines](https://arxiv.org/abs/2512.18102) | B / 64 |
| 181 | [SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs](https://arxiv.org/abs/2609.06149) | B / 62 |
| 263 | [CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection](https://arxiv.org/abs/2609.18862) | C / 59 |
| 336 | [Taint-Based Code Slicing for LLMs-based Malicious NPM Package Detection](https://arxiv.org/abs/2512.12313) | C / 56 |
| 352 | [ProfMalPlus: Agent-Coordinated Detection of Malicious NPM Packages via Static-Dynamic Analysis Synergy](https://arxiv.org/abs/2607.13965) | C / 56 |
| 433 | [Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning](https://arxiv.org/abs/2604.20179) | C / 53 |
| 495 | [Clutch Control: An Attention-based Combinatorial Bandit for Efficient Mutation in JavaScript Engine Fuzzing](https://arxiv.org/abs/2510.12732) | C / 50 |
| 554 | [From Obfuscated to Obvious: A Comprehensive JavaScript Deobfuscation Tool for Security Analysis](https://arxiv.org/abs/2512.14070) | C / 47 |
| 555 | [Multi-Agent Taint Specification Extraction for Vulnerability Detection](https://arxiv.org/abs/2601.10865) | C / 47 |
| 599 | [Exploring Automated Vulnerability Identification in JavaScript Code Using Large Language Models](https://arxiv.org/abs/2609.13816) | D / 44 |

#### Go / Rust (10 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 58 | [Proving the Wrong Program: Miscompilations as a Threat to zkVM Guarantees](https://arxiv.org/abs/2611.04701) | B / 68 |
| 87 | [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](https://arxiv.org/abs/2607.04729) | B / 66 |
| 258 | [KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference](https://arxiv.org/abs/2608.26699) | C / 59 |
| 299 | [Generics-Aware Fuzz Target Generation for Rust Libraries via Structured API Analysis](https://arxiv.org/abs/2608.08637) | C / 58 |
| 344 | [Symbolic Execution Meets Multi-LLM Orchestration: Detecting Memory Vulnerabilities in Incomplete Rust CVE Snippets](https://arxiv.org/abs/2605.00034) | C / 56 |
| 346 | [KVerus: Scalable and Resilient Formal Verification Proof Generation for Rust Code](https://arxiv.org/abs/2605.03822) | C / 56 |
| 481 | [An Empirical Security Evaluation of LLM-Generated Cryptographic Rust Code](https://arxiv.org/abs/2604.27001) | C / 51 |
| 570 | [Mitigating False Positives in Static Memory Safety Analysis of Rust Programs via Reinforcement Learning](https://arxiv.org/abs/2605.04000) | C / 46 |
| 576 | [RustAssure: Differential Symbolic Testing for LLM-Transpiled C-to-Rust Code](https://arxiv.org/abs/2510.07604) | C / 45 |
| 648 | [Prompt Engineering vs. Fine-Tuning for LLM-Based Vulnerability Detection in Solana and Algorand Smart Contracts](https://arxiv.org/abs/2511.11250) | D / 39 |

#### smart contracts / EVM (74 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 9 | [An Effective and Cost-Efficient Agentic Framework for Ethereum Smart Contract Auditing](https://arxiv.org/abs/2601.17833) | B / 74 |
| 27 | [CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?](https://arxiv.org/abs/2606.26216) | B / 71 |
| 40 | [LogicScan: An LLM-driven Framework for Detecting Business Logic Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2602.03271) | B / 69 |
| 41 | [SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing](https://arxiv.org/abs/2602.04418) | B / 69 |
| 46 | [PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance](https://arxiv.org/abs/2608.17220) | B / 69 |
| 55 | [IntentFuzz: A Protocol-Aware Fuzzer for Automated Invariant Violation Detection in Intent-Based Cross-Chain Bridges](https://arxiv.org/abs/2609.13004) | B / 68 |
| 61 | [FLAMES: Fine-tuning LLMs to Synthesize Invariants for Smart Contract Security](https://arxiv.org/abs/2510.21401) | B / 67 |
| 62 | [SmartPoC: Generating Executable and Validated PoCs for Smart Contract Bug Reports](https://arxiv.org/abs/2511.12993) | B / 67 |
| 75 | [CKG-LLM: LLM-Assisted Detection of Smart Contract Access Control Vulnerabilities Based on Knowledge Graphs](https://arxiv.org/abs/2512.06846) | B / 66 |
| 82 | [Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization](https://arxiv.org/abs/2603.26270) | B / 66 |
| 94 | [SmartMemory: Detecting On-chain-off-chain Communication Inconsistency for Smart Contract via Memory-based Agent](https://arxiv.org/abs/2609.34983) | B / 66 |
| 106 | [Beyond Detection: Agentic Attack Synthesis and Simulation for Smart Contracts](https://arxiv.org/abs/2607.15673) | B / 65 |
| 111 | [Function Name Is All You Need to Detect Blockchain Application Attacks](https://arxiv.org/abs/2609.12315) | B / 65 |
| 112 | [Mind the Gap: Detecting Description-Execution Mismatch Attacks in DAO Governance](https://arxiv.org/abs/2609.13601) | B / 65 |
| 124 | [EvoPoC: Automated Exploit Synthesis for DeFi Smart Contracts via Hierarchical Knowledge Graphs](https://arxiv.org/abs/2605.02868) | B / 64 |
| 138 | [LLM-Powered Detection of Price Manipulation in DeFi](https://arxiv.org/abs/2510.21272) | B / 63 |
| 163 | [LISA Technical Report: An Agentic Framework for Smart Contract Auditing](https://arxiv.org/abs/2509.24698) | B / 62 |
| 166 | [Trace: Securing Smart Contract Repository Against Access Control Vulnerability](https://arxiv.org/abs/2510.19254) | B / 62 |
| 175 | [SmartEval: A Benchmark for Evaluating LLM-Generated Smart Contracts from Natural Language Specifications](https://arxiv.org/abs/2605.09610) | B / 62 |
| 193 | [SolAgent: A Specialized Multi-Agent Framework for Solidity Code Generation](https://arxiv.org/abs/2601.23009) | B / 61 |
| 203 | [Decoupled Smart Contract Audits: Lightweight LLM Framework via Distillation and Aggregation](https://arxiv.org/abs/2606.03128) | B / 61 |
| 208 | [When Verified Source Becomes Attack Input: Defending Smart Contracts Against LLM-Based Vulnerability Scanning](https://arxiv.org/abs/2608.28400) | B / 61 |
| 217 | [SCRUTINEER: Detecting Logic-Level Usage Violations of Reusable Components in Smart Contracts](https://arxiv.org/abs/2511.11411) | B / 60 |
| 221 | [LibScan: Smart Contract Library Misuse Detection with Iterative Feedback and Static Verification](https://arxiv.org/abs/2604.00657) | B / 60 |
| 234 | [Revealing Adversarial Smart Contracts through Semantic Interpretation and Uncertainty Estimation](https://arxiv.org/abs/2509.18934) | C / 59 |
| 235 | [LLMs as verification oracles for Solidity](https://arxiv.org/abs/2509.19153) | C / 59 |
| 236 | [Multi-Agent Collaborative Fuzzing with Continuous Reflection for Smart Contracts Vulnerability Detection](https://arxiv.org/abs/2511.12164) | C / 59 |
| 243 | [SCPatcher: Automated Smart Contract Code Repair via Retrieval-Augmented Generation and Knowledge Graph](https://arxiv.org/abs/2604.00687) | C / 59 |
| 248 | [CHAINTRIX: A multi-pipeline LLM-augmented framework for automated smart-contract security auditing](https://arxiv.org/abs/2605.09350) | C / 59 |
| 286 | [LiquiLM: Bridging the Semantic Gap in Liquidity Flaw Audit via DCN and LLMs](https://arxiv.org/abs/2604.03860) | C / 58 |
| 291 | [Bastet: A Fine-Grained Expert-Labeled Dataset for DeFi Smart Contract Vulnerability Detection](https://arxiv.org/abs/2606.03387) | C / 58 |
| 295 | [Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing](https://arxiv.org/abs/2607.21983) | C / 58 |
| 310 | [TraceLLM: Security Diagnosis Through Traces and Smart Contracts in Ethereum](https://arxiv.org/abs/2509.03037) | C / 57 |
| 315 | [Reentrancy Detection in the Age of LLMs](https://arxiv.org/abs/2603.26497) | C / 57 |
| 316 | [ORACAL: A Robust and Explainable Multimodal Framework for Smart Contract Vulnerability Detection with Causal Graph Enrichment](https://arxiv.org/abs/2603.28128) | C / 57 |
| 333 | [Esim: EVM Bytecode Similarity Detection Based on Stable-Semantic Graph](https://arxiv.org/abs/2511.12971) | C / 56 |
| 335 | [BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks](https://arxiv.org/abs/2512.09385) | C / 56 |
| 342 | [Re-Evaluating EVMBench: Are AI Agents Ready for Smart Contract Security?](https://arxiv.org/abs/2603.10795) | C / 56 |
| 345 | [Tailored Prompts, Targeted Protection: Vulnerability-Specific LLM Analysis for Smart Contracts](https://arxiv.org/abs/2605.03697) | C / 56 |
| 349 | [On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus](https://arxiv.org/abs/2606.07363) | C / 56 |
| 350 | [Knowledge Over Parameters: Evolving Smart Contract Vulnerability Detection](https://arxiv.org/abs/2607.01742) | C / 56 |
| 353 | [DeFiScreener: Efficient DeFi Attack Pre-screening in Smart Contracts via Historical Case Matching](https://arxiv.org/abs/2607.22184) | C / 56 |
| 366 | [ConneX: Automatically Resolving Transaction Opacity of Cross-Chain Bridges for Security Analysis](https://arxiv.org/abs/2511.01393) | C / 55 |
| 367 | [PoCo: Agentic Proof-of-Concept Exploit Generation for Smart Contracts](https://arxiv.org/abs/2511.02780) | C / 55 |
| 372 | [SSR: Safeguarding Staking Rewards by Defining and Detecting Logical Defects in DeFi Staking](https://arxiv.org/abs/2601.05827) | C / 55 |
| 376 | [NeuroSCA: Neuro-Symbolic Constraint Abstraction for Smart Contract Hybrid Fuzzing](https://arxiv.org/abs/2603.01272) | C / 55 |
| 377 | [EVMbench: Evaluating AI Agents on Smart Contract Security](https://arxiv.org/abs/2603.04915) | C / 55 |
| 382 | [DeFiFusion: Combining Transaction Events with Smart Contracts to Detect Price Manipulation Attacks](https://arxiv.org/abs/2609.11008) | C / 55 |
| 393 | [TaintSentinel: Path-Level Randomness Vulnerability Detection for Ethereum Smart Contracts](https://arxiv.org/abs/2510.18192) | C / 54 |
| 394 | [One Signature, Multiple Payments: Demystifying and Detecting Signature Replay Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2511.09134) | C / 54 |
| 395 | [Benchmarking Zero-Shot Reasoning Approaches for Error Detection in Solidity Smart Contracts](https://arxiv.org/abs/2603.13239) | C / 54 |
| 399 | [Benchmarking LLM-Based Static Analysis for Secure Smart Contract Development: Reliability, Limitations, and Potential Hybrid Solutions](https://arxiv.org/abs/2605.11163) | C / 54 |
| 416 | [Towards Secure and Explainable Smart Contract Generation with Security-Aware Group Relative Policy Optimization](https://arxiv.org/abs/2509.09942) | C / 53 |
| 420 | [ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contract Vulnerability Detection](https://arxiv.org/abs/2510.17919) | C / 53 |
| 430 | [COBALT-TLA: A Neuro-Symbolic Verification Loop for Cross-Chain Bridge Vulnerability Discovery](https://arxiv.org/abs/2604.12172) | C / 53 |
| 434 | [GoAT-X: A Graph of Auditing Thoughts for Securing Token Transactions in Cross-Chain Contracts](https://arxiv.org/abs/2604.24341) | C / 53 |
| 437 | [Identifying and Characterizing Semantic Clones of Solidity Functions](https://arxiv.org/abs/2604.26526) | C / 53 |
| 457 | [Towards Compositional Generalization in LLMs for Smart Contract Security: A Case Study on Reentrancy Vulnerabilities](https://arxiv.org/abs/2601.06914) | C / 52 |
| 463 | [V2E: Validating Smart Contract Vulnerabilities through Profit-driven Exploit Generation and Execution](https://arxiv.org/abs/2604.13611) | C / 52 |
| 470 | [ContractLens: Latent Security Knowledge for Malicious Smart Contract Detection](https://arxiv.org/abs/2610.04992) | C / 52 |
| 475 | [Large Language Model based Smart Contract Auditing with LLMBugScanner](https://arxiv.org/abs/2512.02069) | C / 51 |
| 524 | [AttackPathGNN: Cross-function vulnerability detection in smart contracts using state interference graphs and conjunction pooling](https://arxiv.org/abs/2606.05986) | C / 49 |
| 541 | [Robust Smart Contract Vulnerability Detection via Contrastive Learning-Enhanced Granular-ball Training](https://arxiv.org/abs/2603.27734) | C / 48 |
| 568 | [Examining the Effectiveness of Transformer-Based Smart Contract Vulnerability Scan](https://arxiv.org/abs/2601.07334) | C / 46 |
| 573 | [Chiral Analysis of Smart Contracts: Detecting Vulnerabilities from Relational Inconsistencies Across Business Paths](https://arxiv.org/abs/2607.17987) | C / 46 |
| 578 | [USCSA: Evolution-Aware Security Analysis for Proxy-Based Upgradeable Smart Contracts](https://arxiv.org/abs/2512.08372) | C / 45 |
| 584 | [Automated Vulnerability Injection in Smart Contracts Using Large Language Models](https://arxiv.org/abs/2609.02624) | C / 45 |
| 603 | [Web3 x AI Agents: Landscape, Integrations, and Foundational Challenges](https://arxiv.org/abs/2508.02773) | D / 43 |
| 616 | [Validating Solidity Code Defects using Symbolic and Concrete Execution powered by Large Language Models](https://arxiv.org/abs/2509.13023) | D / 42 |
| 623 | [Repository-Level Solidity Code Generation with Large Language Models: From Prompting to Fine-Tuning](https://arxiv.org/abs/2606.19988) | D / 42 |
| 630 | [ScamDetect: Towards a Robust, Agnostic Framework to Uncover Threats in Smart Contracts](https://arxiv.org/abs/2508.07094) | D / 41 |
| 648 | [Prompt Engineering vs. Fine-Tuning for LLM-Based Vulnerability Detection in Solana and Algorand Smart Contracts](https://arxiv.org/abs/2511.11250) | D / 39 |
| 649 | [Evaluating the Vulnerability Landscape of LLM-Generated Smart Contracts](https://arxiv.org/abs/2602.04039) | D / 39 |
| 667 | [Towards LLM-assisted High-Quality Property Generation for Solidity Smart Contracts](https://arxiv.org/abs/2607.23308) | D / 36 |

#### binary / firmware (58 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 14 | [The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark](https://arxiv.org/abs/2608.11469) | B / 73 |
| 57 | [Towards Effective Fuzzing of EDK2 Components](https://arxiv.org/abs/2611.03854) | B / 68 |
| 67 | [Agentic Vulnerability Reasoning on COTS Binaries](https://arxiv.org/abs/2605.05000) | B / 67 |
| 92 | [Reveree: Diagnosing LLM Reverse-Engineering Agents](https://arxiv.org/abs/2609.01185) | B / 66 |
| 97 | [Rethinking Neural Decompilation: Candidate Selection as the Hidden Bottleneck](https://arxiv.org/abs/2611.02788) | B / 66 |
| 100 | [Multi-LLM Energy Reasoning for Binary-Free Zero-Day IoT Detection](https://arxiv.org/abs/2512.19945) | B / 65 |
| 103 | [Securing the Dark Matter: A Semantic-Enhanced Neuro-Symbolic Framework for Supply Chain Analysis of Opaque Industrial Software](https://arxiv.org/abs/2605.07737) | B / 65 |
| 110 | [When LLM Decompilers Recompile More and Preserve Less](https://arxiv.org/abs/2609.05370) | B / 65 |
| 113 | [Humans vs. Machines: A Comparison With AI Agents in Software Reverse Engineering](https://arxiv.org/abs/2610.14960) | B / 65 |
| 114 | [SEMPRE: Semantic-Aware Protocol Reverse Engineering via Consistency-Driven Joint Optimization](https://arxiv.org/abs/2610.31844) | B / 65 |
| 123 | [Synergistic Directed Execution and LLM-Driven Analysis for Zero-Day AI-Generated Malware Detection](https://arxiv.org/abs/2603.09044) | B / 64 |
| 132 | [SoK: Are LLMs Reliable at Source Code Recovery? A Taxonomy and Empirical Evaluation](https://arxiv.org/abs/2610.11556) | B / 64 |
| 141 | [Attention Distance: A Novel Metric for Directed Fuzzing with Large Language Models](https://arxiv.org/abs/2512.19758) | B / 63 |
| 147 | [Veritas: Grounding LLM Agents for Reliable Vulnerability Reasoning over Stripped Binaries](https://arxiv.org/abs/2605.15097) | B / 63 |
| 153 | [Echo: Learning-based Matching Decompilation using Trusted Back Translation](https://arxiv.org/abs/2609.18706) | B / 63 |
| 154 | [ReproBench: Benchmarking LLM Agents on Reproducing Vulnerability From Scratch](https://arxiv.org/abs/2609.34450) | B / 63 |
| 170 | [HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation](https://arxiv.org/abs/2601.13864) | B / 62 |
| 177 | [SCARA: A Semantics-Constrained Autonomous Remediation Agent for Opaque Industrial Software Vulnerabilities](https://arxiv.org/abs/2605.19668) | B / 62 |
| 192 | [Exposing Hidden Interfaces: LLM-Guided Type Inference for Reverse Engineering macOS Private Frameworks](https://arxiv.org/abs/2601.01673) | B / 61 |
| 197 | [Implicit Patterns in LLM-Based Binary Analysis](https://arxiv.org/abs/2603.19138) | B / 61 |
| 219 | [LLMs as Firmware Experts: A Runtime-Grown Tree-of-Agents Framework](https://arxiv.org/abs/2511.18438) | B / 60 |
| 302 | [Hieronym: Leveraging Hierarchical Multi-Source Information for Function Renaming in Stripped Binary](https://arxiv.org/abs/2609.12457) | C / 58 |
| 328 | [VulDec: Vulnerability Detection in Binaries via Neural Decompilation](https://arxiv.org/abs/2610.33716) | C / 57 |
| 329 | [Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products](https://arxiv.org/abs/2610.42032) | C / 57 |
| 332 | [Securing LLM-Generated Embedded Firmware through AI Agent-Driven Validation and Patching](https://arxiv.org/abs/2509.09970) | C / 56 |
| 348 | [ASSEMBLAGE-DEEPHISTORY: A Cross-Build Binary Dataset with Temporal Coverage](https://arxiv.org/abs/2605.21615) | C / 56 |
| 378 | [PCodeTrans: Translate Decompiled Pseudocode to Compilable and Executable Equivalent](https://arxiv.org/abs/2603.14855) | C / 55 |
| 380 | [Aray: Deterministic-First Synthesis of Benign Artifacts for YARA Validation](https://arxiv.org/abs/2608.19387) | C / 55 |
| 383 | [ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers](https://arxiv.org/abs/2609.19722) | C / 55 |
| 401 | [Binary Decompilation LLM with Feedback-Driven Multi-Turn Refinement](https://arxiv.org/abs/2606.16162) | C / 54 |
| 407 | [Why Is SHAP Not a Reliable Standalone Explanation Framework for Malware Detection?](https://arxiv.org/abs/2609.04626) | C / 54 |
| 466 | [EntailLLM: Verifying LLM-Generated Vulnerability Discovery Paths with Domain Knowledge via Logic Programming](https://arxiv.org/abs/2608.01763) | C / 52 |
| 477 | [ReSIM: Re-ranking Binary Similarity Embeddings to Improve Function Search Performance](https://arxiv.org/abs/2602.09548) | C / 51 |
| 478 | [CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering](https://arxiv.org/abs/2604.03750) | C / 51 |
| 480 | [Feedback-Driven Execution for LLM-Based Binary Analysis](https://arxiv.org/abs/2604.15136) | C / 51 |
| 483 | [REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange](https://arxiv.org/abs/2606.05493) | C / 51 |
| 498 | [Sift or Get Off the PoC: Applying Information Retrieval to Vulnerability Research with SiftRank](https://arxiv.org/abs/2512.06155) | C / 50 |
| 506 | [FirmCure:Towards Autonomous and Adaptive Rehosting of Linux-Based Firmware](https://arxiv.org/abs/2606.24549) | C / 50 |
| 513 | [InterType: Breaking the Single-Function Barrier in Neural Binary Type Inference](https://arxiv.org/abs/2610.26906) | C / 50 |
| 528 | [N2NMatcher: Towards Inlining-Resilient Binary Decomposition and Module Matching](https://arxiv.org/abs/2608.10043) | C / 49 |
| 540 | [Walma: Learning to See Memory Corruption in WebAssembly](https://arxiv.org/abs/2603.24167) | C / 48 |
| 545 | [Malformer: A Multi-Modal Malware Detector Using Transformers](https://arxiv.org/abs/2608.19052) | C / 48 |
| 551 | [Federated Learning for Malware Image Classification under Data Heterogeneity](https://arxiv.org/abs/2610.25264) | C / 48 |
| 559 | [RAMP: Reversing Adversarial Perturbations to Strengthen Clean-Label Backdoor Attacks against Malware Detectors](https://arxiv.org/abs/2609.27422) | C / 47 |
| 564 | [SoK: Potentials and Challenges of Large Language Models for Reverse Engineering](https://arxiv.org/abs/2509.21821) | C / 46 |
| 600 | [Behavior-Centric Malware Classification with Fine-Grained Malicious Logic Localization](https://arxiv.org/abs/2609.38390) | D / 44 |
| 609 | [Deep Learning-based Binary Analysis for Vulnerability Detection in x86-64 Machine Code](https://arxiv.org/abs/2601.09157) | D / 43 |
| 613 | [A Comparison of Malware Image Transformations Using Grad-CAM and Hybrid Learning Models](https://arxiv.org/abs/2608.12077) | D / 43 |
| 622 | [LCC-LLM: Leveraging Code-Centric Large Language Models for Malware Attribution](https://arxiv.org/abs/2605.05807) | D / 42 |
| 637 | [SEMA-GUARD: Semantic and Graph-Based Vulnerability Detection in Assembly Code](https://arxiv.org/abs/2609.17254) | D / 41 |
| 643 | [VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents](https://arxiv.org/abs/2607.09653) | D / 40 |
| 645 | [Enhancing Multiclass Malware Classification in Resource-Constrained Environments](https://arxiv.org/abs/2609.27950) | D / 40 |
| 652 | [C-ing Clearly: Enhanced Binary Code Explanations using C code](https://arxiv.org/abs/2512.14500) | D / 38 |
| 654 | [SoK: AI-Augmented Binary Reversing](https://arxiv.org/abs/2606.17398) | D / 38 |
| 657 | [Cross-modal Retrieval Models for Stripped Binary Analysis](https://arxiv.org/abs/2512.10393) | D / 37 |
| 662 | [When Machine Learning Meets Vulnerability Discovery: Challenges and Lessons Learned](https://arxiv.org/abs/2508.15042) | D / 36 |
| 674 | [Pretraining on Call Graphs: When Binary Analysis Tasks Profit From Context](https://arxiv.org/abs/2608.02084) | D / 31 |
| 676 | [Automatically Attacking Software Reverse Engineering AI Agents](https://arxiv.org/abs/2605.30667) | D / 29 |

#### web (21 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 8 | [SecureCode: A Production-Grade Multi-Turn Dataset for Training Security-Aware Code Generation Models](https://arxiv.org/abs/2512.18542) | B / 74 |
| 11 | [ABSENTIA: Detecting Broken Access Control Vulnerabilities in Web Applications](https://arxiv.org/abs/2610.00977) | B / 74 |
| 32 | [LLM Agents for Automated Web Vulnerability Reproduction: Are We There Yet?](https://arxiv.org/abs/2510.14700) | B / 70 |
| 38 | [VULSOLVER: Vulnerability Detection via LLM-Driven Constraint Solving](https://arxiv.org/abs/2509.00882) | B / 69 |
| 52 | [RuleForge: Automated Generation and Validation for Web Vulnerability Detection at Scale](https://arxiv.org/abs/2604.01977) | B / 68 |
| 80 | [AXE: Grey-Box Exploitability Confirmation for Localized Vulnerability Reports](https://arxiv.org/abs/2602.14345) | B / 66 |
| 149 | [Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks](https://arxiv.org/abs/2605.23243) | B / 63 |
| 160 | [Multi-Agent Penetration Testing AI for the Web](https://arxiv.org/abs/2508.20816) | B / 62 |
| 182 | [One Pipeline Does Not Fit All: TAILOR, a Type- and State-Aware Framework for CVE Reproduction](https://arxiv.org/abs/2609.37006) | B / 62 |
| 255 | [RECEIPT: Deterministic, Reward-Hacking-Resistant Verification for White-Box Agentic XSS Discovery](https://arxiv.org/abs/2607.18575) | C / 59 |
| 259 | [SpiderSapien: Client-Centric Web Crawler and Security Scanner](https://arxiv.org/abs/2609.02532) | C / 59 |
| 270 | [Ulysses: A Security Harness For Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831) | C / 59 |
| 273 | [A Gingerbread House for LLM Agents: Source-Planned Honeypots That Lure Autonomous Attackers into an Isolated Shadow](https://arxiv.org/abs/2611.07611) | C / 59 |
| 303 | [AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination](https://arxiv.org/abs/2609.19140) | C / 58 |
| 307 | [The Long Con on the Web: Earn-then-Exploit Fraud Attacks against Coding Agents](https://arxiv.org/abs/2611.00725) | C / 58 |
| 424 | [AutoVulnPHP: LLM-Powered Two-Stage PHP Vulnerability Detection and Automated Localization](https://arxiv.org/abs/2601.06177) | C / 53 |
| 438 | [MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents](https://arxiv.org/abs/2605.03952) | C / 53 |
| 539 | [Following Dragons: Code Review-Guided Fuzzing](https://arxiv.org/abs/2602.10487) | C / 48 |
| 558 | [Evaluating LLMs for Real-World Web Vulnerability Detection](https://arxiv.org/abs/2606.21397) | C / 47 |
| 624 | [Understanding the (In)Security of Vibe-Coded Applications](https://arxiv.org/abs/2606.23130) | D / 42 |
| 659 | [A Quasi-Experimental Developer Study of Security Training in LLM-Assisted Web Application Development](https://arxiv.org/abs/2604.17763) | D / 37 |

#### mobile / Android (17 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 7 | [JANUS: Agentic Cross-Language Fuzzing Harness Generation for Android Native Libraries](https://arxiv.org/abs/2610.30218) | A / 75 |
| 49 | [MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes](https://arxiv.org/abs/2609.23980) | B / 69 |
| 188 | [Agentic Discovery and Validation of Android App Vulnerabilities](https://arxiv.org/abs/2508.21579) | B / 61 |
| 231 | [FlowArk: Boosting Agentic Data-flow Analysis for Android Apps via Context-Aware Knowledge Reuse](https://arxiv.org/abs/2607.11308) | B / 60 |
| 237 | [GAPS: Targeted Execution of Android Apps via Static Path Reconstruction](https://arxiv.org/abs/2511.23213) | C / 59 |
| 275 | [Revisiting Third-Party Library Detection: A Ground Truth Dataset and Its Implications Across Security Tasks](https://arxiv.org/abs/2509.04091) | C / 58 |
| 357 | [Moirae: A Multimodal Agent Collaborative Framework for Dynamic Android Malware Detection](https://arxiv.org/abs/2608.27994) | C / 56 |
| 365 | [Evaluating Large Language Models in detecting Secrets in Android Apps](https://arxiv.org/abs/2510.18601) | C / 55 |
| 373 | [Okara: Detection and Attribution of TLS Man-in-the-Middle Vulnerabilities in Android Apps with Foundation Models](https://arxiv.org/abs/2601.22770) | C / 55 |
| 384 | [HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning](https://arxiv.org/abs/2609.26352) | C / 55 |
| 436 | [MARD: A Multi-Agent Framework for Robust Android Malware Detection](https://arxiv.org/abs/2604.25264) | C / 53 |
| 443 | [Evaluating LLMs for Obfuscation Detection and Classification in Android Apps](https://arxiv.org/abs/2606.14233) | C / 53 |
| 488 | [When Label Noise Meets Class Imbalance: A Robust Framework for Android Malware Family Classification](https://arxiv.org/abs/2609.22835) | C / 51 |
| 574 | [MalFlows: Context-aware Fusion of Heterogeneous Flow Semantics for Android Malware Detection](https://arxiv.org/abs/2508.03588) | C / 45 |
| 585 | [Name2Pkg: Lightweight One-Class Android Malware Screening via Name-Package Correspondence Modeling](https://arxiv.org/abs/2609.24389) | C / 45 |
| 596 | [Towards LLM-Enhanced Android Taint Analysis](https://arxiv.org/abs/2608.24269) | D / 44 |
| 668 | [What You Code Is What We Prove: Translating BLE App Logic into Formal Models with LLMs for Vulnerability Detection](https://arxiv.org/abs/2509.09291) | D / 35 |

#### package ecosystem (33 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 16 | [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](https://arxiv.org/abs/2609.15939) | B / 73 |
| 22 | [Autonomous OSS Threat Detection via Taxonomy-Aligned LLMs](https://arxiv.org/abs/2610.01263) | B / 72 |
| 31 | [Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub](https://arxiv.org/abs/2610.11169) | B / 71 |
| 73 | [From Instructions to Exploits: Applying Program Analysis to Malicious Agent Skills Across Natural Language and Code](https://arxiv.org/abs/2610.33489) | B / 67 |
| 130 | [From Component Snapshots to Lifecycle Traces: Agent-Based Software Composition Analysis](https://arxiv.org/abs/2609.18391) | B / 64 |
| 156 | [Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents](https://arxiv.org/abs/2609.39065) | B / 63 |
| 161 | [An Empirical Study of Vulnerabilities in Python Packages and Their Detection](https://arxiv.org/abs/2509.04260) | B / 62 |
| 171 | [Formal Analysis and Supply Chain Security for Agentic AI Skills](https://arxiv.org/abs/2603.00195) | B / 62 |
| 200 | [Secret Stealing Attacks on Local LLM Fine-Tuning through Supply-Chain Model Code Backdoors](https://arxiv.org/abs/2604.27426) | B / 61 |
| 209 | [DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation](https://arxiv.org/abs/2609.28996) | B / 61 |
| 263 | [CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection](https://arxiv.org/abs/2609.18862) | C / 59 |
| 277 | [Library Hallucinations in LLM-Generated Code: A Risk Analysis Grounded in Developer Queries](https://arxiv.org/abs/2509.22202) | C / 58 |
| 279 | [Towards Classifying Benign And Malicious Packages Using Machine Learning](https://arxiv.org/abs/2511.15033) | C / 58 |
| 318 | [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494) | C / 57 |
| 322 | [Evaluating Inference-Time Defenses Against Package Hallucination in LLM-Generated Code](https://arxiv.org/abs/2608.22652) | C / 57 |
| 336 | [Taint-Based Code Slicing for LLMs-based Malicious NPM Package Detection](https://arxiv.org/abs/2512.12313) | C / 56 |
| 352 | [ProfMalPlus: Agent-Coordinated Detection of Malicious NPM Packages via Static-Dynamic Analysis Synergy](https://arxiv.org/abs/2607.13965) | C / 56 |
| 387 | [SINGED: Correct Outputs Do Not Certify Safe Execution in LLM Agents](https://arxiv.org/abs/2609.35889) | C / 55 |
| 405 | [SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills](https://arxiv.org/abs/2608.08468) | C / 54 |
| 411 | [Spoofing the Toolbox: Optimizing Tool Descriptions to Deceive LLM Agents](https://arxiv.org/abs/2610.33182) | C / 54 |
| 423 | [Agentic AI for Autonomous Defense in Software Supply Chain Security: Beyond Provenance to Vulnerability Mitigation](https://arxiv.org/abs/2512.23480) | C / 53 |
| 426 | [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/abs/2601.10338) | C / 53 |
| 433 | [Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning](https://arxiv.org/abs/2604.20179) | C / 53 |
| 444 | [PYPILINE: Malicious PyPI Package Detection via Suspicious API Knowledge and Agent Workflow](https://arxiv.org/abs/2606.19063) | C / 53 |
| 447 | [Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files](https://arxiv.org/abs/2610.09264) | C / 53 |
| 458 | [Cascaded Vulnerability Attacks in Software Supply Chains](https://arxiv.org/abs/2601.20158) | C / 52 |
| 555 | [Multi-Agent Taint Specification Extraction for Vulnerability Detection](https://arxiv.org/abs/2601.10865) | C / 47 |
| 572 | [Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge](https://arxiv.org/abs/2607.10221) | C / 46 |
| 590 | [An LLM-based Quantitative Framework for Evaluating High-Stealthy Backdoor Risks in OSS Supply Chains](https://arxiv.org/abs/2511.13341) | D / 44 |
| 601 | [Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents](https://arxiv.org/abs/2609.39607) | D / 44 |
| 605 | [HFuzzer: Testing Large Language Models for Package Hallucinations via Phrase-based Fuzzing](https://arxiv.org/abs/2509.23835) | D / 43 |
| 671 | [Measuring the Security of the Evolving Software Supply Chain: a Research Agenda](https://arxiv.org/abs/2609.08810) | D / 32 |
| 675 | [Investigating Security Implications of Automatically Generated Code on the Software Supply Chain](https://arxiv.org/abs/2509.20277) | D / 30 |

#### cross-language (67 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 2 | [CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability](https://arxiv.org/abs/2602.03012) | A / 76 |
| 3 | [MemRepair: Hierarchical Memory for Agentic Repository-Level Vulnerability Repair](https://arxiv.org/abs/2605.17444) | A / 76 |
| 21 | [VEX-Bench: Benchmarking LLM Agents for Assessing Exploitability of Software Supply Chain Vulnerabilities](https://arxiv.org/abs/2609.08040) | B / 72 |
| 26 | [RAVEN: Agentic RAG for Automated Vulnerability Repair](https://arxiv.org/abs/2606.22647) | B / 71 |
| 45 | [ContraFix: Skill-Enhanced Contrastive Runtime Analysis for Vulnerability Repair](https://arxiv.org/abs/2605.17450) | B / 69 |
| 48 | [What is the Difference Between Me and You? Benchmarking the Quality Gap Between Human-Written and AI-Generated Code](https://arxiv.org/abs/2609.12708) | B / 69 |
| 53 | [Quality-Assured Fuzz Harness Generation via the Four Principles Framework](https://arxiv.org/abs/2605.21824) | B / 68 |
| 56 | [Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security](https://arxiv.org/abs/2610.24896) | B / 68 |
| 63 | [VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection](https://arxiv.org/abs/2512.07533) | B / 67 |
| 83 | [Seclens: Role-specific Evaluation of LLM's for security vulnerablity detection](https://arxiv.org/abs/2604.01637) | B / 66 |
| 86 | [Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection](https://arxiv.org/abs/2606.30587) | B / 66 |
| 91 | [GraftyVul: Synthesising Insecure Programs Through Real-World Vulnerability Grafting](https://arxiv.org/abs/2608.27928) | B / 66 |
| 98 | [CryptoScope: Utilizing Large Language Models for Automated Cryptographic Logic Vulnerability Detection](https://arxiv.org/abs/2508.11599) | B / 65 |
| 101 | [Beyond Single Bugs: Benchmarking Large Language Models for Multi-Vulnerability Detection](https://arxiv.org/abs/2512.22306) | B / 65 |
| 109 | [VICBench: A Multi-Language Benchmark for Code Vulnerability Detection](https://arxiv.org/abs/2608.12246) | B / 65 |
| 121 | [A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection](https://arxiv.org/abs/2512.16538) | B / 64 |
| 125 | [EvoRepair: Enhancing Vulnerability Repair Agents Through Experience-Based Self-Evolution](https://arxiv.org/abs/2605.30105) | B / 64 |
| 131 | [SecProbe: Adaptive Evaluation of Coding Agents on Cybersecurity Vulnerabilities](https://arxiv.org/abs/2609.33763) | B / 64 |
| 140 | [PATCHEVAL: A New Benchmark for Evaluating LLMs on Patching Real-World Vulnerabilities](https://arxiv.org/abs/2511.11019) | B / 63 |
| 146 | [VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.09461) | B / 63 |
| 151 | [ShadowProbe: Language-Extensible Detection of Hidden Algorithmic Complexity Vulnerabilities](https://arxiv.org/abs/2607.05474) | B / 63 |
| 174 | [How Code Representation Shapes False-Positive Dynamics in Cross-Language LLM Vulnerability Detection](https://arxiv.org/abs/2604.27714) | B / 62 |
| 180 | [Checked-In Secret Detection: Strings Are All You Need](https://arxiv.org/abs/2608.04523) | B / 62 |
| 194 | [QRS: A Rule-Synthesizing Neuro-Symbolic Triad for Autonomous Vulnerability Discovery](https://arxiv.org/abs/2602.09774) | B / 61 |
| 211 | [Newer and Bigger, but Safer? A Longitudinal Study of the Functionality-Security Gap in LLM-Generated Code](https://arxiv.org/abs/2610.08240) | B / 61 |
| 214 | [Code Vulnerability Detection Across Different Programming Languages with AI Models](https://arxiv.org/abs/2508.11710) | B / 60 |
| 223 | [VulStyle: A Multi-Modal Pre-Training for Code Stylometry-Augmented Vulnerability Detection](https://arxiv.org/abs/2604.26313) | B / 60 |
| 239 | [PatchIsland: Orchestration of LLM Agents for Continuous Vulnerability Repair](https://arxiv.org/abs/2601.17471) | C / 59 |
| 247 | [VulKey: Automated Vulnerability Repair Guided by Domain-Specific Repair Patterns](https://arxiv.org/abs/2605.01769) | C / 59 |
| 253 | [Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs](https://arxiv.org/abs/2607.00555) | C / 59 |
| 254 | [The Language of Security: How Prompt Syntax Shapes Secure Code Generation in Open LLMs](https://arxiv.org/abs/2607.15937) | C / 59 |
| 269 | [Trojan Horse: Automated Repository Poisoning against Coding Agents](https://arxiv.org/abs/2610.23109) | C / 59 |
| 282 | [SecCodeBench-V2 Technical Report](https://arxiv.org/abs/2602.15485) | C / 58 |
| 285 | [SecPI: Secure Code Generation with Reasoning Models via Security Reasoning Internalization](https://arxiv.org/abs/2604.03587) | C / 58 |
| 290 | [PromptAudit: Auditing Prompt Sensitivity in LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.24171) | C / 58 |
| 322 | [Evaluating Inference-Time Defenses Against Package Hallucination in LLM-Generated Code](https://arxiv.org/abs/2608.22652) | C / 57 |
| 327 | [CWE-bench: Refocusing Agentic Security from Exploitation to Defense](https://arxiv.org/abs/2610.17020) | C / 57 |
| 338 | [Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming](https://arxiv.org/abs/2601.02060) | C / 56 |
| 343 | [Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis](https://arxiv.org/abs/2604.10800) | C / 56 |
| 351 | [Open-Source Intelligence for Code Provenance and the Security Patterns that Separate Human and Large-Language-Model Implementations of Common Programming Tasks](https://arxiv.org/abs/2607.12524) | C / 56 |
| 368 | [Secure Code Generation at Scale with Reflexion](https://arxiv.org/abs/2511.03898) | C / 55 |
| 390 | [Secure and Functional Code Generation with Self-Evaluation](https://arxiv.org/abs/2610.33450) | C / 55 |
| 396 | [From Theory to Practice: Code Generation Using LLMs for CAPEC and CWE Frameworks](https://arxiv.org/abs/2604.02548) | C / 54 |
| 398 | [MAS-SZZ: Multi-Agentic SZZ Algorithm for Vulnerability-Inducing Commit Identification](https://arxiv.org/abs/2604.24398) | C / 54 |
| 413 | [On the Evaluation of Large Language Models in Multilingual Vulnerability Repair](https://arxiv.org/abs/2508.03470) | C / 53 |
| 419 | [MulVuln: Enhancing Pre-trained LMs with Shared and Language-Specific Knowledge for Multilingual Vulnerability Detection](https://arxiv.org/abs/2510.04397) | C / 53 |
| 428 | [Code Fingerprints: Disentangled Attribution of LLM-Generated Code](https://arxiv.org/abs/2603.04212) | C / 53 |
| 429 | [Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities](https://arxiv.org/abs/2603.10163) | C / 53 |
| 432 | [SAGE: Signal-Amplified Guided Embeddings for LLM-based Vulnerability Detection](https://arxiv.org/abs/2604.19031) | C / 53 |
| 435 | [A systematic literature Review for Transformer-based Software Vulnerability detection](https://arxiv.org/abs/2604.24822) | C / 53 |
| 438 | [MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents](https://arxiv.org/abs/2605.03952) | C / 53 |
| 462 | [The Code Whisperer: LLM and Graph-Based AI for Smell and Vulnerability Resolution](https://arxiv.org/abs/2604.13114) | C / 52 |
| 465 | [An Empirical Study of Security Calibration in Large Language Models for Code](https://arxiv.org/abs/2606.31159) | C / 52 |
| 473 | [Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories](https://arxiv.org/abs/2510.26103) | C / 51 |
| 482 | [An Empirical Evaluation of LLM-Generated Code Security Across Prompting Methods](https://arxiv.org/abs/2605.24298) | C / 51 |
| 501 | [Can Adversarial Code Comments Fool AI Security Reviewers -- Large-Scale Empirical Study of Comment-Based Attacks and Defenses Against LLM Code Analysis](https://arxiv.org/abs/2602.16741) | C / 50 |
| 505 | [FORGE: Multi-Agent Graduated Exploitation and Detection Engineering](https://arxiv.org/abs/2606.03453) | C / 50 |
| 519 | [Quantum-Safe Code Auditing: LLM-Assisted Static Analysis and Quantum-Aware Risk Scoring for Post-Quantum Cryptography Migration](https://arxiv.org/abs/2604.00560) | C / 49 |
| 552 | [When Code Crosses Borders: A Security-Centric Study of LLM-based Code Translation](https://arxiv.org/abs/2509.06504) | C / 47 |
| 557 | [Enhancing Reliability in LLM-Based Secure Code Generation](https://arxiv.org/abs/2605.24300) | C / 47 |
| 575 | [Can LLMs Find Bugs in Code? An Evaluation from Beginner Errors to Security Vulnerabilities in Python and C++](https://arxiv.org/abs/2508.16419) | C / 45 |
| 589 | [On the Difficulty of Selecting Few-Shot Examples for Effective LLM-based Vulnerability Detection](https://arxiv.org/abs/2510.27675) | D / 44 |
| 594 | [Detect--Repair--Verify for LLM-Generated Code: A Multi-Language, Multi-Granularity Empirical Study](https://arxiv.org/abs/2603.23633) | D / 44 |
| 597 | [Vulnerable Code Search: Transferable Attack for Code Language Models](https://arxiv.org/abs/2608.26031) | D / 44 |
| 611 | [Minimal Prompt Perturbations Lead to Code Vulnerabilities: Prompt Fragility and Hidden-State Signals in Coding LLMs](https://arxiv.org/abs/2605.29737) | D / 43 |
| 633 | [Learn from Your Mistakes: Tree-like Self-Play for Secure Code LLMs](https://arxiv.org/abs/2606.03489) | D / 41 |
| 663 | [Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias](https://arxiv.org/abs/2508.17361) | D / 36 |

### 证据 Axis

#### real CVEs (140 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 2 | [CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability](https://arxiv.org/abs/2602.03012) | A / 76 |
| 3 | [MemRepair: Hierarchical Memory for Agentic Repository-Level Vulnerability Repair](https://arxiv.org/abs/2605.17444) | A / 76 |
| 8 | [SecureCode: A Production-Grade Multi-Turn Dataset for Training Security-Aware Code Generation Models](https://arxiv.org/abs/2512.18542) | B / 74 |
| 13 | [VCAO: Verifier-Centered Agentic Orchestration for Strategic OS Vulnerability Discovery](https://arxiv.org/abs/2604.08291) | B / 73 |
| 16 | [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](https://arxiv.org/abs/2609.15939) | B / 73 |
| 24 | [Multi-Agent End-to-End Vulnerability Management for Mitigating Recurring Vulnerabilities](https://arxiv.org/abs/2601.17762) | B / 71 |
| 25 | [VulWeaver: Weaving Broken Semantics for Grounded Vulnerability Detection](https://arxiv.org/abs/2604.10767) | B / 71 |
| 26 | [RAVEN: Agentic RAG for Automated Vulnerability Repair](https://arxiv.org/abs/2606.22647) | B / 71 |
| 28 | [AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration](https://arxiv.org/abs/2607.12058) | B / 71 |
| 29 | [From Runnable to Verifiable: An Independent Reproducibility Study of LLM/Agent-Driven Vulnerability Validation Artifacts](https://arxiv.org/abs/2608.09567) | B / 71 |
| 30 | [The History Is the Detector: Executing CVE Patch History, End-to-End](https://arxiv.org/abs/2609.05335) | B / 71 |
| 32 | [LLM Agents for Automated Web Vulnerability Reproduction: Are We There Yet?](https://arxiv.org/abs/2510.14700) | B / 70 |
| 33 | [Enhancing Continual Learning for Software Vulnerability Prediction: Addressing Catastrophic Forgetting via Hybrid-Confidence-Aware Selective Replay for Temporal LLM Fine-Tuning](https://arxiv.org/abs/2602.23834) | B / 70 |
| 34 | [VulnAgent-R2: Evidence-Calibrated Multi-Agent Auditing for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2603.13384) | B / 70 |
| 50 | [A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code](https://arxiv.org/abs/2611.06294) | B / 69 |
| 51 | [From CVE Entries to Verifiable Exploits: An Automated Multi-Agent Framework for Reproducing CVEs](https://arxiv.org/abs/2509.01835) | B / 68 |
| 52 | [RuleForge: Automated Generation and Validation for Web Vulnerability Detection at Scale](https://arxiv.org/abs/2604.01977) | B / 68 |
| 59 | [SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios](https://arxiv.org/abs/2509.22097) | B / 67 |
| 70 | [PrimSynth: An Agentic Approach to Discover, Validate, and Synthesize Exploit Primitives for Linux Kernel Vulnerabilities](https://arxiv.org/abs/2609.02647) | B / 67 |
| 72 | [An Empirical Analysis of CodeQL False Positives and Query Refinements for Java Vulnerabilities](https://arxiv.org/abs/2609.04535) | B / 67 |
| 79 | [Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection](https://arxiv.org/abs/2602.06751) | B / 66 |
| 80 | [AXE: Grey-Box Exploitability Confirmation for Localized Vulnerability Reports](https://arxiv.org/abs/2602.14345) | B / 66 |
| 84 | [Three Heads Are Better Than One: A Multi-perspective Reasoning Framework for Enhanced Vulnerability Detection](https://arxiv.org/abs/2605.18153) | B / 66 |
| 88 | [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](https://arxiv.org/abs/2607.12316) | B / 66 |
| 90 | [Vul4Py: Benchmarking Automated Vulnerability Repair in Python with Paired Exploit and Functional Oracles](https://arxiv.org/abs/2608.00692) | B / 66 |
| 91 | [GraftyVul: Synthesising Insecure Programs Through Real-World Vulnerability Grafting](https://arxiv.org/abs/2608.27928) | B / 66 |
| 98 | [CryptoScope: Utilizing Large Language Models for Automated Cryptographic Logic Vulnerability Detection](https://arxiv.org/abs/2508.11599) | B / 65 |
| 102 | [VulReaD: Knowledge-Graph-guided Software Vulnerability Reasoning and Detection](https://arxiv.org/abs/2602.10787) | B / 65 |
| 103 | [Securing the Dark Matter: A Semantic-Enhanced Neuro-Symbolic Framework for Supply Chain Analysis of Opaque Industrial Software](https://arxiv.org/abs/2605.07737) | B / 65 |
| 105 | [Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction](https://arxiv.org/abs/2607.01764) | B / 65 |
| 106 | [Beyond Detection: Agentic Attack Synthesis and Simulation for Smart Contracts](https://arxiv.org/abs/2607.15673) | B / 65 |
| 108 | [AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair](https://arxiv.org/abs/2607.29422) | B / 65 |
| 109 | [VICBench: A Multi-Language Benchmark for Code Vulnerability Detection](https://arxiv.org/abs/2608.12246) | B / 65 |
| 110 | [When LLM Decompilers Recompile More and Preserve Less](https://arxiv.org/abs/2609.05370) | B / 65 |
| 116 | [VulRTex: A Reasoning-Guided Approach to Identify Vulnerabilities from Rich-Text Issue Report](https://arxiv.org/abs/2509.03875) | B / 64 |
| 117 | [Ensembling Large Language Models for Code Vulnerability Detection: An Empirical Evaluation](https://arxiv.org/abs/2509.12629) | B / 64 |
| 120 | [VulInstruct: Teaching LLMs Root-Cause Reasoning for Vulnerability Detection via Security Specifications](https://arxiv.org/abs/2511.04014) | B / 64 |
| 129 | [CoSA: Context-Aware Severity Assessment via Context Analysis with Large Language Models](https://arxiv.org/abs/2608.13928) | B / 64 |
| 140 | [PATCHEVAL: A New Benchmark for Evaluating LLMs on Patching Real-World Vulnerabilities](https://arxiv.org/abs/2511.11019) | B / 63 |
| 141 | [Attention Distance: A Novel Metric for Directed Fuzzing with Large Language Models](https://arxiv.org/abs/2512.19758) | B / 63 |
| 142 | [AEGIS: From Clues to Verdicts -- Graph-Guided Deep Vulnerability Reasoning via Dialectics and Meta-Auditing](https://arxiv.org/abs/2603.20637) | B / 63 |
| 143 | [Software Vulnerability Detection Using a Lightweight Graph Neural Network](https://arxiv.org/abs/2603.29216) | B / 63 |
| 146 | [VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.09461) | B / 63 |
| 154 | [ReproBench: Benchmarking LLM Agents on Reproducing Vulnerability From Scratch](https://arxiv.org/abs/2609.34450) | B / 63 |
| 155 | [PatchHolmes: Agentic Patch Retrieval via Listwise Selection](https://arxiv.org/abs/2609.38807) | B / 63 |
| 159 | [RegoMender: A Multi-agent Framework for Automated Rego Policy Repair](https://arxiv.org/abs/2610.29456) | B / 63 |
| 161 | [An Empirical Study of Vulnerabilities in Python Packages and Their Detection](https://arxiv.org/abs/2509.04260) | B / 62 |
| 165 | [QuiLL: An LLM-Based Vulnerability Assessment Framework for the Wild](https://arxiv.org/abs/2510.04056) | B / 62 |
| 166 | [Trace: Securing Smart Contract Repository Against Access Control Vulnerability](https://arxiv.org/abs/2510.19254) | B / 62 |
| 167 | [Diffploit: Facilitating Cross-Version Exploit Migration for Open Source Library Vulnerabilities](https://arxiv.org/abs/2511.12950) | B / 62 |
| 178 | [CyberGym-E2E: Scalable Real-World Benchmark for AI Agents' End-to-End Cybersecurity Capabilities](https://arxiv.org/abs/2606.04460) | B / 62 |
| 182 | [One Pipeline Does Not Fit All: TAILOR, a Type- and State-Aware Framework for CVE Reproduction](https://arxiv.org/abs/2609.37006) | B / 62 |
| 183 | [Adaptive Code Revision Attacks on AI Pull Request Reviewers](https://arxiv.org/abs/2610.05399) | B / 62 |
| 184 | [LLM-based Code Auditing by Inferring and Evaluating Developer Assumptions](https://arxiv.org/abs/2610.15729) | B / 62 |
| 185 | [P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245) | B / 62 |
| 194 | [QRS: A Rule-Synthesizing Neuro-Symbolic Triad for Autonomous Vulnerability Discovery](https://arxiv.org/abs/2602.09774) | B / 61 |
| 199 | [Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection](https://arxiv.org/abs/2604.06633) | B / 61 |
| 206 | [SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing](https://arxiv.org/abs/2607.08949) | B / 61 |
| 207 | [Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities](https://arxiv.org/abs/2607.12723) | B / 61 |
| 210 | [COMPASS: Predicting the Relationship of Multiple Patches for Vulnerabilities with LLMs](https://arxiv.org/abs/2609.39783) | B / 61 |
| 212 | [SEEK: Agentic Knowledge Graph Retrieval for Secure Code Generation](https://arxiv.org/abs/2610.14968) | B / 61 |
| 216 | [MAVUL: Multi-Agent Vulnerability Detection via Contextual Reasoning and Interactive Refinement](https://arxiv.org/abs/2510.00317) | B / 60 |
| 220 | [Execution-State-Aware LLM Reasoning for Automated Proof-of-Vulnerability Generation](https://arxiv.org/abs/2602.13574) | B / 60 |
| 223 | [VulStyle: A Multi-Modal Pre-Training for Code Stylometry-Augmented Vulnerability Detection](https://arxiv.org/abs/2604.26313) | B / 60 |
| 224 | [Lightweight Vulnerability Detection from Code Metrics and Token Features](https://arxiv.org/abs/2605.04260) | B / 60 |
| 225 | [MARGIN: Margin-Aware Regularized Geometry for Imbalanced Vulnerability Detection](https://arxiv.org/abs/2605.10240) | B / 60 |
| 227 | [Transferable Self-Evolving Playbooks for Agentic Security Auditing](https://arxiv.org/abs/2606.16420) | B / 60 |
| 228 | [Knowledge-Enhanced Agentic Vulnerability Repair](https://arxiv.org/abs/2607.00820) | B / 60 |
| 229 | [JavaVulBench: A Java Vulnerability Benchmark with Realistic Splits, a Unified Multi-Backend Harness, and a Leakage-Aware Evaluation Mode](https://arxiv.org/abs/2607.02825) | B / 60 |
| 230 | [The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities](https://arxiv.org/abs/2607.05743) | B / 60 |
| 241 | [Bridging Code Property Graphs and Language Models for Program Analysis](https://arxiv.org/abs/2603.24837) | C / 59 |
| 242 | [Detecting Protracted Vulnerabilities in Open Source Projects](https://arxiv.org/abs/2603.27067) | C / 59 |
| 246 | [AgenticVM: Agentic AI for Adaptive Software Vulnerability Management](https://arxiv.org/abs/2605.01739) | C / 59 |
| 249 | [NeuroLog: Reasoning You Can Audit -- Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT](https://arxiv.org/abs/2606.00669) | C / 59 |
| 252 | [Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning](https://arxiv.org/abs/2606.25356) | C / 59 |
| 256 | [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](https://arxiv.org/abs/2607.24964) | C / 59 |
| 264 | [SelfOp: An Optimization Algorithm for Self-Improving Security Agents](https://arxiv.org/abs/2609.22792) | C / 59 |
| 270 | [Ulysses: A Security Harness For Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831) | C / 59 |
| 273 | [A Gingerbread House for LLM Agents: Source-Planned Honeypots That Lure Autonomous Attackers into an Isolated Shadow](https://arxiv.org/abs/2611.07611) | C / 59 |
| 289 | [Learning Generalizable Multimodal Representations for Software Vulnerability Detection](https://arxiv.org/abs/2604.25711) | C / 58 |
| 290 | [PromptAudit: Auditing Prompt Sensitivity in LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.24171) | C / 58 |
| 292 | [DIG: Oracle-Guided Directed Input Generation for One-Day Vulnerabilities](https://arxiv.org/abs/2606.13037) | C / 58 |
| 293 | [Routing Ceilings Are Domain-Independent: Structural Prior Injection in Code Security Vulnerability Detection](https://arxiv.org/abs/2607.14628) | C / 58 |
| 296 | [HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models](https://arxiv.org/abs/2607.27030) | C / 58 |
| 317 | [Reachability Across the NL/PL Boundary: A Taxonomy-Driven Dataflow Model for LLM-Integrated Applications](https://arxiv.org/abs/2603.28345) | C / 57 |
| 320 | [Graph Is the Verifier: Agentic Reinforcement Learning for Interprocedural Vulnerability Detection](https://arxiv.org/abs/2607.26656) | C / 57 |
| 329 | [Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products](https://arxiv.org/abs/2610.42032) | C / 57 |
| 334 | [PBFuzz: Agentic Directed Fuzzing for PoV Generation](https://arxiv.org/abs/2512.04611) | C / 56 |
| 340 | [LLMs in Code Vulnerability Analysis: A Proof of Concept](https://arxiv.org/abs/2601.08691) | C / 56 |
| 344 | [Symbolic Execution Meets Multi-LLM Orchestration: Detecting Memory Vulnerabilities in Incomplete Rust CVE Snippets](https://arxiv.org/abs/2605.00034) | C / 56 |
| 348 | [ASSEMBLAGE-DEEPHISTORY: A Cross-Build Binary Dataset with Temporal Coverage](https://arxiv.org/abs/2605.21615) | C / 56 |
| 363 | [PatchCon: Patch-aware Weighted Supervised Contrastive Learning for Vulnerability Detection](https://arxiv.org/abs/2611.06583) | C / 56 |
| 371 | [An Empirical Evaluation of LLM-Based Approaches for Code Vulnerability Detection: RAG, SFT, and Dual-Agent Systems](https://arxiv.org/abs/2601.00254) | C / 55 |
| 375 | [FuzzySQL: Uncovering Hidden Vulnerabilities in DBMS Special Features with LLM-Driven Fuzzing](https://arxiv.org/abs/2602.19490) | C / 55 |
| 379 | [TitanCA: Lessons from Orchestrating LLM Agents to Discover 100+ CVEs](https://arxiv.org/abs/2604.17860) | C / 55 |
| 381 | [Athena: Vulnerability-Affected Library Identification via Knowledge Graph Completion](https://arxiv.org/abs/2609.01187) | C / 55 |
| 392 | [PatchSeeker: Mapping NVD Records to their Vulnerability-fixing Commits with LLM Generated Commits and Embeddings](https://arxiv.org/abs/2509.07540) | C / 54 |
| 398 | [MAS-SZZ: Multi-Agentic SZZ Algorithm for Vulnerability-Inducing Commit Identification](https://arxiv.org/abs/2604.24398) | C / 54 |
| 400 | [SEC-bench Pro: Can Language Models Solve Long-Horizon Software Security Tasks?](https://arxiv.org/abs/2605.26548) | C / 54 |
| 404 | [VulnGym: Benchmarking Coding Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2608.02001) | C / 54 |
| 414 | [From Attack Descriptions to Vulnerabilities: A Sentence Transformer-Based Approach](https://arxiv.org/abs/2509.02077) | C / 53 |
| 419 | [MulVuln: Enhancing Pre-trained LMs with Shared and Language-Specific Knowledge for Multilingual Vulnerability Detection](https://arxiv.org/abs/2510.04397) | C / 53 |
| 422 | [Llama-based source code vulnerability detection: Prompt engineering vs Fine tuning](https://arxiv.org/abs/2512.09006) | C / 53 |
| 430 | [COBALT-TLA: A Neuro-Symbolic Verification Loop for Cross-Chain Bridge Vulnerability Discovery](https://arxiv.org/abs/2604.12172) | C / 53 |
| 432 | [SAGE: Signal-Amplified Guided Embeddings for LLM-based Vulnerability Detection](https://arxiv.org/abs/2604.19031) | C / 53 |
| 439 | [Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection](https://arxiv.org/abs/2605.20051) | C / 53 |
| 442 | [FusionVul: A Multimodal Feature Fusion Framework for Source Code Vulnerability Detection](https://arxiv.org/abs/2606.08553) | C / 53 |
| 452 | [VulnRepairEval: An Exploit-Based Evaluation Framework for Assessing Large Language Model Vulnerability Repair Capabilities](https://arxiv.org/abs/2509.03331) | C / 52 |
| 455 | [Vul-R2: A Reasoning LLM for Automated Vulnerability Repair](https://arxiv.org/abs/2510.05480) | C / 52 |
| 456 | [PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting](https://arxiv.org/abs/2511.20555) | C / 52 |
| 464 | [Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities](https://arxiv.org/abs/2605.28893) | C / 52 |
| 471 | [LLM-HyPZ: Hardware Vulnerability Discovery using an LLM-Assisted Hybrid Platform for Zero-Shot Knowledge Extraction and Refinement](https://arxiv.org/abs/2509.00647) | C / 51 |
| 474 | [ReVul-CoT: Towards Effective Software Vulnerability Assessment with Retrieval-Augmented Generation and Chain-of-Thought Prompting](https://arxiv.org/abs/2511.17027) | C / 51 |
| 476 | [SHERLOCK: A Deep Learning Approach To Detect Software Vulnerabilities](https://arxiv.org/abs/2512.12593) | C / 51 |
| 479 | [Vulnerability Detection with Interprocedural Context in Multiple Languages: Assessing Effectiveness and Cost of Modern LLMs](https://arxiv.org/abs/2604.08417) | C / 51 |
| 491 | [CVE-to-ATT&CK Mapping via Evidence-Constrained Ranking](https://arxiv.org/abs/2610.33924) | C / 51 |
| 494 | [LLaVul: A Multimodal LLM for Interpretable Vulnerability Reasoning about Source Code](https://arxiv.org/abs/2509.17337) | C / 50 |
| 496 | [QLCoder: A Query Synthesizer For Static Analysis of Security Vulnerabilities](https://arxiv.org/abs/2511.08462) | C / 50 |
| 499 | [From Lab to Reality: A Practical Evaluation of Deep Learning Models and LLMs for Vulnerability Detection](https://arxiv.org/abs/2512.10485) | C / 50 |
| 500 | [Well Begun is Half Done: Location-Aware and Trace-Guided Iterative Automated Vulnerability Repair](https://arxiv.org/abs/2512.20203) | C / 50 |
| 502 | [Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review](https://arxiv.org/abs/2603.18740) | C / 50 |
| 505 | [FORGE: Multi-Agent Graduated Exploitation and Detection Engineering](https://arxiv.org/abs/2606.03453) | C / 50 |
| 507 | [Beyond Refusal: A Same-Lineage Study of Aligned and Abliterated LLMs for Vulnerability Analysis](https://arxiv.org/abs/2607.05842) | C / 50 |
| 515 | [Beyond Imprecise Distance Metrics: Trace-Guided Directed Greybox Fuzzing via LLM-Predicted Call Stacks](https://arxiv.org/abs/2510.23101) | C / 49 |
| 518 | [Favia: Forensic Agent for Vulnerability-fix Identification and Analysis](https://arxiv.org/abs/2602.12500) | C / 49 |
| 522 | [PLMGH: What Matters in PLM-GNN Hybrids for Code Classification and Vulnerability Detection](https://arxiv.org/abs/2604.25599) | C / 49 |
| 525 | [Data-Centric Benchmarking of Exploit Generation in LLMs: Understanding the Impact of Fine-Tuning](https://arxiv.org/abs/2606.15123) | C / 49 |
| 527 | [VulnGym: Evaluating Vulnerability Management Strategies against Advanced Persistent Threats](https://arxiv.org/abs/2607.24552) | C / 49 |
| 530 | [Predicting CVSS and CWE from CVE Descriptions with Fine-Tuned Small Language Models](https://arxiv.org/abs/2610.24297) | C / 49 |
| 537 | [Focus on What Matters: Fisher-Guided Adaptive Multimodal Fusion for Vulnerability Detection](https://arxiv.org/abs/2601.02438) | C / 48 |
| 540 | [Walma: Learning to See Memory Corruption in WebAssembly](https://arxiv.org/abs/2603.24167) | C / 48 |
| 546 | [HARP: Hierarchical Adaptive Ranking with Preference-Adaptive Fusion for Query-Based CVE Prioritization](https://arxiv.org/abs/2608.19430) | C / 48 |
| 550 | [From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)](https://arxiv.org/abs/2610.20437) | C / 48 |
| 553 | [Automated Vulnerability Validation and Verification: A Large Language Model Approach](https://arxiv.org/abs/2509.24037) | C / 47 |
| 563 | [Revisiting Vulnerability Patch Localization: An Empirical Study and LLM-Based Solution](https://arxiv.org/abs/2509.15777) | C / 46 |
| 569 | [An Empirical Study of the Imbalance Issue in Software Vulnerability Detection](https://arxiv.org/abs/2602.12038) | C / 46 |
| 607 | [Evaluating LLMs for One-Shot Patching of Real and Artificial Vulnerabilities](https://arxiv.org/abs/2511.23408) | D / 43 |
| 627 | [Evaluating the NIST Bugs Framework Against CWE as a Successor for Automated Vulnerability Classification](https://arxiv.org/abs/2609.16433) | D / 42 |
| 655 | [Advanced Topic Modeling Techniques for Categorizing Software Vulnerabilities](https://arxiv.org/abs/2607.03887) | D / 38 |
| 664 | [Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation](https://arxiv.org/abs/2603.10072) | D / 36 |

#### real disclosure / maintainer-confirmed (42 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 9 | [An Effective and Cost-Efficient Agentic Framework for Ethereum Smart Contract Auditing](https://arxiv.org/abs/2601.17833) | B / 74 |
| 12 | [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](https://arxiv.org/abs/2611.03555) | B / 74 |
| 49 | [MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes](https://arxiv.org/abs/2609.23980) | B / 69 |
| 53 | [Quality-Assured Fuzz Harness Generation via the Four Principles Framework](https://arxiv.org/abs/2605.21824) | B / 68 |
| 57 | [Towards Effective Fuzzing of EDK2 Components](https://arxiv.org/abs/2611.03854) | B / 68 |
| 67 | [Agentic Vulnerability Reasoning on COTS Binaries](https://arxiv.org/abs/2605.05000) | B / 67 |
| 68 | [FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction](https://arxiv.org/abs/2605.21779) | B / 67 |
| 88 | [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](https://arxiv.org/abs/2607.12316) | B / 66 |
| 94 | [SmartMemory: Detecting On-chain-off-chain Communication Inconsistency for Smart Contract via Memory-based Agent](https://arxiv.org/abs/2609.34983) | B / 66 |
| 115 | [Keeping Fuzzers on Duty: Repairing Fuzzing Build Breakages in Continuous Open-Source Fuzzing](https://arxiv.org/abs/2611.06358) | B / 65 |
| 124 | [EvoPoC: Automated Exploit Synthesis for DeFi Smart Contracts via Hierarchical Knowledge Graphs](https://arxiv.org/abs/2605.02868) | B / 64 |
| 147 | [Veritas: Grounding LLM Agents for Reliable Vulnerability Reasoning over Stripped Binaries](https://arxiv.org/abs/2605.15097) | B / 63 |
| 148 | [Automated Repair of TEE Partitioning Issues via DSL-Guided and LLM-Assisted Patching](https://arxiv.org/abs/2605.22087) | B / 63 |
| 151 | [ShadowProbe: Language-Extensible Detection of Hidden Algorithmic Complexity Vulnerabilities](https://arxiv.org/abs/2607.05474) | B / 63 |
| 160 | [Multi-Agent Penetration Testing AI for the Web](https://arxiv.org/abs/2508.20816) | B / 62 |
| 167 | [Diffploit: Facilitating Cross-Version Exploit Migration for Open Source Library Vulnerabilities](https://arxiv.org/abs/2511.12950) | B / 62 |
| 207 | [Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities](https://arxiv.org/abs/2607.12723) | B / 61 |
| 245 | [Synthesizing Multi-Agent Harnesses for Vulnerability Discovery](https://arxiv.org/abs/2604.20801) | C / 59 |
| 249 | [NeuroLog: Reasoning You Can Audit -- Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT](https://arxiv.org/abs/2606.00669) | C / 59 |
| 253 | [Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs](https://arxiv.org/abs/2607.00555) | C / 59 |
| 255 | [RECEIPT: Deterministic, Reward-Hacking-Resistant Verification for White-Box Agentic XSS Discovery](https://arxiv.org/abs/2607.18575) | C / 59 |
| 286 | [LiquiLM: Bridging the Semantic Gap in Liquidity Flaw Audit via DCN and LLMs](https://arxiv.org/abs/2604.03860) | C / 58 |
| 311 | [MALF: A Multi-Agent LLM Framework for Intelligent Fuzzing of Industrial Control Protocols](https://arxiv.org/abs/2510.02694) | C / 57 |
| 347 | [VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers](https://arxiv.org/abs/2605.21392) | C / 56 |
| 352 | [ProfMalPlus: Agent-Coordinated Detection of Malicious NPM Packages via Static-Dynamic Analysis Synergy](https://arxiv.org/abs/2607.13965) | C / 56 |
| 365 | [Evaluating Large Language Models in detecting Secrets in Android Apps](https://arxiv.org/abs/2510.18601) | C / 55 |
| 373 | [Okara: Detection and Attribution of TLS Man-in-the-Middle Vulnerabilities in Android Apps with Foundation Models](https://arxiv.org/abs/2601.22770) | C / 55 |
| 375 | [FuzzySQL: Uncovering Hidden Vulnerabilities in DBMS Special Features with LLM-Driven Fuzzing](https://arxiv.org/abs/2602.19490) | C / 55 |
| 379 | [TitanCA: Lessons from Orchestrating LLM Agents to Discover 100+ CVEs](https://arxiv.org/abs/2604.17860) | C / 55 |
| 400 | [SEC-bench Pro: Can Language Models Solve Long-Horizon Software Security Tasks?](https://arxiv.org/abs/2605.26548) | C / 54 |
| 424 | [AutoVulnPHP: LLM-Powered Two-Stage PHP Vulnerability Detection and Automated Localization](https://arxiv.org/abs/2601.06177) | C / 53 |
| 439 | [Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection](https://arxiv.org/abs/2605.20051) | C / 53 |
| 456 | [PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting](https://arxiv.org/abs/2511.20555) | C / 52 |
| 493 | [Locus: Agentic Predicate Synthesis for Directed Fuzzing](https://arxiv.org/abs/2508.21302) | C / 50 |
| 503 | [AFL-ICP: Enhancing Industrial Control Protocol Reliability via Specification-Guided Fuzzing](https://arxiv.org/abs/2605.04760) | C / 50 |
| 504 | [PickleFuzzer: A Case Study in Fuzzing for Discrepancies Between Python Pickle Implementations](https://arxiv.org/abs/2605.15084) | C / 50 |
| 515 | [Beyond Imprecise Distance Metrics: Trace-Guided Directed Greybox Fuzzing via LLM-Predicted Call Stacks](https://arxiv.org/abs/2510.23101) | C / 49 |
| 542 | [MASFuzzer: Fuzz Driver Generation and Adaptive Scheduling via Multidimensional API Sequences](https://arxiv.org/abs/2604.17977) | C / 48 |
| 595 | [Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions](https://arxiv.org/abs/2605.06279) | D / 44 |
| 617 | [MirrorFuzz: Leveraging LLM and Shared Bugs for Deep Learning Framework APIs Fuzzing](https://arxiv.org/abs/2510.15690) | D / 42 |
| 635 | [CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs](https://arxiv.org/abs/2606.29124) | D / 41 |
| 640 | [LLM-Powered Silent Bug Fuzzing in Deep Learning Libraries via Versatile and Controlled Bug Transfer](https://arxiv.org/abs/2602.23065) | D / 40 |

#### wild / production data (194 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 4 | [Antaeus: Hunting Repository-Level Logic Vulnerabilities via Context-Grounded LLM Reasoning](https://arxiv.org/abs/2607.01138) | A / 76 |
| 5 | [LLMVul: A Vulnerability-Labeled Dataset of LLM-Generated C/C++ Functions from Real Production Repositories](https://arxiv.org/abs/2609.10945) | A / 76 |
| 6 | [OpenAnt: LLM-Powered Vulnerability Discovery Through Code Decomposition, Adversarial Verification, and Dynamic Testing](https://arxiv.org/abs/2606.19149) | A / 75 |
| 7 | [JANUS: Agentic Cross-Language Fuzzing Harness Generation for Android Native Libraries](https://arxiv.org/abs/2610.30218) | A / 75 |
| 9 | [An Effective and Cost-Efficient Agentic Framework for Ethereum Smart Contract Auditing](https://arxiv.org/abs/2601.17833) | B / 74 |
| 11 | [ABSENTIA: Detecting Broken Access Control Vulnerabilities in Web Applications](https://arxiv.org/abs/2610.00977) | B / 74 |
| 19 | [Towards a Risk Assessment of Malicious Skill Files in Coding Agents](https://arxiv.org/abs/2608.05223) | B / 72 |
| 21 | [VEX-Bench: Benchmarking LLM Agents for Assessing Exploitability of Software Supply Chain Vulnerabilities](https://arxiv.org/abs/2609.08040) | B / 72 |
| 22 | [Autonomous OSS Threat Detection via Taxonomy-Aligned LLMs](https://arxiv.org/abs/2610.01263) | B / 72 |
| 27 | [CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?](https://arxiv.org/abs/2606.26216) | B / 71 |
| 31 | [Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub](https://arxiv.org/abs/2610.11169) | B / 71 |
| 36 | [Defusing Explosive Prompts: Understanding and Preventing Trigger-Based Prompt Injections in LLM Agents](https://arxiv.org/abs/2609.22510) | B / 70 |
| 38 | [VULSOLVER: Vulnerability Detection via LLM-Driven Constraint Solving](https://arxiv.org/abs/2509.00882) | B / 69 |
| 39 | [Sifting the Noise: A Comparative Study of LLM Agents in Vulnerability False Positive Filtering](https://arxiv.org/abs/2601.22952) | B / 69 |
| 40 | [LogicScan: An LLM-driven Framework for Detecting Business Logic Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2602.03271) | B / 69 |
| 43 | [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/abs/2604.01645) | B / 69 |
| 48 | [What is the Difference Between Me and You? Benchmarking the Quality Gap Between Human-Written and AI-Generated Code](https://arxiv.org/abs/2609.12708) | B / 69 |
| 52 | [RuleForge: Automated Generation and Validation for Web Vulnerability Detection at Scale](https://arxiv.org/abs/2604.01977) | B / 68 |
| 55 | [IntentFuzz: A Protocol-Aware Fuzzer for Automated Invariant Violation Detection in Intent-Based Cross-Chain Bridges](https://arxiv.org/abs/2609.13004) | B / 68 |
| 58 | [Proving the Wrong Program: Miscompilations as a Threat to zkVM Guarantees](https://arxiv.org/abs/2611.04701) | B / 68 |
| 60 | [From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localization](https://arxiv.org/abs/2510.02389) | B / 67 |
| 61 | [FLAMES: Fine-tuning LLMs to Synthesize Invariants for Smart Contract Security](https://arxiv.org/abs/2510.21401) | B / 67 |
| 62 | [SmartPoC: Generating Executable and Validated PoCs for Smart Contract Bug Reports](https://arxiv.org/abs/2511.12993) | B / 67 |
| 73 | [From Instructions to Exploits: Applying Program Analysis to Malicious Agent Skills Across Natural Language and Code](https://arxiv.org/abs/2610.33489) | B / 67 |
| 76 | [RealSec-bench: A Benchmark for Evaluating Secure Code Generation in Real-World Repositories](https://arxiv.org/abs/2601.22706) | B / 66 |
| 82 | [Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization](https://arxiv.org/abs/2603.26270) | B / 66 |
| 89 | [DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2607.13439) | B / 66 |
| 94 | [SmartMemory: Detecting On-chain-off-chain Communication Inconsistency for Smart Contract via Memory-based Agent](https://arxiv.org/abs/2609.34983) | B / 66 |
| 110 | [When LLM Decompilers Recompile More and Preserve Less](https://arxiv.org/abs/2609.05370) | B / 65 |
| 111 | [Function Name Is All You Need to Detect Blockchain Application Attacks](https://arxiv.org/abs/2609.12315) | B / 65 |
| 112 | [Mind the Gap: Detecting Description-Execution Mismatch Attacks in DAO Governance](https://arxiv.org/abs/2609.13601) | B / 65 |
| 113 | [Humans vs. Machines: A Comparison With AI Agents in Software Reverse Engineering](https://arxiv.org/abs/2610.14960) | B / 65 |
| 114 | [SEMPRE: Semantic-Aware Protocol Reverse Engineering via Consistency-Driven Joint Optimization](https://arxiv.org/abs/2610.31844) | B / 65 |
| 115 | [Keeping Fuzzers on Duty: Repairing Fuzzing Build Breakages in Continuous Open-Source Fuzzing](https://arxiv.org/abs/2611.06358) | B / 65 |
| 116 | [VulRTex: A Reasoning-Guided Approach to Identify Vulnerabilities from Rich-Text Issue Report](https://arxiv.org/abs/2509.03875) | B / 64 |
| 122 | [From Coverage to Causes: Data-Centric Fuzzing for JavaScript Engines](https://arxiv.org/abs/2512.18102) | B / 64 |
| 123 | [Synergistic Directed Execution and LLM-Driven Analysis for Zero-Day AI-Generated Malware Detection](https://arxiv.org/abs/2603.09044) | B / 64 |
| 126 | [ARVO: Atlas of Reproducible Vulnerabilities for Open-Source Software](https://arxiv.org/abs/2606.17283) | B / 64 |
| 128 | [Memoir: Learning, Verifying, and Evolving False-Positive Memories for Static Application Security Testing Tools](https://arxiv.org/abs/2608.09181) | B / 64 |
| 130 | [From Component Snapshots to Lifecycle Traces: Agent-Based Software Composition Analysis](https://arxiv.org/abs/2609.18391) | B / 64 |
| 133 | [ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary](https://arxiv.org/abs/2610.13651) | B / 64 |
| 134 | [Names Are Not Objects: Object-Bound Confinement for Compromised AI Coding Agents](https://arxiv.org/abs/2610.14488) | B / 64 |
| 135 | [CyberDual: AI Attackers versus AI Code Reviewers in Real Software Maintenance](https://arxiv.org/abs/2610.34435) | B / 64 |
| 138 | [LLM-Powered Detection of Price Manipulation in DeFi](https://arxiv.org/abs/2510.21272) | B / 63 |
| 150 | [Code-Augur: Agentic Vulnerability Detection via Specification Inference](https://arxiv.org/abs/2606.18619) | B / 63 |
| 153 | [Echo: Learning-based Matching Decompilation using Trusted Back Translation](https://arxiv.org/abs/2609.18706) | B / 63 |
| 156 | [Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents](https://arxiv.org/abs/2609.39065) | B / 63 |
| 157 | [Narratives Mislead: An Empirical Study of How LLMs Misjudge CVSS Severity in Bug Bounty Reports](https://arxiv.org/abs/2610.24623) | B / 63 |
| 158 | [RELAY: Scaling Historical Build Restoration through Rule Reuse and Agentic Repair](https://arxiv.org/abs/2610.27784) | B / 63 |
| 159 | [RegoMender: A Multi-agent Framework for Automated Rego Policy Repair](https://arxiv.org/abs/2610.29456) | B / 63 |
| 160 | [Multi-Agent Penetration Testing AI for the Web](https://arxiv.org/abs/2508.20816) | B / 62 |
| 163 | [LISA Technical Report: An Agentic Framework for Smart Contract Auditing](https://arxiv.org/abs/2509.24698) | B / 62 |
| 166 | [Trace: Securing Smart Contract Repository Against Access Control Vulnerability](https://arxiv.org/abs/2510.19254) | B / 62 |
| 173 | [Revisiting and Expanding the IPv6 Periphery: Global-Scale Measurement and Security Analysis](https://arxiv.org/abs/2604.19487) | B / 62 |
| 179 | [Detecting Vulnerability-Inducing Commits via Multi-Stage Reasoning with LLM-Based Agents](https://arxiv.org/abs/2607.05772) | B / 62 |
| 180 | [Checked-In Secret Detection: Strings Are All You Need](https://arxiv.org/abs/2608.04523) | B / 62 |
| 181 | [SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs](https://arxiv.org/abs/2609.06149) | B / 62 |
| 186 | [Do Coding Agents Understand Why Systems Crash---and Why They Don't?](https://arxiv.org/abs/2610.29332) | B / 62 |
| 188 | [Agentic Discovery and Validation of Android App Vulnerabilities](https://arxiv.org/abs/2508.21579) | B / 61 |
| 190 | [iCodeReviewer: Improving Secure Code Review with Mixture of Prompts](https://arxiv.org/abs/2510.12186) | B / 61 |
| 191 | [Leveraging Self-Paced Learning for Software Vulnerability Detection](https://arxiv.org/abs/2511.09212) | B / 61 |
| 202 | [Quality and Security Signals in AI-Generated Python Refactoring Pull Requests](https://arxiv.org/abs/2605.21453) | B / 61 |
| 205 | [Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases](https://arxiv.org/abs/2606.22263) | B / 61 |
| 208 | [When Verified Source Becomes Attack Input: Defending Smart Contracts Against LLM-Based Vulnerability Scanning](https://arxiv.org/abs/2608.28400) | B / 61 |
| 209 | [DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation](https://arxiv.org/abs/2609.28996) | B / 61 |
| 213 | [When File Ingestion Misleads Language Models: Measuring and Mitigating Divergences in Office Documents](https://arxiv.org/abs/2611.05806) | B / 61 |
| 215 | [Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity](https://arxiv.org/abs/2508.21634) | B / 60 |
| 219 | [LLMs as Firmware Experts: A Runtime-Grown Tree-of-Agents Framework](https://arxiv.org/abs/2511.18438) | B / 60 |
| 221 | [LibScan: Smart Contract Library Misuse Detection with Iterative Feedback and Static Verification](https://arxiv.org/abs/2604.00657) | B / 60 |
| 231 | [FlowArk: Boosting Agentic Data-flow Analysis for Android Apps via Context-Aware Knowledge Reuse](https://arxiv.org/abs/2607.11308) | B / 60 |
| 232 | [RuleAutoPilot: Synthesizing Deployable Suricata Rules from Network Traffic](https://arxiv.org/abs/2609.16231) | B / 60 |
| 233 | [Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail](https://arxiv.org/abs/2609.39086) | B / 60 |
| 234 | [Revealing Adversarial Smart Contracts through Semantic Interpretation and Uncertainty Estimation](https://arxiv.org/abs/2509.18934) | C / 59 |
| 236 | [Multi-Agent Collaborative Fuzzing with Continuous Reflection for Smart Contracts Vulnerability Detection](https://arxiv.org/abs/2511.12164) | C / 59 |
| 237 | [GAPS: Targeted Execution of Android Apps via Static Path Reconstruction](https://arxiv.org/abs/2511.23213) | C / 59 |
| 239 | [PatchIsland: Orchestration of LLM Agents for Continuous Vulnerability Repair](https://arxiv.org/abs/2601.17471) | C / 59 |
| 243 | [SCPatcher: Automated Smart Contract Code Repair via Retrieval-Augmented Generation and Knowledge Graph](https://arxiv.org/abs/2604.00687) | C / 59 |
| 255 | [RECEIPT: Deterministic, Reward-Hacking-Resistant Verification for White-Box Agentic XSS Discovery](https://arxiv.org/abs/2607.18575) | C / 59 |
| 258 | [KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference](https://arxiv.org/abs/2608.26699) | C / 59 |
| 260 | [LLMSec-AV: A Vulnerability Taxonomy and LLM-Driven Software Weakness Discovery Framework for Autonomous Vehicles](https://arxiv.org/abs/2609.09386) | C / 59 |
| 261 | [BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure](https://arxiv.org/abs/2609.11028) | C / 59 |
| 263 | [CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection](https://arxiv.org/abs/2609.18862) | C / 59 |
| 265 | [Cheap to Hypothesize, Costly to Verify: The Defense Surface of Agentic Vulnerability Discovery](https://arxiv.org/abs/2609.35909) | C / 59 |
| 267 | [Aletheia: Permission-Minimality Testing for Coding-Agent Rules](https://arxiv.org/abs/2609.39678) | C / 59 |
| 275 | [Revisiting Third-Party Library Detection: A Ground Truth Dataset and Its Implications Across Security Tasks](https://arxiv.org/abs/2509.04091) | C / 58 |
| 276 | [Detection of security smells in IaC scripts through semantics-aware code and language processing](https://arxiv.org/abs/2509.18790) | C / 58 |
| 279 | [Towards Classifying Benign And Malicious Packages Using Machine Learning](https://arxiv.org/abs/2511.15033) | C / 58 |
| 280 | [CoTDeceptor:Adversarial Code Obfuscation Against CoT-Enhanced LLM Code Agents](https://arxiv.org/abs/2512.21250) | C / 58 |
| 286 | [LiquiLM: Bridging the Semantic Gap in Liquidity Flaw Audit via DCN and LLMs](https://arxiv.org/abs/2604.03860) | C / 58 |
| 287 | [Guiding Symbolic Execution with Static Analysis and LLMs for Vulnerability Discovery](https://arxiv.org/abs/2604.06506) | C / 58 |
| 291 | [Bastet: A Fine-Grained Expert-Labeled Dataset for DeFi Smart Contract Vulnerability Detection](https://arxiv.org/abs/2606.03387) | C / 58 |
| 295 | [Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing](https://arxiv.org/abs/2607.21983) | C / 58 |
| 299 | [Generics-Aware Fuzz Target Generation for Rust Libraries via Structured API Analysis](https://arxiv.org/abs/2608.08637) | C / 58 |
| 300 | [LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles](https://arxiv.org/abs/2608.13450) | C / 58 |
| 302 | [Hieronym: Leveraging Hierarchical Multi-Source Information for Function Renaming in Stripped Binary](https://arxiv.org/abs/2609.12457) | C / 58 |
| 305 | [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](https://arxiv.org/abs/2610.29869) | C / 58 |
| 310 | [TraceLLM: Security Diagnosis Through Traces and Smart Contracts in Ethereum](https://arxiv.org/abs/2509.03037) | C / 57 |
| 313 | [AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software](https://arxiv.org/abs/2512.18567) | C / 57 |
| 315 | [Reentrancy Detection in the Age of LLMs](https://arxiv.org/abs/2603.26497) | C / 57 |
| 317 | [Reachability Across the NL/PL Boundary: A Taxonomy-Driven Dataflow Model for LLM-Integrated Applications](https://arxiv.org/abs/2603.28345) | C / 57 |
| 318 | [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494) | C / 57 |
| 328 | [VulDec: Vulnerability Detection in Binaries via Neural Decompilation](https://arxiv.org/abs/2610.33716) | C / 57 |
| 333 | [Esim: EVM Bytecode Similarity Detection Based on Stable-Semantic Graph](https://arxiv.org/abs/2511.12971) | C / 56 |
| 335 | [BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks](https://arxiv.org/abs/2512.09385) | C / 56 |
| 336 | [Taint-Based Code Slicing for LLMs-based Malicious NPM Package Detection](https://arxiv.org/abs/2512.12313) | C / 56 |
| 341 | [Who Said CVE? How Vulnerability Identifiers Are Mentioned by Humans, Bots, and Agents in Pull Requests](https://arxiv.org/abs/2601.19636) | C / 56 |
| 342 | [Re-Evaluating EVMBench: Are AI Agents Ready for Smart Contract Security?](https://arxiv.org/abs/2603.10795) | C / 56 |
| 345 | [Tailored Prompts, Targeted Protection: Vulnerability-Specific LLM Analysis for Smart Contracts](https://arxiv.org/abs/2605.03697) | C / 56 |
| 346 | [KVerus: Scalable and Resilient Formal Verification Proof Generation for Rust Code](https://arxiv.org/abs/2605.03822) | C / 56 |
| 347 | [VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers](https://arxiv.org/abs/2605.21392) | C / 56 |
| 349 | [On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus](https://arxiv.org/abs/2606.07363) | C / 56 |
| 351 | [Open-Source Intelligence for Code Provenance and the Security Patterns that Separate Human and Large-Language-Model Implementations of Common Programming Tasks](https://arxiv.org/abs/2607.12524) | C / 56 |
| 353 | [DeFiScreener: Efficient DeFi Attack Pre-screening in Smart Contracts via Historical Case Matching](https://arxiv.org/abs/2607.22184) | C / 56 |
| 357 | [Moirae: A Multimodal Agent Collaborative Framework for Dynamic Android Malware Detection](https://arxiv.org/abs/2608.27994) | C / 56 |
| 365 | [Evaluating Large Language Models in detecting Secrets in Android Apps](https://arxiv.org/abs/2510.18601) | C / 55 |
| 366 | [ConneX: Automatically Resolving Transaction Opacity of Cross-Chain Bridges for Security Analysis](https://arxiv.org/abs/2511.01393) | C / 55 |
| 367 | [PoCo: Agentic Proof-of-Concept Exploit Generation for Smart Contracts](https://arxiv.org/abs/2511.02780) | C / 55 |
| 370 | [HarnessAgent: Scaling Automatic Fuzzing Harness Construction with Tool-Augmented LLM Pipelines](https://arxiv.org/abs/2512.03420) | C / 55 |
| 372 | [SSR: Safeguarding Staking Rewards by Defining and Detecting Logical Defects in DeFi Staking](https://arxiv.org/abs/2601.05827) | C / 55 |
| 373 | [Okara: Detection and Attribution of TLS Man-in-the-Middle Vulnerabilities in Android Apps with Foundation Models](https://arxiv.org/abs/2601.22770) | C / 55 |
| 376 | [NeuroSCA: Neuro-Symbolic Constraint Abstraction for Smart Contract Hybrid Fuzzing](https://arxiv.org/abs/2603.01272) | C / 55 |
| 380 | [Aray: Deterministic-First Synthesis of Benign Artifacts for YARA Validation](https://arxiv.org/abs/2608.19387) | C / 55 |
| 383 | [ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers](https://arxiv.org/abs/2609.19722) | C / 55 |
| 384 | [HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning](https://arxiv.org/abs/2609.26352) | C / 55 |
| 388 | [The Innocent Courier: Covert Exfiltration Through Legitimate LLM Web Fetching](https://arxiv.org/abs/2610.01768) | C / 55 |
| 393 | [TaintSentinel: Path-Level Randomness Vulnerability Detection for Ethereum Smart Contracts](https://arxiv.org/abs/2510.18192) | C / 54 |
| 394 | [One Signature, Multiple Payments: Demystifying and Detecting Signature Replay Vulnerabilities in Smart Contracts](https://arxiv.org/abs/2511.09134) | C / 54 |
| 402 | [Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform](https://arxiv.org/abs/2606.26590) | C / 54 |
| 405 | [SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills](https://arxiv.org/abs/2608.08468) | C / 54 |
| 407 | [Why Is SHAP Not a Reliable Standalone Explanation Framework for Malware Detection?](https://arxiv.org/abs/2609.04626) | C / 54 |
| 409 | [ORCAGen: Orchestrating Context-Aware Malware Deception with RAG-Guided Generative AI](https://arxiv.org/abs/2610.12415) | C / 54 |
| 415 | [Cross-Domain Evaluation of Transformer-Based Vulnerability Detection on Open & Industry Data](https://arxiv.org/abs/2509.09313) | C / 53 |
| 416 | [Towards Secure and Explainable Smart Contract Generation with Security-Aware Group Relative Policy Optimization](https://arxiv.org/abs/2509.09942) | C / 53 |
| 421 | [HYDRA: A Hybrid Heuristic-Guided Deep Representation Architecture for Predicting Latent Zero-Day Vulnerabilities in Patched Functions](https://arxiv.org/abs/2511.06220) | C / 53 |
| 423 | [Agentic AI for Autonomous Defense in Software Supply Chain Security: Beyond Provenance to Vulnerability Mitigation](https://arxiv.org/abs/2512.23480) | C / 53 |
| 426 | [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/abs/2601.10338) | C / 53 |
| 433 | [Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning](https://arxiv.org/abs/2604.20179) | C / 53 |
| 434 | [GoAT-X: A Graph of Auditing Thoughts for Securing Token Transactions in Cross-Chain Contracts](https://arxiv.org/abs/2604.24341) | C / 53 |
| 436 | [MARD: A Multi-Agent Framework for Robust Android Malware Detection](https://arxiv.org/abs/2604.25264) | C / 53 |
| 437 | [Identifying and Characterizing Semantic Clones of Solidity Functions](https://arxiv.org/abs/2604.26526) | C / 53 |
| 443 | [Evaluating LLMs for Obfuscation Detection and Classification in Android Apps](https://arxiv.org/abs/2606.14233) | C / 53 |
| 444 | [PYPILINE: Malicious PyPI Package Detection via Suspicious API Knowledge and Agent Workflow](https://arxiv.org/abs/2606.19063) | C / 53 |
| 448 | [Natural Code Transformation Confuses Agents in Vulnerability Analysis](https://arxiv.org/abs/2610.14350) | C / 53 |
| 454 | [CodeCureAgent: Automatic Classification and Repair of Static Analysis Warnings](https://arxiv.org/abs/2509.11787) | C / 52 |
| 460 | [SPECA: Specification-to-Checklist Agentic Auditing for Multi-Implementation Systems -- A Case Study on Ethereum Clients](https://arxiv.org/abs/2602.07513) | C / 52 |
| 461 | [ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents](https://arxiv.org/abs/2603.12614) | C / 52 |
| 466 | [EntailLLM: Verifying LLM-Generated Vulnerability Discovery Paths with Domain Knowledge via Logic Programming](https://arxiv.org/abs/2608.01763) | C / 52 |
| 469 | [Trajectory-Level Security Debt in LLM Coding Agents](https://arxiv.org/abs/2609.35199) | C / 52 |
| 473 | [Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories](https://arxiv.org/abs/2510.26103) | C / 51 |
| 480 | [Feedback-Driven Execution for LLM-Based Binary Analysis](https://arxiv.org/abs/2604.15136) | C / 51 |
| 483 | [REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange](https://arxiv.org/abs/2606.05493) | C / 51 |
| 485 | [Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities](https://arxiv.org/abs/2606.26933) | C / 51 |
| 487 | [Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape](https://arxiv.org/abs/2609.20614) | C / 51 |
| 488 | [When Label Noise Meets Class Imbalance: A Robust Framework for Android Malware Family Classification](https://arxiv.org/abs/2609.22835) | C / 51 |
| 489 | [API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary](https://arxiv.org/abs/2609.33371) | C / 51 |
| 506 | [FirmCure:Towards Autonomous and Adaptive Rehosting of Linux-Based Firmware](https://arxiv.org/abs/2606.24549) | C / 50 |
| 518 | [Favia: Forensic Agent for Vulnerability-fix Identification and Analysis](https://arxiv.org/abs/2602.12500) | C / 49 |
| 524 | [AttackPathGNN: Cross-function vulnerability detection in smart contracts using state interference graphs and conjunction pooling](https://arxiv.org/abs/2606.05986) | C / 49 |
| 532 | [PromptGuard: An Orchestrated Prompting Framework for Principled Synthetic Text Generation for Vulnerable Populations using LLMs with Enhanced Safety, Fairness, and Controllability](https://arxiv.org/abs/2509.08910) | C / 48 |
| 539 | [Following Dragons: Code Review-Guided Fuzzing](https://arxiv.org/abs/2602.10487) | C / 48 |
| 543 | [AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs](https://arxiv.org/abs/2607.01640) | C / 48 |
| 545 | [Malformer: A Multi-Modal Malware Detector Using Transformers](https://arxiv.org/abs/2608.19052) | C / 48 |
| 551 | [Federated Learning for Malware Image Classification under Data Heterogeneity](https://arxiv.org/abs/2610.25264) | C / 48 |
| 554 | [From Obfuscated to Obvious: A Comprehensive JavaScript Deobfuscation Tool for Security Analysis](https://arxiv.org/abs/2512.14070) | C / 47 |
| 555 | [Multi-Agent Taint Specification Extraction for Vulnerability Detection](https://arxiv.org/abs/2601.10865) | C / 47 |
| 558 | [Evaluating LLMs for Real-World Web Vulnerability Detection](https://arxiv.org/abs/2606.21397) | C / 47 |
| 566 | [MalCVE: Malware Detection and CVE Association Using Large Language Models](https://arxiv.org/abs/2510.15567) | C / 46 |
| 567 | [Domain-constrained Synthesis of Inconsistent Key Aspects in Textual Vulnerability Descriptions](https://arxiv.org/abs/2511.16123) | C / 46 |
| 568 | [Examining the Effectiveness of Transformer-Based Smart Contract Vulnerability Scan](https://arxiv.org/abs/2601.07334) | C / 46 |
| 571 | [TUANDROMD-X: Advanced Entropy and Visual Analytics Dataset for Enhanced Malware Detection and Classification](https://arxiv.org/abs/2605.06718) | C / 46 |
| 572 | [Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge](https://arxiv.org/abs/2607.10221) | C / 46 |
| 573 | [Chiral Analysis of Smart Contracts: Detecting Vulnerabilities from Relational Inconsistencies Across Business Paths](https://arxiv.org/abs/2607.17987) | C / 46 |
| 574 | [MalFlows: Context-aware Fusion of Heterogeneous Flow Semantics for Android Malware Detection](https://arxiv.org/abs/2508.03588) | C / 45 |
| 576 | [RustAssure: Differential Symbolic Testing for LLM-Transpiled C-to-Rust Code](https://arxiv.org/abs/2510.07604) | C / 45 |
| 577 | [Detecting Vulnerabilities from Issue Reports for Internet-of-Things](https://arxiv.org/abs/2511.01941) | C / 45 |
| 578 | [USCSA: Evolution-Aware Security Analysis for Proxy-Based Upgradeable Smart Contracts](https://arxiv.org/abs/2512.08372) | C / 45 |
| 585 | [Name2Pkg: Lightweight One-Class Android Malware Screening via Name-Package Correspondence Modeling](https://arxiv.org/abs/2609.24389) | C / 45 |
| 587 | [FalseCrashReducer: Mitigating False Positive Crashes in OSS-Fuzz-Gen Using Agentic AI](https://arxiv.org/abs/2510.02185) | D / 44 |
| 590 | [An LLM-based Quantitative Framework for Evaluating High-Stealthy Backdoor Risks in OSS Supply Chains](https://arxiv.org/abs/2511.13341) | D / 44 |
| 591 | [WildCode Revisited: A Comprehensive Empirical Study on the Security of LLM-Generated Code](https://arxiv.org/abs/2512.04259) | D / 44 |
| 603 | [Web3 x AI Agents: Landscape, Integrations, and Foundational Challenges](https://arxiv.org/abs/2508.02773) | D / 43 |
| 613 | [A Comparison of Malware Image Transformations Using Grad-CAM and Hybrid Learning Models](https://arxiv.org/abs/2608.12077) | D / 43 |
| 622 | [LCC-LLM: Leveraging Code-Centric Large Language Models for Malware Attribution](https://arxiv.org/abs/2605.05807) | D / 42 |
| 623 | [Repository-Level Solidity Code Generation with Large Language Models: From Prompting to Fine-Tuning](https://arxiv.org/abs/2606.19988) | D / 42 |
| 624 | [Understanding the (In)Security of Vibe-Coded Applications](https://arxiv.org/abs/2606.23130) | D / 42 |
| 634 | [Investigating Metamorphic Fuzz Oracle Enhancement via Large Language Models](https://arxiv.org/abs/2606.14164) | D / 41 |
| 635 | [CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs](https://arxiv.org/abs/2606.29124) | D / 41 |
| 640 | [LLM-Powered Silent Bug Fuzzing in Deep Learning Libraries via Versatile and Controlled Bug Transfer](https://arxiv.org/abs/2602.23065) | D / 40 |
| 641 | [From Preventive to Reactive: How AI Coding Assistants Transform Developers' Security Awareness](https://arxiv.org/abs/2605.23130) | D / 40 |
| 646 | [Vibe Coding in Practice: Motivations, Challenges, and a Future Outlook -- a Grey Literature Review](https://arxiv.org/abs/2510.00328) | D / 39 |
| 650 | [LLM-Based Static Verification of Code Against Natural-Language Requirements: An Industrial Experience Report](https://arxiv.org/abs/2605.17926) | D / 39 |
| 668 | [What You Code Is What We Prove: Translating BLE App Logic into Formal Models with LLMs for Vulnerability Detection](https://arxiv.org/abs/2509.09291) | D / 35 |
| 669 | [An Empirical Study on Remote Code Execution in Machine Learning Model Hosting Ecosystems](https://arxiv.org/abs/2601.14163) | D / 35 |
| 675 | [Investigating Security Implications of Automatically Generated Code on the Software Supply Chain](https://arxiv.org/abs/2509.20277) | D / 30 |

#### synthetic / self-built (140 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 14 | [The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark](https://arxiv.org/abs/2608.11469) | B / 73 |
| 20 | [ARQ: Agentic CodeQL Query Refinement for C/C++ Vulnerability Detection](https://arxiv.org/abs/2608.20637) | B / 72 |
| 23 | [AVIATOR: Towards AI-Agentic Vulnerability Injection Workflow for High-Fidelity, Large-Scale Code Security Dataset](https://arxiv.org/abs/2508.20866) | B / 71 |
| 35 | [Agent Audit: A Security AnalS System for LLM Agent Applications](https://arxiv.org/abs/2603.22853) | B / 70 |
| 37 | [HarnessSecurity-Bench: Do Security Mechanisms Really Protect Coding Agent Harnesses?](https://arxiv.org/abs/2610.07639) | B / 70 |
| 42 | [Automated Vulnerability Detection in Source Code Using Deep Representation Learning](https://arxiv.org/abs/2602.23121) | B / 69 |
| 46 | [PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance](https://arxiv.org/abs/2608.17220) | B / 69 |
| 66 | [VulnScout-C: A Lightweight Transformer for C Code Vulnerability Detection](https://arxiv.org/abs/2603.28309) | B / 67 |
| 69 | [CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training](https://arxiv.org/abs/2608.06471) | B / 67 |
| 77 | [Constitutional Spec-Driven Development: Enforcing Security by Construction in AI-Assisted Code Generation](https://arxiv.org/abs/2602.02584) | B / 66 |
| 85 | [Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software](https://arxiv.org/abs/2606.20502) | B / 66 |
| 86 | [Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection](https://arxiv.org/abs/2606.30587) | B / 66 |
| 87 | [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](https://arxiv.org/abs/2607.04729) | B / 66 |
| 91 | [GraftyVul: Synthesising Insecure Programs Through Real-World Vulnerability Grafting](https://arxiv.org/abs/2608.27928) | B / 66 |
| 99 | [Taught by the Flawed: How Dataset Insecurity Breeds Vulnerable AI Code](https://arxiv.org/abs/2511.09879) | B / 65 |
| 100 | [Multi-LLM Energy Reasoning for Binary-Free Zero-Day IoT Detection](https://arxiv.org/abs/2512.19945) | B / 65 |
| 101 | [Beyond Single Bugs: Benchmarking Large Language Models for Multi-Vulnerability Detection](https://arxiv.org/abs/2512.22306) | B / 65 |
| 107 | [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](https://arxiv.org/abs/2607.25225) | B / 65 |
| 118 | [SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-aware Fine-tuning](https://arxiv.org/abs/2510.26457) | B / 64 |
| 131 | [SecProbe: Adaptive Evaluation of Coding Agents on Cybersecurity Vulnerabilities](https://arxiv.org/abs/2609.33763) | B / 64 |
| 137 | [SLEAN: Simple Lightweight Ensemble Analysis Network for Multi-Provider LLM Coordination: Design, Implementation, and Vibe Coding Bug Investigation Case Study](https://arxiv.org/abs/2510.10010) | B / 63 |
| 145 | [Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection](https://arxiv.org/abs/2604.21282) | B / 63 |
| 149 | [Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks](https://arxiv.org/abs/2605.23243) | B / 63 |
| 152 | [Unsaid, Unsafe? Implicit Security Obligations in LLM-Based RTL Code Generation](https://arxiv.org/abs/2608.26588) | B / 63 |
| 172 | [Detecting Data Poisoning in Code Generation LLMs via Black-Box, Vulnerability-Oriented Scanning](https://arxiv.org/abs/2603.17174) | B / 62 |
| 174 | [How Code Representation Shapes False-Positive Dynamics in Cross-Language LLM Vulnerability Detection](https://arxiv.org/abs/2604.27714) | B / 62 |
| 175 | [SmartEval: A Benchmark for Evaluating LLM-Generated Smart Contracts from Natural Language Specifications](https://arxiv.org/abs/2605.09610) | B / 62 |
| 177 | [SCARA: A Semantics-Constrained Autonomous Remediation Agent for Opaque Industrial Software Vulnerabilities](https://arxiv.org/abs/2605.19668) | B / 62 |
| 189 | [SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair](https://arxiv.org/abs/2509.16275) | B / 61 |
| 192 | [Exposing Hidden Interfaces: LLM-Guided Type Inference for Reverse Engineering macOS Private Frameworks](https://arxiv.org/abs/2601.01673) | B / 61 |
| 195 | [SAFuzz: Semantic-Guided Adaptive Fuzzing for LLM-Generated Code](https://arxiv.org/abs/2602.11209) | B / 61 |
| 196 | [Toward Scalable Automated Repository-Level Datasets for Software Vulnerability Detection](https://arxiv.org/abs/2603.17974) | B / 61 |
| 198 | [Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/abs/2604.05292) | B / 61 |
| 200 | [Secret Stealing Attacks on Local LLM Fine-Tuning through Supply-Chain Model Code Backdoors](https://arxiv.org/abs/2604.27426) | B / 61 |
| 201 | [SecureForge: Finding and Preventing Vulnerabilities in LLM-Generated Code via Prompt Optimization](https://arxiv.org/abs/2605.08382) | B / 61 |
| 218 | [VULPO: Context-Aware Vulnerability Detection via On-Policy LLM Optimization](https://arxiv.org/abs/2511.11896) | B / 60 |
| 238 | [CFCEval: Evaluating Security Aspects in Code Generated by Large Language Models](https://arxiv.org/abs/2512.06248) | C / 59 |
| 250 | [Context-Based Adversarial Attacks on AI Code Generators: Vulnerability Analysis and Implications](https://arxiv.org/abs/2606.10945) | C / 59 |
| 251 | [MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation](https://arxiv.org/abs/2606.11416) | C / 59 |
| 257 | [MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing](https://arxiv.org/abs/2608.14216) | C / 59 |
| 269 | [Trojan Horse: Automated Repository Poisoning against Coding Agents](https://arxiv.org/abs/2610.23109) | C / 59 |
| 271 | [Kerkoporta: Injecting Structured-Output Backdoors in Reasoning Coding Agents](https://arxiv.org/abs/2611.00138) | C / 59 |
| 272 | [Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains](https://arxiv.org/abs/2611.06585) | C / 59 |
| 277 | [Library Hallucinations in LLM-Generated Code: A Risk Analysis Grounded in Developer Queries](https://arxiv.org/abs/2509.22202) | C / 58 |
| 297 | [EduPluginBench: Executable Assurance for AI-Generated Educational Plugins](https://arxiv.org/abs/2608.00739) | C / 58 |
| 301 | [AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs](https://arxiv.org/abs/2609.01023) | C / 58 |
| 303 | [AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination](https://arxiv.org/abs/2609.19140) | C / 58 |
| 307 | [The Long Con on the Web: Earn-then-Exploit Fraud Attacks against Coding Agents](https://arxiv.org/abs/2611.00725) | C / 58 |
| 308 | [CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion](https://arxiv.org/abs/2611.04356) | C / 58 |
| 309 | [A.S.E: A Repository-Level Benchmark for Evaluating Security in AI-Generated Code](https://arxiv.org/abs/2508.18106) | C / 57 |
| 319 | [Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code](https://arxiv.org/abs/2607.21641) | C / 57 |
| 321 | [CWEEP: A Lexical Static Analysis Framework for CWE Early Prevention](https://arxiv.org/abs/2607.29604) | C / 57 |
| 324 | [Can escalation channels redirect reward hacking toward defect disclosure?](https://arxiv.org/abs/2608.29460) | C / 57 |
| 326 | [Understanding and Mitigating Cross-Session Attacks via Persistent Artifacts in Agent Skill Composition](https://arxiv.org/abs/2610.13227) | C / 57 |
| 332 | [Securing LLM-Generated Embedded Firmware through AI Agent-Driven Validation and Patching](https://arxiv.org/abs/2509.09970) | C / 56 |
| 338 | [Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming](https://arxiv.org/abs/2601.02060) | C / 56 |
| 339 | [STELP: Secure Transpilation and Execution of LLM-Generated Programs](https://arxiv.org/abs/2601.05467) | C / 56 |
| 354 | [Security Tests as Executable Specifications for LLM Code Generation: Benefits, Trade-offs, and Coverage Limits](https://arxiv.org/abs/2608.09740) | C / 56 |
| 359 | [When Talk Isn't Code: Comparing LLM Agents That Simulate and Develop Software](https://arxiv.org/abs/2610.04639) | C / 56 |
| 360 | [CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat](https://arxiv.org/abs/2610.19005) | C / 56 |
| 362 | [SPLASH: Contrastive Audit Pressure for Detecting and Localizing Security Hallucinations in Generated Code](https://arxiv.org/abs/2610.26001) | C / 56 |
| 369 | [RampoNN: A Reachability-Guided System Falsification for Efficient Cyber-Kinetic Vulnerability Detection](https://arxiv.org/abs/2511.16765) | C / 55 |
| 374 | [Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation](https://arxiv.org/abs/2602.04195) | C / 55 |
| 385 | [LLM Agents Can Easily Tamper With Their Own Traces](https://arxiv.org/abs/2609.30266) | C / 55 |
| 387 | [SINGED: Correct Outputs Do Not Certify Safe Execution in LLM Agents](https://arxiv.org/abs/2609.35889) | C / 55 |
| 396 | [From Theory to Practice: Code Generation Using LLMs for CAPEC and CWE Frameworks](https://arxiv.org/abs/2604.02548) | C / 54 |
| 405 | [SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills](https://arxiv.org/abs/2608.08468) | C / 54 |
| 406 | [Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning](https://arxiv.org/abs/2608.30686) | C / 54 |
| 408 | [Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities](https://arxiv.org/abs/2609.15963) | C / 54 |
| 410 | [ProtoArena: Can AI Agents Discover and Exploit Real-World Cross-Component Protocol Vulnerabilities?](https://arxiv.org/abs/2610.17837) | C / 54 |
| 412 | [Making Small Code LLMs More Efficient for Secure Code Review with Neuro-Symbolic Fine-Tuning](https://arxiv.org/abs/2610.35477) | C / 54 |
| 420 | [ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contract Vulnerability Detection](https://arxiv.org/abs/2510.17919) | C / 53 |
| 425 | [Lightweight Yet Secure: Secure Scripting Language Generation via Lightweight LLMs](https://arxiv.org/abs/2601.06419) | C / 53 |
| 438 | [MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents](https://arxiv.org/abs/2605.03952) | C / 53 |
| 441 | [R+R: Reassessing Java Security API Misuse in Current LLMs: A Replication on JCA and JSSE APIs with External Security Knowledge](https://arxiv.org/abs/2605.31135) | C / 53 |
| 446 | [MAGS: Multi-agent Auto-formalization Guarantees Safety for Agentic Outputs](https://arxiv.org/abs/2609.19391) | C / 53 |
| 450 | [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253) | C / 53 |
| 451 | [Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis](https://arxiv.org/abs/2508.14727) | C / 52 |
| 453 | [Guided Reasoning in LLM-Driven Penetration Testing Using Structured Attack Trees](https://arxiv.org/abs/2509.07939) | C / 52 |
| 457 | [Towards Compositional Generalization in LLMs for Smart Contract Security: A Case Study on Reentrancy Vulnerabilities](https://arxiv.org/abs/2601.06914) | C / 52 |
| 468 | [Beyond Static Guarantees: Measuring the Static-Pass Dynamic-Fail Gap in Security-Sensitive and LLM-Generated Python Code](https://arxiv.org/abs/2609.10762) | C / 52 |
| 478 | [CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering](https://arxiv.org/abs/2604.03750) | C / 51 |
| 481 | [An Empirical Security Evaluation of LLM-Generated Cryptographic Rust Code](https://arxiv.org/abs/2604.27001) | C / 51 |
| 482 | [An Empirical Evaluation of LLM-Generated Code Security Across Prompting Methods](https://arxiv.org/abs/2605.24298) | C / 51 |
| 486 | [Prompt Structure Redistributes, Not Reduces: An Empirical Analysis of Security-Weaknesses in LLM-Generated Python Code](https://arxiv.org/abs/2608.24857) | C / 51 |
| 490 | [CodeMimicry: Exploiting Safety Generalization Lag in Large Language Models via Structured Code Completion](https://arxiv.org/abs/2609.39902) | C / 51 |
| 492 | [VerilogLAVD: LLM-Aided Rule Generation for Vulnerability Detection in Verilog](https://arxiv.org/abs/2508.13092) | C / 50 |
| 497 | [Can LLMs Recover Program Semantics? A Systematic Evaluation with Symbolic Execution](https://arxiv.org/abs/2511.19130) | C / 50 |
| 501 | [Can Adversarial Code Comments Fool AI Security Reviewers -- Large-Scale Empirical Study of Comment-Based Attacks and Defenses Against LLM Code Analysis](https://arxiv.org/abs/2602.16741) | C / 50 |
| 510 | [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](https://arxiv.org/abs/2609.02774) | C / 50 |
| 512 | [Backdooring Sparse Autoencoders](https://arxiv.org/abs/2610.06049) | C / 50 |
| 513 | [InterType: Breaking the Single-Function Barrier in Neural Binary Type Inference](https://arxiv.org/abs/2610.26906) | C / 50 |
| 516 | [Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback](https://arxiv.org/abs/2601.00509) | C / 49 |
| 517 | [Cracking IoT Security: Can LLMs Outsmart Static Analysis Tools?](https://arxiv.org/abs/2601.00559) | C / 49 |
| 520 | [VibeGuard: A Security Gate Framework for AI-Generated Code](https://arxiv.org/abs/2604.01052) | C / 49 |
| 521 | [Towards Personalizing Secure Programming Education with LLM-Injected Vulnerabilities](https://arxiv.org/abs/2604.13955) | C / 49 |
| 529 | [From Requirements to Attack Trees: Grounded LLM Agents for Design-Time Security Review](https://arxiv.org/abs/2610.03820) | C / 49 |
| 535 | [Supporting Students in Navigating LLM-Generated Insecure Code](https://arxiv.org/abs/2511.20878) | C / 48 |
| 538 | [SecCodePRM: A Process Reward Model for Code Security](https://arxiv.org/abs/2602.10418) | C / 48 |
| 544 | [Understanding the Impact of AI Code Assistants on Security API Usage: An Empirical Study](https://arxiv.org/abs/2607.11348) | C / 48 |
| 547 | [Authority Is Not a String: A Capability-Scoped Harness for Prompt-Injection-Resistant Coding Agents](https://arxiv.org/abs/2609.08371) | C / 48 |
| 548 | [Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks](https://arxiv.org/abs/2609.17817) | C / 48 |
| 552 | [When Code Crosses Borders: A Security-Centric Study of LLM-based Code Translation](https://arxiv.org/abs/2509.06504) | C / 47 |
| 560 | [CITADEL: CWE-Guided Insertion of Hardware Trojans via Analysis of DFG-Enabled LLMs](https://arxiv.org/abs/2610.02544) | C / 47 |
| 561 | [Beware EviLLM: Enabling Vulnerability Injection via Large Language Models](https://arxiv.org/abs/2610.03857) | C / 47 |
| 580 | [Persistent Human Feedback, LLMs, and Static Analyzers for Secure Code Generation and Vulnerability Detection](https://arxiv.org/abs/2602.05868) | C / 45 |
| 584 | [Automated Vulnerability Injection in Smart Contracts Using Large Language Models](https://arxiv.org/abs/2609.02624) | C / 45 |
| 586 | [Can We Trust the AI Pair Programmer? Copilot for API Misuse Detection and Correction](https://arxiv.org/abs/2509.16795) | D / 44 |
| 594 | [Detect--Repair--Verify for LLM-Generated Code: A Multi-Language, Multi-Granularity Empirical Study](https://arxiv.org/abs/2603.23633) | D / 44 |
| 597 | [Vulnerable Code Search: Transferable Attack for Code Language Models](https://arxiv.org/abs/2608.26031) | D / 44 |
| 601 | [Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents](https://arxiv.org/abs/2609.39607) | D / 44 |
| 602 | [Thinking in Graphs: Neo4j-Backed Exploit-Chain Reasoning for LLM Penetration-Testing Agents](https://arxiv.org/abs/2610.20902) | D / 44 |
| 604 | [Detecting Stealthy Data Poisoning Attacks in AI Code Generators](https://arxiv.org/abs/2508.21636) | D / 43 |
| 608 | [SecureCodeRL: Security-Aware Reinforcement Learning for Code Generation with Partial-Credit Rewards](https://arxiv.org/abs/2601.01184) | D / 43 |
| 611 | [Minimal Prompt Perturbations Lead to Code Vulnerabilities: Prompt Fragility and Hidden-State Signals in Coding LLMs](https://arxiv.org/abs/2605.29737) | D / 43 |
| 612 | [Acoda: Adversarial Code Obfuscation for Defending against LLM-based Analysis](https://arxiv.org/abs/2606.11755) | D / 43 |
| 614 | [RTLGuard: A Lightweight Teacher-Student Defense for Poisoned RTL Code Generation Models](https://arxiv.org/abs/2608.26049) | D / 43 |
| 615 | [A Study of the Reliability of Agentic AI-Generated Programs](https://arxiv.org/abs/2609.18298) | D / 43 |
| 618 | [GPTrace: Effective Crash Deduplication Using LLM Embeddings](https://arxiv.org/abs/2512.01609) | D / 42 |
| 625 | [Security Vulnerability Patterns in AI-Generated Code: A Cross-Model Comparative Study](https://arxiv.org/abs/2607.20713) | D / 42 |
| 628 | [OPBackdoor: Opportunistic Backdoors via Alibi-Aligned Reasoning](https://arxiv.org/abs/2609.24826) | D / 42 |
| 629 | [Learning from Failures: A Failure-Driven Prompt Refinement for LLM-Based Vulnerability Analysis](https://arxiv.org/abs/2610.08405) | D / 42 |
| 632 | [LLM-CSEC: Empirical Evaluation of Security in C/C++ Code Generated by Large Language Models](https://arxiv.org/abs/2511.18966) | D / 41 |
| 636 | [Comprendia: AI-Augmented Code Comprehension](https://arxiv.org/abs/2608.10290) | D / 41 |
| 637 | [SEMA-GUARD: Semantic and Graph-Based Vulnerability Detection in Assembly Code](https://arxiv.org/abs/2609.17254) | D / 41 |
| 638 | [RiskyPy: Toward Model-Calibrated Prompt Generation for Joint Security and Functionality Evaluation of LLM-Generated Code](https://arxiv.org/abs/2610.40735) | D / 41 |
| 639 | [AutoBaxBuilder: Bootstrapping Code Security Benchmarking](https://arxiv.org/abs/2512.21132) | D / 40 |
| 643 | [VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents](https://arxiv.org/abs/2607.09653) | D / 40 |
| 644 | [Cross-Cutting Security Analysis of LLM-Generated Code via Metamorphic Testing and Association Rule Mining](https://arxiv.org/abs/2607.12089) | D / 40 |
| 647 | [Death by a Thousand Prompts: Open Model Vulnerability Analysis](https://arxiv.org/abs/2511.03247) | D / 39 |
| 648 | [Prompt Engineering vs. Fine-Tuning for LLM-Based Vulnerability Detection in Solana and Algorand Smart Contracts](https://arxiv.org/abs/2511.11250) | D / 39 |
| 649 | [Evaluating the Vulnerability Landscape of LLM-Generated Smart Contracts](https://arxiv.org/abs/2602.04039) | D / 39 |
| 651 | [LLM-Assisted Detection and Repair of Hardware Security Vulnerabilities in Verilog Designs](https://arxiv.org/abs/2608.04907) | D / 39 |
| 652 | [C-ing Clearly: Enhanced Binary Code Explanations using C code](https://arxiv.org/abs/2512.14500) | D / 38 |
| 656 | [Poster: Rethinking Security in LLM Code Generation through Real-World Risk Scenarios](https://arxiv.org/abs/2607.23088) | D / 38 |
| 657 | [Cross-modal Retrieval Models for Stripped Binary Analysis](https://arxiv.org/abs/2512.10393) | D / 37 |
| 658 | [A Prompt-Based Framework for Loop Vulnerability Detection Using Local LLMs](https://arxiv.org/abs/2601.15352) | D / 37 |
| 665 | [RAVEN: Retrieval-Augmented Vulnerability Exploration Network for Memory Corruption Analysis in User Code and Binary Programs](https://arxiv.org/abs/2604.17948) | D / 36 |
| 672 | [Agentic Interpretation: Lattice-Structured Evidence for LLM-Based Program Analysis](https://arxiv.org/abs/2605.12694) | D / 31 |
| 676 | [Automatically Attacking Software Reverse Engineering AI Agents](https://arxiv.org/abs/2605.30667) | D / 29 |

#### open artifacts (80 papers)

| Overall Rank | Paper | Tier |
|---:|---|---|
| 5 | [LLMVul: A Vulnerability-Labeled Dataset of LLM-Generated C/C++ Functions from Real Production Repositories](https://arxiv.org/abs/2609.10945) | A / 76 |
| 6 | [OpenAnt: LLM-Powered Vulnerability Discovery Through Code Decomposition, Adversarial Verification, and Dynamic Testing](https://arxiv.org/abs/2606.19149) | A / 75 |
| 8 | [SecureCode: A Production-Grade Multi-Turn Dataset for Training Security-Aware Code Generation Models](https://arxiv.org/abs/2512.18542) | B / 74 |
| 12 | [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](https://arxiv.org/abs/2611.03555) | B / 74 |
| 13 | [VCAO: Verifier-Centered Agentic Orchestration for Strategic OS Vulnerability Discovery](https://arxiv.org/abs/2604.08291) | B / 73 |
| 15 | [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](https://arxiv.org/abs/2608.26882) | B / 73 |
| 17 | [CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices](https://arxiv.org/abs/2609.21344) | B / 73 |
| 18 | [Secure Code Generation via Online Reinforcement Learning with Vulnerability Reward Model](https://arxiv.org/abs/2602.07422) | B / 72 |
| 19 | [Towards a Risk Assessment of Malicious Skill Files in Coding Agents](https://arxiv.org/abs/2608.05223) | B / 72 |
| 21 | [VEX-Bench: Benchmarking LLM Agents for Assessing Exploitability of Software Supply Chain Vulnerabilities](https://arxiv.org/abs/2609.08040) | B / 72 |
| 22 | [Autonomous OSS Threat Detection via Taxonomy-Aligned LLMs](https://arxiv.org/abs/2610.01263) | B / 72 |
| 28 | [AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration](https://arxiv.org/abs/2607.12058) | B / 71 |
| 34 | [VulnAgent-R2: Evidence-Calibrated Multi-Agent Auditing for Repository-Level Vulnerability Detection](https://arxiv.org/abs/2603.13384) | B / 70 |
| 35 | [Agent Audit: A Security AnalS System for LLM Agent Applications](https://arxiv.org/abs/2603.22853) | B / 70 |
| 47 | [CS-Guard: Benchmarking LLM Guardrails for Code Generation Security](https://arxiv.org/abs/2609.09798) | B / 69 |
| 48 | [What is the Difference Between Me and You? Benchmarking the Quality Gap Between Human-Written and AI-Generated Code](https://arxiv.org/abs/2609.12708) | B / 69 |
| 53 | [Quality-Assured Fuzz Harness Generation via the Four Principles Framework](https://arxiv.org/abs/2605.21824) | B / 68 |
| 54 | [The Illusion of Safety: Multi-Tier Verification of AI vs. Human C++ Code](https://arxiv.org/abs/2607.00107) | B / 68 |
| 59 | [SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios](https://arxiv.org/abs/2509.22097) | B / 67 |
| 61 | [FLAMES: Fine-tuning LLMs to Synthesize Invariants for Smart Contract Security](https://arxiv.org/abs/2510.21401) | B / 67 |
| 63 | [VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection](https://arxiv.org/abs/2512.07533) | B / 67 |
| 92 | [Reveree: Diagnosing LLM Reverse-Engineering Agents](https://arxiv.org/abs/2609.01185) | B / 66 |
| 93 | [ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure?](https://arxiv.org/abs/2609.30325) | B / 66 |
| 95 | [INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems](https://arxiv.org/abs/2610.20776) | B / 66 |
| 97 | [Rethinking Neural Decompilation: Candidate Selection as the Hidden Bottleneck](https://arxiv.org/abs/2611.02788) | B / 66 |
| 107 | [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](https://arxiv.org/abs/2607.25225) | B / 65 |
| 120 | [VulInstruct: Teaching LLMs Root-Cause Reasoning for Vulnerability Detection via Security Specifications](https://arxiv.org/abs/2511.04014) | B / 64 |
| 122 | [From Coverage to Causes: Data-Centric Fuzzing for JavaScript Engines](https://arxiv.org/abs/2512.18102) | B / 64 |
| 141 | [Attention Distance: A Novel Metric for Directed Fuzzing with Large Language Models](https://arxiv.org/abs/2512.19758) | B / 63 |
| 146 | [VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.09461) | B / 63 |
| 170 | [HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation](https://arxiv.org/abs/2601.13864) | B / 62 |
| 171 | [Formal Analysis and Supply Chain Security for Agentic AI Skills](https://arxiv.org/abs/2603.00195) | B / 62 |
| 175 | [SmartEval: A Benchmark for Evaluating LLM-Generated Smart Contracts from Natural Language Specifications](https://arxiv.org/abs/2605.09610) | B / 62 |
| 176 | [From Controlled to the Wild: Evaluation of Pentesting Agents for the Real-World](https://arxiv.org/abs/2605.10834) | B / 62 |
| 187 | [Simple Features Beat Most AI Control Monitors](https://arxiv.org/abs/2610.41713) | B / 62 |
| 193 | [SolAgent: A Specialized Multi-Agent Framework for Solidity Code Generation](https://arxiv.org/abs/2601.23009) | B / 61 |
| 229 | [JavaVulBench: A Java Vulnerability Benchmark with Realistic Splits, a Unified Multi-Backend Harness, and a Leakage-Aware Evaluation Mode](https://arxiv.org/abs/2607.02825) | B / 60 |
| 244 | [AgentSZZ: Teaching the LLM Agent to Play Detective with Bug-Inducing Commits](https://arxiv.org/abs/2604.02665) | C / 59 |
| 274 | [Large Language Models Versus Static Code Analysis Tools: A Systematic Benchmark for Vulnerability Detection](https://arxiv.org/abs/2508.04448) | C / 58 |
| 282 | [SecCodeBench-V2 Technical Report](https://arxiv.org/abs/2602.15485) | C / 58 |
| 283 | [SecureRAG-RTL: A Retrieval-Augmented, Multi-Agent, Zero-Shot LLM-Driven Framework for Hardware Vulnerability Detection](https://arxiv.org/abs/2603.05689) | C / 58 |
| 293 | [Routing Ceilings Are Domain-Independent: Structural Prior Injection in Code Security Vulnerability Detection](https://arxiv.org/abs/2607.14628) | C / 58 |
| 296 | [HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models](https://arxiv.org/abs/2607.27030) | C / 58 |
| 297 | [EduPluginBench: Executable Assurance for AI-Generated Educational Plugins](https://arxiv.org/abs/2608.00739) | C / 58 |
| 303 | [AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination](https://arxiv.org/abs/2609.19140) | C / 58 |
| 313 | [AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software](https://arxiv.org/abs/2512.18567) | C / 57 |
| 318 | [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494) | C / 57 |
| 325 | [A Queryable Graph-Based Security Analysis Framework for O-RAN](https://arxiv.org/abs/2609.06855) | C / 57 |
| 331 | [All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching](https://arxiv.org/abs/2509.07225) | C / 56 |
| 332 | [Securing LLM-Generated Embedded Firmware through AI Agent-Driven Validation and Patching](https://arxiv.org/abs/2509.09970) | C / 56 |
| 337 | [Diverse LLMs vs. Vulnerabilities: Who Detects and Fixes Them Better?](https://arxiv.org/abs/2512.12536) | C / 56 |
| 342 | [Re-Evaluating EVMBench: Are AI Agents Ready for Smart Contract Security?](https://arxiv.org/abs/2603.10795) | C / 56 |
| 344 | [Symbolic Execution Meets Multi-LLM Orchestration: Detecting Memory Vulnerabilities in Incomplete Rust CVE Snippets](https://arxiv.org/abs/2605.00034) | C / 56 |
| 345 | [Tailored Prompts, Targeted Protection: Vulnerability-Specific LLM Analysis for Smart Contracts](https://arxiv.org/abs/2605.03697) | C / 56 |
| 355 | [Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems](https://arxiv.org/abs/2608.21095) | C / 56 |
| 368 | [Secure Code Generation at Scale with Reflexion](https://arxiv.org/abs/2511.03898) | C / 55 |
| 377 | [EVMbench: Evaluating AI Agents on Smart Contract Security](https://arxiv.org/abs/2603.04915) | C / 55 |
| 391 | [VISION: Robust and Interpretable Code Vulnerability Detection Leveraging Counterfactual Augmentation](https://arxiv.org/abs/2508.18933) | C / 54 |
| 402 | [Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform](https://arxiv.org/abs/2606.26590) | C / 54 |
| 418 | [Hound: Relation-First Knowledge Graphs for Complex-System Reasoning in Security Audits](https://arxiv.org/abs/2510.09633) | C / 53 |
| 422 | [Llama-based source code vulnerability detection: Prompt engineering vs Fine tuning](https://arxiv.org/abs/2512.09006) | C / 53 |
| 426 | [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/abs/2601.10338) | C / 53 |
| 428 | [Code Fingerprints: Disentangled Attribution of LLM-Generated Code](https://arxiv.org/abs/2603.04212) | C / 53 |
| 431 | [SynthFix: Adaptive Neuro-Symbolic Code Vulnerability Repair](https://arxiv.org/abs/2604.17184) | C / 53 |
| 478 | [CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering](https://arxiv.org/abs/2604.03750) | C / 51 |
| 483 | [REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange](https://arxiv.org/abs/2606.05493) | C / 51 |
| 496 | [QLCoder: A Query Synthesizer For Static Analysis of Security Vulnerabilities](https://arxiv.org/abs/2511.08462) | C / 50 |
| 498 | [Sift or Get Off the PoC: Applying Information Retrieval to Vulnerability Research with SiftRank](https://arxiv.org/abs/2512.06155) | C / 50 |
| 514 | [Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation](https://arxiv.org/abs/2509.19533) | C / 49 |
| 519 | [Quantum-Safe Code Auditing: LLM-Assisted Static Analysis and Quantum-Aware Risk Scoring for Post-Quantum Cryptography Migration](https://arxiv.org/abs/2604.00560) | C / 49 |
| 523 | [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](https://arxiv.org/abs/2606.04739) | C / 49 |
| 534 | [Distilling Lightweight Language Models for C/C++ Vulnerabilities](https://arxiv.org/abs/2510.06645) | C / 48 |
| 536 | [UncertaintyZoo: A Unified Toolkit for Quantifying Predictive Uncertainty in Deep Learning Systems](https://arxiv.org/abs/2512.06406) | C / 48 |
| 553 | [Automated Vulnerability Validation and Verification: A Large Language Model Approach](https://arxiv.org/abs/2509.24037) | C / 47 |
| 554 | [From Obfuscated to Obvious: A Comprehensive JavaScript Deobfuscation Tool for Security Analysis](https://arxiv.org/abs/2512.14070) | C / 47 |
| 588 | [Evaluating Line-level Localization Ability of Learning-based Code Vulnerability Detection Models](https://arxiv.org/abs/2510.11202) | D / 44 |
| 595 | [Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions](https://arxiv.org/abs/2605.06279) | D / 44 |
| 598 | [Evaluating Context Segmentation in Locally Deployable SLMs for Cybersecurity CTF Tasks](https://arxiv.org/abs/2609.12839) | D / 44 |
| 621 | [AdverMCTS: Combating Pseudo-Correctness in Code Generation via Adversarial Monte Carlo Tree Search](https://arxiv.org/abs/2604.10449) | D / 42 |
| 639 | [AutoBaxBuilder: Bootstrapping Code Security Benchmarking](https://arxiv.org/abs/2512.21132) | D / 40 |

