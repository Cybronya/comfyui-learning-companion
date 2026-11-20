---
name: image_to_image_inpaint_upscale_lora_2
type: Image To Image
frequency: 6
level: strong
coverage: 0.934
common_nodes: [CLIPLoader, CLIPTextEncode, CR Latent Input Switch, CR Text, ConditioningZeroOut, EmptySD3LatentImage, Image Comparer (rgthree), ImpactGaussianBlurMask, InpaintModelConditioning, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/星绘-Z-Image-奇幻国风人像摄影（内置图片反推、重绘、放大）_2011335946712649729.json, 平台全量/星绘-Z-Image-港式氛围感人像_1999871333758627841.json, 平台全量/星绘-Z-Image——哈苏人像滤镜（内置重绘、放大）_1998659302397202433.json, 平台全量/星绘-Z-Image—新年人像特辑大片（内置图片反推、重绘、放大）_2010586741563985921.json, 平台全量/星绘-Z-Image—氛围感新年妆容（内置重绘、放大）_1998938372255178753.json, 平台全量/星绘_Z-image_手部优化_手部姿势生成器_1998938052129120258.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/星绘-Z-Image-奇幻国风人像摄影（内置图片反推、重绘、放大）_2011335946712649729.json、平台全量/星绘-Z-Image-港式氛围感人像_1999871333758627841.json、平台全量/星绘-Z-Image——哈苏人像滤镜（内置重绘、放大）_1998659302397202433.json、平台全量/星绘-Z-Image—新年人像特辑大片（内置图片反推、重绘、放大）_2010586741563985921.json、平台全量/星绘-Z-Image—氛围感新年妆容（内置重绘、放大）_1998938372255178753.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Latent Input Switch`
- `CR Text`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 3/6 个有
- `Qwen3_VQA` —— 3/6 个有
- `MultiplePathsInput` —— 2/6 个有
- `MultiplePathsInputPlus` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.8 | 0.2 - 0.8 | 6 | 58% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.8，观测区间 0.2 - 0.8，6 个样本
