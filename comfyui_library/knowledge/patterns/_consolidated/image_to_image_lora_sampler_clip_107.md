---
name: image_to_image_lora_sampler_clip_107
type: Image To Image
frequency: 3
level: moderate
coverage: 0.879333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转写实真人2511（零偏移_高还原）工作流_2013182174513602561.json, 图片生成/图生图/千问Qwen-image-2512-fp8-洗图、图生图工作流_2061646116659228674.json, 图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）+去除横纹_2012875763338448897.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_107

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/动漫转写实真人2511（零偏移_高还原）工作流_2013182174513602561.json、图片生成/图生图/千问Qwen-image-2512-fp8-洗图、图生图工作流_2061646116659228674.json、图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）+去除横纹_2012875763338448897.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `RunningHub Deepcleaner` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `Easy_QwenEdit2509` —— 1/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 3 | 42% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | dpmpp_2m | - | 3 | 33% |
| 重绘幅度 | exponential | - | 3 | 33% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，3 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m，3 个样本，一致性 33%
- 重绘幅度 最常用 exponential，3 个样本，一致性 33%
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
