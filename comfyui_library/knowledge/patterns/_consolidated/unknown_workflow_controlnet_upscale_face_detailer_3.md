---
name: unknown_workflow_controlnet_upscale_face_detailer_3
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.84275
common_nodes: [AIO_Preprocessor, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DetailDaemonSamplerNode, FaceDetailer, Image Comparer (rgthree), ImageLoader, ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, JWStringConcat, KSampler, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, MultiplePathsInput, PreviewImage, Qwen3_VQA, QwenImageDiffsynthControlnet, RandomNoise, SamplerCustomAdvanced, SamplerEulerAncestral, SaveImage, Seed (rgthree), ShowText|pysssss, SplitSigmas, String Literal, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image + Sigma Split 双阶段渲染_1997541959206125569.json, 图片生成/文生图/Z-Image×ControlNet 2.1二阶Refiner增强技巧 LoRA人物替换_2002219399727726593.json, 图片生成/文生图/造相ControlNet2.0高低噪渲染+SeedVR2亿级像素_2000807895858020353.json, 图片生成/文生图/造相ControlNet2.1高低噪渲染+SeedVR2亿级像素_2001611142990577666.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_face_detailer_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image + Sigma Split 双阶段渲染_1997541959206125569.json、图片生成/文生图/Z-Image×ControlNet 2.1二阶Refiner增强技巧 LoRA人物替换_2002219399727726593.json、图片生成/文生图/造相ControlNet2.0高低噪渲染+SeedVR2亿级像素_2000807895858020353.json、图片生成/文生图/造相ControlNet2.1高低噪渲染+SeedVR2亿级像素_2001611142990577666.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `FaceDetailer`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `JWStringConcat`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `MultiplePathsInput`
- `PreviewImage`
- `Qwen3_VQA`
- `QwenImageDiffsynthControlnet`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `SplitSigmas`
- `String Literal`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `Florence2ModelLoader` —— 3/4 个有
- `Florence2Run` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `GetImageSize+` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `ImageScaleToMaxDimension` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `Latent Switch (JPS)` —— 2/4 个有
- `Model Switch (JPS)` —— 2/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Miaoshouai_Tagger` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
