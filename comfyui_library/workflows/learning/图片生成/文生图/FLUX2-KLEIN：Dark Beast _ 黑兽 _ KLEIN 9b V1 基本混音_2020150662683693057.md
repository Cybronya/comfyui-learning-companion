---
key: 图片生成/文生图/FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1 基本混音_2020150662683693057.json
name: FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1 基本混音_2020150662683693057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1 基本混音_2020150662683693057.json
hash: e90d9e7c82cbc671
coverage: 0.972222
learned_at: 2026-10-19 22:29:38
nodes: [VAEDecode, CLIPLoader, VAELoader, LayerUtility: PurgeVRAM, UNETLoader, ConditioningZeroOut, KSampler, EmptyFlux2LatentImage, MuyeSizeSelector, CLIPTextEncode, ProcessString, Text Concatenate, JDCN_StringToList, CR Text, CR Prompt Text, SaveImage, easy showAnything, LoadImage, RH_LLMAPI_Pro_Node, CR Prompt Text, CR Text Replace, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 611208274298738, "steps": 10}
---

# 图片生成/文生图/FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1 基本混音_2020150662683693057.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1 基本混音_2020150662683693057.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `EmptyFlux2LatentImage`
- `MuyeSizeSelector`
- `CLIPTextEncode` ★核心
- `ProcessString`
- `Text Concatenate`
- `JDCN_StringToList`
- `CR Text`
- `CR Prompt Text`
- `SaveImage`
- `easy showAnything`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `CR Text Replace`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `611208274298738`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`VAEDecode`、`CLIPLoader`、`VAELoader`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`ConditioningZeroOut`、`KSampler`、`EmptyFlux2LatentImage`、`MuyeSizeSelector`、`CLIPTextEncode`、`ProcessString`、`Text Concatenate`、`JDCN_StringToList`、`CR Text`、`CR Prompt Text`、`SaveImage`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`CR Text Replace`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
