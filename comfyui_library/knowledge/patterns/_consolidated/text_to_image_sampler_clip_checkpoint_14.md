---
name: text_to_image_sampler_clip_checkpoint_14
type: Text To Image
frequency: 3
level: moderate
coverage: 0.735667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: [CR Upscale Image]
members: [图片生成/文生图/1971514623306448898.json, 图片生成/文生图/1979464950139752450.json, 图片生成/文生图/controlnet文生图SD_2106555235891245058.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1971514623306448898.json、图片生成/文生图/1979464950139752450.json、图片生成/文生图/controlnet文生图SD_2106555235891245058.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CR Upscale Image` —— 1/3 个有
- `EmptyImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1000 | 768 - 1536 | 3 | 71% |
| 高度 | 1032 | 768 - 1536 | 3 | 71% |
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 5 | 2.8 - 7.53 | 3 | 62% |
| 采样算法 | dpmpp_sde | - | 3 | 33% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1000，观测区间 768 - 1536，3 个样本
- 高度 中位数 1032，观测区间 768 - 1536，3 个样本
- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 2.8 - 7.53，3 个样本
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 33%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Upscale Image
