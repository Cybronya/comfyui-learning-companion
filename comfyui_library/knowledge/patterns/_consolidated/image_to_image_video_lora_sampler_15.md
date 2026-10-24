---
name: image_to_image_video_lora_sampler_15
type: Image To Image
frequency: 2
level: weak
coverage: 0.851
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DisableNoise, Image Comparer (rgthree), KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2, SplitSigmas, UNETLoader, VAEDecode, VAEEncode, VAELoader, WanVideoNAG, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Kontext万物融图+Wan2.2洗图（手动编辑）_1955827510690942977.json, 图片生成/图生图/Z-image+Wan 2.2 -局部质感增强洗图_2011065279308107777.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Kontext万物融图+Wan2.2洗图（手动编辑）_1955827510690942977.json、图片生成/图生图/Z-image+Wan 2.2 -局部质感增强洗图_2011065279308107777.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DisableNoise`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WanVideoNAG`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `InpaintCrop` —— 1/2 个有
- `InpaintStitch` —— 1/2 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.575 | - | 2 | 26% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.575，样本不足，未给区间，2 个样本，取值分散，一致性仅 26%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
