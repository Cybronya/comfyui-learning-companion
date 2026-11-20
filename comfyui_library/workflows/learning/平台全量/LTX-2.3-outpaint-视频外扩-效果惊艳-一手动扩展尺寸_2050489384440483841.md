---
key: 平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳-一手动扩展尺寸_2050489384440483841.json
name: LTX-2.3-outpaint-视频外扩-效果惊艳-一手动扩展尺寸_2050489384440483841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳-一手动扩展尺寸_2050489384440483841.json
hash: 53969328fa51edd5
coverage: 0.982143
learned_at: 2026-11-14 00:37:04
nodes: [RandomNoise, EmptyImage, LTXAVTextEncoderLoader, LTXVConditioning, CLIPTextEncode, LTXVPreprocess, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, CM_FloatToInt, CFGGuider, KSamplerSelect, ManualSigmas, CLIPTextEncode, LoraLoaderModelOnly, LTXVAudioVAELoader, CheckpointLoaderSimple, LTXICLoRALoaderModelOnly, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTX2SamplingPreviewOverride, LTXVConcatAVLatent, PrimitiveBoolean, VAEDecodeTiled, Color Correct (mtb), ResizeImageMaskNode, ImagePadKJ, SimpleMath+, Int, Int, Int, Int, Text, VHS_LoadVideo, VHS_VideoInfo, Int, Int, VHS_VideoCombine, VHS_VideoCombine, ResizeImageMaskNode, ResizeImageMaskNode, GetImageSize, Switch image [Crystools], Color Correct (mtb), SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, ImageConcanate, CustomAddLabel, Switch image [Crystools], PrimitiveBoolean, Note, ShowAnything|Mie, ShowAnything|Mie, ShowAnything|Mie, ShowAnything|Mie, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳-一手动扩展尺寸_2050489384440483841.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳-一手动扩展尺寸_2050489384440483841.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（56 个）：
- `RandomNoise`
- `EmptyImage`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `LTXAddVideoICLoRAGuide`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTX2SamplingPreviewOverride`
- `LTXVConcatAVLatent`
- `PrimitiveBoolean`
- `VAEDecodeTiled` ★核心
- `Color Correct (mtb)`
- `ResizeImageMaskNode`
- `ImagePadKJ`
- `SimpleMath+`
- `Int`
- `Int`
- `Int`
- `Int`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `GetImageSize`
- `Switch image [Crystools]`
- `Color Correct (mtb)`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `ImageConcanate`
- `CustomAddLabel`
- `Switch image [Crystools]`
- `PrimitiveBoolean`
- `Note`
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **98%**（55/56）

**有卡**：`RandomNoise`、`EmptyImage`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVPreprocess`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXICLoRALoaderModelOnly`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTX2SamplingPreviewOverride`、`LTXVConcatAVLatent`、`PrimitiveBoolean`、`VAEDecodeTiled`、`Color Correct (mtb)`、`ResizeImageMaskNode`、`ImagePadKJ`、`SimpleMath+`、`Int`、`Text`、`VHS_LoadVideo`、`VHS_VideoInfo`、`VHS_VideoCombine`、`GetImageSize`、`Switch image [Crystools]`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`ImageConcanate`、`CustomAddLabel`、`ShowAnything|Mie`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo、LTXAVTextEncoderLoader
