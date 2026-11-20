---
name: text_to_image_lora_sampler_clip_28
type: Text To Image
frequency: 23
level: strong
coverage: 0.857043
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1一键图片换装图生图处理工具_2102528994515181569.json, 图片生成/图生图/Qwen Image 2.1一键图片换装图生图，人物服饰替换处理工具_2102908589479387138.json, 图片生成/图生图/Qwen Image 2.1一键图片换装｜换装类图生图专用｜服装替换细节到位_2102270303454982146.json, 图片生成/图生图/Qwen Image 2.1一键扩图图生图处理生成工具_2102516145378127874.json, 图片生成/图生图/Qwen Image 2.1一键扩图图生图工作流，图生图写实扩图处理工具_2107231075868172290.json, 图片生成/图生图/Qwen Image 2.1一键扩图实战版｜边界延展不留痕｜横竖屏随你切换_2102626840547516418.json, 图片生成/图生图/Qwen Image 2.1一键扩图｜画面秒变超宽幅｜构图不够能延展_2102603964750581761.json, 图片生成/图生图/Qwen Image 2.1一键抠图PNG通道输出，透明背景图生图工具_2102886783691354114.json, 图片生成/图生图/Qwen Image 2.1一键抠图透明背景 自动识别主体电商产品照_2105356519280824321.json, 图片生成/图生图/Qwen Image 2.1一键换装图片服装替换，电商模特图生图自动完成工具_2103901904890851329.json, 图片生成/图生图/Qwen Image 2.1一键换装｜图片服装替换自动完成｜电商模特好帮手_2102224257387425794.json, 图片生成/图生图/Qwen Image 2.1万能输入工作流 文生图图生图处理工具_2113338289234202625.json, 图片生成/图生图/Qwen Image 2.1人物换头图片换脸图生图处理工具_2102520964331425794.json, 图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2107565485087870977.json, 图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2107938760527798274.json, 图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2108332170640187393.json, 图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json, 图片生成/图生图/Qwen Image 2.1洗图反推提示词，图生图图像分析与提示词提取工具_2103236925317537793.json, 图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110244395655188481.json, 图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110370717484273665.json, 图片生成/图生图/Qwen image 2.1高清修复流程，老图一键放大到4K_2110478470630436865.json, 图片生成/图生图/Qwen-Image-2.1 写实照片转动漫｜二次元风格化_2112483717431255042.json, 图片生成/图生图/Qwen_image_2.1高清修复流程，老图一键放大到4K_2113105105196249089.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1一键图片换装图生图处理工具_2102528994515181569.json、图片生成/图生图/Qwen Image 2.1一键图片换装图生图，人物服饰替换处理工具_2102908589479387138.json、图片生成/图生图/Qwen Image 2.1一键图片换装｜换装类图生图专用｜服装替换细节到位_2102270303454982146.json、图片生成/图生图/Qwen Image 2.1一键扩图图生图处理生成工具_2102516145378127874.json、图片生成/图生图/Qwen Image 2.1一键扩图图生图工作流，图生图写实扩图处理工具_2107231075868172290.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 22/23 个有
- `孤海注释` —— 22/23 个有
- `ComfySwitchNode` —— 21/23 个有
- `ResolutionSelector` —— 21/23 个有
- `TextGenerateLTX2Prompt` —— 15/23 个有
- `BatchImagesNode` —— 14/23 个有
- `Fast Groups Bypasser (rgthree)` —— 11/23 个有
- `GetNode` —— 11/23 个有
- `Image Comparer (rgthree)` —— 11/23 个有
- `SetNode` —— 11/23 个有
- `ImageResize+` —— 10/23 个有
- `ImageScaleBy` —— 10/23 个有
- `PreviewImage` —— 10/23 个有
- `SeedVR2LoadDiTModel` —— 10/23 个有
- `SeedVR2LoadVAEModel` —— 10/23 个有
- `SeedVR2VideoUpscaler` —— 10/23 个有
- `TTP_Image_Assy` —— 10/23 个有
- `TTP_Image_Tile_Batch` —— 10/23 个有
- `TTP_Tile_image_size` —— 10/23 个有
- `easy imageSize` —— 10/23 个有
- `LayerUtility: PurgeVRAM` —— 9/23 个有
- `Anything Everywhere3` —— 5/23 个有
- `CR Prompt Text` —— 5/23 个有
- `ImageResizeKJv2` —— 5/23 个有
- `LayerUtility: ImageReel` —— 5/23 个有
- `LayerUtility: ImageReelComposit` —— 5/23 个有
- `PreviewAny` —— 5/23 个有
- `CR Text` —— 4/23 个有
- `Latent Switch (JPS)` —— 4/23 个有
- `DWPreprocessor` —— 1/23 个有
- `DapaoImagePadDirectionNode` —— 1/23 个有
- `DepthAnythingV2Preprocessor` —— 1/23 个有
- `EmptyImage` —— 1/23 个有
- `GetImageSize` —— 1/23 个有
- `ImageConcanate` —— 1/23 个有
- `LineArtPreprocessor` —— 1/23 个有
- `SaveImageAdvanced` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（29/23 个样本）：Steps较低可能导致细节不足
