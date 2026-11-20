---
key: 平台全量/FLUX.1 Fill 扩图 & 重绘 工作流_1863905133766836225.json
name: FLUX.1 Fill 扩图 & 重绘 工作流_1863905133766836225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.1 Fill 扩图 & 重绘 工作流_1863905133766836225.json
hash: 466e78d67f817d92
coverage: 0.923077
learned_at: 2026-11-14 00:25:01
nodes: [DifferentialDiffusion, CLIPTextEncode, KSampler, UNETLoader, DifferentialDiffusion, DualCLIPLoader, VAELoader, VAEDecode, KSampler, InpaintModelConditioning, CLIPTextEncode, LoadImage, CLIPTextEncode, PreviewImage, FluxGuidance, FluxGuidance, InpaintModelConditioning, UNETLoader, DualCLIPLoader, VAEDecode, SaveImage, CLIPTextEncode, VAELoader, LoadImage, PreviewImage, ImagePadForOutpaint]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 240271602959452, "steps": 20}
---

# 平台全量/FLUX.1 Fill 扩图 & 重绘 工作流_1863905133766836225.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.1 Fill 扩图 & 重绘 工作流_1863905133766836225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `DifferentialDiffusion`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `FluxGuidance`
- `FluxGuidance`
- `InpaintModelConditioning`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `PreviewImage`
- `ImagePadForOutpaint`

## 关键参数

- `seed` = `240271602959452`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`DifferentialDiffusion`、`CLIPTextEncode`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`InpaintModelConditioning`、`LoadImage`、`FluxGuidance`、`SaveImage`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
