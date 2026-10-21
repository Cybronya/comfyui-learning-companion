---
name: unknown_workflow_sampler_clip_unet_90
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.974
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1909419548767100930.json, 图片生成/文生图/1909435534924460034.json, 图片生成/文生图/1917390442533687298.json, 图片生成/文生图/1920589333093617666.json, 图片生成/文生图/1921046708803796993.json, 图片生成/文生图/1954389130199351298.json, 图片生成/文生图/1985548530460860417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_90

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1909419548767100930.json、图片生成/文生图/1909435534924460034.json、图片生成/文生图/1917390442533687298.json、图片生成/文生图/1920589333093617666.json、图片生成/文生图/1921046708803796993.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `TTP_Image_Tile_Batch` —— 2/7 个有
- `CLIPAttentionMultiply` —— 1/7 个有
- `ModelSamplingFlux` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1920 | 7 | 70% |
| 高度 | 1024 | 1024 - 1536 | 7 | 84% |
| 采样步数 | 25 | 20 - 35 | 7 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 0.9 | - | 2 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1920，7 个样本
- 高度 中位数 1024，观测区间 1024 - 1536，7 个样本，取值集中（一致性 84%）
- 采样步数 中位数 25，观测区间 20 - 35，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
