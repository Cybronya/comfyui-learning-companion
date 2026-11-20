---
key: 平台全量/LTX2.3-视频二创语音重绘_2054183330219864066.json
name: LTX2.3-视频二创语音重绘_2054183330219864066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3-视频二创语音重绘_2054183330219864066.json
hash: 9466649c91b64dc5
coverage: 0.882353
learned_at: 2026-11-14 00:38:15
nodes: [VAELoaderKJ, DualCLIPLoader, UNETLoader, VHS_VideoCombine, SimpleMath+, LTXICLoRALoaderModelOnly, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, VAELoaderKJ, LTXVAudioVAEEncode, RandomNoise, KSamplerSelect, CFGGuider, LTXVConditioning, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, LTXAddVideoICLoRAGuide, LTX2SamplingPreviewOverride, SamplerCustomAdvanced, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, ImageResizeKJv2, EmptyLTXVLatentVideo, GetImageSize, ComfyMathExpression, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.3-视频二创语音重绘_2054183330219864066.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3-视频二创语音重绘_2054183330219864066.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（34 个）：
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `SimpleMath+`
- `LTXICLoRALoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAELoaderKJ`
- `LTXVAudioVAEEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVConditioning`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTX2SamplingPreviewOverride`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ComfyMathExpression`
- `VHS_LoadVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`VHS_VideoCombine`、`SimpleMath+`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAEEncode`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`LTXVConditioning`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`LTXAddVideoICLoRAGuide`、`LTX2SamplingPreviewOverride`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`GetImageSize`、`ComfyMathExpression`、`VHS_LoadVideo`

**用到的条目**：CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo、LTXVAudioVAEDecode、LTXVAudioVAEEncode
