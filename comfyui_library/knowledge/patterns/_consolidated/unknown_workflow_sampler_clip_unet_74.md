---
name: unknown_workflow_sampler_clip_unet_74
type: Unknown Workflow
frequency: 4
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CreateVideo, DualCLIPLoader, KSampler, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1993298338619604994.json, 视频生成/图生视频/1993306482808733698.json, 视频生成/图生视频/1997647681071853569.json, 视频生成/文生视频/Hunyuan 1.5 480P 文生视频加速版_1993293448365146113.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1993298338619604994.json、视频生成/图生视频/1993306482808733698.json、视频生成/图生视频/1997647681071853569.json、视频生成/文生视频/Hunyuan 1.5 480P 文生视频加速版_1993293448365146113.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `KSampler`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `HunyuanVideo15ImageToVideo` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `EmptyHunyuanVideo15Latent` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 12 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 12，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
