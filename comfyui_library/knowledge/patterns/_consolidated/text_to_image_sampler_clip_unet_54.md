---
name: text_to_image_sampler_clip_unet_54
type: Text To Image
frequency: 11
level: weak
coverage: 0.868818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ColorMatchV2, EmptyLatentImage, ImageScaleToTotalPixelsX, KSampler, KSamplerSelect, PreviewImage, QwenImage21Cache, RandomNoise, ReferenceLatent, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Seed (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2105063037303611394.json, 图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2105449510007824385.json, 图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2108641792710234114.json, 图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json, 图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2105581124431990785.json, 图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2108117843421257730.json, 图片生成/图生图/qwen-image-2.1服装模特姿势裂变｜一致性多角度出图_2108444022342770689.json, 图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105050635933667330.json, 图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105403211334115329.json, 图片生成/文生图/qwen-image-2.1-文生图-游戏角色设计_2102599454053457921.json, 视频生成/文生视频/qwen-image-2.1-文生图-游戏角色设计_2102954996517134338.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_54

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2105063037303611394.json、图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2105449510007824385.json、图片生成/图生图/qwen image 2.1服装模特图姿势裂变 电商服装多角度出图_2108641792710234114.json、图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2101840140003012609.json、图片生成/图生图/qwen-image-2.1-服装模特图姿势裂变_2105581124431990785.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 7/11 个有
- `ImageTile+` —— 7/11 个有
- `ImageUntile+` —— 7/11 个有
- `LoadImage` —— 7/11 个有
- `PreviewAny` —— 7/11 个有
- `PrimitiveStringMultiline` —— 7/11 个有
- `easy ifElse` —— 7/11 个有
- `JjkText` —— 6/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `solarL_SaveImagesToZip` —— 6/11 个有
- `孤海注释` —— 6/11 个有
- `VOSR2ModelLoader` —— 4/11 个有
- `VOSR2Upscale` —— 4/11 个有
- `easy positive` —— 4/11 个有
- `easy showAnything` —— 4/11 个有
- `EmptyImage` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 11 | 8% |
| 高度 | 80 | 80 - 1024 | 11 | 8% |
| 采样步数 | 4 | 4 - 25 | 11 | 23% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 40% |
| 采样算法 | er_sde | - | 11 | 55% |
| 调度器 | beta | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 8%
- 高度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 8%
- 采样步数 中位数 4，观测区间 4 - 25，11 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 er_sde，11 个样本，一致性 55%
- 调度器 最常用 beta，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（8/11 个样本）：Steps较低可能导致细节不足
