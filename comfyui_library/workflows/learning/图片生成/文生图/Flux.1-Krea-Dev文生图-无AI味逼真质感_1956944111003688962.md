---
key: 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962.json
name: Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962.json
hash: 1b0c5f6f0901cc93
coverage: 0.642857
learned_at: 2026-10-07 23:25:18
nodes: [VAELoader, DualCLIPLoader, MarkdownNote, MarkdownNote, UNETLoader, VAEDecode, KSampler, ConditioningZeroOut, RH_Translator, CLIPTextEncode, CR SDXL Aspect Ratio, SaveImage, Text Multiline, easy showAnything]
patterns: []
missing: [Text Multiline, CR SDXL Aspect Ratio]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 481883940804976, "steps": 20}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1956944111003688962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAELoader`
- `DualCLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `CR SDXL Aspect Ratio`
- `SaveImage`
- `Text Multiline`
- `easy showAnything`

## 关键参数

- `seed` = `481883940804976`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（9/14）

**有卡**：`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`VAEDecode`、`KSampler`、`ConditioningZeroOut`、`RH_Translator`、`CLIPTextEncode`、`SaveImage`

**缺卡**（2）：`Text Multiline`、`CR SDXL Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、DualCLIPLoader、SaveImage

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
