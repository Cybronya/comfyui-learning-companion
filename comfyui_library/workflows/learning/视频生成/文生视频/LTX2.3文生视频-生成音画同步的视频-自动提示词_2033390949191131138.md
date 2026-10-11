---
key: 视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频-自动提示词_2033390949191131138.json
name: LTX2.3文生视频-生成音画同步的视频-自动提示词_2033390949191131138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频-自动提示词_2033390949191131138.json
hash: 43eabf6709b7375d
coverage: 0.767857
learned_at: 2026-10-11 03:48:36
nodes: [MarkdownNote, LTXVScheduler, ImageScaleBy, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, RandomNoise, Reroute, KSampler, LTXVSeparateAVLatent, PrimitiveInt, LTXVCropGuides, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LatentUpscaleModelLoader, LTXVConcatAVLatent, EmptyImage, VAEDecode, GetImageSize, PrimitiveInt, PreviewAny, TextGenerateLTX2Prompt, Text, DualCLIPLoader, 数学运算_孤海, MarkdownNote, CreateVideo, VAEDecodeTiled, LTXVAudioVAEDecode, SaveVideo, PrimitiveFloat, MarkdownNote, easy anythingIndexSwitch, MultiTextConcatenate, Int, Int, Int, Int, Text, ShowText, RH_LLMAPI_Pro_Node, CR Prompt Text, CR Prompt Text, MarkdownNote, VHS_VideoCombine, CustomAddLabel]
patterns: []
missing: [easy anythingIndexSwitch, 数学运算_孤海, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 477956196758761, "steps": 4, "width": 97}
discoveries: [次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `数学运算_孤海` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频-自动提示词_2033390949191131138.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频-自动提示词_2033390949191131138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `MarkdownNote`
- `LTXVScheduler`
- `ImageScaleBy`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Reroute`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `EmptyImage`
- `VAEDecode` ★核心
- `GetImageSize`
- `PrimitiveInt`
- `PreviewAny`
- `TextGenerateLTX2Prompt`
- `Text`
- `DualCLIPLoader`
- `数学运算_孤海`
- `MarkdownNote`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SaveVideo`
- `PrimitiveFloat`
- `MarkdownNote`
- `easy anythingIndexSwitch`
- `MultiTextConcatenate`
- `Int`
- `Int`
- `Int`
- `Int`
- `Text`
- `ShowText`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `CR Prompt Text`
- `MarkdownNote`
- `VHS_VideoCombine`
- `CustomAddLabel`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `477956196758761`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **77%**（43/56）

**有卡**：`LTXVScheduler`、`ImageScaleBy`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`KSampler`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`EmptyImage`、`VAEDecode`、`GetImageSize`、`TextGenerateLTX2Prompt`、`Text`、`DualCLIPLoader`、`CreateVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SaveVideo`、`MultiTextConcatenate`、`Int`、`ShowText`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`CustomAddLabel`

**缺卡**（4）：`easy anythingIndexSwitch`、`数学运算_孤海`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `数学运算_孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
