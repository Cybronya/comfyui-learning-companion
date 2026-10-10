---
key: 视频生成/文生视频/wan2.2-rapid-mega-aio-v12_1996131644778168321.json
name: wan2.2-rapid-mega-aio-v12_1996131644778168321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-rapid-mega-aio-v12_1996131644778168321.json
hash: 1df73e8043870797
coverage: 0.8125
learned_at: 2026-10-11 02:57:39
nodes: [WanVaceToVideo, ModelSamplingSD3, LoadImage, WanVideoVACEStartToEndFrame, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, LoadImage, KSampler, VAEDecode, VHS_VideoCombine, ShellAgentPluginInputInteger, ShellAgentPluginInputInteger, PrimitiveInt, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v12.1.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 6456545463455, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2-rapid-mega-aio-v12_1996131644778168321.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-rapid-mega-aio-v12_1996131644778168321.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ShellAgentPluginInputInteger`
- `ShellAgentPluginInputInteger`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v12.1.safetensors`
- `seed` = `6456545463455`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`WanVaceToVideo`、`ModelSamplingSD3`、`LoadImage`、`WanVideoVACEStartToEndFrame`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`ShellAgentPluginInputInteger`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ModelSamplingSD3、VHS_VideoCombine、WanVaceToVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
