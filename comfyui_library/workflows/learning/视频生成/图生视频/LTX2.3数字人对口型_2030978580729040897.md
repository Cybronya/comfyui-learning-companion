---
key: 视频生成/图生视频/LTX2.3数字人对口型_2030978580729040897.json
name: LTX2.3数字人对口型_2030978580729040897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030978580729040897.json
hash: 9fc59f13f7074a7f
coverage: 0.972222
learned_at: 2026-10-15 22:35:28
nodes: [SamplerCustomAdvanced, CFGGuider, KSamplerSelect, CLIPTextEncode, PrimitiveBoolean, RandomNoise, VAELoaderKJ, LTXVSeparateAVLatent, CLIPTextEncode, SimpleMath+, CM_IntToFloat, Int, DualCLIPLoader, LTX2_NAG, LTXVConcatAVLatent, CM_IntToFloat, VAEDecode, Int, Int, LayerUtility: ImageScaleByAspectRatio V2, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, ManualSigmas, LoadImage, UNETLoader, VAELoaderKJ, PrimitiveStringMultiline, LoadAudio, VHS_VideoCombine, LazySwitch1way, TrimAudioDuration, MelBandRoFormerModelLoader, MelBandRoFormerSampler, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3数字人对口型_2030978580729040897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030978580729040897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `RandomNoise`
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `CM_IntToFloat`
- `Int`
- `DualCLIPLoader`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `CM_IntToFloat`
- `VAEDecode` ★核心
- `Int`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `ManualSigmas`
- `LoadImage`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `VHS_VideoCombine`
- `LazySwitch1way`
- `TrimAudioDuration`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`KSamplerSelect`、`CLIPTextEncode`、`PrimitiveBoolean`、`RandomNoise`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`SimpleMath+`、`CM_IntToFloat`、`Int`、`DualCLIPLoader`、`LTX2_NAG`、`LTXVConcatAVLatent`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`LoadImage`、`UNETLoader`、`LoadAudio`、`VHS_VideoCombine`、`LazySwitch1way`、`TrimAudioDuration`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
