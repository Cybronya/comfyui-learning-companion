---
key: 平台全量/Ltx2.5视频自动反推生视频_2089709955942273025.json
name: Ltx2.5视频自动反推生视频_2089709955942273025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Ltx2.5视频自动反推生视频_2089709955942273025.json
hash: bd0a5f769e50e801
coverage: 0.878788
learned_at: 2026-11-14 00:39:30
nodes: [CLIPTextEncode, LTXVConcatAVLatent, LTXVDualCFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, SaveVideo, ComfyMathExpression, LTXVConditioning, CreateVideo, LTXVAudioVAEDecode, MarkdownNote, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, llama_cpp_model_loader, llama_cpp_parameters, PrimitiveInt, ResolutionSelector, VHS_LoadVideo, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, UNETLoader, VAELoader, VAELoader, CLIPLoader, PreviewAny, PreviewAny, llama_cpp_instruct_adv]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 平台全量/Ltx2.5视频自动反推生视频_2089709955942273025.json

> 来源文件 `comfyui_library/workflows/平台全量/Ltx2.5视频自动反推生视频_2089709955942273025.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（33 个）：
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `ComfyMathExpression`
- `LTXVConditioning`
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PrimitiveInt`
- `ResolutionSelector`
- `VHS_LoadVideo`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `PreviewAny`
- `PreviewAny`
- `llama_cpp_instruct_adv`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVDualCFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SaveVideo`、`ComfyMathExpression`、`LTXVConditioning`、`CreateVideo`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ResolutionSelector`、`VHS_LoadVideo`、`llama_cpp_instruct_adv`、`UNETLoader`、`VAELoader`、`CLIPLoader`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、ResolutionSelector、UNETLoader、KSamplerSelect、LTXVDualCFGGuider、SamplerCustomAdvanced
