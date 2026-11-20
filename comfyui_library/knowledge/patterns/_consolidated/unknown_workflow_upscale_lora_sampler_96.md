---
name: unknown_workflow_upscale_lora_sampler_96
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.939
common_nodes: [BasicGuider, CLIPLoader, DF_Text_Box, Fast Groups Bypasser (rgthree), GH_CropRestore, GH_MaskCropV2, Get Image Size, GulfSeaImageMergeMask, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ColorImage, LoadImage, LoraLoaderModelOnly, ManualSigmas, QwenImage21SageAttentionT8, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, WujiCleaner, WujiUpscaler2, 图像缩放V2_孤海, 图像缩放范围孤海]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114593938492448769.json, 图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114615796927393794.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_96

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114593938492448769.json、图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114615796927393794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `DF_Text_Box`
- `Fast Groups Bypasser (rgthree)`
- `GH_CropRestore`
- `GH_MaskCropV2`
- `Get Image Size`
- `GulfSeaImageMergeMask`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ColorImage`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `QwenImage21SageAttentionT8`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiCleaner`
- `WujiUpscaler2`
- `图像缩放V2_孤海`
- `图像缩放范围孤海`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
