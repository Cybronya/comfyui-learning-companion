---
key: 平台全量/ComfyUI官方示例14：Flux.1 Canny工作流_ComfyUI从入门到精通_1932795013279748097.json
name: ComfyUI官方示例14：Flux.1 Canny工作流_ComfyUI从入门到精通_1932795013279748097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI官方示例14：Flux.1 Canny工作流_ComfyUI从入门到精通_1932795013279748097.json
hash: 99cc8b52271374e5
coverage: 1
learned_at: 2026-11-14 00:22:27
nodes: [CLIPTextEncode, FluxGuidance, InstructPixToPixConditioning, DualCLIPLoader, VAELoader, VAEDecode, SaveImage, CLIPTextEncode, UNETLoader, LoadImage, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 618818168519502, "steps": 20}
---

# 平台全量/ComfyUI官方示例14：Flux.1 Canny工作流_ComfyUI从入门到精通_1932795013279748097.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI官方示例14：Flux.1 Canny工作流_ComfyUI从入门到精通_1932795013279748097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `618818168519502`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`InstructPixToPixConditioning`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`UNETLoader`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
