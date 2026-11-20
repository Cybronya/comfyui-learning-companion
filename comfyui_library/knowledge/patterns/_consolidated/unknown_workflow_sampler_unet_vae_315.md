---
name: unknown_workflow_sampler_unet_vae_315
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.852
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ManualSigmas, SamplerCustom, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image2.1-图像编辑不移位一致性lora_2116693668991164417.json, 图片生成/图生图/Qwen-image2.1-图像编辑不移位（一致性lora）_2116431964881375233.json, 图片生成/图生图/Qwen-image2.1-终极局部重绘（完美解决接缝色差）_2104548066190774274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_315

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1-图像编辑不移位一致性lora_2116693668991164417.json、图片生成/图生图/Qwen-image2.1-图像编辑不移位（一致性lora）_2116431964881375233.json、图片生成/图生图/Qwen-image2.1-终极局部重绘（完美解决接缝色差）_2104548066190774274.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ManualSigmas`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `ColorMatchV2` —— 1/3 个有
- `InpaintCropImproved` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `InpaintStitchImproved` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
