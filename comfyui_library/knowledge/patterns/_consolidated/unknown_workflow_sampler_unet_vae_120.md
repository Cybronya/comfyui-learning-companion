---
name: unknown_workflow_sampler_unet_vae_120
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.766889
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, SaveAudioMP3, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/ace step1.5一键AI写歌、生成背景音乐，自带提示词推理_2092459072607047681.json, 音频生成/音频生成/ace1.5 多语言风格音乐生成_2019227846987751425.json, 音频生成/音频生成/ace1.5词生歌_2084554800502501377.json, 音频生成/音频生成/ace1.5音乐生成_2018972681219088385.json, 音频生成/音频生成/▶▶ACE-Step-音乐&歌曲生成流_2043662562075615233.json, 音频生成/音频生成/无限画布ACE-Step 1.5 XL Turbo音乐生成工作流_2074758959570968577.json, 音频生成/音频生成/编曲、bgm生成_2053301419213631490.json, 音频生成/音频生成/编曲、歌曲生成、bgm_2048663825725001730.json, 音频生成/音频生成/超越Suno！ACE-Step 1.5 XL Turbo音乐生成工作流_2045344730900336641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_120

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（音频生成/音频生成/ace step1.5一键AI写歌、生成背景音乐，自带提示词推理_2092459072607047681.json、音频生成/音频生成/ace1.5 多语言风格音乐生成_2019227846987751425.json、音频生成/音频生成/ace1.5词生歌_2084554800502501377.json、音频生成/音频生成/ace1.5音乐生成_2018972681219088385.json、音频生成/音频生成/▶▶ACE-Step-音乐&歌曲生成流_2043662562075615233.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveAudioMP3`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeAceStepAudio1.5` —— 8/9 个有
- `PrimitiveInt` —— 7/9 个有
- `CR Text` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `AceStepLLMSongPlanner` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `llama_cpp_model_loader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 9 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 29% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 9/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，9 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
- 高发问题（9/9 个样本）：发现KSampler但没有VAEDecode
