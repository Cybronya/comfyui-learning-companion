---
key: 视频生成/文生视频/LTX 2.3  文生视频工作流_2048223868342505474.json
name: LTX 2.3  文生视频工作流_2048223868342505474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3  文生视频工作流_2048223868342505474.json
hash: 4e15d1766643c1a0
coverage: 0.48913
learned_at: 2026-10-15 22:44:31
nodes: [SetNode, SetNode, SetNode, GetNode, SetNode, Seed (rgthree), SetNode, GetNode, GetNode, SetNode, SimpleCalculatorKJ, GetNode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, SetNode, VAEDecodeTiled, KSamplerSelect, GetNode, VAEDecodeTiled, GetNode, SimpleMath+, ManualSigmas, VHS_VideoCombine, SamplerCustom, SamplerCustom, LTXVConditioning, EmptyLTXVLatentVideo, GetNode, GetNode, LTXVLatentUpsampler, LTXVConcatAVLatent, ManualSigmas, GetNode, GetNode, GetNode, GetNode, SetNode, INTConstant, GetNode, SimpleMath+, SimpleMath+, LTXVConcatAVLatent, SetNode, SetNode, GetNode, ShowText|pysssss, SetNode, LTXVSeparateAVLatent, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, LTXVSeparateAVLatent, SetNode, LTXVAudioVAEDecode, VHS_VideoCombine, TextInput_, RH_LLMAPI_Pro_Node, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, SetNode, LatentUpscaleModelLoader, SetNode, DualCLIPLoader, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, LTX2SamplingPreviewOverride, GetNode, GetNode, LTX2SamplingPreviewOverride, GetNode, MarkdownNote, DiffusionModelLoaderKJ, TextInput_, INTConstant, INTConstant, CLIPTextEncode, CLIPTextEncode, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/文生视频/LTX 2.3  文生视频工作流_2048223868342505474.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3  文生视频工作流_2048223868342505474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（92 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Seed (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SimpleMath+`
- `ManualSigmas`
- `VHS_VideoCombine`
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `ShowText|pysssss`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `TextInput_`
- `RH_LLMAPI_Pro_Node`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `MarkdownNote`
- `DiffusionModelLoaderKJ`
- `TextInput_`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **49%**（45/92）

**有卡**：`Seed (rgthree)`、`SimpleCalculatorKJ`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`VAEDecodeTiled`、`SimpleMath+`、`ManualSigmas`、`VHS_VideoCombine`、`SamplerCustom`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`INTConstant`、`LTXVAudioVAEDecode`、`TextInput_`、`RH_LLMAPI_Pro_Node`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LTX2SamplingPreviewOverride`、`DiffusionModelLoaderKJ`、`CLIPTextEncode`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、KSamplerSelect、SamplerCustom、LTXVLatentUpsampler、Seed (rgthree)、LTXVConcatAVLatent、LTXVSeparateAVLatent
