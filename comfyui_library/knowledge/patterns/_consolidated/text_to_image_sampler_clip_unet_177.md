---
name: text_to_image_sampler_clip_unet_177
type: Text To Image
frequency: 4
level: moderate
coverage: 0.97725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/🦖可正可邪-Z-IMAGE_1993956349084188673.json, 平台全量/Anima-2.9B-preview-v1 文生图_2094062510424018946.json, 平台全量/ComfyUI模特生成工作流_电商模特_模特自由_AI模特生成器_2022529060114534402.json, 平台全量/api-z-image-qufuxiaozi_1995333151222378498.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_177

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/🦖可正可邪-Z-IMAGE_1993956349084188673.json、平台全量/Anima-2.9B-preview-v1 文生图_2094062510424018946.json、平台全量/ComfyUI模特生成工作流_电商模特_模特自由_AI模特生成器_2022529060114534402.json、平台全量/api-z-image-qufuxiaozi_1995333151222378498.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `Int` —— 2/4 个有
- `AnyAspectRatio` —— 1/4 个有
- `CompressImages` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `Text _O` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 10 - 30 | 4 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 4 | 26% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1116 | 696 - 2416 | 4 | 52% |
| 高度 | 1488 | 1080 - 1920 | 4 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 10 - 30，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，4 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1116，观测区间 696 - 2416，4 个样本
- 高度 中位数 1488，观测区间 1080 - 1920，4 个样本
