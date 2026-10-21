---
name: unknown_workflow_video_sampler_clip_209
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.972
common_nodes: [CFGGuider, CLIPTextEncode, CM_IntToFloat, DualCLIPLoader, EmptyLTXVLatentVideo, Int, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, LoadAudio, LoadImage, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveBoolean, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SimpleMath+, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2030978580729040897.json, 视频生成/图生视频/2055872851491737601.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_209

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2030978580729040897.json、视频生成/图生视频/2055872851491737601.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Int`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch1way`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
