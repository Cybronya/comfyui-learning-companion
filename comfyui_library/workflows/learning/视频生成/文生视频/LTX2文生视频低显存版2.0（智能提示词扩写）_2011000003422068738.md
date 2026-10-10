---
key: 视频生成/文生视频/LTX2文生视频低显存版2.0（智能提示词扩写）_2011000003422068738.json
name: LTX2文生视频低显存版2.0（智能提示词扩写）_2011000003422068738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2文生视频低显存版2.0（智能提示词扩写）_2011000003422068738.json
hash: 4c1e849a29557197
coverage: 0.735849
learned_at: 2026-10-11 03:07:10
nodes: [CFGGuider, KSamplerSelect, RandomNoise, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, ManualSigmas, LTXVConditioning, CLIPTextEncode, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, RandomNoise, KSamplerSelect, CFGGuider, ImageScaleBy, JoinStrings, VAEDecodeTiled, GetImageSize, PrimitiveInt, PrimitiveFloat, PrimitiveInt, CLIPTextEncode, LTXVAudioVAEDecode, easy cleanGpuUsed, CheckpointLoaderSimple, VHS_VideoCombine, JoinStrings, Text Multiline, ShowText|pysssss, Fast Groups Muter (rgthree), TextInput_, Text Multiline, MarkdownNote, MarkdownNote, Any Switch (rgthree), RH_LLMAPI_Pro_Node, ShowText|pysssss, TextInput_, easy showAnything, EmptyImage, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, Qwen3_VQA]
patterns: []
missing: [CR Text, Text Multiline, Text Multiline, easy cleanGpuUsed]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2文生视频低显存版2.0（智能提示词扩写）_2011000003422068738.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2文生视频低显存版2.0（智能提示词扩写）_2011000003422068738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（53 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ImageScaleBy`
- `JoinStrings`
- `VAEDecodeTiled` ★核心
- `GetImageSize`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `easy cleanGpuUsed`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `JoinStrings`
- `Text Multiline`
- `ShowText|pysssss`
- `Fast Groups Muter (rgthree)`
- `TextInput_`
- `Text Multiline`
- `MarkdownNote`
- `MarkdownNote`
- `Any Switch (rgthree)`
- `RH_LLMAPI_Pro_Node`
- `ShowText|pysssss`
- `TextInput_`
- `easy showAnything`
- `EmptyImage`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `Qwen3_VQA`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **74%**（39/53）

**有卡**：`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVScheduler`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`ImageScaleBy`、`JoinStrings`、`VAEDecodeTiled`、`GetImageSize`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`TextInput_`、`RH_LLMAPI_Pro_Node`、`EmptyImage`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`Qwen3_VQA`

**缺卡**（4）：`CR Text`、`Text Multiline`、`Text Multiline`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
