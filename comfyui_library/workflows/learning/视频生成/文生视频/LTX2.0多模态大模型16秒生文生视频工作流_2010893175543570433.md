---
key: 视频生成/文生视频/LTX2.0多模态大模型16秒生文生视频工作流_2010893175543570433.json
name: LTX2.0多模态大模型16秒生文生视频工作流_2010893175543570433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0多模态大模型16秒生文生视频工作流_2010893175543570433.json
hash: 6c8caf93d169b9b6
coverage: 0.551282
learned_at: 2026-10-11 03:07:10
nodes: [ManualSigmas, KSamplerSelect, EmptyImage, LTXVEmptyLatentAudio, ImageScaleBy, GetImageSize, KSamplerSelect, LTXVSeparateAVLatent, Reroute, LTXVAudioVAELoader, Reroute, PrimitiveInt, Reroute, Reroute, Reroute, Reroute, Reroute, CheckpointLoaderSimple, CFGGuider, Reroute, Reroute, Reroute, LTXVConditioning, Reroute, Reroute, EmptyLTXVLatentVideo, Reroute, Reroute, Reroute, LTXVCropGuides, RandomNoise, RandomNoise, LTXVLatentUpsampler, LTXVAudioVAEDecode, LTXVSeparateAVLatent, Reroute, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, MarkdownNote, Reroute, LTXVConcatAVLatent, Reroute, Reroute, SamplerCustomAdvanced, LTXVScheduler, LatentUpscaleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, MarkdownNote, MarkdownNote, Note, PrimitiveFloat, PrimitiveInt, Int, LTXAVTextEncoderLoader, Note, MemoryCleaner, JoinStrings, ShowText|pysssss, VAEDecodeTiled, easy showAnything, MemoryCleaner, CLIPTextEncode, Fast Groups Bypasser (rgthree), Int, Int, Qwen3_VQA, JoinStrings, TextInput_, VHS_VideoCombine, TextInput_]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.0多模态大模型16秒生文生视频工作流_2010893175543570433.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0多模态大模型16秒生文生视频工作流_2010893175543570433.json`

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
- `Reroute`
- `LTXVAudioVAELoader`
- `Reroute`
- `PrimitiveInt`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVConditioning`
- `Reroute`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVCropGuides`
- `RandomNoise`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `Reroute`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `Reroute`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVScheduler`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `PrimitiveFloat`
- `PrimitiveInt`
- `Int`
- `LTXAVTextEncoderLoader`
- `Note`
- `MemoryCleaner`
- `JoinStrings`
- `ShowText|pysssss`
- `VAEDecodeTiled` ★核心
- `easy showAnything`
- `MemoryCleaner`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `Int`
- `Qwen3_VQA`
- `JoinStrings`
- `TextInput_`
- `VHS_VideoCombine`
- `TextInput_`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **55%**（43/78）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`EmptyImage`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`GetImageSize`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`CFGGuider`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`RandomNoise`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVScheduler`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`Int`、`LTXAVTextEncoderLoader`、`MemoryCleaner`、`JoinStrings`、`VAEDecodeTiled`、`Qwen3_VQA`、`TextInput_`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
