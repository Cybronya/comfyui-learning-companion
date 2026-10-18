---
key: 视频生成/图生视频/LTX2.3数字人口播长视频稳定版 图生视频加速版_2102355217873461250.json
name: LTX2.3数字人口播长视频稳定版 图生视频加速版_2102355217873461250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人口播长视频稳定版 图生视频加速版_2102355217873461250.json
hash: 7ff8ed81a8391f45
coverage: 0.617284
learned_at: 2026-10-17 02:28:51
nodes: [DualCLIPLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, SetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, MelBandRoFormerSampler, GetNode, GetNode, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEDecode, GetNode, GetNode, SamplerCustomAdvanced, RandomNoise, RandomNoise, GetNode, CFGGuider, LTXVConditioning, KSamplerSelect, ManualSigmas, ManualSigmas, LTXVSeparateAVLatent, LTXVImgToVideoInplace, GetNode, GetNode, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, LatentUpscaleModelLoader, LatentUpscaleModelLoader, MathExpression|pysssss, SetNode, SetNode, TTResolutionSelector, GetNode, GetNode, MelBandRoFormerModelLoader, SetNode, CLIPTextEncode, VAEDecodeTiled, DiffusionModelLoaderKJ, VHS_VideoCombine, LTX2_NAG, GetNode, CLIPTextEncode, Bool, Int, Int, Float, MathExpression|pysssss, Audio Duration (mtb), AudioCrop, JWString, JWString, LoadAudio, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3数字人口播长视频稳定版 图生视频加速版_2102355217873461250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人口播长视频稳定版 图生视频加速版_2102355217873461250.json`

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
- `LoadAudio`
- `LoadImage`

## 知识

覆盖率 **62%**（50/81）

**有卡**：`DualCLIPLoader`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVConditioning`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`MathExpression|pysssss`、`TTResolutionSelector`、`MelBandRoFormerModelLoader`、`CLIPTextEncode`、`VAEDecodeTiled`、`DiffusionModelLoaderKJ`、`VHS_VideoCombine`、`LTX2_NAG`、`Bool`、`Int`、`Float`、`Audio Duration (mtb)`、`AudioCrop`、`JWString`、`LoadAudio`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler、LTXVConcatAVLatent
