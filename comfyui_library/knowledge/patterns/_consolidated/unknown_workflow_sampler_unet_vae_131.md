---
name: unknown_workflow_sampler_unet_vae_131
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.958667
common_nodes: [BasicScheduler, CLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, SamplerCustom, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Boogu Image 0.1 Single-Image Edit_2072998833342423040.json, 图片生成/文生图/Boogu-Image 0.1 单图编辑_2067856537388933122.json, 图片生成/文生图/Boogu_Base_edit_图像编辑工作流_2069278108913594370.json, 图片生成/文生图/boogu_edit_example_2068254277000327170.json, 图片生成/文生图/boogu编辑图片_2067805061354446849.json, 图片生成/文生图/image_boogu_edit图片编辑工作流_2088517071389941762.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_131

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Boogu Image 0.1 Single-Image Edit_2072998833342423040.json、图片生成/文生图/Boogu-Image 0.1 单图编辑_2067856537388933122.json、图片生成/文生图/Boogu_Base_edit_图像编辑工作流_2069278108913594370.json、图片生成/文生图/boogu_edit_example_2068254277000327170.json、图片生成/文生图/boogu编辑图片_2067805061354446849.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
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
- `PreviewImage` —— 3/6 个有
- `ConstrainImage|pysssss` —— 1/6 个有
- `FluxKontextImageScale` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `GetImageSize+` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1536 | 6 | 78% |
| 高度 | 1024 | 1024 - 2048 | 6 | 66% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1536，6 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，6 个样本
