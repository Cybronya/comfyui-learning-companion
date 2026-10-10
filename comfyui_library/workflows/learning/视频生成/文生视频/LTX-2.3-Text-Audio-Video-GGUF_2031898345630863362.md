---
key: 视频生成/文生视频/LTX-2.3-Text-Audio-Video-GGUF_2031898345630863362.json
name: LTX-2.3-Text-Audio-Video-GGUF_2031898345630863362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-Text-Audio-Video-GGUF_2031898345630863362.json
hash: 1c269f871af13a74
coverage: 0.808511
learned_at: 2026-10-11 03:16:45
nodes: [CFGGuider, ManualSigmas, GetNode, SetLatentNoiseMask, SetNode, SetNode, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, RandomNoise, SolidMask, LTXVAudioVAEEncode, LTXVSeparateAVLatent, CreateVideo, GetNode, KSamplerSelect, SetNode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVConditioning, Float, LTXVSeparateAVLatent, LTXVLatentUpsampler, GetNode, LTXVConcatAVLatent, GetNode, MarkdownNote, EmptyImage, SaveVideo, AudioCrop, PrimitiveInt, VAEDecodeTiled, CLIPTextEncode, LoraLoaderModelOnly, UnetLoaderGGUF, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, DualCLIPLoader, LoadAudio, CLIPTextEncode, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX-2.3-Text-Audio-Video-GGUF_2031898345630863362.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-Text-Audio-Video-GGUF_2031898345630863362.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `CFGGuider`
- `ManualSigmas`
- `GetNode`
- `SetLatentNoiseMask`
- `SetNode`
- `SetNode`
- `ImageScaleBy`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `GetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `Float`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `MarkdownNote`
- `EmptyImage`
- `SaveVideo`
- `AudioCrop`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **81%**（38/47）

**有卡**：`CFGGuider`、`ManualSigmas`、`SetLatentNoiseMask`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`RandomNoise`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVSeparateAVLatent`、`CreateVideo`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVConditioning`、`Float`、`LTXVLatentUpsampler`、`EmptyImage`、`SaveVideo`、`AudioCrop`、`VAEDecodeTiled`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent、LTXVSeparateAVLatent
