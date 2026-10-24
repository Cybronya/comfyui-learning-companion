---
name: unknown_workflow_sampler_unet_vae_143
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.758857
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), KSampler, LoadImage, PreviewImage, ResolutionSelector, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 产品溶图（自适应透视校正）_2109548528275120129.json, 图片生成/图生图/Qwen Image 2.1 人物换姿势（服装模特姿势复刻）_2106943198722613250.json, 图片生成/图生图/Qwen image 2.1 图像高清修复+4K高清放大_2109465429235290113.json, 图片生成/图生图/Qwen image 2.1 高清修复 4K_2109886590741995522.json, 图片生成/图生图/Qwen image2.1洗图工作流_2102617237571067905.json, 图片生成/图生图/Qwen-Image-2.1 任意风格转写实_2110205939604344834.json, 图片生成/图生图/Qwen-Image-2.1 写实照片转动漫_2112103901817298946.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_143

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 产品溶图（自适应透视校正）_2109548528275120129.json、图片生成/图生图/Qwen Image 2.1 人物换姿势（服装模特姿势复刻）_2106943198722613250.json、图片生成/图生图/Qwen image 2.1 图像高清修复+4K高清放大_2109465429235290113.json、图片生成/图生图/Qwen image 2.1 高清修复 4K_2109886590741995522.json、图片生成/图生图/Qwen image2.1洗图工作流_2102617237571067905.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 6/7 个有
- `ImageScaleBy` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `QwenImage21Cache` —— 6/7 个有
- `SeedVR2LoadDiTModel` —— 6/7 个有
- `SeedVR2LoadVAEModel` —— 6/7 个有
- `SeedVR2VideoUpscaler` —— 6/7 个有
- `TTP_Image_Assy` —— 6/7 个有
- `TTP_Image_Tile_Batch` —— 6/7 个有
- `TTP_Tile_image_size` —— 6/7 个有
- `easy imageSize` —— 6/7 个有
- `LayerUtility: PurgeVRAM` —— 5/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `LayerUtility: ImageReel` —— 3/7 个有
- `LayerUtility: ImageReelComposit` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `BatchImagesNode` —— 2/7 个有
- `CR Prompt Text` —— 2/7 个有
- `CR Text` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `Latent Switch (JPS)` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `TextGenerateLTX2Prompt` —— 2/7 个有
- `DWPreprocessor` —— 1/7 个有
- `DepthAnythingV2Preprocessor` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LineArtPreprocessor` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy setNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 10 | 7 - 36 | 7 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 7 - 36，7 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
