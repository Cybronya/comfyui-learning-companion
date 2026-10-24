---
name: unknown_workflow_sampler_unet_vae_40
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.862467
common_nodes: [BatchImagesNode, CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json, 图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json, 图片生成/图生图/Face Swap  Qwen-Image-2.1模特换头+换脸_2102208882394357762.json, 图片生成/图生图/Face+Swap换脸+Qwen-Image-2.1模特换头+换脸_2110526511987122178.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2101985763167653889.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102008336353939458.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102025891684634626.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102585909454659586.json, 图片生成/图生图/Qwen Image 2.1 图像编辑 Image Edit_2112444323198488578.json, 图片生成/图生图/Qwen Image 2.1 图片换装！B站艾橘溪_2101836548382740482.json, 图片生成/图生图/Qwen Image 2.1 多图编辑_2104447345671888898.json, 图片生成/图生图/Qwen image 2.1 多图编辑_2101841037932191746.json, 图片生成/图生图/Qwen_image_2.1图片编辑(提示词增强_2105113064805855234.json, 图片生成/图生图/Qwen_image_2.1图片编辑(提示词增强_2105490232509558786.json, 图片生成/文生图/Qwen image 2.1图片编辑(提示词增强）_2101808961656811521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_40

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json、图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json、图片生成/图生图/Face Swap  Qwen-Image-2.1模特换头+换脸_2102208882394357762.json、图片生成/图生图/Face+Swap换脸+Qwen-Image-2.1模特换头+换脸_2110526511987122178.json、图片生成/图生图/Qwen Image 2.1 一键图片换装_2101985763167653889.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 15 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 8/15 个有
- `easy showAnything` —— 7/15 个有
- `Image Comparer (rgthree)` —— 6/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/15 个有
- `SaveImageAdvanced` —— 5/15 个有
- `ImageConcatMulti` —— 4/15 个有
- `ImageResizeKJv2` —— 4/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `ImageConcanate` —— 2/15 个有
- `Latent Switch (JPS)` —— 2/15 个有
- `PreviewAny` —— 2/15 个有
- `RH_Translator` —— 2/15 个有
- `GetImageSize` —— 1/15 个有
- `PrimitiveStringMultiline` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 25 - 50 | 15 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 15 | 100% |
| 高度 | 1024 | 1024 - 1024 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 25 - 50，15 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，15 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，15 个样本，取值集中（一致性 100%）
