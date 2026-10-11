---
key: 视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json
name: LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json
hash: 5338b6d56d79241d
coverage: 0.613636
learned_at: 2026-10-11 03:48:35
nodes: [CFGGuider, RandomNoise, Reroute, Reroute, CheckpointLoaderSimple, Reroute, PathchSageAttentionKJ, LTXVChunkFeedForward, Reroute, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, LTXVPreprocess, LoraLoaderModelOnly, ResizeImagesByLongerEdge, KSamplerSelect, Reroute, LTXVAudioVAELoader, LTXVImgToVideoInplace, Reroute, KSamplerSelect, EmptyImage, GetImageSize, EmptyLTXVLatentVideo, RandomNoise, SamplerCustomAdvanced, Reroute, LatentUpscaleModelLoader, Reroute, Reroute, Reroute, CFGGuider, Reroute, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, ImageScaleBy, GetImageSize, LTXVConcatAVLatent, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LTXVConditioning, VAEDecode, ManualSigmas, WhisperSTT, Reroute, INTConstant, LTXVConcatAVLatent, LTXVAudioVAEDecode, easy showAnything, PreviewAudio, Reroute, Reroute, CreateVideo, LTXVSeparateAVLatent, SaveVideo, Reroute, LTXVLatentUpsampler, Reroute, ManualSigmas, SamplerCustomAdvanced, LTXVCropGuides, Reroute, Reroute, Reroute, LTXVImgToVideoInplace, Reroute, LTXVSeparateAVLatent, Reroute, CR Prompt Text, LoadImage, LoadAudio, Bjornulf_ShowInt, easy seed, FB_Qwen3TTSVoiceClone, PreviewAudio, PainterAudioLength, CM_FloatToInt, SimpleMath+, Reroute, Reroute, Reroute, CLIPTextEncode, CLIPTextEncode, CR Text]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, CR Prompt Text, easy seed]
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `CFGGuider`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVAudioVAELoader`
- `LTXVImgToVideoInplace`
- `Reroute`
- `KSamplerSelect` ★核心
- `EmptyImage`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `LatentUpscaleModelLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `CFGGuider`
- `Reroute`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVConcatAVLatent`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVConditioning`
- `VAEDecode` ★核心
- `ManualSigmas`
- `WhisperSTT`
- `Reroute`
- `INTConstant`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `easy showAnything`
- `PreviewAudio`
- `Reroute`
- `Reroute`
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `SaveVideo`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVImgToVideoInplace`
- `Reroute`
- `LTXVSeparateAVLatent`
- `Reroute`
- `CR Prompt Text`
- `LoadImage`
- `LoadAudio`
- `Bjornulf_ShowInt`
- `easy seed`
- `FB_Qwen3TTSVoiceClone`
- `PreviewAudio`
- `PainterAudioLength`
- `CM_FloatToInt`
- `SimpleMath+`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **61%**（54/88）

**有卡**：`CFGGuider`、`RandomNoise`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`KSamplerSelect`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`EmptyImage`、`GetImageSize`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`ImageScaleBy`、`LTXVConcatAVLatent`、`ImpactInt`、`LTXVConditioning`、`VAEDecode`、`ManualSigmas`、`WhisperSTT`、`INTConstant`、`LTXVAudioVAEDecode`、`PreviewAudio`、`CreateVideo`、`LTXVSeparateAVLatent`、`SaveVideo`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LoadImage`、`LoadAudio`、`Bjornulf_ShowInt`、`FB_Qwen3TTSVoiceClone`、`PainterAudioLength`、`CM_FloatToInt`、`CLIPTextEncode`

**缺卡**（5）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`CR Prompt Text`、`easy seed`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
