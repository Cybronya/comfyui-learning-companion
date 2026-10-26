---
key: 音频生成/音频生成/🔊 一句话生成游戏音效｜Stable Audio 3 Small SFX V1.1_2114675404417101825.json
name: 🔊 一句话生成游戏音效｜Stable Audio 3 Small SFX V1.1_2114675404417101825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/🔊 一句话生成游戏音效｜Stable Audio 3 Small SFX V1.1_2114675404417101825.json
hash: feb3574b0eaf5c28
coverage: 1
learned_at: 2026-10-26 22:17:38
nodes: [CheckpointLoaderSimple, CLIPLoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentAudio, KSampler, VAEDecodeAudio, SaveAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "stable_audio_3_small_sfx.safetensors", "denoise": 1, "height": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 1093761339906084, "steps": 8, "width": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/🔊 一句话生成游戏音效｜Stable Audio 3 Small SFX V1.1_2114675404417101825.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/🔊 一句话生成游戏音效｜Stable Audio 3 Small SFX V1.1_2114675404417101825.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（8 个）：
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentAudio` ★核心
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `SaveAudio`

## 关键参数

- `checkpoint` = `stable_audio_3_small_sfx.safetensors`
- `width` = `4`
- `height` = `1`
- `seed` = `1093761339906084`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`CheckpointLoaderSimple`、`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentAudio`、`KSampler`、`VAEDecodeAudio`、`SaveAudio`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、VAEDecodeAudio、EmptyLatentAudio、SaveAudio、sd15-t2i-basic

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
