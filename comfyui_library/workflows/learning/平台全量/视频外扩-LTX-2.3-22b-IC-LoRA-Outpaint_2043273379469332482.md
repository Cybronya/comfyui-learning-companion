---
key: 平台全量/视频外扩-LTX-2.3-22b-IC-LoRA-Outpaint_2043273379469332482.json
name: 视频外扩-LTX-2.3-22b-IC-LoRA-Outpaint_2043273379469332482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频外扩-LTX-2.3-22b-IC-LoRA-Outpaint_2043273379469332482.json
hash: f82b6e9028f69172
coverage: 0.97619
learned_at: 2026-11-14 02:37:32
nodes: [RandomNoise, EmptyImage, LTXAVTextEncoderLoader, LTXVConditioning, Color Correct (mtb), ResizeImageMaskNode, VHS_LoadVideo, ResizeImageMaskNode, CLIPTextEncode, LTXVPreprocess, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, CM_FloatToInt, CFGGuider, KSamplerSelect, ManualSigmas, LTXVCropGuides, LTXVSeparateAVLatent, CLIPTextEncode, LoraLoaderModelOnly, LTXVAudioVAELoader, CheckpointLoaderSimple, LTXICLoRALoaderModelOnly, ImageConcanate, Note, PrimitiveBoolean, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTX2SamplingPreviewOverride, LTXVConcatAVLatent, Switch image [Crystools], GetImageSize, PrimitiveBoolean, VHS_VideoCombine, VAEDecodeTiled, Color Correct (mtb), VHS_VideoCombine, Switch image [Crystools], SamplerCustomAdvanced, ImagePadKJ, ResizeImageMaskNode, VHS_VideoInfo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 平台全量/视频外扩-LTX-2.3-22b-IC-LoRA-Outpaint_2043273379469332482.json

> 来源文件 `comfyui_library/workflows/平台全量/视频外扩-LTX-2.3-22b-IC-LoRA-Outpaint_2043273379469332482.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（42 个）：
- `RandomNoise`
- `EmptyImage`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `Color Correct (mtb)`
- `ResizeImageMaskNode`
- `VHS_LoadVideo`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `LTXAddVideoICLoRAGuide`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `ImageConcanate`
- `Note`
- `PrimitiveBoolean`
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTX2SamplingPreviewOverride`
- `LTXVConcatAVLatent`
- `Switch image [Crystools]`
- `GetImageSize`
- `PrimitiveBoolean`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `Color Correct (mtb)`
- `VHS_VideoCombine`
- `Switch image [Crystools]`
- `SamplerCustomAdvanced` ★核心
- `ImagePadKJ`
- `ResizeImageMaskNode`
- `VHS_VideoInfo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **98%**（41/42）

**有卡**：`RandomNoise`、`EmptyImage`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`Color Correct (mtb)`、`ResizeImageMaskNode`、`VHS_LoadVideo`、`CLIPTextEncode`、`LTXVPreprocess`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXICLoRALoaderModelOnly`、`ImageConcanate`、`PrimitiveBoolean`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTX2SamplingPreviewOverride`、`LTXVConcatAVLatent`、`Switch image [Crystools]`、`GetImageSize`、`VHS_VideoCombine`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`ImagePadKJ`、`VHS_VideoInfo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo、LTXAVTextEncoderLoader
