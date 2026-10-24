---
name: unknown_workflow_sampler_unet_vae_335
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.786
common_nodes: [CLIPLoader, CR Text, ComfySwitchNode, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, Fast Groups Muter (rgthree), KSampler, MiniMaxMusic3TextEncode, ModelAttentionBackend, RH_RhartAudioSunoV55Custom, RH_Screenwriter, SaveAudio, Seed (rgthree), ShowText|pysssss, UNETLoader, VAEDecodeAudio, VAEDecodeAudioTiled, VAELoader, WujiMusicianACEStep15XL, easy boolean]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/MiNiMxa3、Ace1.5xl、Suno5.5三合一自动音乐创作最强工作流_2091761118665592833.json, 音频生成/音频生成/MiNiMxa3、Ace1.5xl、Suno5.5三合一自动音乐创作最强工作流_2091792754799104002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_335

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/MiNiMxa3、Ace1.5xl、Suno5.5三合一自动音乐创作最强工作流_2091761118665592833.json、音频生成/音频生成/MiNiMxa3、Ace1.5xl、Suno5.5三合一自动音乐创作最强工作流_2091792754799104002.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `Fast Groups Muter (rgthree)`
- `KSampler`
- `MiniMaxMusic3TextEncode`
- `ModelAttentionBackend`
- `RH_RhartAudioSunoV55Custom`
- `RH_Screenwriter`
- `SaveAudio`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAEDecodeAudioTiled`
- `VAELoader`
- `WujiMusicianACEStep15XL`
- `easy boolean`

**可变部分**（部分 workflow 才有）：
- `WujiLyricist2` —— 1/2 个有
- `WujiLyricist3` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
