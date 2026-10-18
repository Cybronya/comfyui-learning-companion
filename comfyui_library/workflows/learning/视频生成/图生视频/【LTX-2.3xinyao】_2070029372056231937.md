---
key: 视频生成/图生视频/【LTX-2.3xinyao】_2070029372056231937.json
name: 【LTX-2.3xinyao】_2070029372056231937.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【LTX-2.3xinyao】_2070029372056231937.json
hash: 93fe16f8ab84e7e8
coverage: 0.84127
learned_at: 2026-10-15 22:40:34
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, KSamplerSelect, Reroute, LTXVAudioVAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, SolidMask, LTXVPreprocess, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, LTXVConcatAVLatent, SetLatentNoiseMask, PrimitiveInt, CreateVideo, LTXVConditioning, CFGGuider, LTXVImgToVideoInplace, LTXVImgToVideoInplace, ResizeImagesByLongerEdge, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, MarkdownNote, PrimitiveInt, PrimitiveStringMultiline, TrimAudioDuration, Text _O, Text _O, HeartMuLa_Generate, SaveAudio, LoadAudio, HeartMuLa_Transcribe, ShowText|pysssss, Text _O, PrimitiveBoolean, CLIPTextEncode, CLIPTextEncode, Label (rgthree), Fast Groups Bypasser (rgthree), CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, ComfyMathExpression, SaveVideo, ManualSigmas, RandomNoise, LoadImage, PrimitiveStringMultiline, PrimitiveInt, PrimitiveFloat, LoadAudio]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/【LTX-2.3xinyao】_2070029372056231937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070029372056231937.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SolidMask`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `PrimitiveInt`
- `CreateVideo`
- `LTXVConditioning`
- `CFGGuider`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `TrimAudioDuration`
- `Text _O`
- `Text _O`
- `HeartMuLa_Generate`
- `SaveAudio`
- `LoadAudio`
- `HeartMuLa_Transcribe`
- `ShowText|pysssss`
- `Text _O`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `ComfyMathExpression`
- `SaveVideo`
- `ManualSigmas`
- `RandomNoise`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LoadAudio`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **84%**（53/63）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SolidMask`、`LTXVPreprocess`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`CreateVideo`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`TrimAudioDuration`、`Text _O`、`HeartMuLa_Generate`、`SaveAudio`、`LoadAudio`、`HeartMuLa_Transcribe`、`PrimitiveBoolean`、`CLIPTextEncode`、`Label (rgthree)`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`SaveVideo`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
