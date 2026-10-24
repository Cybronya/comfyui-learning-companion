---
name: image_to_image_lora_sampler_unet_84
type: Image To Image
frequency: 8
level: weak
coverage: 0.81025
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转写实真人2511（零偏移_高还原）工作流_2013182174513602561.json, 图片生成/图生图/千问Qwen-image-2512-fp8-洗图、图生图工作流_2061646116659228674.json, 图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）+去除横纹_2012875763338448897.json, 图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）正式版-高还原_2009527411641159681.json, 图片生成/图生图/工作流基础系列11-QwenImageEdit2511单图编辑_2004000394919485442.json, 图片生成/图生图/工作流基础系列12-QwenImageEdit2511双图编辑_2004026267299135489.json, 图片生成/图生图/组件系列12-QWEN-EDIT-2511单图编辑_2059098441153859586.json, 图片生成/图生图/组件系列13-QWEN-EDIT-2511多图编辑_2059099538136322050.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_84

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/动漫转写实真人2511（零偏移_高还原）工作流_2013182174513602561.json、图片生成/图生图/千问Qwen-image-2512-fp8-洗图、图生图工作流_2061646116659228674.json、图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）+去除横纹_2012875763338448897.json、图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）正式版-高还原_2009527411641159681.json、图片生成/图生图/工作流基础系列11-QwenImageEdit2511单图编辑_2004000394919485442.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
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
- `ModelSamplingAuraFlow` —— 7/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `Seed (rgthree)` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `TextEncodeQwenImageEditPlus` —— 6/8 个有
- `CFGNorm` —— 5/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `CR Text` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `CLIPTextEncode` —— 3/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `KSamplerAdvanced` —— 2/8 个有
- `ReferenceLatent` —— 2/8 个有
- `RunningHub Deepcleaner` —— 2/8 个有
- `TextEncodeQwenImageEdit` —— 2/8 个有
- `easy promptList` —— 2/8 个有
- `Easy_QwenEdit2509` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 8 | 0% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 0.6 - 1 | 6 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，6 个样本，取值集中（一致性 84%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
