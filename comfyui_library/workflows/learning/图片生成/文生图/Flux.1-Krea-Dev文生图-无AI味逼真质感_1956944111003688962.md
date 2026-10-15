---
key: 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962.json
name: Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962.json
hash: 1b0c5f6f0901cc93
coverage: 0.642857
learned_at: 2026-10-10 20:58:36
nodes: [VAELoader, DualCLIPLoader, MarkdownNote, MarkdownNote, UNETLoader, VAEDecode, KSampler, ConditioningZeroOut, RH_Translator, CLIPTextEncode, CR SDXL Aspect Ratio, SaveImage, Text Multiline, easy showAnything]
patterns: []
missing: [Text Multiline, CR SDXL Aspect Ratio]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 481883940804976, "steps": 20}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962.json`

## 结构

**节点**（14 个）：
- `VAELoader`
- `DualCLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader`
- `VAEDecode`
- `KSampler`
- `ConditioningZeroOut`
- `RH_Translator`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `SaveImage`
- `Text Multiline`
- `easy showAnything`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `481883940804976`
- `steps` = `20`

## 知识

覆盖率 **64%**（9/14）

**有卡**：`VAELoader`、`DualCLIPLoader`、`MarkdownNote`、`UNETLoader`、`VAEDecode`、`KSampler`、`ConditioningZeroOut`、`RH_Translator`

**缺卡**（2）：`Text Multiline`、`CR SDXL Aspect Ratio`

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
