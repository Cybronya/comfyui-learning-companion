---
name: unknown_workflow_controlnet_sampler_clip_31
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9185
common_nodes: [ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetLoader, DualCLIPLoader, FluxGuidance, ImageScale, KSamplerSelect, LayerColor: AutoAdjustV2, LoadImage, ModelSamplingFlux, PreviewImage, RandomNoise, SDXLEmptyLatentSizePicker+, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/F.1+Advanced ControlNet+遮罩_1924358166027694081.json, 图片生成/文生图/Flux CN Union Pro 2.0通用基础生成_1924342356764446722.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/F.1+Advanced ControlNet+遮罩_1924358166027694081.json、图片生成/文生图/Flux CN Union Pro 2.0通用基础生成_1924342356764446722.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApplySingle_v2`
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageScale`
- `KSamplerSelect`
- `LayerColor: AutoAdjustV2`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SDXLEmptyLatentSizePicker+`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InspyrenetRembg` —— 1/2 个有
- `Mask Invert` —— 1/2 个有
- `MaskToImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768x1280 (0.6) | - | 2 | 50% |
| 高度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.75 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 768x1280 (0.6)，2 个样本，一致性 50%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.75，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
