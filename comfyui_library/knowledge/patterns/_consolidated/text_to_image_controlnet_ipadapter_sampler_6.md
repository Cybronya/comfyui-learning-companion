---
name: text_to_image_controlnet_ipadapter_sampler_6
type: Text To Image
frequency: 2
level: weak
coverage: 0.8655
common_nodes: [ApplyEcomIDAdvanced, CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EcomIDFaceAnalysis, EcomID_PulidModelLoader, EmptyLatentImage, GetImageSize+, GrowMaskWithBlur, IPAdapter, IPAdapterUnifiedLoader, Image Comparer (rgthree), Image Overlay, InstantIDModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LoadImage, PreviewImage, PulidEvaClipLoader, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch, preview_mask]
problems: []
missing: []
members: [平台全量/写真摄影_1890296710458122242.json, 平台全量/写真照片换背景XL+FLUX_1920673219714416642.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_sampler_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/写真摄影_1890296710458122242.json、平台全量/写真照片换背景XL+FLUX_1920673219714416642.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyEcomIDAdvanced`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EcomIDFaceAnalysis`
- `EcomID_PulidModelLoader`
- `EmptyLatentImage`
- `GetImageSize+`
- `GrowMaskWithBlur`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `PreviewImage`
- `PulidEvaClipLoader`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.15 | - | 2 | 100% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.35 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.15，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
