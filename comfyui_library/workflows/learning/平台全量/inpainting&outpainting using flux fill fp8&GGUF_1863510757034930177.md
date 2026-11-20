---
key: 平台全量/inpainting&outpainting using flux fill fp8&GGUF_1863510757034930177.json
name: inpainting&outpainting using flux fill fp8&GGUF_1863510757034930177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/inpainting&outpainting using flux fill fp8&GGUF_1863510757034930177.json
hash: 8e56de1096b43acb
coverage: 0.7
learned_at: 2026-11-14 01:12:51
nodes: [Reroute, Reroute, Reroute, Reroute, ImagePadForOutpaint, KSampler, SaveImage, PreviewImage, VAEDecode, Reroute, CLIPTextEncode, FluxGuidance, InpaintModelConditioning, CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, UNETLoader, LoraLoader, LoadImage, VAELoader]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "FLUX.1-Turbo-Alpha.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 604706789025929, "steps": 8, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/inpainting&outpainting using flux fill fp8&GGUF_1863510757034930177.json

> 来源文件 `comfyui_library/workflows/平台全量/inpainting&outpainting using flux fill fp8&GGUF_1863510757034930177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImagePadForOutpaint`
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoadImage`
- `VAELoader`

**识别到的模式**：lora

## 关键参数

- `seed` = `604706789025929`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `lora_name` = `FLUX.1-Turbo-Alpha.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **70%**（14/20）

**有卡**：`ImagePadForOutpaint`、`KSampler`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`FluxGuidance`、`InpaintModelConditioning`、`DifferentialDiffusion`、`DualCLIPLoader`、`UNETLoader`、`LoraLoader`、`LoadImage`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
