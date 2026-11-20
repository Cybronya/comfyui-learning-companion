---
key: 平台全量/【上新】局部重绘-flux+fill+inpaint+example_1860178078814310401.json
name: 【上新】局部重绘-flux+fill+inpaint+example_1860178078814310401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【上新】局部重绘-flux+fill+inpaint+example_1860178078814310401.json
hash: 69f8645aa3222dcd
coverage: 0.933333
learned_at: 2026-11-14 01:22:44
nodes: [Label (rgthree), Label (rgthree), FluxGuidance, UNETLoader, DifferentialDiffusion, DualCLIPLoader, CLIPTextEncode, InpaintModelConditioning, KSampler, VAELoader, VAEDecode, SaveImage, LoadImage, CLIPTextEncode, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 213020970102315, "steps": 20}
---

# 平台全量/【上新】局部重绘-flux+fill+inpaint+example_1860178078814310401.json

> 来源文件 `comfyui_library/workflows/平台全量/【上新】局部重绘-flux+fill+inpaint+example_1860178078814310401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `FluxGuidance`
- `UNETLoader` ★核心
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`

## 关键参数

- `seed` = `213020970102315`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`Label (rgthree)`、`FluxGuidance`、`UNETLoader`、`DifferentialDiffusion`、`DualCLIPLoader`、`CLIPTextEncode`、`InpaintModelConditioning`、`KSampler`、`VAELoader`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
