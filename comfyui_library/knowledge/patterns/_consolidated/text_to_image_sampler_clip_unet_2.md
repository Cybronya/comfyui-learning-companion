---
name: text_to_image_sampler_clip_unet_2
type: Text To Image
frequency: 11
level: weak
coverage: 0.695182
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy getNode, easy setNode, CR Prompt Text, Seed (rgthree)]
members: [图片生成/图生图/2102094333674614786.json, 图片生成/图生图/2102238523955965954.json, 图片生成/图生图/2102391245615230977.json, 图片生成/图生图/2102495775229046786.json, 图片生成/图生图/2102543389462982657.json, 图片生成/图生图/2102555854674419713.json, 图片生成/图生图/2102585557531578370.json, 图片生成/图生图/2102628402149806081.json, 图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列，局部重绘文生图图生图_2103952709224325121.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端详拆第11集｜新手逐节点拆解_2103728447376936962.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/2102094333674614786.json、图片生成/图生图/2102238523955965954.json、图片生成/图生图/2102391245615230977.json、图片生成/图生图/2102495775229046786.json、图片生成/图生图/2102543389462982657.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 11 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `Seed (rgthree)` —— 10/11 个有
- `ShowText|pysssss` —— 10/11 个有
- `easy setNode` —— 10/11 个有
- `solarL_SaveImagesToZip` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `BatchImagesNode` —— 8/11 个有
- `GetNode` —— 8/11 个有
- `PreviewAny` —— 8/11 个有
- `SetNode` —— 8/11 个有
- `TextGenerateLTX2Prompt` —— 8/11 个有
- `easy showAnything` —— 7/11 个有
- `SeedVR2LoadDiTModel` —— 4/11 个有
- `SeedVR2LoadVAEModel` —— 4/11 个有
- `SeedVR2VideoUpscaler` —— 4/11 个有
- `Any Switch (rgthree)` —— 3/11 个有
- `ImageScaleBy` —— 3/11 个有
- `RHLLMChatNode` —— 3/11 个有
- `ResizeLongestToNode` —— 3/11 个有
- `easy getNode` —— 3/11 个有
- `EmptyFlux2LatentImage` —— 2/11 个有
- `Fast Bypasser (rgthree)` —— 2/11 个有
- `LoraLoader` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `SplitImageWithAlpha` —— 2/11 个有
- `VOSR2ModelLoader` —— 2/11 个有
- `VOSR2Upscale` —— 2/11 个有
- `easy float` —— 2/11 个有
- `easy int` —— 2/11 个有
- `ImageResize+` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `TTP_Image_Assy` —— 1/11 个有
- `TTP_Image_Tile_Batch` —— 1/11 个有
- `TTP_Tile_image_size` —— 1/11 个有
- `easy imageSize` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 11 | 0% |
| 高度 | 80 | 80 - 1024 | 11 | 0% |
| 采样步数 | 4 | 4 - 20 | 11 | 16% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 76% |
| 采样算法 | er_sde | - | 11 | 91% |
| 调度器 | beta | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 模型强度 | 0.4 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 20，11 个样本，取值分散，一致性仅 16%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 91%
- 调度器 最常用 beta，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、easy getNode、easy setNode、CR Prompt Text
