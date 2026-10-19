---
name: unknown_workflow_video_lora_clip_11
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.787667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/03-01-01-WAN2.1-文生视频-原生_1989233803006709761.json, 视频生成/文生视频/04-01-01-WAN2.2-文生视频-原生_1990967339145437186.json, 视频生成/文生视频/1972827331947614209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/03-01-01-WAN2.1-文生视频-原生_1989233803006709761.json、视频生成/文生视频/04-01-01-WAN2.2-文生视频-原生_1990967339145437186.json、视频生成/文生视频/1972827331947614209.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
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
- `KSamplerAdvanced` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `SaveWEBM` —— 2/3 个有
- `CFGZeroStar` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `SaveAnimatedWEBP` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 1 - 6 | 3 | 44% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | simple | - | 3 | 33% |
| 重绘幅度 | 1 | - | 3 | 33% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 6，3 个样本，取值分散，一致性仅 44%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 simple，3 个样本，一致性 33%
- 重绘幅度 最常用 1，3 个样本，一致性 33%
