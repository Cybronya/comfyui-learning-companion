---
key: 视频生成/文生视频/wan2.2文生视频_2021070799720943618.json
name: wan2.2文生视频_2021070799720943618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频_2021070799720943618.json
hash: 09c941e65e00ef90
coverage: 0.923077
learned_at: 2026-10-15 22:47:36
nodes: [LoadImage, CLIPTextEncode, LoadImage, WanVideoVACEStartToEndFrame, ModelSamplingSD3, PrimitiveInt, WanVaceToVideo, CheckpointLoaderSimple, KSampler, VAEDecode, SaveImage, CLIPTextEncode, DuckHideNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v12.2.safetensors", "denoise": 1, "sampler_name": "dpmpp_sde", "scheduler": "beta", "seed": 6456545463455, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2文生视频_2021070799720943618.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频_2021070799720943618.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `WanVaceToVideo`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `DuckHideNode`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v12.2.safetensors`
- `seed` = `6456545463455`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`LoadImage`、`CLIPTextEncode`、`WanVideoVACEStartToEndFrame`、`ModelSamplingSD3`、`WanVaceToVideo`、`CheckpointLoaderSimple`、`KSampler`、`VAEDecode`、`SaveImage`、`DuckHideNode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveImage、ModelSamplingSD3、WanVaceToVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
