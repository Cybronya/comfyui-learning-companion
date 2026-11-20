---
name: unknown_workflow_sampler_unet_vae_88
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.803091
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, SaveAudioMP3, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/ACE-Step1.5 文生音乐双Clip_2018882325588742146.json, 音频生成/音频生成/ACE1.5音乐生成_2030182345428439042.json, 音频生成/音频生成/ACE_Step-Ai歌曲音乐一键生成工作流_2069067060977684481.json, 音频生成/音频生成/ACE_Step开源音乐生成器_2058059955965612033.json, 音频生成/音频生成/Ace-Step1.5X工作流(打造你的专属音乐)_2054411129350311938.json, 音频生成/音频生成/Acestep1.5音乐制作_2043518374143070209.json, 音频生成/音频生成/ace-step 1.5 _ 音乐生成最佳搭档_2075297299286286338.json, 音频生成/音频生成/多人合唱-音乐生成-ACE-STEP1.5XL_2045332746666516482.json, 音频生成/音频生成/方格智联-ACE-1.5音乐_2086670840938192898.json, 音频生成/音频生成/无限画布ACE-Step 1.5 XL Turbo音乐生成工作流_2074758959570968577.json, 音频生成/音频生成/音乐生成-ACE-STEP1.5XL_2045321458674573313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_88

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（音频生成/音频生成/ACE-Step1.5 文生音乐双Clip_2018882325588742146.json、音频生成/音频生成/ACE1.5音乐生成_2030182345428439042.json、音频生成/音频生成/ACE_Step-Ai歌曲音乐一键生成工作流_2069067060977684481.json、音频生成/音频生成/ACE_Step开源音乐生成器_2058059955965612033.json、音频生成/音频生成/Ace-Step1.5X工作流(打造你的专属音乐)_2054411129350311938.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 10/11 个有
- `PrimitiveInt` —— 8/11 个有
- `Int` —— 6/11 个有
- `CR Text` —— 5/11 个有
- `Float` —— 5/11 个有
- `JjkText` —— 2/11 个有
- `PrimitiveFloat` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `AV_VAELoader` —— 1/11 个有
- `Text` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 11 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 11 | 0% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 11/11 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，11 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，11 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：发现KSampler但没有VAEDecode
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
