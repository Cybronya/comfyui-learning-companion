---
name: unknown_workflow_sampler_unet_vae_276
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8014
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/文字生歌曲 MiniMax Music_2090725556378750978.json, 音频生成/音频生成/真·最强开源音乐生成 minimaxmusic  suno之下第一人_2089988506549571586.json, 音频生成/音频生成/音乐生成 海螺 Music 3_2088110025138069505.json, 音频生成/音频生成/音乐生成 海螺 Music 3_2088981046997118977.json, 音频生成/音频生成/音乐生成器：minimax_music_3音乐生成_2092150851132542977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_276

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/文字生歌曲 MiniMax Music_2090725556378750978.json、音频生成/音频生成/真·最强开源音乐生成 minimaxmusic  suno之下第一人_2089988506549571586.json、音频生成/音频生成/音乐生成 海螺 Music 3_2088110025138069505.json、音频生成/音频生成/音乐生成 海螺 Music 3_2088981046997118977.json、音频生成/音频生成/音乐生成器：minimax_music_3音乐生成_2092150851132542977.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `KSampler`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `SeedNode`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `VAEDecodeAudioTiled` —— 4/5 个有
- `PreviewAudio` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `Float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
