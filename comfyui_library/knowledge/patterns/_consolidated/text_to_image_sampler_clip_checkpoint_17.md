---
name: text_to_image_sampler_clip_checkpoint_17
type: Text To Image
frequency: 4
level: weak
coverage: 0.975
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/API - SD3.5文生图_2091140151840952322.json, 图片生成/文生图/ComfyUI基础文生图工作流_2083027862839447554.json, 图片生成/文生图/ComfyUI基础文生图工作流_2087084704964112385.json, 图片生成/文生图/Kinghere_Z-image卓越美学文生图_1999757899914244098.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/API - SD3.5文生图_2091140151840952322.json、图片生成/文生图/ComfyUI基础文生图工作流_2083027862839447554.json、图片生成/文生图/ComfyUI基础文生图工作流_2087084704964112385.json、图片生成/文生图/Kinghere_Z-image卓越美学文生图_1999757899914244098.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 16 - 1080 | 4 | 29% |
| 高度 | 512 | 512 - 1920 | 4 | 29% |
| 采样步数 | 20 | 10 - 20 | 4 | 75% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 4 | 52% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 16 - 1080，4 个样本，取值分散，一致性仅 29%
- 高度 中位数 512，观测区间 512 - 1920，4 个样本，取值分散，一致性仅 29%
- 采样步数 中位数 20，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
