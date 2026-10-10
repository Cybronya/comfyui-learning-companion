---
key: 视频生成/文生视频/LTX2.0文生视频gguf版本_2012499867683262466.json
name: LTX2.0文生视频gguf版本_2012499867683262466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频gguf版本_2012499867683262466.json
hash: 4be3d045dc9f8841
coverage: 0.576923
learned_at: 2026-10-11 03:07:10
nodes: [ManualSigmas, KSamplerSelect, EmptyImage, LTXVEmptyLatentAudio, ImageScaleBy, GetImageSize, KSamplerSelect, LTXVSeparateAVLatent, PrimitiveInt, Reroute, Reroute, Reroute, Reroute, CFGGuider, Reroute, Reroute, LTXVConditioning, Reroute, Reroute, EmptyLTXVLatentVideo, Reroute, LTXVCropGuides, RandomNoise, RandomNoise, LTXVAudioVAEDecode, LTXVSeparateAVLatent, Reroute, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, JoinStrings, Reroute, Reroute, Reroute, Reroute, MarkdownNote, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVScheduler, PrimitiveInt, PrimitiveFloat, VHS_VideoCombine, Note, Note, CLIPTextEncode, CLIPTextEncode, Reroute, Reroute, Reroute, INTConstant, INTConstant, INTConstant, Reroute, LTXVLatentUpsampler, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, MarkdownNote, MarkdownNote, ShowText|pysssss, PurgeVRAM_UTK, VAELoader, VAELoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleModelLoader, TextInput_, VAEDecodeTiled, PurgeVRAM_UTK, UnetLoaderGGUF, Qwen3_VQA, DualCLIPLoader, DualCLIPLoaderGGUF, TextInput_, SomethingToString]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.0文生视频gguf版本_2012499867683262466.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频gguf版本_2012499867683262466.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（78 个）：
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `EmptyImage`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CFGGuider`
- `Reroute`
- `Reroute`
- `LTXVConditioning`
- `Reroute`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `LTXVCropGuides`
- `RandomNoise`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `Reroute`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `JoinStrings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVScheduler`
- `PrimitiveInt`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `MarkdownNote`
- `ShowText|pysssss`
- `PurgeVRAM_UTK`
- `VAELoader`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `TextInput_`
- `VAEDecodeTiled` ★核心
- `PurgeVRAM_UTK`
- `UnetLoaderGGUF` ★核心
- `Qwen3_VQA`
- `DualCLIPLoader`
- `DualCLIPLoaderGGUF`
- `TextInput_`
- `SomethingToString`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（45/78）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`EmptyImage`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`GetImageSize`、`LTXVSeparateAVLatent`、`CFGGuider`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`RandomNoise`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`JoinStrings`、`LTXVScheduler`、`VHS_VideoCombine`、`CLIPTextEncode`、`INTConstant`、`LTXVLatentUpsampler`、`PurgeVRAM_UTK`、`VAELoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`TextInput_`、`VAEDecodeTiled`、`UnetLoaderGGUF`、`Qwen3_VQA`、`DualCLIPLoader`、`DualCLIPLoaderGGUF`、`SomethingToString`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
