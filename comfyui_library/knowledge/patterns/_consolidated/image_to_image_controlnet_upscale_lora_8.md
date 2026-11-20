---
name: image_to_image_controlnet_upscale_lora_8
type: Image To Image
frequency: 3
level: strong
coverage: 0.629667
common_nodes: [Any Switch (rgthree), Blur, CLIPLoader, CLIPTextEncode, CannyEdgePreprocessor, ConditioningZeroOut, DF_Integer, DepthAnythingV2Preprocessor, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Float, GetImageSize, GetNode, HEDPreprocessor, ImageCASharpening+, ImageResize+, ImageScaleToMaxDimension, Int, KSampler, LayerUtility: BooleanOperatorV2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchLoader, ModelSamplingAuraFlow, OpenposePreprocessor, PreviewImage, PrimitiveInt, PrimitiveStringMultiline, QwenImageDiffsynthControlnet, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, SimpleMath+, StringFunction|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy boolean, easy cleanGpuUsed, easy ifElse, easy imageSizeByLongerSide, easy imageSizeBySide, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, 图像缩放V2_孤海, 数学运算_孤海]
problems: []
missing: []
members: [图片生成/图生图/z_image_turbo-姿态控制-人像lora随心写真_2061996345078145026.json, 图片生成/图生图/z_image_turbo-姿态控制-人像lora随心写真_2063531081051234305.json, 图片生成/文生图/z_image_turbo-姿态控制-人像lora随心写真_2064520176695078914.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/z_image_turbo-姿态控制-人像lora随心写真_2061996345078145026.json、图片生成/图生图/z_image_turbo-姿态控制-人像lora随心写真_2063531081051234305.json、图片生成/文生图/z_image_turbo-姿态控制-人像lora随心写真_2064520176695078914.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Blur`
- `CLIPLoader`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `ConditioningZeroOut`
- `DF_Integer`
- `DepthAnythingV2Preprocessor`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `GetImageSize`
- `GetNode`
- `HEDPreprocessor`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleToMaxDimension`
- `Int`
- `KSampler`
- `LayerUtility: BooleanOperatorV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `OpenposePreprocessor`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `StringFunction|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageSizeByLongerSide`
- `easy imageSizeBySide`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `图像缩放V2_孤海`
- `数学运算_孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 12 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 12，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
