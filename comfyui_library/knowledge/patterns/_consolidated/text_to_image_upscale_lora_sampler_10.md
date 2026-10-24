---
name: text_to_image_upscale_lora_sampler_10
type: Text To Image
frequency: 12
level: strong
coverage: 0.829333
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageResize+, ImageScaleBy, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy imageSize, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2107565485087870977.json, 图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2107938760527798274.json, 图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2108332170640187393.json, 图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json, 图片生成/图生图/Qwen Image 2.1洗图反推提示词，图生图图像分析与提示词提取工具_2103236925317537793.json, 图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110244395655188481.json, 图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110370717484273665.json, 图片生成/图生图/Qwen image 2.1高清修复流程，老图一键放大到4K_2110478470630436865.json, 图片生成/图生图/Qwen-Image-2.1 写实照片转动漫｜二次元风格化_2112483717431255042.json, 图片生成/文生图/Qwen Image 2.1文生图图生视频高清工作流合集处理工具_2102497280900296705.json, 图片生成/文生图/Qwen-Image-2.1 亚洲人像摄影胶片｜复古质感写真直出_2112382443893387265.json, 图片生成/文生图/Qwen2.1 亚洲摄影人像写真｜4K高清直出质感大片_2112369800302387201.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2107565485087870977.json、图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2107938760527798274.json、图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2108332170640187393.json、图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json、图片生成/图生图/Qwen Image 2.1洗图反推提示词，图生图图像分析与提示词提取工具_2103236925317537793.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 11/12 个有
- `QwenImage21Cache` —— 11/12 个有
- `LayerUtility: PurgeVRAM` —— 10/12 个有
- `LoadImage` —— 10/12 个有
- `CR Prompt Text` —— 6/12 个有
- `LayerUtility: ImageReel` —— 5/12 个有
- `LayerUtility: ImageReelComposit` —— 5/12 个有
- `Anything Everywhere3` —— 4/12 个有
- `BatchImagesNode` —— 4/12 个有
- `ImageResizeKJv2` —— 4/12 个有
- `PreviewAny` —— 4/12 个有
- `TextGenerateLTX2Prompt` —— 4/12 个有
- `CR Text` —— 3/12 个有
- `Latent Switch (JPS)` —— 3/12 个有
- `Color Grading JK` —— 2/12 个有
- `Any Switch (rgthree)` —— 1/12 个有
- `DWPreprocessor` —— 1/12 个有
- `DepthAnythingV2Preprocessor` —— 1/12 个有
- `GetImageSize` —— 1/12 个有
- `ImageConcanate` —— 1/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `LineArtPreprocessor` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（18/12 个样本）：Steps较低可能导致细节不足
