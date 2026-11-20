---
name: image_to_image_sampler_clip_unet_116
type: Image To Image
frequency: 4
level: moderate
coverage: 0.7145
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImpactInt, ImpactMinMax, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, RHHiddenNodes, RepeatLatentBatch, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy float, easy imageSize, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2极致美学-turbo8步极速图像重绘！迄今超强一键反推2K洗图重绘+MJ平替+可选4K高清放大_2070336060541984770.json, 图片生成/图生图/Qwen Image 2512图像重绘！一键洗图！_1900353474218045441.json, 图片生成/图生图/Z-Image-Base图像重绘！迄今超强一键洗图！照片级真实感+可选4K高清放大_2016446377663926273.json, 图片生成/图生图/z-image图像重绘！迄今超强一键洗图！照片级真实感_1993967232592052226.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_116

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Krea2极致美学-turbo8步极速图像重绘！迄今超强一键反推2K洗图重绘+MJ平替+可选4K高清放大_2070336060541984770.json、图片生成/图生图/Qwen Image 2512图像重绘！一键洗图！_1900353474218045441.json、图片生成/图生图/Z-Image-Base图像重绘！迄今超强一键洗图！照片级真实感+可选4K高清放大_2016446377663926273.json、图片生成/图生图/z-image图像重绘！迄今超强一键洗图！照片级真实感_1993967232592052226.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `ImpactMinMax`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `RepeatLatentBatch`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy float`
- `easy imageSize`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Dapao_LlamaChat` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageCASharpening+` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 25 | 4 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 25，4 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
