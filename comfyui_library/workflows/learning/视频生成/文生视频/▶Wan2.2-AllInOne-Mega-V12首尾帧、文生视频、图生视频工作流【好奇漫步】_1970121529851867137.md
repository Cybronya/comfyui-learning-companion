---
key: 视频生成/文生视频/▶Wan2.2-AllInOne-Mega-V12首尾帧、文生视频、图生视频工作流【好奇漫步】_1970121529851867137.json
name: ▶Wan2.2-AllInOne-Mega-V12首尾帧、文生视频、图生视频工作流【好奇漫步】_1970121529851867137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/▶Wan2.2-AllInOne-Mega-V12首尾帧、文生视频、图生视频工作流【好奇漫步】_1970121529851867137.json
hash: 2e2b7a0390877543
coverage: 0.857143
learned_at: 2026-10-10 23:10:01
nodes: [CLIPTextEncode, KSampler, VHS_VideoCombine, ModelSamplingSD3, PrimitiveInt, VAEDecode, WanVaceToVideo, LoadImage, LoadImage, WanVideoVACEStartToEndFrame, CLIPTextEncode, CheckpointLoaderSimple, LoadImage, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v12.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "beta", "seed": 6456545463455, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/▶Wan2.2-AllInOne-Mega-V12首尾帧、文生视频、图生视频工作流【好奇漫步】_1970121529851867137.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/▶Wan2.2-AllInOne-Mega-V12首尾帧、文生视频、图生视频工作流【好奇漫步】_1970121529851867137.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `WanVaceToVideo`
- `LoadImage`
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `6456545463455`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v12.safetensors`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPTextEncode`、`KSampler`、`VHS_VideoCombine`、`ModelSamplingSD3`、`VAEDecode`、`WanVaceToVideo`、`LoadImage`、`WanVideoVACEStartToEndFrame`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ModelSamplingSD3、VHS_VideoCombine、WanVaceToVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
