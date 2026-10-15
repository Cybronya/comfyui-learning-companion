---
key: 视频生成/图生视频/LTX2.3口播数字人长视频稳定版无字幕图生视频图生短视频加速版15秒3分钟_2060321086079852545.json
name: LTX2.3口播数字人长视频稳定版无字幕图生视频图生短视频加速版15秒3分钟_2060321086079852545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3口播数字人长视频稳定版无字幕图生视频图生短视频加速版15秒3分钟_2060321086079852545.json
hash: 36c3de4d35019af2
coverage: 0.580247
learned_at: 2026-10-15 02:41:27
nodes: [DualCLIPLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, SetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, MelBandRoFormerSampler, GetNode, GetNode, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEDecode, GetNode, GetNode, SamplerCustomAdvanced, RandomNoise, RandomNoise, GetNode, CFGGuider, LTXVConditioning, KSamplerSelect, ManualSigmas, ManualSigmas, LTXVSeparateAVLatent, LTXVImgToVideoInplace, GetNode, GetNode, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, LatentUpscaleModelLoader, LatentUpscaleModelLoader, MathExpression|pysssss, SetNode, SetNode, TTResolutionSelector, GetNode, GetNode, MelBandRoFormerModelLoader, SetNode, CLIPTextEncode, VAEDecodeTiled, DiffusionModelLoaderKJ, VHS_VideoCombine, LTX2_NAG, GetNode, CLIPTextEncode, Bool, Int, Int, Float, LoadImage, LoadAudio, MathExpression|pysssss, Audio Duration (mtb), AudioCrop, JWString, JWString]
patterns: []
missing: [Audio Duration (mtb), MathExpression|pysssss, MathExpression|pysssss]
discoveries: [次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/LTX2.3口播数字人长视频稳定版无字幕图生视频图生短视频加速版15秒3分钟_2060321086079852545.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3口播数字人长视频稳定版无字幕图生视频图生短视频加速版15秒3分钟_2060321086079852545.json`

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
- `LoadImage`
- `LoadAudio`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `AudioCrop`
- `JWString`
- `JWString`

## 知识

覆盖率 **58%**（47/81）

**有卡**：`DualCLIPLoader`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVConditioning`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`TTResolutionSelector`、`MelBandRoFormerModelLoader`、`CLIPTextEncode`、`VAEDecodeTiled`、`DiffusionModelLoaderKJ`、`VHS_VideoCombine`、`LTX2_NAG`、`Bool`、`Int`、`Float`、`LoadImage`、`LoadAudio`、`AudioCrop`、`JWString`

**缺卡**（3）：`Audio Duration (mtb)`、`MathExpression|pysssss`、`MathExpression|pysssss`

**用到的条目**：CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
