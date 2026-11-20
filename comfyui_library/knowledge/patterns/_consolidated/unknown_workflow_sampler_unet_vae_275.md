---
name: unknown_workflow_sampler_unet_vae_275
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.7568
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Ace Step 1.5xl turbo文生音乐工作流_2090785357209100290.json, 音频生成/音频生成/最新Acestep-xl-turbo音乐歌曲生成工作流_2042845013394067458.json, 音频生成/音频生成/编曲、bgm生成_2053301419213631490.json, 音频生成/音频生成/编曲、歌曲生成、bgm_2048663825725001730.json, 音频生成/音频生成/音乐歌曲_ACE_2069334357084561410.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_275

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/Ace Step 1.5xl turbo文生音乐工作流_2090785357209100290.json、音频生成/音频生成/最新Acestep-xl-turbo音乐歌曲生成工作流_2042845013394067458.json、音频生成/音频生成/编曲、bgm生成_2053301419213631490.json、音频生成/音频生成/编曲、歌曲生成、bgm_2048663825725001730.json、音频生成/音频生成/音乐歌曲_ACE_2069334357084561410.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveAudioMP3` —— 4/5 个有
- `PrimitiveInt` —— 3/5 个有
- `Label (rgthree)` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `LoadImage` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `SaveAudioAdvanced` —— 1/5 个有
- `easy float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 5 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 5 | 0% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，5 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
