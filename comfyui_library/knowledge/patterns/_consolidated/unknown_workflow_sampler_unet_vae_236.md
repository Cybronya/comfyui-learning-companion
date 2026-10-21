---
name: unknown_workflow_sampler_unet_vae_236
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.581
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, PreviewAny, PrimitiveInt, PrimitiveStringMultiline, SaveAudio, Seed (rgthree), SomethingToString, StringConcatenate, StringTrim, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio, VAELoader, easy float, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/音乐生成_AceStep-v15-xl-turbo-一句话生成带歌词的音乐_2091185483287191553.json, 音频生成/音频生成/音乐生成_AceStep1.5_2019988579958661121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_236

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/音乐生成_AceStep-v15-xl-turbo-一句话生成带歌词的音乐_2091185483287191553.json、音频生成/音频生成/音乐生成_AceStep1.5_2019988579958661121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `Seed (rgthree)`
- `SomethingToString`
- `StringConcatenate`
- `StringTrim`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `easy float`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `JWStringSplit` —— 1/2 个有
- `JWStringToInteger` —— 1/2 个有
- `JsonExtractString` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `SaveStringKJ` —— 1/2 个有
- `SaveText` —— 1/2 个有
- `StringReplace` —— 1/2 个有
- `UNETLoader_Any` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
