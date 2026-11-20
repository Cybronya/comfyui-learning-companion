---
name: image_to_image_inpaint_lora_sampler_24
type: Image To Image
frequency: 2
level: weak
coverage: 0.9125
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DrawMaskOnImage, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), ImagePadForOutpaint, InpaintModelConditioning, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/扩图专辑——Z-image+Flux-fill-OneReward+Flux-2-klein扩图流_2001819543137841154.json, 平台全量/工作流系列-Klein模型工作流集合_2101494386466054146.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/扩图专辑——Z-image+Flux-fill-OneReward+Flux-2-klein扩图流_2001819543137841154.json、平台全量/工作流系列-Klein模型工作流集合_2101494386466054146.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `INPAINT_InpaintWithModel` —— 1/2 个有
- `INPAINT_LoadInpaintModel` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `PainterFluxImageEdit` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `YC Color Match` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
