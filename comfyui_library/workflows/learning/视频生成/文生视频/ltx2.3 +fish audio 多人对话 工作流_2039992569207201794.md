---
key: 视频生成/文生视频/ltx2.3 +fish audio 多人对话 工作流_2039992569207201794.json
name: ltx2.3 +fish audio 多人对话 工作流_2039992569207201794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3 +fish audio 多人对话 工作流_2039992569207201794.json
hash: 5a6fbb5f7173e3e4
coverage: 0.868421
learned_at: 2026-10-15 22:47:22
nodes: [ManualSigmas, SamplerCustomAdvanced, RandomNoise, RandomNoise, KSamplerSelect, LatentUpscaleModelLoader, CFGGuider, CFGGuider, Reroute, SamplerCustomAdvanced, LTXVLatentUpsampler, SetNode, DualCLIPLoader, LTXVConditioning, VAELoaderKJ, ManualSigmas, Int, PrimitiveInt, SimpleMath+, MelBandRoFormerSampler, LTXVAudioVAEEncode, CLIPTextEncode, LTXVAudioVAEDecode, UNETLoader, SetLatentNoiseMask, ComfyMathExpression, MelBandRoFormerModelLoader, GetNode, SoundFlow_GetLength, SimpleMath+, SimpleMath+, QZ_ResolutionPreset, VAELoaderKJ, ConcatTextOfUtils, LTXVSeparateAVLatent, VAEDecodeTiled, CreateVideo, easy cleanGpuUsed, ConcatTextOfUtils, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVCropGuides, KSamplerSelect, LTXVConcatAVLatent, LTXVConcatAVLatent, SolidMask, CM_FloatToInt, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, ImageResizeKJv2, RH_LLMAPI_Pro_Node, LoadImage, ShowAnything|Mie, CLIPTextEncode, SaveVideo, FishS2MultiSpeakerTTS, LoadAudio, PreviewAudio, TrimAudio, Audio To Text (mtb), easy showAnything, LoadAudio, TrimAudio, Load Whisper (mtb), Audio To Text (mtb), MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveNode, CR Text, easy showAnything, easy showAnything, PreviewAudio, TrimAudioDuration, easy showAnything, easy showAnything, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
---

# 视频生成/文生视频/ltx2.3 +fish audio 多人对话 工作流_2039992569207201794.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3 +fish audio 多人对话 工作流_2039992569207201794.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `CFGGuider`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `DualCLIPLoader`
- `LTXVConditioning`
- `VAELoaderKJ`
- `ManualSigmas`
- `Int`
- `PrimitiveInt`
- `SimpleMath+`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `UNETLoader` ★核心
- `SetLatentNoiseMask`
- `ComfyMathExpression`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `SoundFlow_GetLength`
- `SimpleMath+`
- `SimpleMath+`
- `QZ_ResolutionPreset`
- `VAELoaderKJ`
- `ConcatTextOfUtils`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `easy cleanGpuUsed`
- `ConcatTextOfUtils`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `SolidMask`
- `CM_FloatToInt`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `ShowAnything|Mie`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `FishS2MultiSpeakerTTS`
- `LoadAudio`
- `PreviewAudio`
- `TrimAudio`
- `Audio To Text (mtb)`
- `easy showAnything`
- `LoadAudio`
- `TrimAudio`
- `Load Whisper (mtb)`
- `Audio To Text (mtb)`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `PrimitiveNode`
- `CR Text`
- `easy showAnything`
- `easy showAnything`
- `PreviewAudio`
- `TrimAudioDuration`
- `easy showAnything`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`

## 知识

覆盖率 **87%**（66/76）

**有卡**：`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`CFGGuider`、`LTXVLatentUpsampler`、`DualCLIPLoader`、`LTXVConditioning`、`VAELoaderKJ`、`Int`、`SimpleMath+`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`UNETLoader`、`SetLatentNoiseMask`、`ComfyMathExpression`、`MelBandRoFormerModelLoader`、`SoundFlow_GetLength`、`QZ_ResolutionPreset`、`ConcatTextOfUtils`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`CreateVideo`、`easy cleanGpuUsed`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`SolidMask`、`CM_FloatToInt`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`ShowAnything|Mie`、`SaveVideo`、`FishS2MultiSpeakerTTS`、`LoadAudio`、`PreviewAudio`、`TrimAudio`、`Audio To Text (mtb)`、`Load Whisper (mtb)`、`CR Text`、`TrimAudioDuration`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
