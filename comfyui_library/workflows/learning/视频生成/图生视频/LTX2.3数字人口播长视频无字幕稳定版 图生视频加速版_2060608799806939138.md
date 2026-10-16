---
key: 视频生成/图生视频/LTX2.3数字人口播长视频无字幕稳定版 图生视频加速版_2060608799806939138.json
name: LTX2.3数字人口播长视频无字幕稳定版 图生视频加速版_2060608799806939138.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2060608799806939138.json
hash: e8a05cb983393a97
coverage: 0.617284
learned_at: 2026-10-15 22:38:48
nodes: [DualCLIPLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, SetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, MelBandRoFormerSampler, GetNode, GetNode, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEDecode, GetNode, GetNode, SamplerCustomAdvanced, RandomNoise, RandomNoise, GetNode, CFGGuider, LTXVConditioning, KSamplerSelect, ManualSigmas, ManualSigmas, LTXVSeparateAVLatent, LTXVImgToVideoInplace, GetNode, GetNode, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, LatentUpscaleModelLoader, LatentUpscaleModelLoader, MathExpression|pysssss, SetNode, SetNode, TTResolutionSelector, GetNode, GetNode, MelBandRoFormerModelLoader, SetNode, CLIPTextEncode, VAEDecodeTiled, DiffusionModelLoaderKJ, VHS_VideoCombine, LTX2_NAG, GetNode, CLIPTextEncode, Bool, Int, Int, Float, MathExpression|pysssss, Audio Duration (mtb), AudioCrop, JWString, JWString, LoadImage, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3数字人口播长视频无字幕稳定版 图生视频加速版_2060608799806939138.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060608799806939138.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（81 个）：
- `DualCLIPLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `GetNode`
- `CFGGuider`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LatentUpscaleModelLoader`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `TTResolutionSelector`
- `GetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `DiffusionModelLoaderKJ`
- `VHS_VideoCombine`
- `LTX2_NAG`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Bool`
- `Int`
- `Int`
- `Float`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `AudioCrop`
- `JWString`
- `JWString`
- `LoadImage`
- `LoadAudio`

## 知识

覆盖率 **62%**（50/81）

**有卡**：`DualCLIPLoader`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVConditioning`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`MathExpression|pysssss`、`TTResolutionSelector`、`MelBandRoFormerModelLoader`、`CLIPTextEncode`、`VAEDecodeTiled`、`DiffusionModelLoaderKJ`、`VHS_VideoCombine`、`LTX2_NAG`、`Bool`、`Int`、`Float`、`Audio Duration (mtb)`、`AudioCrop`、`JWString`、`LoadImage`、`LoadAudio`

**用到的条目**：CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler、LTXVConcatAVLatent
