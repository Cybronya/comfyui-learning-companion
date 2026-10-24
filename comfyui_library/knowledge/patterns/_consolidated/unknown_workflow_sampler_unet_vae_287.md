---
name: unknown_workflow_sampler_unet_vae_287
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.773333
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, RH_LLMAPI_NODE, SaveAudioMP3, Text Multiline, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/Ai音乐-评分超过Suno V5！-Acestep-xl-turbo音乐歌曲生成-输入主题-自动生成歌曲_2043176701164789761.json, 音频生成/音频生成/ace1.5音乐歌曲生成-自动生成歌词和风格-速度快_2019064388140933122.json, 音频生成/音频生成/ace1.5音乐歌曲生成-自动生成歌词和风格_2021322986116096002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_287

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/Ai音乐-评分超过Suno V5！-Acestep-xl-turbo音乐歌曲生成-输入主题-自动生成歌曲_2043176701164789761.json、音频生成/音频生成/ace1.5音乐歌曲生成-自动生成歌词和风格-速度快_2019064388140933122.json、音频生成/音频生成/ace1.5音乐歌曲生成-自动生成歌词和风格_2021322986116096002.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `RH_LLMAPI_NODE`
- `SaveAudioMP3`
- `Text Multiline`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Float` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `MultiTextConcatenate` —— 1/3 个有
- `RH_Utils` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `TextConcatenator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
