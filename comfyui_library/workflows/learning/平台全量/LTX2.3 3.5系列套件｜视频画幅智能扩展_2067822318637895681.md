---
key: 平台全量/LTX2.3 3.5系列套件｜视频画幅智能扩展_2067822318637895681.json
name: LTX2.3 3.5系列套件｜视频画幅智能扩展_2067822318637895681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3 3.5系列套件｜视频画幅智能扩展_2067822318637895681.json
hash: 10ab693baa7e0235
coverage: 0.960784
learned_at: 2026-11-14 00:37:27
nodes: [LTXVConditioning, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVCropGuides, LTXVSeparateAVLatent, CM_FloatToInt, CFGGuider, RandomNoise, GemmaAPITextEncode, PrimitiveString, GemmaAPITextEncode, ManualSigmas, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVPreprocess, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVAudioVAEDecode, ImageConcanate, Switch image [Crystools], Color Correct (mtb), VAEDecodeTiled, CLIPTextEncode, LTXVAudioVAELoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, VHS_VideoCombine, GetImageSize, ImageResizeKJv2, Switch image [Crystools], Note, VHS_VideoCombine, LTXICLoRALoaderModelOnly, LTXVImgToVideoConditionOnly, LoadImage, PrimitiveBoolean, Int, VHS_VideoInfo, Int, Int, GetImageSize+, PrimitiveBoolean, ResizeAndPadImage, image_scale_pixel_v2, LoraLoaderModelOnly, image_scale_pixel_v2, VHS_LoadVideo, Color Correct (mtb), CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 平台全量/LTX2.3 3.5系列套件｜视频画幅智能扩展_2067822318637895681.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3 3.5系列套件｜视频画幅智能扩展_2067822318637895681.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（51 个）：
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `CM_FloatToInt`
- `CFGGuider`
- `RandomNoise`
- `GemmaAPITextEncode`
- `PrimitiveString`
- `GemmaAPITextEncode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVPreprocess`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ImageConcanate`
- `Switch image [Crystools]`
- `Color Correct (mtb)`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `GetImageSize`
- `ImageResizeKJv2`
- `Switch image [Crystools]`
- `Note`
- `VHS_VideoCombine`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVImgToVideoConditionOnly`
- `LoadImage`
- `PrimitiveBoolean`
- `Int`
- `VHS_VideoInfo`
- `Int`
- `Int`
- `GetImageSize+`
- `PrimitiveBoolean`
- `ResizeAndPadImage`
- `image_scale_pixel_v2`
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`
- `VHS_LoadVideo`
- `Color Correct (mtb)`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors`

## 知识

覆盖率 **96%**（49/51）

**有卡**：`LTXVConditioning`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`CM_FloatToInt`、`CFGGuider`、`RandomNoise`、`GemmaAPITextEncode`、`ManualSigmas`、`KSamplerSelect`、`LTXAddVideoICLoRAGuide`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`ImageConcanate`、`Switch image [Crystools]`、`Color Correct (mtb)`、`VAEDecodeTiled`、`CLIPTextEncode`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`GetImageSize`、`ImageResizeKJv2`、`LTXICLoRALoaderModelOnly`、`LTXVImgToVideoConditionOnly`、`LoadImage`、`PrimitiveBoolean`、`Int`、`VHS_VideoInfo`、`GetImageSize+`、`ResizeAndPadImage`、`image_scale_pixel_v2`、`VHS_LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
