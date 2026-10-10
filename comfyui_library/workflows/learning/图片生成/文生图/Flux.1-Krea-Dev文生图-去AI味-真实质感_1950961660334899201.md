---
key: Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201.json
name: Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201.json
hash: cc92df0d49f87ce3
coverage: 0.75
learned_at: 2026-10-10 20:58:36
nodes: [VAELoader, DualCLIPLoader, UNETLoader, VAEDecode, KSampler, easy showAnything, RH_Translator, CR SDXL Aspect Ratio, CLIPTextEncode, ConditioningZeroOut, SaveImage, Text Multiline]
patterns: []
missing: [Text Multiline, CR SDXL Aspect Ratio]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 675365315847874, "steps": 20}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201.json

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

覆盖率 **75%**（9/12）

**有卡**：`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`VAEDecode`、`KSampler`、`RH_Translator`、`CLIPTextEncode`、`ConditioningZeroOut`、`SaveImage`

**缺卡**（2）：`Text Multiline`、`CR SDXL Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、DualCLIPLoader、SaveImage

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
