---
name: unknown_workflow_sampler_unet_vae_185
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.758
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Ace Step 1.5xl turbo文生音乐工作流_2090785357209100290.json, 音频生成/音频生成/acestep_v1.5_xl_BASE_音乐生成_2042893593232285698.json, 音频生成/音频生成/acestep_v1.5_xl_SFT_音乐生成_2042899033756274690.json, 音频生成/音频生成/acestep_v1.5_xl_turbo 音乐生成_2016715807329361921.json, 音频生成/音频生成/最新Acestep-xl-turbo音乐歌曲生成工作流_2042845013394067458.json, 音频生成/音频生成/歌曲创作_2042845860060471298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_185

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（音频生成/音频生成/Ace Step 1.5xl turbo文生音乐工作流_2090785357209100290.json、音频生成/音频生成/acestep_v1.5_xl_BASE_音乐生成_2042893593232285698.json、音频生成/音频生成/acestep_v1.5_xl_SFT_音乐生成_2042899033756274690.json、音频生成/音频生成/acestep_v1.5_xl_turbo 音乐生成_2016715807329361921.json、音频生成/音频生成/最新Acestep-xl-turbo音乐歌曲生成工作流_2042845013394067458.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
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
- `SaveAudioMP3` —— 5/6 个有
- `LoadImage` —— 4/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `Label (rgthree)` —— 2/6 个有
- `PreviewAudio` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SaveAudioAdvanced` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 6 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 6 | 8% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，6 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，6 个样本，取值分散，一致性仅 8%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
