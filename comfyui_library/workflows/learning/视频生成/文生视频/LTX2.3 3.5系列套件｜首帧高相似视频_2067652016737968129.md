---
key: 视频生成/文生视频/LTX2.3 3.5系列套件｜首帧高相似视频_2067652016737968129.json
name: LTX2.3 3.5系列套件｜首帧高相似视频_2067652016737968129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 3.5系列套件｜首帧高相似视频_2067652016737968129.json
hash: f05a9f06e1a36417
coverage: 0.945652
learned_at: 2026-10-11 20:21:25
nodes: [KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, RandomNoise, RandomNoise, RandomNoise, CM_FloatToInt, Image_Resize_longsize, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVConcatAVLatent, CFGGuider, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, LTXVConditioning, LTX2_NAG, VRAMReserver, Seed Everywhere, PrimitiveFloat, CLIPTextEncode, LatentUpscaleModelLoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, SimpleMath+, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVAudioVAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXFaceDetector, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, Sigmas Easing, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, LTXLikenessGuide, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LTXVAudioVAEDecode, CreateVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecodeTiled, STGGuiderAdvanced, LTXVImgToVideoConditionOnly, LoraLoaderModelOnly, SaveVideo, PrimitiveBoolean, LoadImage, PrimitiveInt, VHS_VideoCombine, Text, Text, Text, LTX2_NAG, LTX2_NAG, Text, Text, Text, Text, Text, Text, PromptRelaySmartEncode, image_scale_pixel_v2]
patterns: []
missing: [Sigmas Easing, SimpleMath+, Seed Everywhere]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `Sigmas Easing` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3 3.5系列套件｜首帧高相似视频_2067652016737968129.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 3.5系列套件｜首帧高相似视频_2067652016737968129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `CM_FloatToInt`
- `Image_Resize_longsize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `LTX2_NAG`
- `VRAMReserver`
- `Seed Everywhere`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `SimpleMath+`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXFaceDetector`
- `LTXLikenessGuide`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `Sigmas Easing`
- `LTXLikenessGuide`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `LTXLikenessGuide`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `STGGuiderAdvanced`
- `LTXVImgToVideoConditionOnly`
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `PrimitiveBoolean`
- `LoadImage`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `Text`
- `Text`
- `Text`
- `LTX2_NAG`
- `LTX2_NAG`
- `Text`
- `Text`
- `Text`
- `Text`
- `Text`
- `Text`
- `PromptRelaySmartEncode`
- `image_scale_pixel_v2`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **95%**（87/92）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`CM_FloatToInt`、`Image_Resize_longsize`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTX2_NAG`、`VRAMReserver`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LTXFaceDetector`、`LTXLikenessGuide`、`LTXLatentAnchorAware`、`LTXLikenessAnchor`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`STGGuiderAdvanced`、`PrimitiveBoolean`、`LoadImage`、`VHS_VideoCombine`、`Text`、`PromptRelaySmartEncode`、`image_scale_pixel_v2`

**缺卡**（3）：`Sigmas Easing`、`SimpleMath+`、`Seed Everywhere`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Sigmas Easing` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
