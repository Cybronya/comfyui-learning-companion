---
name: unknown_workflow_video_lora_clip_11
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.851
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/03-01-01-WAN2.1-文生视频-原生_1989233803006709761.json, 视频生成/文生视频/04-01-01-WAN2.2-文生视频-原生_1990967339145437186.json, 视频生成/文生视频/MoviiGen1.1_文生视频_1923566284871823361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/03-01-01-WAN2.1-文生视频-原生_1989233803006709761.json、视频生成/文生视频/04-01-01-WAN2.2-文生视频-原生_1990967339145437186.json、视频生成/文生视频/MoviiGen1.1_文生视频_1923566284871823361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 2/3 个有
- `SaveWEBM` —— 2/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `SaveAnimatedWEBP` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `TorchCompileModel` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 18 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 5 | 1 - 6 | 3 | 46% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 18，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 6，3 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
