---
name: unknown_workflow_inpaint_sampler_clip_61
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.831
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Color Panel, ConditioningZeroOut, DeepTranslatorTextNode, DifferentialDiffusion, DownloadAndLoadFlorence2Model, Florence2Run, FluxGuidance, ImageCrop, ImageToMask, InpaintModelConditioning, Int, KSampler, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader, easy imageConcat, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Flux-Redux 漫画人物一键快速换装_1951929706251759617.json, 图片生成/图生图/Nunchaku极速换装Fill+ACE+Redux_1943999439797125121.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_61

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux-Redux 漫画人物一键快速换装_1951929706251759617.json、图片生成/图生图/Nunchaku极速换装Fill+ACE+Redux_1943999439797125121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Color Panel`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `FluxGuidance`
- `ImageCrop`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AutoDownloadBiRefNetModel` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `NunchakuTextEncoderLoader` —— 1/2 个有
- `RembgByBiRefNet` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26.5 | - | 2 | 94% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 26.5，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
