---
key: 平台全量/ComfyUI官方示例12：Flux.1 inpainting工作流 _ ComfyUI从入门到精通_1932782711759065090.json
name: ComfyUI官方示例12：Flux.1 inpainting工作流 _ ComfyUI从入门到精通_1932782711759065090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI官方示例12：Flux.1 inpainting工作流 _ ComfyUI从入门到精通_1932782711759065090.json
hash: 66ed6698098fc5f8
coverage: 1
learned_at: 2026-11-14 00:22:26
nodes: [UNETLoader, CLIPTextEncode, CLIPTextEncode, DualCLIPLoader, VAELoader, FluxGuidance, VAEDecode, InpaintModelConditioning, SaveImage, DifferentialDiffusion, LoadImage, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 190442738686256, "steps": 20}
---

# 平台全量/ComfyUI官方示例12：Flux.1 inpainting工作流 _ ComfyUI从入门到精通_1932782711759065090.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI官方示例12：Flux.1 inpainting工作流 _ ComfyUI从入门到精通_1932782711759065090.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `FluxGuidance`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `SaveImage`
- `DifferentialDiffusion`
- `LoadImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `190442738686256`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoader`、`FluxGuidance`、`VAEDecode`、`InpaintModelConditioning`、`SaveImage`、`DifferentialDiffusion`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
