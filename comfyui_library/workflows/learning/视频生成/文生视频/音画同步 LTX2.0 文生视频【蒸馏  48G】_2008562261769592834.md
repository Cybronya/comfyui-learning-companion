---
key: 视频生成/文生视频/音画同步 LTX2.0 文生视频【蒸馏  48G】_2008562261769592834.json
name: 音画同步 LTX2.0 文生视频【蒸馏  48G】_2008562261769592834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/音画同步 LTX2.0 文生视频【蒸馏  48G】_2008562261769592834.json
hash: 5218415ff6079a42
coverage: 0.772727
learned_at: 2026-10-11 03:07:16
nodes: [ManualSigmas, CFGGuider, KSamplerSelect, LatentUpscaleModelLoader, SamplerCustomAdvanced, EmptyImage, LTXAVTextEncoderLoader, LTXVAudioVAELoader, CLIPTextEncode, LTXVConditioning, CFGGuider, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetImageSize, ImageScaleBy, PrimitiveInt, PrimitiveFloat, PrimitiveInt, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVConcatAVLatent, LTXVLatentUpsampler, LoraLoaderModelOnly, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, SimpleMath+, Primitive integer [Crystools], Primitive integer [Crystools], VHS_VideoCombine, SimpleMath+, VHS_VideoCombine, LoadImage, RandomNoise, Primitive integer [Crystools], Primitive integer [Crystools], RandomNoise, CheckpointLoaderSimple, PrimitiveStringMultiline]
patterns: []
missing: [Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], SimpleMath+, SimpleMath+]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-distilled-fp8.safetensors", "height": 25, "width": 121}
discoveries: [次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/音画同步 LTX2.0 文生视频【蒸馏  48G】_2008562261769592834.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/音画同步 LTX2.0 文生视频【蒸馏  48G】_2008562261769592834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（44 个）：
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `EmptyImage`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetImageSize`
- `ImageScaleBy`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `SimpleMath+`
- `VHS_VideoCombine`
- `LoadImage`
- `RandomNoise`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **77%**（34/44）

**有卡**：`ManualSigmas`、`CFGGuider`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`EmptyImage`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVConcatAVLatent`、`GetImageSize`、`ImageScaleBy`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`LoadImage`、`RandomNoise`、`CheckpointLoaderSimple`

**缺卡**（6）：`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`SimpleMath+`、`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
