---
key: 平台全量/Y-kontext_inpaint_workflow_1943974335478632449.json
name: Y-kontext_inpaint_workflow_1943974335478632449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Y-kontext_inpaint_workflow_1943974335478632449.json
hash: 286e14da8fce8ab9
coverage: 0.928571
learned_at: 2026-11-14 01:07:43
nodes: [FluxKontextImageScale, Kontext Inpainting Conditioning, DualCLIPLoader, VAELoader, KSampler, FluxGuidance, VAEDecode, PreviewImage, SaveImage, CLIPTextEncode, LoadImage, CLIPTextEncode, UNETLoader, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 556730054549297, "steps": 28}
---

# 平台全量/Y-kontext_inpaint_workflow_1943974335478632449.json

> 来源文件 `comfyui_library/workflows/平台全量/Y-kontext_inpaint_workflow_1943974335478632449.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `FluxKontextImageScale`
- `Kontext Inpainting Conditioning`
- `DualCLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `FluxGuidance`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `556730054549297`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`FluxKontextImageScale`、`Kontext Inpainting Conditioning`、`DualCLIPLoader`、`VAELoader`、`KSampler`、`FluxGuidance`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
