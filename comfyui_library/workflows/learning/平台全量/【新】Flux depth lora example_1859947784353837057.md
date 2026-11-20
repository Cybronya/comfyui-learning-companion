---
key: 平台全量/【新】Flux depth lora example_1859947784353837057.json
name: 【新】Flux depth lora example_1859947784353837057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【新】Flux depth lora example_1859947784353837057.json
hash: 666c710af13929b8
coverage: 1
learned_at: 2026-11-14 01:24:18
nodes: [VAEDecode, CLIPTextEncode, FluxGuidance, InstructPixToPixConditioning, SaveImage, LoraLoaderModelOnly, KSampler, DualCLIPLoader, UNETLoader, VAELoader, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 560965543380687, "steps": 20}
---

# 平台全量/【新】Flux depth lora example_1859947784353837057.json

> 来源文件 `comfyui_library/workflows/平台全量/【新】Flux depth lora example_1859947784353837057.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `560965543380687`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`FluxGuidance`、`InstructPixToPixConditioning`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
