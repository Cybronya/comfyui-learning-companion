---
key: 音频生成/音频生成/VividMuse Stable Audio 3 Medium Workflow_2058890111261175809.json
name: VividMuse Stable Audio 3 Medium Workflow_2058890111261175809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/VividMuse Stable Audio 3 Medium Workflow_2058890111261175809.json
hash: 7daed80c07695938
coverage: 0.833333
learned_at: 2026-10-18 03:04:57
nodes: [CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, VAEDecodeAudio, KSampler, PrimitiveStringMultiline, VAEDecodeAudio, KSampler, Fast Groups Bypasser (rgthree), easy promptList, easy promptList, easy promptList, CLIPLoader, CheckpointLoaderSimple, CLIPLoader, easy promptList, PrimitiveStringMultiline, Note, EmptyLatentAudio, SaveAudio, SaveAudio, Seed (rgthree)]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "stable_audio_3_medium_base.safetensors", "denoise": 1, "height": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 0, "steps": 10, "width": 60}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/VividMuse Stable Audio 3 Medium Workflow_2058890111261175809.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/VividMuse Stable Audio 3 Medium Workflow_2058890111261175809.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `CLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `easy promptList`
- `PrimitiveStringMultiline`
- `Note`
- `EmptyLatentAudio` ★核心
- `SaveAudio`
- `SaveAudio`
- `Seed (rgthree)`

## 关键参数

- `checkpoint` = `stable_audio_3_medium_base.safetensors`
- `seed` = `0`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `60`
- `height` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`CLIPTextEncode`、`CheckpointLoaderSimple`、`VAEDecodeAudio`、`KSampler`、`easy promptList`、`CLIPLoader`、`EmptyLatentAudio`、`SaveAudio`、`Seed (rgthree)`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、Seed (rgthree)、VAEDecodeAudio、EmptyLatentAudio、easy promptList

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
