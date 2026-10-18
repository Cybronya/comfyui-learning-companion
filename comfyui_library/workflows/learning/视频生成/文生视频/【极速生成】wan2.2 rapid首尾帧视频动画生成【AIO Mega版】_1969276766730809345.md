---
key: 视频生成/文生视频/【极速生成】wan2.2 rapid首尾帧视频动画生成【AIO Mega版】_1969276766730809345.json
name: 【极速生成】wan2.2 rapid首尾帧视频动画生成【AIO Mega版】_1969276766730809345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【极速生成】wan2.2 rapid首尾帧视频动画生成【AIO Mega版】_1969276766730809345.json
hash: 0ff3ee3022df6d02
coverage: 0.95
learned_at: 2026-10-15 22:43:46
nodes: [CLIPTextEncode, WanVideoVACEStartToEndFrame, WanVaceToVideo, Note, KSampler, VHS_VideoCombine, easy clearCacheAll, easy cleanGpuUsed, VAEDecode, ModelSamplingSD3, CLIPTextEncode, KSampler, easy clearCacheAll, easy cleanGpuUsed, VAEDecode, ModelSamplingSD3, CLIPTextEncode, KSampler, easy clearCacheAll, easy cleanGpuUsed, VAEDecode, ModelSamplingSD3, INTConstant, CLIPTextEncode, WanVaceToVideo, VHS_VideoCombine, INTConstant, WanVaceToVideo, INTConstant, WanVideoVACEStartToEndFrame, CLIPTextEncode, VHS_VideoCombine, LoadImage, LoadImage, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), LoadImage, CheckpointLoaderSimple, CheckpointLoaderSimple, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v2.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 171857637663566, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/【极速生成】wan2.2 rapid首尾帧视频动画生成【AIO Mega版】_1969276766730809345.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969276766730809345.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（40 个）：
- `CLIPTextEncode` ★核心
- `WanVideoVACEStartToEndFrame`
- `WanVaceToVideo`
- `Note`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `VHS_VideoCombine`
- `INTConstant`
- `WanVaceToVideo`
- `INTConstant`
- `WanVideoVACEStartToEndFrame`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `171857637663566`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v2.safetensors`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`CLIPTextEncode`、`WanVideoVACEStartToEndFrame`、`WanVaceToVideo`、`KSampler`、`VHS_VideoCombine`、`easy clearCacheAll`、`easy cleanGpuUsed`、`VAEDecode`、`ModelSamplingSD3`、`INTConstant`、`LoadImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
