---
name: text_to_image_upscale_latent_upscale_lora_24
type: Text To Image
frequency: 2
level: weak
coverage: 0.589
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, DetailDaemonSamplerNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GenerateNoise, GetNode, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LGNoiseInjectionLatent, LatentUpscaleBy, Load Lora, LoadImage, ModelSamplingAuraFlow, ModelSamplingZImage, PreviewImage, Qwen3_VQA, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, TextGenerate, Textbox, UNETLoader, UnetLoaderGGUF, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ZImageGemma4Qwen3VL和高级皮肤细节增强_2057842771427414017.json, 图片生成/文生图/Z Image-Gemma 4 -Qwen 3 VL 和高级皮肤细节增强_2052240536588832770.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ZImageGemma4Qwen3VL和高级皮肤细节增强_2057842771427414017.json、图片生成/文生图/Z Image-Gemma 4 -Qwen 3 VL 和高级皮肤细节增强_2052240536588832770.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DetailDaemonSamplerNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GenerateNoise`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LGNoiseInjectionLatent`
- `LatentUpscaleBy`
- `Load Lora`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ModelSamplingZImage`
- `PreviewImage`
- `Qwen3_VQA`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TextGenerate`
- `Textbox`
- `UNETLoader`
- `UnetLoaderGGUF`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 5 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | bong_tangent | - | 2 | 100% |
| 重绘幅度 | 0.38 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 bong_tangent，2 个样本，一致性 100%
- 重绘幅度 中位数 0.38，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（6/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
