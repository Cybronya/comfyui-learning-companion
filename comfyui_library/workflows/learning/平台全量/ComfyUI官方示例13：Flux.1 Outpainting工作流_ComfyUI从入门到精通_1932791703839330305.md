---
key: 平台全量/ComfyUI官方示例13：Flux.1 Outpainting工作流_ComfyUI从入门到精通_1932791703839330305.json
name: ComfyUI官方示例13：Flux.1 Outpainting工作流_ComfyUI从入门到精通_1932791703839330305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI官方示例13：Flux.1 Outpainting工作流_ComfyUI从入门到精通_1932791703839330305.json
hash: ac71f59628e9c94e
coverage: 1
learned_at: 2026-11-14 00:22:26
nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, VAEDecode, InpaintModelConditioning, SaveImage, DifferentialDiffusion, VAELoader, UNETLoader, ImagePadForOutpaint, CLIPTextEncode, LoadImage, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 804330990739588, "steps": 20}
---

# 平台全量/ComfyUI官方示例13：Flux.1 Outpainting工作流_ComfyUI从入门到精通_1932791703839330305.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI官方示例13：Flux.1 Outpainting工作流_ComfyUI从入门到精通_1932791703839330305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `FluxGuidance`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `SaveImage`
- `DifferentialDiffusion`
- `VAELoader`
- `UNETLoader` ★核心
- `ImagePadForOutpaint`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `804330990739588`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPTextEncode`、`DualCLIPLoader`、`FluxGuidance`、`VAEDecode`、`InpaintModelConditioning`、`SaveImage`、`DifferentialDiffusion`、`VAELoader`、`UNETLoader`、`ImagePadForOutpaint`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
