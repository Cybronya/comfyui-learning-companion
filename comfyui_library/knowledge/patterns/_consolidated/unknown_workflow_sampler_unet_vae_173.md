---
name: unknown_workflow_sampler_unet_vae_173
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.911667
common_nodes: [BasicScheduler, CLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, SamplerCustom, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Boogu-Image 图片编辑_2068185847907835905.json, 图片生成/图生图/Boogu_Edit工作流_2067413961858965505.json, 图片生成/图生图/Boogu_Image_edit 单图编辑_2067731696430178305.json, 图片生成/图生图/boogu_edit_图像编辑-图生图_2069074867202383874.json, 图片生成/图生图/boogu_edit_图像编辑_2069391664145321986.json, 图片生成/文生图/boogu编辑图片_2067805061354446849.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_173

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Boogu-Image 图片编辑_2068185847907835905.json、图片生成/图生图/Boogu_Edit工作流_2067413961858965505.json、图片生成/图生图/Boogu_Image_edit 单图编辑_2067731696430178305.json、图片生成/图生图/boogu_edit_图像编辑-图生图_2069074867202383874.json、图片生成/图生图/boogu_edit_图像编辑_2069391664145321986.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

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
- `PreviewImage` —— 4/6 个有
- `FluxKontextImageScale` —— 2/6 个有
- `GetImageSize+` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `Text` —— 2/6 个有
- `ImageConcanate` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `JWStringConcat` —— 1/6 个有
- `PDRatioSelector` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `图像缩放V2_孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1024 - 1536 | 6 | 84% |
| 高度 | 1024 | 1024 - 1280 | 6 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 1024 - 1536，6 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 1024 - 1280，6 个样本，取值集中（一致性 89%）
