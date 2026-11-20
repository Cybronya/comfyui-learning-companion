---
name: image_to_image_lora_sampler_unet_71
type: Image To Image
frequency: 8
level: strong
coverage: 0.86675
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/KERA-2-EDIT 单图编辑工作流_2080375312747155458.json, 图片生成/图生图/KERA-2-EDIT-ANY-IMAGE-1 单图编辑工作流_2077623406463381506.json, 图片生成/图生图/KREA-2 单图编辑_2083582526848847874.json, 图片生成/图生图/KREA-2-EDIT-One-image-V2 单图编辑工作流_2079953132267859969.json, 图片生成/图生图/Krea 2 Edit 图片编辑v1.2_ New Storyboard & Inpainting_2080138587139563521.json, 图片生成/图生图/Krea_2-Edit+V1.2-单图像编辑_2081573244439719937.json, 图片生成/图生图/全新虚拟试衣！Krea 2 Outfit Transfer 单图编辑工作流_2080180833553571842.json, 图片生成/文生图/单图遮罩编辑 (Krea 2 Identity Edit v1.2)_2079889918284877826.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_71

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/KERA-2-EDIT 单图编辑工作流_2080375312747155458.json、图片生成/图生图/KERA-2-EDIT-ANY-IMAGE-1 单图编辑工作流_2077623406463381506.json、图片生成/图生图/KREA-2 单图编辑_2083582526848847874.json、图片生成/图生图/KREA-2-EDIT-One-image-V2 单图编辑工作流_2079953132267859969.json、图片生成/图生图/Krea 2 Edit 图片编辑v1.2_ New Storyboard & Inpainting_2080138587139563521.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 7/8 个有
- `ResizeImageMaskNode` —— 6/8 个有
- `VAEDecode` —— 6/8 个有
- `GrowMask` —— 5/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `ImageBlur` —— 5/8 个有
- `ImageToMask` —— 5/8 个有
- `MaskPreview+` —— 5/8 个有
- `MaskToImage` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `ImageCompositeMasked` —— 4/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `ImageScaleBy` —— 3/8 个有
- `TextInput_` —— 2/8 个有
- `VAEUtils_VAEDecodeTiled` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LoadImageMask` —— 1/8 个有
- `image_scale_pixel_v2` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 8 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，8 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
