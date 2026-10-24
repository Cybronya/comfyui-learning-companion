---
key: 图片生成/图生图/Flux.1-Krea-Dev文生图 nuchaku加速版_1951464859126976513.json
name: Flux.1-Krea-Dev文生图 nuchaku加速版_1951464859126976513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev文生图 nuchaku加速版_1951464859126976513.json
hash: 314cb36c299cbbf8
coverage: 0.916667
learned_at: 2026-10-23 10:58:43
nodes: [easy showAnything, RH_Translator, CLIPTextEncode, VAELoader, DualCLIPLoader, Text Multiline, VAEDecode, ConditioningZeroOut, CR SDXL Aspect Ratio, NunchakuFluxDiTLoader, KSampler, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 495292067738225, "steps": 20}
---

# 图片生成/图生图/Flux.1-Krea-Dev文生图 nuchaku加速版_1951464859126976513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev文生图 nuchaku加速版_1951464859126976513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `easy showAnything`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `Text Multiline`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CR SDXL Aspect Ratio`
- `NunchakuFluxDiTLoader`
- `KSampler` ★核心
- `SaveImage`

## 关键参数

- `seed` = `495292067738225`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`RH_Translator`、`CLIPTextEncode`、`VAELoader`、`DualCLIPLoader`、`Text Multiline`、`VAEDecode`、`ConditioningZeroOut`、`CR SDXL Aspect Ratio`、`NunchakuFluxDiTLoader`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、DualCLIPLoader、NunchakuFluxDiTLoader、CR SDXL Aspect Ratio
