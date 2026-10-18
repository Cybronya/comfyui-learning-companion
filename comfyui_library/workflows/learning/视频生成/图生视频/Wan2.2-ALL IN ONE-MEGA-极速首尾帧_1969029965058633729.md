---
key: 视频生成/图生视频/Wan2.2-ALL IN ONE-MEGA-极速首尾帧_1969029965058633729.json
name: Wan2.2-ALL IN ONE-MEGA-极速首尾帧_1969029965058633729.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-ALL IN ONE-MEGA-极速首尾帧_1969029965058633729.json
hash: b3892a9914fe3773
coverage: 0.705882
learned_at: 2026-10-15 22:31:47
nodes: [CLIPTextEncode, Note, WanVideoVACEStartToEndFrame, ModelSamplingSD3, WanVaceToVideo, VAEDecode, KSampler, PrimitiveInt, VHS_VideoCombine, PrimitiveInt, LoadImage, LoadImage, CLIPTextEncode, PrimitiveInt, CheckpointLoaderSimple, wanBlockSwap, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 261298560151054, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-ALL IN ONE-MEGA-极速首尾帧_1969029965058633729.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969029965058633729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `WanVideoVACEStartToEndFrame`
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `CheckpointLoaderSimple` ★核心
- `wanBlockSwap`
- `MarkdownNote`

## 关键参数

- `seed` = `261298560151054`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **71%**（12/17）

**有卡**：`CLIPTextEncode`、`WanVideoVACEStartToEndFrame`、`ModelSamplingSD3`、`WanVaceToVideo`、`VAEDecode`、`KSampler`、`VHS_VideoCombine`、`LoadImage`、`CheckpointLoaderSimple`、`wanBlockSwap`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ModelSamplingSD3、VHS_VideoCombine、WanVaceToVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
