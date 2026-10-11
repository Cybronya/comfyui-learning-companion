---
key: 视频生成/文生视频/ltx2.3 多人对话工作流-宠物对话_2039689143625719809.json
name: ltx2.3 多人对话工作流-宠物对话_2039689143625719809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3 多人对话工作流-宠物对话_2039689143625719809.json
hash: b076c3c6c80faecf
coverage: 0.791667
learned_at: 2026-10-11 19:49:44
nodes: [ManualSigmas, SamplerCustomAdvanced, RandomNoise, RandomNoise, KSamplerSelect, LatentUpscaleModelLoader, CFGGuider, CFGGuider, Reroute, SamplerCustomAdvanced, LTXVLatentUpsampler, SetNode, DualCLIPLoader, LTXVConditioning, VAELoaderKJ, ManualSigmas, Int, PrimitiveInt, SimpleMath+, MelBandRoFormerSampler, LTXVAudioVAEEncode, CLIPTextEncode, LTXVAudioVAEDecode, UNETLoader, SetLatentNoiseMask, ComfyMathExpression, MelBandRoFormerModelLoader, PrimitiveNode, ImageResizeKJv2, GetNode, SoundFlow_GetLength, TrimAudioDuration, SimpleMath+, SimpleMath+, QZ_ResolutionPreset, CM_FloatToInt, PreviewAudio, FB_Qwen3TTSDialogueInference, PreviewAudio, VAELoaderKJ, ShowAnything|Mie, ConcatTextOfUtils, LTXVSeparateAVLatent, VAEDecodeTiled, CreateVideo, easy cleanGpuUsed, ConcatTextOfUtils, RH_LLMAPI_Pro_Node, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVCropGuides, KSamplerSelect, LTXVConcatAVLatent, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceClonePrompt, CLIPTextEncode, LTXVConcatAVLatent, easy showAnything, FB_Qwen3TTSVoiceDesign, FB_Qwen3TTSVoiceDesign, easy showAnything, FB_Qwen3TTSRoleBank, LoadImage, ttN text, PreviewAudio, SolidMask, CR Text, easy showAnything, RH_LLMAPI_Pro_Node, SaveVideo]
patterns: []
missing: [CR Text, ShowAnything|Mie, SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed, ttN text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `ttN text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/ltx2.3 多人对话工作流-宠物对话_2039689143625719809.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3 多人对话工作流-宠物对话_2039689143625719809.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
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
- `PrimitiveNode`
- `ImageResizeKJv2`
- `GetNode`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `SimpleMath+`
- `SimpleMath+`
- `QZ_ResolutionPreset`
- `CM_FloatToInt`
- `PreviewAudio`
- `FB_Qwen3TTSDialogueInference`
- `PreviewAudio`
- `VAELoaderKJ`
- `ShowAnything|Mie`
- `ConcatTextOfUtils`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `easy cleanGpuUsed`
- `ConcatTextOfUtils`
- `RH_LLMAPI_Pro_Node`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceClonePrompt`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `easy showAnything`
- `FB_Qwen3TTSVoiceDesign`
- `FB_Qwen3TTSVoiceDesign`
- `easy showAnything`
- `FB_Qwen3TTSRoleBank`
- `LoadImage`
- `ttN text`
- `PreviewAudio`
- `SolidMask`
- `CR Text`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `SaveVideo`

## 知识

覆盖率 **79%**（57/72）

**有卡**：`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`CFGGuider`、`LTXVLatentUpsampler`、`DualCLIPLoader`、`LTXVConditioning`、`VAELoaderKJ`、`Int`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`UNETLoader`、`SetLatentNoiseMask`、`ComfyMathExpression`、`MelBandRoFormerModelLoader`、`ImageResizeKJv2`、`SoundFlow_GetLength`、`TrimAudioDuration`、`QZ_ResolutionPreset`、`CM_FloatToInt`、`PreviewAudio`、`FB_Qwen3TTSDialogueInference`、`ConcatTextOfUtils`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`CreateVideo`、`RH_LLMAPI_Pro_Node`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`FB_Qwen3TTSVoiceClonePrompt`、`FB_Qwen3TTSVoiceDesign`、`FB_Qwen3TTSRoleBank`、`LoadImage`、`SolidMask`、`SaveVideo`

**缺卡**（7）：`CR Text`、`ShowAnything|Mie`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`、`ttN text`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN text` 知识库中没有该节点类型的任何知识
