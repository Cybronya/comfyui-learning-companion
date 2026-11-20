---
name: image_to_image_inpaint_lora_sampler_12
type: Image To Image
frequency: 2
level: weak
coverage: 0.8795
common_nodes: [AnimaLLLiteApply, CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), InpaintPreprocessor, KSampler, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PainterFluxImageEdit, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Anima正式版-局部重绘+高清放大_2064625144798208002.json, 图片生成/图生图/局部重绘+高清Anima放大正式版ENG_2087106202491777025.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Anima正式版-局部重绘+高清放大_2064625144798208002.json、图片生成/图生图/局部重绘+高清Anima放大正式版ENG_2087106202491777025.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `AnimaLLLiteApply`
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `InpaintPreprocessor`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PainterFluxImageEdit`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
