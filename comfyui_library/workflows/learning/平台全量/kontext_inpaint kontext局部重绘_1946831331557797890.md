---
key: 平台全量/kontext_inpaint kontext局部重绘_1946831331557797890.json
name: kontext_inpaint kontext局部重绘_1946831331557797890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/kontext_inpaint kontext局部重绘_1946831331557797890.json
hash: 415ec80944f49234
coverage: 0.916667
learned_at: 2026-11-14 01:13:40
nodes: [DualCLIPLoader, UNETLoader, VAELoader, VAEDecode, SaveImage, KSampler, CLIPTextEncode, FluxKontextImageScale, FluxGuidance, Kontext Inpainting Conditioning, PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 535363184584601, "steps": 28}
---

# 平台全量/kontext_inpaint kontext局部重绘_1946831331557797890.json

> 来源文件 `comfyui_library/workflows/平台全量/kontext_inpaint kontext局部重绘_1946831331557797890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `FluxKontextImageScale`
- `FluxGuidance`
- `Kontext Inpainting Conditioning`
- `PreviewImage`
- `LoadImage`

## 关键参数

- `seed` = `535363184584601`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`KSampler`、`CLIPTextEncode`、`FluxKontextImageScale`、`FluxGuidance`、`Kontext Inpainting Conditioning`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
