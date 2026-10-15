---
key: 图片生成/文生图/Flux.1-Krea-Dev文生图_1951846909747122177.json
name: Flux.1-Krea-Dev文生图_1951846909747122177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图_1951846909747122177.json
hash: 1737904a764afa62
coverage: 0.6
learned_at: 2026-10-10 20:58:36
nodes: [VAELoader, DualCLIPLoader, MarkdownNote, MarkdownNote, UNETLoader, SaveImage, VAEDecode, KSampler, ConditioningZeroOut, easy showAnything, RH_Translator, CLIPTextEncode, CR SDXL Aspect Ratio, Primitive integer [Crystools], Text Multiline]
patterns: []
missing: [Primitive integer [Crystools], Text Multiline, CR SDXL Aspect Ratio]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 299977613053003, "steps": 20}
discoveries: [次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux.1-Krea-Dev文生图_1951846909747122177.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图_1951846909747122177.json`

## 结构

**节点**（15 个）：
- `VAELoader`
- `DualCLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader`
- `SaveImage`
- `VAEDecode`
- `KSampler`
- `ConditioningZeroOut`
- `easy showAnything`
- `RH_Translator`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `Primitive integer [Crystools]`
- `Text Multiline`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `299977613053003`
- `steps` = `20`

## 知识

覆盖率 **60%**（9/15）

**有卡**：`VAELoader`、`DualCLIPLoader`、`MarkdownNote`、`UNETLoader`、`SaveImage`、`VAEDecode`、`KSampler`、`ConditioningZeroOut`

**缺卡**（3）：`Primitive integer [Crystools]`、`Text Multiline`、`CR SDXL Aspect Ratio`

## 学习发现

- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
