---
key: 平台全量/ComfyUI官方示例15：Flux.1 Depth工作流 _ ComfyUI从入门到精通_1932799950428196865.json
name: ComfyUI官方示例15：Flux.1 Depth工作流 _ ComfyUI从入门到精通_1932799950428196865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI官方示例15：Flux.1 Depth工作流 _ ComfyUI从入门到精通_1932799950428196865.json
hash: 6ac66093aacb9081
coverage: 1
learned_at: 2026-11-14 00:22:27
nodes: [CLIPTextEncode, FluxGuidance, InstructPixToPixConditioning, DualCLIPLoader, VAELoader, VAEDecode, SaveImage, LoadImage, CLIPTextEncode, KSampler, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 291478812695228, "steps": 20}
---

# 平台全量/ComfyUI官方示例15：Flux.1 Depth工作流 _ ComfyUI从入门到精通_1932799950428196865.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI官方示例15：Flux.1 Depth工作流 _ ComfyUI从入门到精通_1932799950428196865.json`

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
- `LoadImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `291478812695228`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`InstructPixToPixConditioning`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`KSampler`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
