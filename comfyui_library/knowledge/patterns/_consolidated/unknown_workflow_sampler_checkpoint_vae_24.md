---
name: unknown_workflow_sampler_checkpoint_vae_24
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.635
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, PrimitiveStringMultiline, SaveAudioMP3, TextEncodeAceStepAudio1.5, VAEDecodeAudio]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/ACE Step 1.5 Music Gen 音乐创作_2075068237804556289.json, 音频生成/音频生成/ACE-Step1.5 文生音乐_2018856388780367874.json, 音频生成/音频生成/ACE-Step1.5 歌曲创作_2043931078825615362.json, 音频生成/音频生成/ACE-Step1.5歌曲创作 附带教程_2044232351034642433.json, 音频生成/音频生成/ACE-Step1.5歌曲创作（附·提示词模版）_2041468135462674434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/ACE Step 1.5 Music Gen 音乐创作_2075068237804556289.json、音频生成/音频生成/ACE-Step1.5 文生音乐_2018856388780367874.json、音频生成/音频生成/ACE-Step1.5 歌曲创作_2043931078825615362.json、音频生成/音频生成/ACE-Step1.5歌曲创作 附带教程_2044232351034642433.json、音频生成/音频生成/ACE-Step1.5歌曲创作（附·提示词模版）_2041468135462674434.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 4/5 个有
- `Float` —— 2/5 个有
- `LoadImage` —— 1/5 个有
- `SaveAudio` —— 1/5 个有
- `SaveImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
