---
key: 平台全量/【新】flux fill outpaint example_1859960427764649985.json
name: 【新】flux fill outpaint example_1859960427764649985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【新】flux fill outpaint example_1859960427764649985.json
hash: 509d1299b34e85c1
coverage: 1
learned_at: 2026-11-14 01:24:19
nodes: [CLIPTextEncode, FluxGuidance, DifferentialDiffusion, VAEDecode, InpaintModelConditioning, ImagePadForOutpaint, CLIPTextEncode, SaveImage, KSampler, UNETLoader, LoadImage, DualCLIPLoader, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 107189544230927, "steps": 20}
---

# 平台全量/【新】flux fill outpaint example_1859960427764649985.json

> 来源文件 `comfyui_library/workflows/平台全量/【新】flux fill outpaint example_1859960427764649985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `DifferentialDiffusion`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `ImagePadForOutpaint`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`

## 关键参数

- `seed` = `107189544230927`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`DifferentialDiffusion`、`VAEDecode`、`InpaintModelConditioning`、`ImagePadForOutpaint`、`SaveImage`、`KSampler`、`UNETLoader`、`LoadImage`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
