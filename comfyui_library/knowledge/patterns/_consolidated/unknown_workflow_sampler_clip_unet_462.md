---
name: unknown_workflow_sampler_clip_unet_462
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [ApplyPulidFlux, ApplyTeaCachePatch, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxForwardOverrider, FluxGuidance, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SDXLEmptyLatentSizePicker+, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【一键换脸】FLUX_PulID2 最逼真换脸_1954387597353205762.json, 图片生成/文生图/👽_____Caricature Portrait_讽刺漫画肖像_1965464010881646594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_462

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【一键换脸】FLUX_PulID2 最逼真换脸_1954387597353205762.json、图片生成/文生图/👽_____Caricature Portrait_讽刺漫画肖像_1965464010881646594.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `ApplyTeaCachePatch`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxForwardOverrider`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SDXLEmptyLatentSizePicker+`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `LoadImageAsMaskFromUrl` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832x1152 (0.72) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 832x1152 (0.72)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
