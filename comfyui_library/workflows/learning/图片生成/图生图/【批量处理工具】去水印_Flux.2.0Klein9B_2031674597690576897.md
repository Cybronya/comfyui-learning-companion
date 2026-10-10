---
key: 图片生成/图生图/【批量处理工具】去水印_Flux.2.0Klein9B_2031674597690576897.json
name: 【批量处理工具】去水印_Flux.2.0Klein9B_2031674597690576897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【批量处理工具】去水印_Flux.2.0Klein9B_2031674597690576897.json
hash: 798183356fb13bf5
coverage: 0.681818
learned_at: 2026-10-10 20:48:13
nodes: [RHBatchImages:, easy imageCount, SaveImage, HAIGC_SaveImagesToZip, RHExtractImage, easy forLoopStart, easy batchAnything, ConditioningZeroOut, easy showAnything, scale, TextInput_, JjkText, ReferenceLatent, VAEEncode, UNETLoader, KSampler, VAEDecode, CLIPLoader, CLIPTextEncode, VAELoader, RHUploadZip, easy forLoopEnd]
patterns: []
missing: [RHBatchImages:, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageCount]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 718533911977687, "steps": 4}
discoveries: [次要节点 `RHBatchImages:` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【批量处理工具】去水印_Flux.2.0Klein9B_2031674597690576897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【批量处理工具】去水印_Flux.2.0Klein9B_2031674597690576897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `RHBatchImages:`
- `easy imageCount`
- `SaveImage`
- `HAIGC_SaveImagesToZip`
- `RHExtractImage`
- `easy forLoopStart`
- `easy batchAnything`
- `ConditioningZeroOut`
- `easy showAnything`
- `scale`
- `TextInput_`
- `JjkText`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `RHUploadZip`
- `easy forLoopEnd`

## 关键参数

- `seed` = `718533911977687`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`SaveImage`、`HAIGC_SaveImagesToZip`、`RHExtractImage`、`ConditioningZeroOut`、`scale`、`TextInput_`、`ReferenceLatent`、`VAEEncode`、`UNETLoader`、`KSampler`、`VAEDecode`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`RHUploadZip`

**缺卡**（5）：`RHBatchImages:`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy imageCount`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `RHBatchImages:` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
