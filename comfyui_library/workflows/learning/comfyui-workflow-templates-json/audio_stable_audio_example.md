---
key: comfyui-workflow-templates-json/audio_stable_audio_example.json
name: audio_stable_audio_example
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_stable_audio_example.json
hash: 15fccec0aa3fd6bb
official: true
coverage: 0.888889
learned_at: 2026-10-10 22:47:01
nodes: [CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, CLIPLoader, EmptyLatentAudio, KSampler, VAEDecodeAudio, MarkdownNote, SaveAudioAdvanced]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 4.98, "checkpoint": "stable-audio-open-1.0.safetensors", "denoise": 1, "height": 1, "sampler_name": "dpmpp_3m_sde_gpu", "scheduler": "exponential", "seed": 840755638734093, "steps": 50, "width": 47.6}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_stable_audio_example.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_stable_audio_example.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（9 个）：
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `EmptyLatentAudio` ★核心
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `MarkdownNote`
- `SaveAudioAdvanced`

## 关键参数

- `checkpoint` = `stable-audio-open-1.0.safetensors`
- `width` = `47.6`
- `height` = `1`
- `seed` = `840755638734093`
- `steps` = `50`
- `cfg` = `4.98`
- `sampler_name` = `dpmpp_3m_sde_gpu`
- `scheduler` = `exponential`
- `denoise` = `1`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`CheckpointLoaderSimple`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentAudio`、`KSampler`、`VAEDecodeAudio`、`SaveAudioAdvanced`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、VAEDecodeAudio、EmptyLatentAudio、SaveAudioAdvanced、sd15-t2i-basic

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
