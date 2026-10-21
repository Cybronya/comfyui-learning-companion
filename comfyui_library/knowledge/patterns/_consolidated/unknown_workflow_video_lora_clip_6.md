---
name: unknown_workflow_video_lora_clip_6
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.8726
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/03-01-01-WAN2.1-文生视频-原生_1989233803006709761.json, 视频生成/文生视频/04-01-01-WAN2.2-文生视频-原生_1990967339145437186.json, 视频生成/文生视频/1972827331947614209.json, 视频生成/文生视频/1923566284871823361.json, 视频生成/文生视频/1923578202491711490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/03-01-01-WAN2.1-文生视频-原生_1989233803006709761.json、视频生成/文生视频/04-01-01-WAN2.2-文生视频-原生_1990967339145437186.json、视频生成/文生视频/1972827331947614209.json、视频生成/文生视频/1923566284871823361.json、视频生成/文生视频/1923578202491711490.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 4/5 个有
- `KSampler` —— 3/5 个有
- `KSamplerAdvanced` —— 2/5 个有
- `SaveWEBM` —— 2/5 个有
- `TorchCompileModel` —— 2/5 个有
- `CFGZeroStar` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `SaveAnimatedWEBP` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 30 | 3 | 32% |
| Prompt 约束强度(CFG) | 4 | 1 - 6 | 5 | 39% |
| 采样算法 | uni_pc | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 30，3 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 6，5 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 uni_pc，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
