---
name: unknown_workflow_video_upscale_latent_upscale_158
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8565
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2_NAG, LTXTiledSampler, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, PromptRelayEncode, RandomNoise, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3 自用优化版 T2V customer Audio_2063969507642798081.json, 视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_158

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/LTX2.3 自用优化版 T2V customer Audio_2063969507642798081.json、视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXTiledSampler`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 1/2 个有
- `LTXVAudioVAEDecode` —— 1/2 个有
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LTXVEmptyLatentAudio` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 25 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
