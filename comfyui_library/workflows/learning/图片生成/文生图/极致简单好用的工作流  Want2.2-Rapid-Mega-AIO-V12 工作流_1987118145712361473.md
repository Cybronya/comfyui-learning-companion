---
key: 图片生成/文生图/极致简单好用的工作流  Want2.2-Rapid-Mega-AIO-V12 工作流_1987118145712361473.json
name: 极致简单好用的工作流  Want2.2-Rapid-Mega-AIO-V12 工作流_1987118145712361473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/极致简单好用的工作流  Want2.2-Rapid-Mega-AIO-V12 工作流_1987118145712361473.json
hash: b6d6f5f171efd6bf
coverage: 0.705882
learned_at: 2026-10-09 20:13:12
nodes: [CheckpointLoaderSimple, WanVideoVACEStartToEndFrame, CLIPTextEncode, LoadImage, KSampler, VHS_VideoCombine, ModelSamplingSD3, VAEDecode, LoadImage, CLIPTextEncode, WanVaceToVideo, PrimitiveInt, Note, LoadAudio, Note, Label (rgthree), Note]
patterns: []
missing: [Label (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v12.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 6456545463455, "steps": 4}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/极致简单好用的工作流  Want2.2-Rapid-Mega-AIO-V12 工作流_1987118145712361473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1987118145712361473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `CheckpointLoaderSimple` ★核心
- `WanVideoVACEStartToEndFrame`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `PrimitiveInt`
- `Note`
- `LoadAudio`
- `Note`
- `Label (rgthree)`
- `Note`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v12.safetensors`
- `seed` = `6456545463455`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **71%**（12/17）

**有卡**：`CheckpointLoaderSimple`、`WanVideoVACEStartToEndFrame`、`CLIPTextEncode`、`LoadImage`、`KSampler`、`VHS_VideoCombine`、`ModelSamplingSD3`、`VAEDecode`、`WanVaceToVideo`、`LoadAudio`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LoadAudio、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
