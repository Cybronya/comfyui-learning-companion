---
key: 视频生成/文生视频/文生视频+图生视频+首尾帧工作流（Wan2.2-Rapid-AIO-Mega）_2044790035236528130.json
name: 文生视频+图生视频+首尾帧工作流（Wan2.2-Rapid-AIO-Mega）_2044790035236528130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频+图生视频+首尾帧工作流（Wan2.2-Rapid-AIO-Mega）_2044790035236528130.json
hash: 7a68c922a2b20f19
coverage: 0.761905
learned_at: 2026-10-11 19:49:49
nodes: [SimpleMath+, CLIPTextEncode, INTConstant, INTConstant, CM_IntToFloat, INTConstant, CLIPTextEncode, INTConstant, Note, WanVaceToVideo, PrimitiveInt, VAEDecode, CheckpointLoaderSimple, ModelSamplingSD3, KSampler, VHS_VideoCombine, LoadImage, LoadImage, WanVideoVACEStartToEndFrame, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: []
missing: [SimpleMath+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v12.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "beta", "seed": 6456545463455, "steps": 4}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/文生视频+图生视频+首尾帧工作流（Wan2.2-Rapid-AIO-Mega）_2044790035236528130.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频+图生视频+首尾帧工作流（Wan2.2-Rapid-AIO-Mega）_2044790035236528130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `CM_IntToFloat`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `Note`
- `WanVaceToVideo`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v12.safetensors`
- `seed` = `6456545463455`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`CLIPTextEncode`、`INTConstant`、`CM_IntToFloat`、`WanVaceToVideo`、`VAEDecode`、`CheckpointLoaderSimple`、`ModelSamplingSD3`、`KSampler`、`VHS_VideoCombine`、`LoadImage`、`WanVideoVACEStartToEndFrame`

**缺卡**（1）：`SimpleMath+`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CM_IntToFloat、INTConstant、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
