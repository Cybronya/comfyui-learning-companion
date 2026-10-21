---
name: unknown_workflow_controlnet_sampler_clip_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.851667
common_nodes: [ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerColor: AutoAdjustV2, SDXLEmptyLatentSizePicker+, Mask Invert, GetImageSize+]
members: [图片生成/文生图/1924342356764446722.json, 图片生成/文生图/1924358166027694081.json, 图片生成/文生图/1924361876212207618.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1924342356764446722.json、图片生成/文生图/1924358166027694081.json、图片生成/文生图/1924361876212207618.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `ACN_AdvancedControlNetApplySingle_v2`
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
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
- `ImageScale` —— 2/3 个有
- `LayerColor: AutoAdjustV2` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `SDXLEmptyLatentSizePicker+` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImageToMask` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `InspyrenetRembg` —— 1/3 个有
- `Int` —— 1/3 个有
- `Mask Invert` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 2 | 50% |
| 高度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | 0.1 - 0.9 | 3 | 38% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，2 个样本，一致性 50%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，观测区间 0.1 - 0.9，3 个样本，取值分散，一致性仅 38%
- 这些节点还没有知识卡，系统对它们的理解有限：LayerColor: AutoAdjustV2、SDXLEmptyLatentSizePicker+、Mask Invert、GetImageSize+
