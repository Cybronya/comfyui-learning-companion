---
key: 音频生成/音频生成/MiNiMxa3、Ace1.5xl、Suno5.5三合一自动音乐创作最强工作流_2091761118665592833.json
name: MiNiMxa3、Ace1.5xl、Suno5.5三合一自动音乐创作最强工作流_2091761118665592833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/MiNiMxa3、Ace1.5xl、Suno5.5三合一自动音乐创作最强工作流_2091761118665592833.json
hash: ce751b4a313ae56c
coverage: 0.785714
learned_at: 2026-10-18 17:45:37
nodes: [WujiMusicianACEStep15XL, Note, RH_RhartAudioSunoV55Custom, SaveAudio, SaveAudio, UNETLoader, CLIPLoader, VAELoader, ModelAttentionBackend, MarkdownNote, ComfySwitchNode, easy boolean, Fast Groups Muter (rgthree), ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, VAEDecodeAudioTiled, VAEDecodeAudio, Seed (rgthree), RH_Screenwriter, ShowText|pysssss, CR Text, CR Text, ShowText|pysssss, MiniMaxMusic3TextEncode, KSampler, SaveAudio, CR Text, WujiLyricist3]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1111111112, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/MiNiMxa3、Ace1.5xl、Suno5.5三合一自动音乐创作最强工作流_2091761118665592833.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/MiNiMxa3、Ace1.5xl、Suno5.5三合一自动音乐创作最强工作流_2091761118665592833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（28 个）：
- `WujiMusicianACEStep15XL`
- `Note`
- `RH_RhartAudioSunoV55Custom`
- `SaveAudio`
- `SaveAudio`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelAttentionBackend`
- `MarkdownNote`
- `ComfySwitchNode`
- `easy boolean`
- `Fast Groups Muter (rgthree)`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `VAEDecodeAudioTiled` ★核心
- `VAEDecodeAudio` ★核心
- `Seed (rgthree)`
- `RH_Screenwriter`
- `ShowText|pysssss`
- `CR Text`
- `CR Text`
- `ShowText|pysssss`
- `MiniMaxMusic3TextEncode`
- `KSampler` ★核心
- `SaveAudio`
- `CR Text`
- `WujiLyricist3`

## 关键参数

- `seed` = `1111111112`
- `steps` = `30`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`WujiMusicianACEStep15XL`、`RH_RhartAudioSunoV55Custom`、`SaveAudio`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelAttentionBackend`、`easy boolean`、`ConditioningZeroOut`、`EmptyMiniMaxMusic3LatentAudio`、`VAEDecodeAudioTiled`、`VAEDecodeAudio`、`Seed (rgthree)`、`RH_Screenwriter`、`CR Text`、`MiniMaxMusic3TextEncode`、`KSampler`、`WujiLyricist3`

**用到的条目**：KSampler、VAELoader、CLIPLoader、ConditioningZeroOut、UNETLoader、Seed (rgthree)、VAEDecodeAudio、VAEDecodeAudioTiled

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
