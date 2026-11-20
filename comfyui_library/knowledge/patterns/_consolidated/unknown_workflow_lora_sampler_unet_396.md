---
name: unknown_workflow_lora_sampler_unet_396
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6945
common_nodes: [CLIPLoader, GH_CropRestore, GH_MaskCropV2, GetImageSize, GulfSeaImageMergeMask, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ColorImage, LoadImageGoohai, LoraLoaderModelOnly, ManualSigmas, PreviewImage, SaveImage, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, 图像缩放V2_孤海, 孤海注释]
problems: []
missing: []
members: [平台全量/万物迁移 qwen_image_2.1_turbo_1922162142739382273.json, 平台全量/局部重绘_1866795567509651458.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_396

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/万物迁移 qwen_image_2.1_turbo_1922162142739382273.json、平台全量/局部重绘_1866795567509651458.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `GH_CropRestore`
- `GH_MaskCropV2`
- `GetImageSize`
- `GulfSeaImageMergeMask`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ColorImage`
- `LoadImageGoohai`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `图像缩放V2_孤海`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `Int` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `QwenImage21Cache` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustom` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text Concatenate (JPS)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
