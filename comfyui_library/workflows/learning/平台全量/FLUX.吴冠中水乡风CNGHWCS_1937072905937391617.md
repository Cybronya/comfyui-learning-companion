---
key: 平台全量/FLUX.吴冠中水乡风CNGHWCS_1937072905937391617.json
name: FLUX.吴冠中水乡风CNGHWCS_1937072905937391617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.吴冠中水乡风CNGHWCS_1937072905937391617.json
hash: 31e13470d44ff25f
coverage: 0.842105
learned_at: 2026-11-14 00:25:14
nodes: [BasicGuider, SamplerCustomAdvanced, KSamplerSelect, VAEDecode, SaveImage, PreviewImage, RandomNoise, TextCombinerTwo, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, FluxResolutionNode, ShowText|pysssss, DualCLIPLoader, EmptyLatentImage, VAELoader, JjkText, RH_Translator, LoraLoader]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "flux1-dev-fp8.safetensors", "height": 1280, "lora_name": "FLUX.吴冠中水乡风CNGHWCS_v1.0.safetensors", "strength_clip": 1, "strength_model": 1.0000000000000002, "width": 1024}
---

# 平台全量/FLUX.吴冠中水乡风CNGHWCS_1937072905937391617.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.吴冠中水乡风CNGHWCS_1937072905937391617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `RandomNoise`
- `TextCombinerTwo`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `FluxResolutionNode`
- `ShowText|pysssss`
- `DualCLIPLoader`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `JjkText`
- `RH_Translator`
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `flux1-dev-fp8.safetensors`
- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `lora_name` = `FLUX.吴冠中水乡风CNGHWCS_v1.0.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`BasicGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`VAEDecode`、`SaveImage`、`RandomNoise`、`TextCombinerTwo`、`BasicScheduler`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`FluxResolutionNode`、`DualCLIPLoader`、`EmptyLatentImage`、`VAELoader`、`RH_Translator`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
