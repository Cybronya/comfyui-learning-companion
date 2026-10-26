---
key: 数字人/数字人/无痕视频扩图 视频编辑 LTX2.3_2042587548962263042.json
name: 无痕视频扩图 视频编辑 LTX2.3_2042587548962263042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/无痕视频扩图 视频编辑 LTX2.3_2042587548962263042.json
hash: 94621f93945028e0
coverage: 0.978261
learned_at: 2026-10-26 02:03:16
nodes: [RandomNoise, GetImageSize, CFGGuider, KSamplerSelect, ManualSigmas, CheckpointLoaderSimple, Switch image [Crystools], ResizeImageMaskNode, ResizeImageMaskNode, ResizeImageMaskNode, Color Correct (mtb), PrimitiveBoolean, Note, Int, Int, ImagePadKJ, Switch image [Crystools], Color Correct (mtb), VAEDecodeTiled, VHS_VideoCombine, SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTX2SamplingPreviewOverride, Text, Int, Int, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CLIPTextEncode, VHS_VideoInfo, LTXVConditioning, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, CM_FloatToInt, EmptyImage, PrimitiveBoolean, CLIPTextEncode, LTXVPreprocess, LTXVImgToVideoConditionOnly, LTXAddVideoICLoRAGuide, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 数字人/数字人/无痕视频扩图 视频编辑 LTX2.3_2042587548962263042.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/无痕视频扩图 视频编辑 LTX2.3_2042587548962263042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（46 个）：
- `RandomNoise`
- `GetImageSize`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `Switch image [Crystools]`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `Color Correct (mtb)`
- `PrimitiveBoolean`
- `Note`
- `Int`
- `Int`
- `ImagePadKJ`
- `Switch image [Crystools]`
- `Color Correct (mtb)`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTX2SamplingPreviewOverride`
- `Text`
- `Int`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `VHS_VideoInfo`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `CM_FloatToInt`
- `EmptyImage`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `LTXAddVideoICLoRAGuide`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **98%**（45/46）

**有卡**：`RandomNoise`、`GetImageSize`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`CheckpointLoaderSimple`、`Switch image [Crystools]`、`ResizeImageMaskNode`、`Color Correct (mtb)`、`PrimitiveBoolean`、`Int`、`ImagePadKJ`、`VAEDecodeTiled`、`VHS_VideoCombine`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTX2SamplingPreviewOverride`、`Text`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`VHS_VideoInfo`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`EmptyImage`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`LTXAddVideoICLoRAGuide`、`VHS_LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
