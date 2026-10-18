---
key: 音频生成/音频生成/Ai音乐-评分超过Suno V5！-Acestep-xl-turbo音乐歌曲生成-输入主题-自动生成歌曲_2043176701164789761.json
name: Ai音乐-评分超过Suno V5！-Acestep-xl-turbo音乐歌曲生成-输入主题-自动生成歌曲_2043176701164789761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Ai音乐-评分超过Suno V5！-Acestep-xl-turbo音乐歌曲生成-输入主题-自动生成歌曲_2043176701164789761.json
hash: beb6591951f9ee88
coverage: 0.818182
learned_at: 2026-10-18 02:28:39
nodes: [DualCLIPLoader, VAELoader, ConditioningZeroOut, UNETLoader, TextEncodeAceStepAudio1.5, Text Multiline, PrimitiveNode, EmptyAceStep1.5LatentAudio, SaveAudioMP3, ModelSamplingAuraFlow, VAEDecodeAudio, KSampler, MarkdownNote, MultiTextConcatenate, TextConcatenator, RH_Utils, SimpleMath+, Float, RH_LLMAPI_NODE, easy showAnything, RH_LLMAPI_NODE, easy showAnything]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 466612459056667, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Ai音乐-评分超过Suno V5！-Acestep-xl-turbo音乐歌曲生成-输入主题-自动生成歌曲_2043176701164789761.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Ai音乐-评分超过Suno V5！-Acestep-xl-turbo音乐歌曲生成-输入主题-自动生成歌曲_2043176701164789761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `DualCLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `TextEncodeAceStepAudio1.5`
- `Text Multiline`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `SaveAudioMP3`
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `MultiTextConcatenate`
- `TextConcatenator`
- `RH_Utils`
- `SimpleMath+`
- `Float`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `easy showAnything`

## 关键参数

- `seed` = `466612459056667`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`DualCLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`UNETLoader`、`TextEncodeAceStepAudio1.5`、`Text Multiline`、`EmptyAceStep1.5LatentAudio`、`SaveAudioMP3`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`KSampler`、`MultiTextConcatenate`、`TextConcatenator`、`RH_Utils`、`SimpleMath+`、`Float`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
