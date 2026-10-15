---
key: 图片生成/文生图/Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201.json
name: Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201.json
hash: cc92df0d49f87ce3
coverage: 0.916667
learned_at: 2026-10-15 22:26:25
nodes: [VAELoader, DualCLIPLoader, UNETLoader, VAEDecode, KSampler, easy showAnything, RH_Translator, CR SDXL Aspect Ratio, CLIPTextEncode, ConditioningZeroOut, SaveImage, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 675365315847874, "steps": 20}
---

# 图片生成/文生图/Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `easy showAnything`
- `RH_Translator`
- `CR SDXL Aspect Ratio`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `Text Multiline`

## 关键参数

- `seed` = `675365315847874`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`VAEDecode`、`KSampler`、`RH_Translator`、`CR SDXL Aspect Ratio`、`CLIPTextEncode`、`ConditioningZeroOut`、`SaveImage`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、DualCLIPLoader、CR SDXL Aspect Ratio
