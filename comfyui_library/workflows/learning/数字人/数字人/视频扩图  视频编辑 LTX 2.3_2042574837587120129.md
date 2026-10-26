---
key: 数字人/数字人/视频扩图  视频编辑 LTX 2.3_2042574837587120129.json
name: 视频扩图  视频编辑 LTX 2.3_2042574837587120129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频扩图  视频编辑 LTX 2.3_2042574837587120129.json
hash: 12f14871d12f6437
coverage: 0.97619
learned_at: 2026-10-26 02:05:14
nodes: [LTXVConcatAVLatent, EmptyLTXVLatentVideo, CM_FloatToInt, RandomNoise, GetImageSize, EmptyImage, CFGGuider, LTXVImgToVideoConditionOnly, LTX2SamplingPreviewOverride, KSamplerSelect, ManualSigmas, LTXVCropGuides, LTXVSeparateAVLatent, LTXAVTextEncoderLoader, PrimitiveBoolean, LTXVEmptyLatentAudio, LTXVPreprocess, LTXAddVideoICLoRAGuide, LTXVAudioVAELoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, CLIPTextEncode, SamplerCustomAdvanced, Switch image [Crystools], ResizeImageMaskNode, ResizeImageMaskNode, Color Correct (mtb), CLIPTextEncode, VHS_VideoInfo, PrimitiveBoolean, VAEDecodeTiled, Color Correct (mtb), Switch image [Crystools], Note, ResizeImageMaskNode, VHS_VideoCombine, VHS_VideoCombine, ImagePadKJ, LTXVConditioning, VHS_LoadVideo, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 数字人/数字人/视频扩图  视频编辑 LTX 2.3_2042574837587120129.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频扩图  视频编辑 LTX 2.3_2042574837587120129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（42 个）：
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `RandomNoise`
- `GetImageSize`
- `EmptyImage`
- `CFGGuider`
- `LTXVImgToVideoConditionOnly`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXAVTextEncoderLoader`
- `PrimitiveBoolean`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXAddVideoICLoRAGuide`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `Switch image [Crystools]`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `Color Correct (mtb)`
- `CLIPTextEncode` ★核心
- `VHS_VideoInfo`
- `PrimitiveBoolean`
- `VAEDecodeTiled` ★核心
- `Color Correct (mtb)`
- `Switch image [Crystools]`
- `Note`
- `ResizeImageMaskNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImagePadKJ`
- `LTXVConditioning`
- `VHS_LoadVideo`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **98%**（41/42）

**有卡**：`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`RandomNoise`、`GetImageSize`、`EmptyImage`、`CFGGuider`、`LTXVImgToVideoConditionOnly`、`LTX2SamplingPreviewOverride`、`KSamplerSelect`、`ManualSigmas`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXAVTextEncoderLoader`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXAddVideoICLoRAGuide`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`Switch image [Crystools]`、`ResizeImageMaskNode`、`Color Correct (mtb)`、`VHS_VideoInfo`、`VAEDecodeTiled`、`VHS_VideoCombine`、`ImagePadKJ`、`LTXVConditioning`、`VHS_LoadVideo`、`Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
