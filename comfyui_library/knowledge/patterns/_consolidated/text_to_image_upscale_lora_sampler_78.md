---
name: text_to_image_upscale_lora_sampler_78
type: Text To Image
frequency: 3
level: weak
coverage: 0.606333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKVCache, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageSharpenKJ, ImageUpscaleWithModel, JjkText, KSampler, LatentColorMatchSimple, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewAny, SaveImageAndMetadata_, SetNode, Text Concatenate, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2图推大合集 图生图洗图多方案集合_2105412413075054593.json, 图片生成/图生图/Krea2图生图推演大合集｜李泽钧精选多场景一网打尽_2105109475588927490.json, 图片生成/图生图/李泽钧-Krea2图推大合集_2090641332904747010.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Krea2图推大合集 图生图洗图多方案集合_2105412413075054593.json、图片生成/图生图/Krea2图生图推演大合集｜李泽钧精选多场景一网打尽_2105109475588927490.json、图片生成/图生图/李泽钧-Krea2图推大合集_2090641332904747010.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKVCache`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageSharpenKJ`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSampler`
- `LatentColorMatchSimple`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveImageAndMetadata_`
- `SetNode`
- `Text Concatenate`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `SaveImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1432 | 3 | 0% |
| 高度 | 80 | 80 - 1536 | 3 | 0% |
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1432，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，3 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（26/3 个样本）：Steps较低可能导致细节不足
