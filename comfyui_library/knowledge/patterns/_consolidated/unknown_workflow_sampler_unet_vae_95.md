---
name: unknown_workflow_sampler_unet_vae_95
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9593
common_nodes: [BasicScheduler, CLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, SamplerCustom, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/boogu_edit_图片编辑_2068898671525195778.json, 图片生成/图生图/boogu_edit图像编辑_2068963144776638466.json, 图片生成/图生图/boogu_image_edit 图生图_2074490249920729090.json, 图片生成/图生图/image_boogu_edit图片编辑工作流_2082720783633305601.json, 图片生成/图生图/【遇见AI】boogu image edit 基础工作流_2067908267849900034.json, 图片生成/图生图/布谷boogu_image图像编辑单图编辑_2074485181544751106.json, 图片生成/图生图/高清洗图（增强控制细节）_2099854123326857217.json, 图片生成/文生图/Boogu Image 0.1 Single-Image Edit_2072998833342423040.json, 图片生成/文生图/Boogu-Image 0.1 单图编辑_2067856537388933122.json, 图片生成/文生图/image_boogu_edit图片编辑工作流_2088517071389941762.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_95

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/boogu_edit_图片编辑_2068898671525195778.json、图片生成/图生图/boogu_edit图像编辑_2068963144776638466.json、图片生成/图生图/boogu_image_edit 图生图_2074490249920729090.json、图片生成/图生图/image_boogu_edit图片编辑工作流_2082720783633305601.json、图片生成/图生图/【遇见AI】boogu image edit 基础工作流_2067908267849900034.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/10 个有
- `GetImageSize` —— 4/10 个有
- `Text` —— 3/10 个有
- `ConstrainImage|pysssss` —— 2/10 个有
- `FluxKontextImageScale` —— 2/10 个有
- `GetImageSizeAndCount` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `RH_Translator` —— 1/10 个有
- `图像缩放V2_孤海` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 10 | 82% |
| 高度 | 1024 | 512 - 2048 | 10 | 61% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，10 个样本，取值集中（一致性 82%）
- 高度 中位数 1024，观测区间 512 - 2048，10 个样本
