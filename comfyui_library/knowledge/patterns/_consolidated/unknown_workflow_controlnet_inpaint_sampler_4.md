---
name: unknown_workflow_controlnet_inpaint_sampler_4
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.87325
common_nodes: [ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, ConditioningZeroOut, ControlNetLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetImageSize+, GrowMaskWithBlur, ImageResizeKJ, InpaintModelConditioning, Int, KSamplerSelect, LoadImage, MaskToImage, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键换背景丨商品广告设计丨保留文字细节_1922928502058926082.json, 图片生成/图生图/产品摄影_1922263430609223682.json, 图片生成/文生图/FLUX Union-Pro商品摄影【入档】_2111193485226373121.json, 图片生成/文生图/Flux-电商-人台图重绘_1924361876212207618.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键换背景丨商品广告设计丨保留文字细节_1922928502058926082.json、图片生成/图生图/产品摄影_1922263430609223682.json、图片生成/文生图/FLUX Union-Pro商品摄影【入档】_2111193485226373121.json、图片生成/文生图/Flux-电商-人台图重绘_1924361876212207618.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `ACN_AdvancedControlNetApplySingle_v2`
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `GrowMaskWithBlur`
- `ImageResizeKJ`
- `InpaintModelConditioning`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `MaskToImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: LoadFlorence2Model` —— 3/4 个有
- `LayerMask: ObjectDetectorFL2` —— 3/4 个有
- `LayerMask: SAM2Ultra` —— 3/4 个有
- `ImageToMask` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.2 | 0.1 - 0.5 | 4 | 34% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.2，观测区间 0.1 - 0.5，4 个样本，取值分散，一致性仅 34%
