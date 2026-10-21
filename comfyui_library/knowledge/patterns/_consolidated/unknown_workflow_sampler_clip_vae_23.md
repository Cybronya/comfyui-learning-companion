---
name: unknown_workflow_sampler_clip_vae_23
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9138
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuPulidApply, NunchakuPulidLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [Text Multiline, SDXLEmptyLatentSizePicker+, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1924625965945974786.json, 图片生成/文生图/1925107417154318337.json, 图片生成/文生图/1925472577286754305.json, 图片生成/文生图/1931572247486771202.json, 图片生成/文生图/1932623266177556482.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_23

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1924625965945974786.json、图片生成/文生图/1925107417154318337.json、图片生成/文生图/1925472577286754305.json、图片生成/文生图/1931572247486771202.json、图片生成/文生图/1932623266177556482.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuPulidApply`
- `NunchakuPulidLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/5 个有
- `ControlNetApplyAdvanced` —— 3/5 个有
- `ControlNetLoader` —— 3/5 个有
- `NunchakuFluxLoraLoader` —— 3/5 个有
- `SetUnionControlNetType` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `DualCLIPLoader` —— 2/5 个有
- `InpaintModelConditioning` —— 2/5 个有
- `KSampler` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `CLIPVisionEncode` —— 1/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `ImageAndMaskResizeNode` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `InstructPixToPixConditioning` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `NunchakuTextEncoderLoaderV2` —— 1/5 个有
- `SDXLEmptyLatentSizePicker+` —— 1/5 个有
- `StyleModelApply` —— 1/5 个有
- `StyleModelLoader` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 704x1408 (0.5) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、SDXLEmptyLatentSizePicker+、LayerUtility: ImageScaleByAspectRatio V2
