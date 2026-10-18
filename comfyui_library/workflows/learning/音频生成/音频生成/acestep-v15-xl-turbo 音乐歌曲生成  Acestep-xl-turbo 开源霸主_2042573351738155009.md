---
key: 音频生成/音频生成/acestep-v15-xl-turbo 音乐歌曲生成  Acestep-xl-turbo 开源霸主_2042573351738155009.json
name: acestep-v15-xl-turbo 音乐歌曲生成  Acestep-xl-turbo 开源霸主_2042573351738155009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/acestep-v15-xl-turbo 音乐歌曲生成  Acestep-xl-turbo 开源霸主_2042573351738155009.json
hash: 231c3b34d9102dbe
coverage: 0.878788
learned_at: 2026-10-18 02:28:45
nodes: [DualCLIPLoader, ConditioningZeroOut, VAEDecodeAudio, UNETLoader, SaveAudioMP3, ModelSamplingAuraFlow, PrimitiveNode, easy anythingIndexSwitch, CR Prompt Text, CR Prompt Text, RegexExtract, RegexExtract, TextEncodeAceStepAudio1.5, KSampler, VAELoader, PreviewAny, RH_LLMAPI_Pro_Node, easy anythingIndexSwitch, ConditioningZeroOut, ModelSamplingAuraFlow, CR Prompt Text, CR Prompt Text, SaveAudioMP3, VAELoader, UNETLoader, DualCLIPLoader, VAEDecodeAudio, TextEncodeAceStepAudio1.5, PrimitiveNode, EmptyAceStep1.5LatentAudio, EmptyAceStep1.5LatentAudio, KSampler, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1.2, "denoise": 1, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 1017857826010670, "steps": 12}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/acestep-v15-xl-turbo 音乐歌曲生成  Acestep-xl-turbo 开源霸主_2042573351738155009.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/acestep-v15-xl-turbo 音乐歌曲生成  Acestep-xl-turbo 开源霸主_2042573351738155009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `UNETLoader` ★核心
- `SaveAudioMP3`
- `ModelSamplingAuraFlow`
- `PrimitiveNode`
- `easy anythingIndexSwitch`
- `CR Prompt Text`
- `CR Prompt Text`
- `RegexExtract`
- `RegexExtract`
- `TextEncodeAceStepAudio1.5`
- `KSampler` ★核心
- `VAELoader`
- `PreviewAny`
- `RH_LLMAPI_Pro_Node`
- `easy anythingIndexSwitch`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CR Prompt Text`
- `CR Prompt Text`
- `SaveAudioMP3`
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAEDecodeAudio` ★核心
- `TextEncodeAceStepAudio1.5`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `EmptyAceStep1.5LatentAudio`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `1017857826010670`
- `steps` = `12`
- `cfg` = `1.2`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`DualCLIPLoader`、`ConditioningZeroOut`、`VAEDecodeAudio`、`UNETLoader`、`SaveAudioMP3`、`ModelSamplingAuraFlow`、`easy anythingIndexSwitch`、`CR Prompt Text`、`RegexExtract`、`TextEncodeAceStepAudio1.5`、`KSampler`、`VAELoader`、`RH_LLMAPI_Pro_Node`、`EmptyAceStep1.5LatentAudio`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、CR Prompt Text

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
