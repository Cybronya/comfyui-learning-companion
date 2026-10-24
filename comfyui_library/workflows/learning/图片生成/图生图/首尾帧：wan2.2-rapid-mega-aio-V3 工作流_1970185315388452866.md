---
key: 图片生成/图生图/首尾帧：wan2.2-rapid-mega-aio-V3 工作流_1970185315388452866.json
name: 首尾帧：wan2.2-rapid-mega-aio-V3 工作流_1970185315388452866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/首尾帧：wan2.2-rapid-mega-aio-V3 工作流_1970185315388452866.json
hash: 6d4dbf71fa7ba945
coverage: 0.941176
learned_at: 2026-10-23 13:33:12
nodes: [WanVaceToVideo, Note, KSampler, ModelSamplingSD3, INTConstant, WanVideoVACEStartToEndFrame, CheckpointLoaderSimple, LoadImage, LoadImage, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, easy clearCacheAll, VAEDecode, VHS_VideoCombine, Int, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v3.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 133876060420641, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/首尾帧：wan2.2-rapid-mega-aio-V3 工作流_1970185315388452866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/首尾帧：wan2.2-rapid-mega-aio-V3 工作流_1970185315388452866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `WanVaceToVideo`
- `Note`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `INTConstant`
- `WanVideoVACEStartToEndFrame`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Int`
- `Int`

## 关键参数

- `seed` = `133876060420641`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v3.safetensors`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`WanVaceToVideo`、`KSampler`、`ModelSamplingSD3`、`INTConstant`、`WanVideoVACEStartToEndFrame`、`CheckpointLoaderSimple`、`LoadImage`、`CLIPTextEncode`、`easy cleanGpuUsed`、`easy clearCacheAll`、`VAEDecode`、`VHS_VideoCombine`、`Int`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Int、INTConstant、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
