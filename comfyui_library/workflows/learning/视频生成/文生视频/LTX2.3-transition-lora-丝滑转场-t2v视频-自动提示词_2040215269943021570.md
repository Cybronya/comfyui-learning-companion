---
key: 视频生成/文生视频/LTX2.3-transition-lora-丝滑转场-t2v视频-自动提示词_2040215269943021570.json
name: LTX2.3-transition-lora-丝滑转场-t2v视频-自动提示词_2040215269943021570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-transition-lora-丝滑转场-t2v视频-自动提示词_2040215269943021570.json
hash: 4b33e56a670dd6e4
coverage: 0.849057
learned_at: 2026-10-11 19:49:37
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, MarkdownNote, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, PrimitiveBoolean, CFGGuider, CLIPTextEncode, LTXVConditioning, ManualSigmas, CLIPTextEncode, LTX2_NAG, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, llama_cpp_model_loader, SimpleMath+, CR Text Concatenate, JjkText, RH_Utils, JWFloat, CR Text Concatenate, TTResolutionSelector, llama_cpp_parameters, Int, CreateVideo, CustomAddLabel, VAEDecodeTiled, SaveVideo, ShowAnything|Mie, llama_cpp_instruct_adv, PrimitiveStringMultiline]
patterns: []
missing: [CR Text Concatenate, CR Text Concatenate, ShowAnything|Mie, SimpleMath+]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3-transition-lora-丝滑转场-t2v视频-自动提示词_2040215269943021570.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-transition-lora-丝滑转场-t2v视频-自动提示词_2040215269943021570.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（53 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `PrimitiveBoolean`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `llama_cpp_model_loader`
- `SimpleMath+`
- `CR Text Concatenate`
- `JjkText`
- `RH_Utils`
- `JWFloat`
- `CR Text Concatenate`
- `TTResolutionSelector`
- `llama_cpp_parameters`
- `Int`
- `CreateVideo`
- `CustomAddLabel`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `ShowAnything|Mie`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（45/53）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`ComfyMathExpression`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTXVConditioning`、`LTX2_NAG`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`llama_cpp_model_loader`、`RH_Utils`、`JWFloat`、`TTResolutionSelector`、`llama_cpp_parameters`、`Int`、`CreateVideo`、`CustomAddLabel`、`VAEDecodeTiled`、`SaveVideo`、`llama_cpp_instruct_adv`

**缺卡**（4）：`CR Text Concatenate`、`CR Text Concatenate`、`ShowAnything|Mie`、`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
