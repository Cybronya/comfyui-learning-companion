---
key: 图片生成/文生图/Flux.2  基础文生图，自动优化提示词_1995785114007244801.json
name: Flux.2  基础文生图，自动优化提示词_1995785114007244801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2  基础文生图，自动优化提示词_1995785114007244801.json
hash: df081b5af49f7243
coverage: 0.85
learned_at: 2026-10-19 21:32:32
nodes: [CLIPLoader, VAELoader, Anything Everywhere, KSampler, ConditioningZeroOut, ReferenceLatent, CLIPTextEncode, LayerUtility: PurgeVRAM V2, SaveImage, UnetLoaderGGUF, PathchSageAttentionKJ, ModelPatchTorchSettings, RH_Translator, VAEDecode, PreviewAny, easy ifElse, PrimitiveBoolean, Text Multiline, Qwen2.5, QwenImageLatentAspectRatio]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 220437662497415, "steps": 20}
---

# 图片生成/文生图/Flux.2  基础文生图，自动优化提示词_1995785114007244801.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2  基础文生图，自动优化提示词_1995785114007244801.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `RH_Translator`
- `VAEDecode` ★核心
- `PreviewAny`
- `easy ifElse`
- `PrimitiveBoolean`
- `Text Multiline`
- `Qwen2.5`
- `QwenImageLatentAspectRatio`

## 关键参数

- `seed` = `220437662497415`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`ConditioningZeroOut`、`ReferenceLatent`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`UnetLoaderGGUF`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`RH_Translator`、`VAEDecode`、`PrimitiveBoolean`、`Text Multiline`、`Qwen2.5`、`QwenImageLatentAspectRatio`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、ReferenceLatent、QwenImageLatentAspectRatio
