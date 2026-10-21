---
name: text_to_image_sampler_clip_unet_26
type: Text To Image
frequency: 12
level: weak
coverage: 0.707583
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy getNode, easy setNode, CR Prompt Text, Seed (rgthree)]
members: [图片生成/图生图/2102094333674614786.json, 图片生成/图生图/2102238523955965954.json, 图片生成/图生图/2102391245615230977.json, 图片生成/图生图/2102495775229046786.json, 图片生成/图生图/2102543389462982657.json, 图片生成/图生图/2102555854674419713.json, 图片生成/图生图/2102585557531578370.json, 图片生成/图生图/2102628402149806081.json, 图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json, 图片生成/文生图/Qwen Image 2.1文生图图生视频高清工作流合集处理工具_2102497280900296705.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列，局部重绘文生图图生图_2103952709224325121.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端详拆第11集｜新手逐节点拆解_2103728447376936962.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_26

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/2102094333674614786.json、图片生成/图生图/2102238523955965954.json、图片生成/图生图/2102391245615230977.json、图片生成/图生图/2102495775229046786.json、图片生成/图生图/2102543389462982657.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 11/12 个有
- `CR Prompt Text` —— 11/12 个有
- `JjkText` —— 11/12 个有
- `LayerUtility: ImageReel` —— 11/12 个有
- `LayerUtility: ImageReelComposit` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `solarL_SaveImagesToZip` —— 11/12 个有
- `孤海注释` —— 11/12 个有
- `Seed (rgthree)` —— 10/12 个有
- `ShowText|pysssss` —— 10/12 个有
- `easy setNode` —— 10/12 个有
- `GetNode` —— 9/12 个有
- `SetNode` —— 9/12 个有
- `BatchImagesNode` —— 8/12 个有
- `PreviewAny` —— 8/12 个有
- `TextGenerateLTX2Prompt` —— 8/12 个有
- `easy showAnything` —— 7/12 个有
- `SeedVR2LoadDiTModel` —— 5/12 个有
- `SeedVR2LoadVAEModel` —— 5/12 个有
- `SeedVR2VideoUpscaler` —— 5/12 个有
- `Any Switch (rgthree)` —— 4/12 个有
- `ImageScaleBy` —— 4/12 个有
- `RHLLMChatNode` —— 3/12 个有
- `ResizeLongestToNode` —— 3/12 个有
- `easy getNode` —— 3/12 个有
- `EmptyFlux2LatentImage` —— 2/12 个有
- `Fast Bypasser (rgthree)` —— 2/12 个有
- `ImageResize+` —— 2/12 个有
- `LoraLoader` —— 2/12 个有
- `PrimitiveBoolean` —— 2/12 个有
- `SplitImageWithAlpha` —— 2/12 个有
- `TTP_Image_Assy` —— 2/12 个有
- `TTP_Image_Tile_Batch` —— 2/12 个有
- `TTP_Tile_image_size` —— 2/12 个有
- `VOSR2ModelLoader` —— 2/12 个有
- `VOSR2Upscale` —— 2/12 个有
- `easy float` —— 2/12 个有
- `easy imageSize` —— 2/12 个有
- `easy int` —— 2/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 12 | 0% |
| 高度 | 80 | 80 - 1024 | 12 | 0% |
| 采样步数 | 4 | 4 - 20 | 12 | 17% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 12 | 77% |
| 采样算法 | er_sde | - | 12 | 92% |
| 调度器 | beta | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| LoRA 模型强度 | 0.4 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，12 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，12 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 20，12 个样本，取值分散，一致性仅 17%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，12 个样本
- 采样算法 最常用 er_sde，12 个样本，一致性 92%
- 调度器 最常用 beta，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、easy getNode、easy setNode、CR Prompt Text
