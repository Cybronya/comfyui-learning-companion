---
key: 音频生成/音频生成/MusicCreation(音乐创作)-MinimaxMusic_2109862183365599233.json
name: MusicCreation(音乐创作)-MinimaxMusic_2109862183365599233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/MusicCreation(音乐创作)-MinimaxMusic_2109862183365599233.json
hash: dd740479adab0601
coverage: 0.916667
learned_at: 2026-10-18 18:02:23
nodes: [ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, MiniMaxMusic3TextEncode, PrimitiveFloat, Text Multiline, CLIPLoader, UNETLoader, VAEDecodeAudio, VAELoader, SaveAudioAdvanced, KSampler, Text Multiline]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1.7, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 440022244728542, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/MusicCreation(音乐创作)-MinimaxMusic_2109862183365599233.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/MusicCreation(音乐创作)-MinimaxMusic_2109862183365599233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `MiniMaxMusic3TextEncode`
- `PrimitiveFloat`
- `Text Multiline`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `SaveAudioAdvanced`
- `KSampler` ★核心
- `Text Multiline`

## 关键参数

- `seed` = `440022244728542`
- `steps` = `30`
- `cfg` = `1.7`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ConditioningZeroOut`、`EmptyMiniMaxMusic3LatentAudio`、`MiniMaxMusic3TextEncode`、`Text Multiline`、`CLIPLoader`、`UNETLoader`、`VAEDecodeAudio`、`VAELoader`、`SaveAudioAdvanced`、`KSampler`

**用到的条目**：KSampler、VAELoader、CLIPLoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyMiniMaxMusic3LatentAudio、MiniMaxMusic3TextEncode

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
