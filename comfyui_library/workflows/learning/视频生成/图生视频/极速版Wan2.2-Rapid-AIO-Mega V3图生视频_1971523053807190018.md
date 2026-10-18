---
key: 视频生成/图生视频/极速版Wan2.2-Rapid-AIO-Mega V3图生视频_1971523053807190018.json
name: 极速版Wan2.2-Rapid-AIO-Mega V3图生视频_1971523053807190018.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/极速版Wan2.2-Rapid-AIO-Mega V3图生视频_1971523053807190018.json
hash: 59f4a59636c5984c
coverage: 0.782609
learned_at: 2026-10-15 22:31:57
nodes: [LayerUtility: ImageScaleByAspectRatio V2, WanVideoVACEStartToEndFrame, Note, Note, Note, Int, easy float, SimpleMath+, CheckpointLoaderSimple, ApplySageAttention, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, LoadImage, Int, WanVaceToVideo, VAEDecode, VHS_VideoCombine, KSampler, easy seed, LoadImage, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v3.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "beta", "seed": 845847597438430, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/极速版Wan2.2-Rapid-AIO-Mega V3图生视频_1971523053807190018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971523053807190018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVACEStartToEndFrame`
- `Note`
- `Note`
- `Note`
- `Int`
- `easy float`
- `SimpleMath+`
- `CheckpointLoaderSimple` ★核心
- `ApplySageAttention`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `Int`
- `WanVaceToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `easy seed`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v3.safetensors`
- `seed` = `845847597438430`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVACEStartToEndFrame`、`Int`、`easy float`、`SimpleMath+`、`CheckpointLoaderSimple`、`ApplySageAttention`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`、`WanVaceToVideo`、`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`easy seed`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、easy seed、Int、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
