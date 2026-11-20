---
name: unknown_workflow_sampler_unet_vae_118
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.77
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, SaveAudioMP3, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/ace step1.5一键AI写歌、生成背景音乐，自带提示词推理_2092459072607047681.json, 音频生成/音频生成/ace1.5 多语言风格音乐生成_2019227846987751425.json, 音频生成/音频生成/ace1.5词生歌_2084554800502501377.json, 音频生成/音频生成/ace1.5音乐生成_2018972681219088385.json, 音频生成/音频生成/acestep_v1.5_xl_BASE_音乐生成_2042893593232285698.json, 音频生成/音频生成/acestep_v1.5_xl_SFT_音乐生成_2042899033756274690.json, 音频生成/音频生成/acestep_v1.5_xl_turbo 音乐生成_2016715807329361921.json, 音频生成/音频生成/歌曲创作_2042845860060471298.json, 音频生成/音频生成/音频-音乐歌曲生成-Acestep-xl-turbo_2043627967057764353.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_118

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（音频生成/音频生成/ace step1.5一键AI写歌、生成背景音乐，自带提示词推理_2092459072607047681.json、音频生成/音频生成/ace1.5 多语言风格音乐生成_2019227846987751425.json、音频生成/音频生成/ace1.5词生歌_2084554800502501377.json、音频生成/音频生成/ace1.5音乐生成_2018972681219088385.json、音频生成/音频生成/acestep_v1.5_xl_BASE_音乐生成_2042893593232285698.json…）

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
- `PrimitiveFloat` —— 5/9 个有
- `LoadImage` —— 4/9 个有
- `PrimitiveStringMultiline` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `PrimitiveInt` —— 2/9 个有
- `easy seed` —— 2/9 个有
- `AceStepLLMSongPlanner` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `RegexExtract` —— 1/9 个有
- `llama_cpp_model_loader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 9 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 9 | 0% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 9/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，9 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，9 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：发现KSampler但没有VAEDecode
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
