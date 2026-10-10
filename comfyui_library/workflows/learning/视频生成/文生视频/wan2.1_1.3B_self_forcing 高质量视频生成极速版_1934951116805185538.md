---
key: 视频生成/文生视频/wan2.1_1.3B_self_forcing 高质量视频生成极速版_1934951116805185538.json
name: wan2.1_1.3B_self_forcing 高质量视频生成极速版_1934951116805185538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1_1.3B_self_forcing 高质量视频生成极速版_1934951116805185538.json
hash: 02eb7556298db1bf
coverage: 0.714286
learned_at: 2026-10-10 23:09:31
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, ModelSamplingSD3, CFGZeroStar, PatchModelPatcherOrder, UNETLoader, VAELoader, INTConstant, INTConstant, CLIPLoader, PathchSageAttentionKJ, Note, EmptyHunyuanLatentVideo, easy batchAnything, easy forLoopEnd, easy showAnything, easy forLoopStart, Text Load Line From File, FloatConstant, Video_Upscale_With_Model, RIFE VFI, VHS_VideoCombine, Int, VHS_VideoCombine, Text Multiline, INTConstant, KSampler]
patterns: []
missing: [RIFE VFI, Text Load Line From File, Text Multiline, easy batchAnything, easy forLoopEnd, easy forLoopStart]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 636347855998451, "steps": 8}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.1_1.3B_self_forcing 高质量视频生成极速版_1934951116805185538.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.1_1.3B_self_forcing 高质量视频生成极速版_1934951116805185538.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CFGZeroStar`
- `PatchModelPatcherOrder`
- `UNETLoader` ★核心
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `Note`
- `EmptyHunyuanLatentVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy showAnything`
- `easy forLoopStart`
- `Text Load Line From File`
- `FloatConstant`
- `Video_Upscale_With_Model`
- `RIFE VFI`
- `VHS_VideoCombine`
- `Int`
- `VHS_VideoCombine`
- `Text Multiline`
- `INTConstant`
- `KSampler` ★核心

## 关键参数

- `seed` = `636347855998451`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（20/28）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingSD3`、`CFGZeroStar`、`PatchModelPatcherOrder`、`UNETLoader`、`VAELoader`、`INTConstant`、`CLIPLoader`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`FloatConstant`、`Video_Upscale_With_Model`、`VHS_VideoCombine`、`Int`、`KSampler`

**缺卡**（6）：`RIFE VFI`、`Text Load Line From File`、`Text Multiline`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStar、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
