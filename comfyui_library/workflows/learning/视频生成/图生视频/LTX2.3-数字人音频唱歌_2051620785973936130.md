---
key: 视频生成/图生视频/LTX2.3-数字人音频唱歌_2051620785973936130.json
name: LTX2.3-数字人音频唱歌_2051620785973936130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2051620785973936130.json
hash: 1ec98ecfc6fc15c2
coverage: 0.709091
learned_at: 2026-10-15 22:37:23
nodes: [EmptyLTXVLatentVideo, LTXVImgToVideoInplace, MelBandRoFormerSampler, LTXVAudioVAEEncode, SetLatentNoiseMask, GetNode, GetNode, GetNode, MelBandRoFormerModelLoader, GetNode, GetNode, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, UNETLoader, LoraLoaderModelOnly, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTX2SamplingPreviewOverride, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, LTXVConcatAVLatent, LTX2_NAG, GetNode, MathExpression|pysssss, SetNode, Float, MathExpression|pysssss, SetNode, SetNode, CreateVideo, GetNode, LTXVAudioVAEDecode, GetNode, VAEDecodeTiled, SaveVideo, GetNode, SolidMask, Audio Duration (mtb), LoadAudio, AudioCrop, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, PathchSageAttentionKJ, LTXVChunkFeedForward, SetNode, LoraLoaderModelOnly, LTXVConditioning, GetNode, CLIPTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3-数字人音频唱歌_2051620785973936130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051620785973936130.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTX2SamplingPreviewOverride`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LTX2_NAG`
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `Float`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `CreateVideo`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `GetNode`
- `SolidMask`
- `Audio Duration (mtb)`
- `LoadAudio`
- `AudioCrop`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `GetNode`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **71%**（39/55）

**有卡**：`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`MelBandRoFormerModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTX2SamplingPreviewOverride`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`LTXVConcatAVLatent`、`LTX2_NAG`、`MathExpression|pysssss`、`Float`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`SaveVideo`、`SolidMask`、`Audio Duration (mtb)`、`LoadAudio`、`AudioCrop`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTXVConditioning`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
