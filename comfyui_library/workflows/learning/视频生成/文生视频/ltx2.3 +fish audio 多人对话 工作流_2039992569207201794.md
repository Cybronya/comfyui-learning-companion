---
key: 视频生成/文生视频/ltx2.3 +fish audio 多人对话 工作流_2039992569207201794.json
name: ltx2.3 +fish audio 多人对话 工作流_2039992569207201794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3 +fish audio 多人对话 工作流_2039992569207201794.json
hash: 5a6fbb5f7173e3e4
coverage: 0.75
learned_at: 2026-10-11 19:49:44
nodes: [ManualSigmas, SamplerCustomAdvanced, RandomNoise, RandomNoise, KSamplerSelect, LatentUpscaleModelLoader, CFGGuider, CFGGuider, Reroute, SamplerCustomAdvanced, LTXVLatentUpsampler, SetNode, DualCLIPLoader, LTXVConditioning, VAELoaderKJ, ManualSigmas, Int, PrimitiveInt, SimpleMath+, MelBandRoFormerSampler, LTXVAudioVAEEncode, CLIPTextEncode, LTXVAudioVAEDecode, UNETLoader, SetLatentNoiseMask, ComfyMathExpression, MelBandRoFormerModelLoader, GetNode, SoundFlow_GetLength, SimpleMath+, SimpleMath+, QZ_ResolutionPreset, VAELoaderKJ, ConcatTextOfUtils, LTXVSeparateAVLatent, VAEDecodeTiled, CreateVideo, easy cleanGpuUsed, ConcatTextOfUtils, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVCropGuides, KSamplerSelect, LTXVConcatAVLatent, LTXVConcatAVLatent, SolidMask, CM_FloatToInt, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, ImageResizeKJv2, RH_LLMAPI_Pro_Node, LoadImage, ShowAnything|Mie, CLIPTextEncode, SaveVideo, FishS2MultiSpeakerTTS, LoadAudio, PreviewAudio, TrimAudio, Audio To Text (mtb), easy showAnything, LoadAudio, TrimAudio, Load Whisper (mtb), Audio To Text (mtb), MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveNode, CR Text, easy showAnything, easy showAnything, PreviewAudio, TrimAudioDuration, easy showAnything, easy showAnything, RH_LLMAPI_Pro_Node]
patterns: []
missing: [Audio To Text (mtb), Audio To Text (mtb), CR Text, Load Whisper (mtb), ShowAnything|Mie, SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed]
discoveries: [次要节点 `Audio To Text (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Audio To Text (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Load Whisper (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
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

覆盖率 **75%**（57/76）

**有卡**：`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`CFGGuider`、`LTXVLatentUpsampler`、`DualCLIPLoader`、`LTXVConditioning`、`VAELoaderKJ`、`Int`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`UNETLoader`、`SetLatentNoiseMask`、`ComfyMathExpression`、`MelBandRoFormerModelLoader`、`SoundFlow_GetLength`、`QZ_ResolutionPreset`、`ConcatTextOfUtils`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`CreateVideo`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`SolidMask`、`CM_FloatToInt`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`SaveVideo`、`FishS2MultiSpeakerTTS`、`LoadAudio`、`PreviewAudio`、`TrimAudio`、`TrimAudioDuration`

**缺卡**（9）：`Audio To Text (mtb)`、`Audio To Text (mtb)`、`CR Text`、`Load Whisper (mtb)`、`ShowAnything|Mie`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Audio To Text (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Audio To Text (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Load Whisper (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
