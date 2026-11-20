---
key: 平台全量/Wan2.2视频修复工作流高清，4k画质，电影质感_2096031326502739970.json
name: Wan2.2视频修复工作流高清，4k画质，电影质感_2096031326502739970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2视频修复工作流高清，4k画质，电影质感_2096031326502739970.json
hash: f239a1ed07cbdc05
coverage: 0.636364
learned_at: 2026-11-14 01:06:24
nodes: [CLIPTextEncode, VAEEncode, UNETLoader, CLIPLoader, VAELoader, RHHiddenNodes, ModelSamplingSD3, easy showAnything, MuyeTextEditOutput, easy promptConcat, CLIPTextEncode, MuyeTextEditOutput, 孤海注释, VAEDecode, VHS_VideoInfo, KSampler, SetNode, PrimitiveFloat, 孤海注释, GetNode, ComfyNumberConvert, GetNode, ImageScaleToMaxDimension, VHS_VideoCombine, GetNode, GetNode, SetNode, Int, SetNode, Int, ComfyMathExpression, VHS_LoadVideo, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 980315471200131, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2视频修复工作流高清，4k画质，电影质感_2096031326502739970.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2视频修复工作流高清，4k画质，电影质感_2096031326502739970.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `RHHiddenNodes`
- `ModelSamplingSD3`
- `easy showAnything`
- `MuyeTextEditOutput`
- `easy promptConcat`
- `CLIPTextEncode` ★核心
- `MuyeTextEditOutput`
- `孤海注释`
- `VAEDecode` ★核心
- `VHS_VideoInfo`
- `KSampler` ★核心
- `SetNode`
- `PrimitiveFloat`
- `孤海注释`
- `GetNode`
- `ComfyNumberConvert`
- `GetNode`
- `ImageScaleToMaxDimension`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `Int`
- `SetNode`
- `Int`
- `ComfyMathExpression`
- `VHS_LoadVideo`
- `MarkdownNote`

## 关键参数

- `seed` = `980315471200131`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **64%**（21/33）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`RHHiddenNodes`、`ModelSamplingSD3`、`MuyeTextEditOutput`、`easy promptConcat`、`VAEDecode`、`VHS_VideoInfo`、`KSampler`、`ComfyNumberConvert`、`ImageScaleToMaxDimension`、`VHS_VideoCombine`、`Int`、`ComfyMathExpression`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、VAEEncode、easy promptConcat

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
