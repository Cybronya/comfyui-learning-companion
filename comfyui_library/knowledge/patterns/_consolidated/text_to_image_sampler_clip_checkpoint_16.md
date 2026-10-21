---
name: text_to_image_sampler_clip_checkpoint_16
type: Text To Image
frequency: 4
level: moderate
coverage: 0.7705
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: [CR Upscale Image]
members: [图片生成/文生图/1971514623306448898.json, 图片生成/文生图/1979464950139752450.json, 图片生成/文生图/ComfyUI system workflow_2072886879170686978.json, 图片生成/文生图/controlnet文生图SD_2106555235891245058.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1971514623306448898.json、图片生成/文生图/1979464950139752450.json、图片生成/文生图/ComfyUI system workflow_2072886879170686978.json、图片生成/文生图/controlnet文生图SD_2106555235891245058.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `LoadImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `CR Upscale Image` —— 1/4 个有
- `EmptyImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 884 | 512 - 1536 | 4 | 60% |
| 高度 | 900 | 512 - 1536 | 4 | 61% |
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 6.265 | 2.8 - 8 | 4 | 64% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | karras | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 884，观测区间 512 - 1536，4 个样本
- 高度 中位数 900，观测区间 512 - 1536，4 个样本
- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 6.265，观测区间 2.8 - 8，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 karras，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Upscale Image
