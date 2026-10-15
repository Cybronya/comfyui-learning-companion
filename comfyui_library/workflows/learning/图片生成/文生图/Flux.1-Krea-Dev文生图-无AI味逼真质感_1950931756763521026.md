---
key: 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1950931756763521026.json
name: Flux.1-Krea-Dev文生图-无AI味逼真质感_1950931756763521026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1950931756763521026.json
hash: af03e4982a3887cf
coverage: 0.8
learned_at: 2026-10-15 22:26:25
nodes: [VAELoader, DualCLIPLoader, MarkdownNote, MarkdownNote, UNETLoader, SaveImage, VAEDecode, KSampler, ConditioningZeroOut, easy showAnything, RH_Translator, CLIPTextEncode, Text Multiline, CR SDXL Aspect Ratio, Primitive integer [Crystools]]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 299977613053003, "steps": 20}
---

# 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1950931756763521026.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1950931756763521026.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `VAELoader`
- `DualCLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `easy showAnything`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `CR SDXL Aspect Ratio`
- `Primitive integer [Crystools]`

## 关键参数

- `seed` = `299977613053003`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`SaveImage`、`VAEDecode`、`KSampler`、`ConditioningZeroOut`、`RH_Translator`、`CLIPTextEncode`、`Text Multiline`、`CR SDXL Aspect Ratio`、`Primitive integer [Crystools]`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、DualCLIPLoader、CR SDXL Aspect Ratio
