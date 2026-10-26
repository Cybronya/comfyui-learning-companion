---
name: image_to_image_lora_sampler_unet_130
type: Image To Image
frequency: 5
level: strong
coverage: 0.8862
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, JoinStrings, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, SaveImage, Text, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【楚心钟陌】FireRed，动漫转真人全新效果_2030913879080968194.json, 图片生成/图生图/【楚心钟陌】上色测试_2017648649022476290.json, "图片生成/图生图/【楚心钟陌】全新炼制2511Edit,bbbs风格转换_2017879867953520641.json", 图片生成/图生图/【楚心钟陌】墨心_2033923657151549442.json, 图片生成/图生图/图生图-极快纸绘_2064888698222759938.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_130

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/【楚心钟陌】FireRed，动漫转真人全新效果_2030913879080968194.json、图片生成/图生图/【楚心钟陌】上色测试_2017648649022476290.json、图片生成/图生图/【楚心钟陌】全新炼制2511Edit,bbbs风格转换_2017879867953520641.json、图片生成/图生图/【楚心钟陌】墨心_2033923657151549442.json、图片生成/图生图/图生图-极快纸绘_2064888698222759938.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToMegapixels` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `ControlNetApplyAdvanced` —— 3/5 个有
- `ControlNetLoader` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ImageScaleBy` —— 3/5 个有
- `LayerUtility: PurgeVRAM V2` —— 3/5 个有
- `SeedVR2LoadDiTModel` —— 3/5 个有
- `SeedVR2LoadVAEModel` —— 3/5 个有
- `SeedVR2VideoUpscaler` —— 3/5 个有
- `SetUnionControlNetType` —— 3/5 个有
- `Seed_` —— 2/5 个有
- `TextEncodeQwenImageEditPlus` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/5 个有
- `RunningHub Deepcleaner` —— 1/5 个有
- `ttN seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_2m | - | 5 | 60% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，5 个样本，一致性 60%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（13/5 个样本）：Steps较低可能导致细节不足
