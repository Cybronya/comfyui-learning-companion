---
key: 视频生成/图生视频/LTX2.3-生成带货视频_2046078367643996161.json
name: LTX2.3-生成带货视频_2046078367643996161.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046078367643996161.json
hash: 801f091f20bdfcd8
coverage: 0.902439
learned_at: 2026-10-15 22:36:54
nodes: [CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, PrimitiveBoolean, PrimitiveInt, MarkdownNote, RandomNoise, RandomNoise, MarkdownNote, CR Text, LTXVConcatAVLatent, KSamplerSelect, CM_FloatToInt, INTConstant, CFGGuider, CLIPTextEncode, LTXVAudioVAEDecode, CR Text, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConditioning, GLM_Text_Chat, TextEncodeQwenImageEditPlus, VAELoader, TextEncodeQwenImageEdit, CLIPLoader, UNETLoader, ImageScale, VAEEncode, VAEDecode, SamplerCustomAdvanced, VAEDecodeTiled, ModelPatchTorchSettings, LTXVChunkFeedForward, VHS_VideoCombine, RH_LLMAPI_Pro_Node, SaveImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, PathchSageAttentionKJ, MarkdownNote, Qwen3TTSModelLoader, LoadAudio, PrimitiveFloat, PreviewAny, INTConstant, INTConstant, easy mathInt, SetLatentNoiseMask, EmptyLTXVLatentVideo, RH_LLMAPI_Pro_Node, ManualSigmas, CheckpointLoaderSimple, LTXAVTextEncoderLoader, easy mathInt, LTXVImgToVideoConditionOnly, LTXVAudioVAEEncode, SolidMask, CLIPTextEncode, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVImgToVideoConditionOnly, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleModelLoader, CR Text, LTXVAudioVAELoader, CR Text, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, PreviewAny, Qwen3TTSVoiceClone, LoadImage, LoraLoaderModelOnly, RH_GetAudioDuration, ComfyMathExpression, Fast Groups Muter (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 746385264575355, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3-生成带货视频_2046078367643996161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046078367643996161.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `MarkdownNote`
- `RandomNoise`
- `RandomNoise`
- `MarkdownNote`
- `CR Text`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CM_FloatToInt`
- `INTConstant`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CR Text`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `GLM_Text_Chat`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `TextEncodeQwenImageEdit`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ImageScale`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `VHS_VideoCombine`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `PathchSageAttentionKJ`
- `MarkdownNote`
- `Qwen3TTSModelLoader`
- `LoadAudio`
- `PrimitiveFloat`
- `PreviewAny`
- `INTConstant`
- `INTConstant`
- `easy mathInt`
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `RH_LLMAPI_Pro_Node`
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `easy mathInt`
- `LTXVImgToVideoConditionOnly`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `CLIPTextEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `CR Text`
- `LTXVAudioVAELoader`
- `CR Text`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `PreviewAny`
- `Qwen3TTSVoiceClone`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `RH_GetAudioDuration`
- `ComfyMathExpression`
- `Fast Groups Muter (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `746385264575355`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **90%**（74/82）

**有卡**：`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`PrimitiveBoolean`、`RandomNoise`、`CR Text`、`CM_FloatToInt`、`INTConstant`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVConditioning`、`GLM_Text_Chat`、`TextEncodeQwenImageEditPlus`、`VAELoader`、`TextEncodeQwenImageEdit`、`CLIPLoader`、`UNETLoader`、`ImageScale`、`VAEEncode`、`VAEDecode`、`VAEDecodeTiled`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`SaveImage`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`PathchSageAttentionKJ`、`Qwen3TTSModelLoader`、`LoadAudio`、`easy mathInt`、`SetLatentNoiseMask`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVImgToVideoConditionOnly`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXVLatentUpsampler`、`LoadImage`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`ImageScaleToTotalPixels`、`Qwen3TTSVoiceClone`、`RH_GetAudioDuration`、`ComfyMathExpression`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
