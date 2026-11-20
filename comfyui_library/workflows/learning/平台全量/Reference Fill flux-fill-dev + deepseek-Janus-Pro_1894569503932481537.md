---
key: 平台全量/Reference Fill flux-fill-dev + deepseek-Janus-Pro_1894569503932481537.json
name: Reference Fill flux-fill-dev + deepseek-Janus-Pro_1894569503932481537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Reference Fill flux-fill-dev + deepseek-Janus-Pro_1894569503932481537.json
hash: 369aa8e4f0fbe9a5
coverage: 0.863636
learned_at: 2026-11-14 00:54:48
nodes: [CLIPTextEncode, VAEDecode, KSampler, ImageResize+, FluxGuidance, InpaintModelConditioning, easy showAnything, UNETLoader, JanusModelLoader, CLIPTextEncode, PreviewImage, MaskToImage, ImagePadForOutpaint, PreviewImage, ImageRemoveAlpha+, DifferentialDiffusion, Cut By Mask, LoadImage, DualCLIPLoader, VAELoader, JanusImageUnderstanding, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1022635500471175, "steps": 20}
---

# 平台全量/Reference Fill flux-fill-dev + deepseek-Janus-Pro_1894569503932481537.json

> 来源文件 `comfyui_library/workflows/平台全量/Reference Fill flux-fill-dev + deepseek-Janus-Pro_1894569503932481537.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ImageResize+`
- `FluxGuidance`
- `InpaintModelConditioning`
- `easy showAnything`
- `UNETLoader` ★核心
- `JanusModelLoader`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `MaskToImage`
- `ImagePadForOutpaint`
- `PreviewImage`
- `ImageRemoveAlpha+`
- `DifferentialDiffusion`
- `Cut By Mask`
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`
- `JanusImageUnderstanding`
- `SaveImage`

## 关键参数

- `seed` = `1022635500471175`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`KSampler`、`ImageResize+`、`FluxGuidance`、`InpaintModelConditioning`、`UNETLoader`、`JanusModelLoader`、`MaskToImage`、`ImagePadForOutpaint`、`ImageRemoveAlpha+`、`DifferentialDiffusion`、`Cut By Mask`、`LoadImage`、`DualCLIPLoader`、`VAELoader`、`JanusImageUnderstanding`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
