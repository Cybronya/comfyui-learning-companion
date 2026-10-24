---
name: text_to_image_upscale_lora_sampler_46
type: Text To Image
frequency: 5
level: strong
coverage: 0.7112
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), Images to RGB, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, PreviewImage, QwenImage21Cache, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1图片编辑文生图图生图处理工具_2102536916045484034.json, 图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2103891330228379650.json, 图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2106077135336198145.json, 图片生成/图生图/QwenImage2.1图片编辑｜角色四视图生成 角色一致性图生图利器_2104022222749913090.json, 图片生成/图生图/角色四视图一键生成 QwenImage2.1超高一致性图生图_2104301701854486529.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图片编辑文生图图生图处理工具_2102536916045484034.json、图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2103891330228379650.json、图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2106077135336198145.json、图片生成/图生图/QwenImage2.1图片编辑｜角色四视图生成 角色一致性图生图利器_2104022222749913090.json、图片生成/图生图/角色四视图一键生成 QwenImage2.1超高一致性图生图_2104301701854486529.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `Images to RGB`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PreviewImage`
- `QwenImage21Cache`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `FaceAnalysisModels` —— 4/5 个有
- `FaceEmbedDistance` —— 4/5 个有
- `GetImageSizeAndCount` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `ImageStitch` —— 4/5 个有
- `ComfyMathExpression` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `ImageScaleToMaxDimension` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `AILab_ImageCrop` —— 2/5 个有
- `AutoCropFaces` —— 2/5 个有
- `Bounded Image Crop with Mask` —— 2/5 个有
- `CheckpointLoaderSimple` —— 2/5 个有
- `ImageBatchMulti` —— 2/5 个有
- `ImageBlend` —— 2/5 个有
- `ImagePadForOutpaint` —— 2/5 个有
- `ImageToMask` —— 2/5 个有
- `MaskToImage` —— 2/5 个有
- `SAM3_VideoTrack` —— 2/5 个有
- `SCAIL2ColoredMask` —— 2/5 个有
- `easy float` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `ComfyOrNode` —— 1/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `JsonExtractString` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有
- `TextGenerate` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
