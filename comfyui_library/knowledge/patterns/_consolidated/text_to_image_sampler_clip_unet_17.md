---
name: text_to_image_sampler_clip_unet_17
type: Text To Image
frequency: 4
level: strong
coverage: 0.9335
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1959919853350105089.json, 图片生成/文生图/1969671833953988610.json, 图片生成/文生图/1970727639172476929.json, 图片生成/文生图/boogu_image_base 文生图_1900216622093840386.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1959919853350105089.json、图片生成/文生图/1969671833953988610.json、图片生成/文生图/1970727639172476929.json、图片生成/文生图/boogu_image_base 文生图_1900216622093840386.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

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
- `FluxResolutionNode` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 768 - 1024 | 4 | 86% |
| 高度 | 1376 | 768 - 1536 | 4 | 77% |
| 采样步数 | 32.5 | 30 - 35 | 4 | 92% |
| Prompt 约束强度(CFG) | 3.25 | 3 - 4 | 4 | 88% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 768 - 1024，4 个样本，取值集中（一致性 86%）
- 高度 中位数 1376，观测区间 768 - 1536，4 个样本
- 采样步数 中位数 32.5，观测区间 30 - 35，4 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 3.25，观测区间 3 - 4，4 个样本，取值集中（一致性 88%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
