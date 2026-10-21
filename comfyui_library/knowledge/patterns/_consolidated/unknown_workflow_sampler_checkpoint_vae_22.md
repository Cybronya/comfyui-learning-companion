---
name: unknown_workflow_sampler_checkpoint_vae_22
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.881
common_nodes: [CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, SaveAudioMP3, TextEncodeAceStepAudio1.5, VAEDecodeAudio]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/ACE-Step 1.5 音乐生成：4G显存就能玩 AI 音乐！_2019098979203555329.json, 音频生成/音频生成/极速秒级音乐生成 ACE Step_2017803333347581954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/ACE-Step 1.5 音乐生成：4G显存就能玩 AI 音乐！_2019098979203555329.json、音频生成/音频生成/极速秒级音乐生成 ACE Step_2017803333347581954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `Float` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有

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
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
