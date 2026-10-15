---
key: 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1986360219359969282.json
name: Flux.1-Krea-Dev文生图-无AI味逼真质感_1986360219359969282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1986360219359969282.json
hash: 9941bd03eea58fd4
coverage: 0.692308
learned_at: 2026-10-10 20:58:36
nodes: [VAELoader, DualCLIPLoader, UNETLoader, VAEDecode, ConditioningZeroOut, easy showAnything, RH_Translator, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, Primitive integer [Crystools], Text Multiline, SaveImage]
patterns: []
missing: [Primitive integer [Crystools], Text Multiline, CR SDXL Aspect Ratio]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 145247182581619, "steps": 20}
discoveries: [次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1986360219359969282.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1986360219359969282.json`

## 结构

**节点**（13 个）：
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader`
- `VAEDecode`
- `ConditioningZeroOut`
- `easy showAnything`
- `RH_Translator`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `145247182581619`
- `steps` = `20`

## 知识

覆盖率 **69%**（9/13）

**有卡**：`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`VAEDecode`、`ConditioningZeroOut`、`easy showAnything`、`RH_Translator`、`CLIPTextEncode`、`CR SDXL Aspect Ratio`

**缺卡**（3）：`Primitive integer [Crystools]`、`Text Multiline`、`CR SDXL Aspect Ratio`

## 学习发现

- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
