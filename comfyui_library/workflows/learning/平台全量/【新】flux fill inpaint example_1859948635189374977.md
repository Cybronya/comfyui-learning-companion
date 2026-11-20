---
key: 平台全量/【新】flux fill inpaint example_1859948635189374977.json
name: 【新】flux fill inpaint example_1859948635189374977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【新】flux fill inpaint example_1859948635189374977.json
hash: 315a57eabf788022
coverage: 1
learned_at: 2026-11-14 01:24:19
nodes: [CLIPTextEncode, FluxGuidance, DifferentialDiffusion, VAEDecode, InpaintModelConditioning, UNETLoader, CLIPTextEncode, DualCLIPLoader, LoadImage, VAELoader, SaveImage, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 885169018105602, "steps": 20}
---

# 平台全量/【新】flux fill inpaint example_1859948635189374977.json

> 来源文件 `comfyui_library/workflows/平台全量/【新】flux fill inpaint example_1859948635189374977.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `DifferentialDiffusion`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `LoadImage`
- `VAELoader`
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `885169018105602`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`DifferentialDiffusion`、`VAEDecode`、`InpaintModelConditioning`、`UNETLoader`、`DualCLIPLoader`、`LoadImage`、`VAELoader`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
