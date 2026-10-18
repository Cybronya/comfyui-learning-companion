---
key: 音频生成/音频生成/audio_minimax_music_3_Comfy官方工作流_2088632634527277058.json
name: audio_minimax_music_3_Comfy官方工作流_2088632634527277058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/audio_minimax_music_3_Comfy官方工作流_2088632634527277058.json
hash: a544a13cf2b4adc5
coverage: 0.785714
learned_at: 2026-10-18 17:45:48
nodes: [UNETLoader, CLIPLoader, VAELoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, VAEDecodeAudio, VAEDecodeAudioTiled, ComfySwitchNode, MarkdownNote, MarkdownNote, SaveAudioAdvanced, SeedNode, MiniMaxMusic3TextEncode]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1.7, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1111111112, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/audio_minimax_music_3_Comfy官方工作流_2088632634527277058.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/audio_minimax_music_3_Comfy官方工作流_2088632634527277058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecodeAudioTiled` ★核心
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `SaveAudioAdvanced`
- `SeedNode`
- `MiniMaxMusic3TextEncode`

## 关键参数

- `seed` = `1111111112`
- `steps` = `30`
- `cfg` = `1.7`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`EmptyMiniMaxMusic3LatentAudio`、`KSampler`、`VAEDecodeAudio`、`VAEDecodeAudioTiled`、`SaveAudioAdvanced`、`SeedNode`、`MiniMaxMusic3TextEncode`

**用到的条目**：KSampler、VAELoader、CLIPLoader、ConditioningZeroOut、UNETLoader、SeedNode、VAEDecodeAudio、VAEDecodeAudioTiled

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
