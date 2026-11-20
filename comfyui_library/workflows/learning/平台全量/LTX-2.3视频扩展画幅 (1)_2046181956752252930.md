---
key: 平台全量/LTX-2.3视频扩展画幅 (1)_2046181956752252930.json
name: LTX-2.3视频扩展画幅 (1)_2046181956752252930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.3视频扩展画幅 (1)_2046181956752252930.json
hash: 442381e1089fd42e
coverage: 1
learned_at: 2026-11-14 00:37:11
nodes: [LTXVConcatAVLatent, EmptyLTXVLatentVideo, CM_FloatToInt, RandomNoise, CFGGuider, LTXVImgToVideoConditionOnly, LTXAddVideoICLoRAGuide, LTX2SamplingPreviewOverride, KSamplerSelect, ManualSigmas, LTXVCropGuides, LTXVSeparateAVLatent, LTXAVTextEncoderLoader, SamplerCustomAdvanced, LTXVEmptyLatentAudio, Color Correct (mtb), VAEDecodeTiled, LoraLoaderModelOnly, VHS_VideoInfo, ResizeImageMaskNode, ResizeImageMaskNode, Color Correct (mtb), Switch image [Crystools], GetImageSize, CLIPTextEncode, LTXVConditioning, LTXVPreprocess, Switch image [Crystools], ResizeImageMaskNode, PrimitiveBoolean, EmptyImage, PrimitiveBoolean, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, CheckpointLoaderSimple, ImagePadKJ, CLIPTextEncode, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 平台全量/LTX-2.3视频扩展画幅 (1)_2046181956752252930.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.3视频扩展画幅 (1)_2046181956752252930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（39 个）：
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `RandomNoise`
- `CFGGuider`
- `LTXVImgToVideoConditionOnly`
- `LTXAddVideoICLoRAGuide`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `Color Correct (mtb)`
- `VAEDecodeTiled` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoInfo`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `Color Correct (mtb)`
- `Switch image [Crystools]`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVPreprocess`
- `Switch image [Crystools]`
- `ResizeImageMaskNode`
- `PrimitiveBoolean`
- `EmptyImage`
- `PrimitiveBoolean`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `ImagePadKJ`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`RandomNoise`、`CFGGuider`、`LTXVImgToVideoConditionOnly`、`LTXAddVideoICLoRAGuide`、`LTX2SamplingPreviewOverride`、`KSamplerSelect`、`ManualSigmas`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXAVTextEncoderLoader`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`Color Correct (mtb)`、`VAEDecodeTiled`、`LoraLoaderModelOnly`、`VHS_VideoInfo`、`ResizeImageMaskNode`、`Switch image [Crystools]`、`GetImageSize`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVPreprocess`、`PrimitiveBoolean`、`EmptyImage`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`ImagePadKJ`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo、LTXAVTextEncoderLoader
