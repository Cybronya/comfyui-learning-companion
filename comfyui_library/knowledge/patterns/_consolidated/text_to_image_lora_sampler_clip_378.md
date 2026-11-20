---
name: text_to_image_lora_sampler_clip_378
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8444
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Moss搭配QwenImage2.1，文生图与图片编辑双引擎_2112615940293742594.json, 图片生成/图生图/Qwen Image 2.1 PE图像编辑加速版 高效改图方案_2109362662906875905.json, 图片生成/图生图/QwenImage2.1 turbo六图编辑，高效改图图生图方案_2111901617984458753.json, 图片生成/图生图/（6图编辑）QwenImage2.1 turbo专用工作流 高效改图方案_2111592341713801218.json, 图片生成/文生图/Moss+QwenImage2.1 二合一｜文生图加图片编辑双修_2112397825056272386.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_378

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Moss搭配QwenImage2.1，文生图与图片编辑双引擎_2112615940293742594.json、图片生成/图生图/Qwen Image 2.1 PE图像编辑加速版 高效改图方案_2109362662906875905.json、图片生成/图生图/QwenImage2.1 turbo六图编辑，高效改图图生图方案_2111901617984458753.json、图片生成/图生图/（6图编辑）QwenImage2.1 turbo专用工作流 高效改图方案_2111592341713801218.json、图片生成/文生图/Moss+QwenImage2.1 二合一｜文生图加图片编辑双修_2112397825056272386.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有
- `CFGGuider` —— 3/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `QwenImage21Cache` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `Any Switch (rgthree)` —— 2/5 个有
- `BasicGuider` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `JsonExtractString` —— 2/5 个有
- `SkipLayerGuidanceDiTSimple` —— 2/5 个有
- `TextGenerate` —— 2/5 个有
- `easy isNone` —— 2/5 个有
- `ImageCompare` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_QwenImagePromptEnhancer` —— 1/5 个有
- `SaveImageAdvanced` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 5 | 0% |
| 高度 | 80 | 80 - 1024 | 5 | 0% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
