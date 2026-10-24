---
name: text_to_image_sampler_clip_checkpoint_22
type: Text To Image
frequency: 3
level: moderate
coverage: 0.759667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, Image Comparer (rgthree), KSampler, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/【AI小王子】21.实时图像裁剪_2046850831487602690.json, 图片生成/文生图/【AI小王子】23.文生图面部修复_2046873587751067650.json, 图片生成/文生图/高清修复+手脸修复工作流V1.1_2028341868513206273.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【AI小王子】21.实时图像裁剪_2046850831487602690.json、图片生成/文生图/【AI小王子】23.文生图面部修复_2046873587751067650.json、图片生成/文生图/高清修复+手脸修复工作流V1.1_2028341868513206273.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `FaceDetailer` —— 2/3 个有
- `UltralyticsDetectorProvider` —— 2/3 个有
- `GridLoras` —— 1/3 个有
- `ImageCrop` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `SAMLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 8 | 7 - 8 | 3 | 94% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 960 | 3 | 68% |
| 高度 | 512 | 512 - 1280 | 3 | 53% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 7 - 8，3 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 960，3 个样本
- 高度 中位数 512，观测区间 512 - 1280，3 个样本
