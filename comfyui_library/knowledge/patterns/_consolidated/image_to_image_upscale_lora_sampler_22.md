---
name: image_to_image_upscale_lora_sampler_22
type: Image To Image
frequency: 2
level: weak
coverage: 0.7785
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResizeKJv2, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveInt, PrimitiveStringMultiline, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Red-Z-Image-Turbo 红潮造像 RH _ 本地运行完整流程_2000463008281264130.json, 图片生成/文生图/红潮-Z-Image-Turbo 洗图 V1_2075079379469819906.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Red-Z-Image-Turbo 红潮造像 RH _ 本地运行完整流程_2000463008281264130.json、图片生成/文生图/红潮-Z-Image-Turbo 洗图 V1_2075079379469819906.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy seed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.675 | - | 2 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.675，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
