---
name: text_to_image_sampler_clip_unet_11
type: Text To Image
frequency: 5
level: weak
coverage: 0.859
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ColorMatchV2, EmptyLatentImage, ImageScaleToTotalPixelsX, KSampler, KSamplerSelect, PreviewImage, QwenImage21Cache, RandomNoise, ReferenceLatent, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Seed (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [ImageTile+, ImageUntile+, Seed (rgthree)]
members: [图片生成/图生图/2101840140003012609.json, 图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105050635933667330.json, 图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105403211334115329.json, 图片生成/文生图/qwen-image-2.1-文生图-游戏角色设计_2102599454053457921.json, 视频生成/文生视频/qwen-image-2.1-文生图-游戏角色设计_2102954996517134338.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2101840140003012609.json、图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105050635933667330.json、图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105403211334115329.json、图片生成/文生图/qwen-image-2.1-文生图-游戏角色设计_2102599454053457921.json、视频生成/文生视频/qwen-image-2.1-文生图-游戏角色设计_2102954996517134338.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `EmptyLatentImage`
- `ImageScaleToTotalPixelsX`
- `KSampler`
- `KSamplerSelect`
- `PreviewImage`
- `QwenImage21Cache`
- `RandomNoise`
- `ReferenceLatent`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VOSR2ModelLoader` —— 4/5 个有
- `VOSR2Upscale` —— 4/5 个有
- `easy positive` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `JjkText` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `solarL_SaveImagesToZip` —— 2/5 个有
- `孤海注释` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageTile+` —— 1/5 个有
- `ImageUntile+` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `easy ifElse` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 5 | 28% |
| 高度 | 1024 | 80 - 1024 | 5 | 28% |
| 采样步数 | 25 | 4 - 25 | 5 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 5 | 29% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 28%
- 高度 中位数 1024，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 28%
- 采样步数 中位数 25，观测区间 4 - 25，5 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ImageTile+、ImageUntile+、Seed (rgthree)
