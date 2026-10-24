---
key: 图片生成/图生图/FLUX图生图+Lora_洗图v1.0_1943306830044930049.json
name: FLUX图生图+Lora_洗图v1.0_1943306830044930049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX图生图+Lora_洗图v1.0_1943306830044930049.json
hash: a17e1bd45eaba086
coverage: 1
learned_at: 2026-10-23 10:54:51
nodes: [BasicGuider, RandomNoise, KSamplerSelect, DualCLIPLoader, UNETLoader, SamplerCustomAdvanced, SaveImage, LoraLoader, ConstrainImage|pysssss, VAELoader, VAEEncode, VAEDecode, BasicScheduler, easy imageSize, LoadImage, CLIPTextEncode]
patterns: [lora]
missing: []
parameters: {"lora_name": "manhua-000006.safetensors", "strength_clip": 1, "strength_model": 0.7000000000000001}
---

# 图片生成/图生图/FLUX图生图+Lora_洗图v1.0_1943306830044930049.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX图生图+Lora_洗图v1.0_1943306830044930049.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `LoraLoader` ★核心
- `ConstrainImage|pysssss`
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `easy imageSize`
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `manhua-000006.safetensors`
- `strength_model` = `0.7000000000000001`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`DualCLIPLoader`、`UNETLoader`、`SamplerCustomAdvanced`、`SaveImage`、`LoraLoader`、`ConstrainImage|pysssss`、`VAELoader`、`VAEEncode`、`VAEDecode`、`BasicScheduler`、`easy imageSize`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEEncode
