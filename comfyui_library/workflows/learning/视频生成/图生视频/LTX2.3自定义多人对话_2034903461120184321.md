---
key: 视频生成/图生视频/LTX2.3自定义多人对话_2034903461120184321.json
name: LTX2.3自定义多人对话_2034903461120184321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3自定义多人对话_2034903461120184321.json
hash: 3e4fbb69a767a897
coverage: 0.769231
learned_at: 2026-10-15 22:35:46
nodes: [LTXVConcatAVLatent, KSamplerSelect, CFGGuider, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, PrimitiveFloat, PrimitiveInt, MarkdownNote, RandomNoise, RandomNoise, LTXVImgToVideoConditionOnly, CM_FloatToInt, INTConstant, INTConstant, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVPreprocess, CheckpointLoaderSimple, ManualSigmas, EmptyLTXVLatentVideo, SolidMask, SetNode, PreviewAudio, SimpleMath+, Audio Duration (mtb), TrimAudioDuration, SetNode, LatentUpscaleModelLoader, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVAudioVAELoader, SetNode, VHS_VideoCombine, SamplerCustomAdvanced, LTXVImgToVideoConditionOnly, LTX2SamplingPreviewOverride, VAELoader, LTXVSeparateAVLatent, LTXVLatentUpsampler, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, TDQwen3TTSDefineSpeaker, TDQwen3TTSDefineSpeaker, CR Text, PrimitiveBoolean, ImageScaleToTotalPixels, GetImageSize+, easy showAnything, CR Text, MarkdownNote, SimpleMath+, GetNode, easy showAnything, SetNode, INTConstant, ComfySwitchNode, LTXVEmptyLatentAudio, SetNode, GetNode, GetNode, ComfySwitchNode, GetNode, LoadAudio, Fast Groups Muter (rgthree), LoraLoaderModelOnly, Fast Groups Muter (rgthree), LoadAudio, LoadAudio, LoadImage, llama_cpp_model_loader, TDQwen3TTSMultiDialog, Fast Groups Muter (rgthree), llama_cpp_instruct_adv, MelBandRoFormerModelLoader, MelBandRoFormerSampler, TDQwen3TTSModelLoader, LTXAVTextEncoderLoader, SaveAudio, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3自定义多人对话_2034903461120184321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034903461120184321.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PrimitiveFloat`
- `PrimitiveInt`
- `MarkdownNote`
- `RandomNoise`
- `RandomNoise`
- `LTXVImgToVideoConditionOnly`
- `CM_FloatToInt`
- `INTConstant`
- `INTConstant`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `CheckpointLoaderSimple` ★核心
- `ManualSigmas`
- `EmptyLTXVLatentVideo`
- `SolidMask`
- `SetNode`
- `PreviewAudio`
- `SimpleMath+`
- `Audio Duration (mtb)`
- `TrimAudioDuration`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVAudioVAELoader`
- `SetNode`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTX2SamplingPreviewOverride`
- `VAELoader`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `TDQwen3TTSDefineSpeaker`
- `TDQwen3TTSDefineSpeaker`
- `CR Text`
- `PrimitiveBoolean`
- `ImageScaleToTotalPixels`
- `GetImageSize+`
- `easy showAnything`
- `CR Text`
- `MarkdownNote`
- `SimpleMath+`
- `GetNode`
- `easy showAnything`
- `SetNode`
- `INTConstant`
- `ComfySwitchNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `LoadAudio`
- `Fast Groups Muter (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Muter (rgthree)`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `llama_cpp_model_loader`
- `TDQwen3TTSMultiDialog`
- `Fast Groups Muter (rgthree)`
- `llama_cpp_instruct_adv`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `TDQwen3TTSModelLoader`
- `LTXAVTextEncoderLoader`
- `SaveAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（70/91）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`RandomNoise`、`LTXVImgToVideoConditionOnly`、`CM_FloatToInt`、`INTConstant`、`LTXVPreprocess`、`CheckpointLoaderSimple`、`EmptyLTXVLatentVideo`、`SolidMask`、`PreviewAudio`、`SimpleMath+`、`Audio Duration (mtb)`、`TrimAudioDuration`、`LatentUpscaleModelLoader`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVAudioVAELoader`、`VHS_VideoCombine`、`LTX2SamplingPreviewOverride`、`VAELoader`、`LTXVLatentUpsampler`、`easy cleanGpuUsed`、`TDQwen3TTSDefineSpeaker`、`CR Text`、`PrimitiveBoolean`、`ImageScaleToTotalPixels`、`GetImageSize+`、`LTXVEmptyLatentAudio`、`LoadAudio`、`LoraLoaderModelOnly`、`LoadImage`、`llama_cpp_model_loader`、`TDQwen3TTSMultiDialog`、`llama_cpp_instruct_adv`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`TDQwen3TTSModelLoader`、`LTXAVTextEncoderLoader`、`SaveAudio`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
