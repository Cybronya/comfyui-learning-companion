---
name: text_to_image_upscale_lora_sampler_88
type: Text To Image
frequency: 3
level: strong
coverage: 0.807667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ColorCorrect, ConditioningZeroOut, EmptyLatentImage, GetImageSize, INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, JoinStrings, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Lora Loader Stack (rgthree), PreviewImage, SamplerCustom, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, Text, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, 孤海注释, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转真人-多种采集_2077571701059178498.json, 图片生成/图生图/动漫转真人-多种采集_2077928843595304961.json, 图片生成/图生图/动漫转真人-多采超清天花板_2076803986665066498.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_88

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/动漫转真人-多种采集_2077571701059178498.json、图片生成/图生图/动漫转真人-多种采集_2077928843595304961.json、图片生成/图生图/动漫转真人-多采超清天花板_2076803986665066498.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorCorrect`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JoinStrings`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `Text`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `孤海注释`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
