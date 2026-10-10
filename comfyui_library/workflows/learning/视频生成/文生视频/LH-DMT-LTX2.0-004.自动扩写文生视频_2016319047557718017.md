---
key: 视频生成/文生视频/LH-DMT-LTX2.0-004.自动扩写文生视频_2016319047557718017.json
name: LH-DMT-LTX2.0-004.自动扩写文生视频_2016319047557718017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LH-DMT-LTX2.0-004.自动扩写文生视频_2016319047557718017.json
hash: 740b72b7114684c4
coverage: 0.829787
learned_at: 2026-10-11 03:07:08
nodes: [Note, Note, CR Text, CR Text, JoinStrings, Qwen3_VQA, CLIPTextEncode, INTConstant, INTConstant, INTConstant, EmptyImage, SomethingToString, ShowText|pysssss, PrimitiveInt, PrimitiveInt, PrimitiveFloat, LatentUpscaleModelLoader, CLIPTextEncode, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVConditioning, RandomNoise, LTXVScheduler, KSamplerSelect, LTXVSeparateAVLatent, CFGGuider, LTXVCropGuides, LTXVAudioVAEDecode, LTXVLatentUpsampler, RandomNoise, CFGGuider, SamplerCustomAdvanced, ManualSigmas, SamplerCustomAdvanced, KSamplerSelect, LTXVConcatAVLatent, VAEDecodeTiled, LTXVSeparateAVLatent, VHS_VideoCombine, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: [CR Text, CR Text]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LH-DMT-LTX2.0-004.自动扩写文生视频_2016319047557718017.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LH-DMT-LTX2.0-004.自动扩写文生视频_2016319047557718017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `Note`
- `Note`
- `CR Text`
- `CR Text`
- `JoinStrings`
- `Qwen3_VQA`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `EmptyImage`
- `SomethingToString`
- `ShowText|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `RandomNoise`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **83%**（39/47）

**有卡**：`JoinStrings`、`Qwen3_VQA`、`CLIPTextEncode`、`INTConstant`、`EmptyImage`、`SomethingToString`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVConditioning`、`RandomNoise`、`LTXVScheduler`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`CFGGuider`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`ManualSigmas`、`VAEDecodeTiled`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`

**缺卡**（2）：`CR Text`、`CR Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
