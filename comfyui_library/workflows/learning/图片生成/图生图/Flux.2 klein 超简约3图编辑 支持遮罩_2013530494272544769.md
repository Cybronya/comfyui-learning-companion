---
key: 图片生成/图生图/Flux.2 klein 超简约3图编辑 支持遮罩_2013530494272544769.json
name: Flux.2 klein 超简约3图编辑 支持遮罩_2013530494272544769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 klein 超简约3图编辑 支持遮罩_2013530494272544769.json
hash: 83fe703d72a19295
coverage: 0.395833
learned_at: 2026-10-23 10:58:48
nodes: [GetNode, GetNode, GetNode, GetNode, Image Comparer (rgthree), GetNode, GetNode, ToBinaryMask, SetNode, GetNode, LoadImage, SetNode, PlaySound|pysssss, SetNode, GetNode, GetNode, Any Switch (rgthree), RH_LLMAPI_NODE, Display Any (rgthree), SetNode, Fast Groups Bypasser (rgthree), Mask Fill Holes, GetNode, GetNode, CR Text, SetNode, SetNode, SetNode, UNETLoader, SetNode, GetNode, SetNode, SetNode, Int, Int, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), VAEDecode, KSampler, Reroute, GetNode, GetNode, LoadImage, VAELoader, CLIPLoader, PainterFluxImageEdit, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 927159346593895, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux.2 klein 超简约3图编辑 支持遮罩_2013530494272544769.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 klein 超简约3图编辑 支持遮罩_2013530494272544769.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `ToBinaryMask`
- `SetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `PlaySound|pysssss`
- `SetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `RH_LLMAPI_NODE`
- `Display Any (rgthree)`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Mask Fill Holes`
- `GetNode`
- `GetNode`
- `CR Text`
- `SetNode`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Reroute`
- `GetNode`
- `GetNode`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `PainterFluxImageEdit`
- `CR Text`

## 关键参数

- `seed` = `927159346593895`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **40%**（19/48）

**有卡**：`ToBinaryMask`、`LoadImage`、`PlaySound|pysssss`、`RH_LLMAPI_NODE`、`Display Any (rgthree)`、`Mask Fill Holes`、`CR Text`、`UNETLoader`、`Int`、`SaveImage`、`VAEDecode`、`KSampler`、`VAELoader`、`CLIPLoader`、`PainterFluxImageEdit`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、LoadImage、PainterFluxImageEdit、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
