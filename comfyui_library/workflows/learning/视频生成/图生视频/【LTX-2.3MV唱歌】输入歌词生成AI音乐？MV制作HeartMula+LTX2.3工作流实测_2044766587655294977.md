---
key: 视频生成/图生视频/【LTX-2.3MV唱歌】输入歌词生成AI音乐？MV制作HeartMula+LTX2.3工作流实测_2044766587655294977.json
name: 【LTX-2.3MV唱歌】输入歌词生成AI音乐？MV制作HeartMula+LTX2.3工作流实测_2044766587655294977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044766587655294977.json
hash: 33f875df72d80ca0
coverage: 0.84127
learned_at: 2026-10-15 22:36:40
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, KSamplerSelect, Reroute, LTXVAudioVAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, SolidMask, LTXVPreprocess, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, LTXVConcatAVLatent, SetLatentNoiseMask, PrimitiveInt, CreateVideo, LTXVConditioning, CFGGuider, LTXVImgToVideoInplace, LTXVImgToVideoInplace, ResizeImagesByLongerEdge, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, MarkdownNote, PrimitiveInt, PrimitiveStringMultiline, TrimAudioDuration, Text _O, Text _O, HeartMuLa_Generate, SaveAudio, LoadAudio, HeartMuLa_Transcribe, ShowText|pysssss, Text _O, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, LoadImage, LoadAudio, PrimitiveBoolean, CLIPTextEncode, CLIPTextEncode, Label (rgthree), Fast Groups Bypasser (rgthree), CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, ComfyMathExpression, SaveVideo, ManualSigmas, RandomNoise]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/【LTX-2.3MV唱歌】输入歌词生成AI音乐？MV制作HeartMula+LTX2.3工作流实测_2044766587655294977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044766587655294977.json`

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
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadAudio`
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

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **84%**（53/63）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SolidMask`、`LTXVPreprocess`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`CreateVideo`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`TrimAudioDuration`、`Text _O`、`HeartMuLa_Generate`、`SaveAudio`、`LoadAudio`、`HeartMuLa_Transcribe`、`LoadImage`、`PrimitiveBoolean`、`CLIPTextEncode`、`Label (rgthree)`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
