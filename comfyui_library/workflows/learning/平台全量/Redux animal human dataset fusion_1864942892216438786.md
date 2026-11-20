---
key: 平台全量/Redux animal human dataset fusion_1864942892216438786.json
name: Redux animal human dataset fusion_1864942892216438786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Redux animal human dataset fusion_1864942892216438786.json
hash: 77e968498c70451c
coverage: 1
learned_at: 2026-11-14 00:54:42
nodes: [FluxGuidance, StyleModelApply, StyleModelApply, CLIPVisionEncode, CLIPVisionEncode, LoadImage, KSampler, VAELoader, CLIPTextEncode, CLIPTextEncodeFlux, VAEDecode, SaveImage, CLIPVisionLoader, StyleModelLoader, UNETLoader, DualCLIPLoader, CR Aspect Ratio, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "ddim_uniform", "seed": 705101691670441, "steps": 25}
---

# 平台全量/Redux animal human dataset fusion_1864942892216438786.json

> 来源文件 `comfyui_library/workflows/平台全量/Redux animal human dataset fusion_1864942892216438786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `FluxGuidance`
- `StyleModelApply`
- `StyleModelApply`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoadImage`
- `KSampler` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CR Aspect Ratio`
- `LoadImage`

## 关键参数

- `seed` = `705101691670441`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `ddim_uniform`
- `denoise` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`FluxGuidance`、`StyleModelApply`、`CLIPVisionEncode`、`LoadImage`、`KSampler`、`VAELoader`、`CLIPTextEncode`、`CLIPTextEncodeFlux`、`VAEDecode`、`SaveImage`、`CLIPVisionLoader`、`StyleModelLoader`、`UNETLoader`、`DualCLIPLoader`、`CR Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、CLIPTextEncodeFlux
