---
name: unknown_workflow_sampler_unet_vae_170
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.787714
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/【开源】MiniMax_Music3 音乐生成_2088147284696584193.json, 音频生成/音频生成/【遇见AI】Minimax Music 3开源音乐模型，最长支持5分钟_2088855416225755138.json, 音频生成/音频生成/文字生歌曲 MiniMax Music_2090725556378750978.json, 音频生成/音频生成/海螺Minimax Music3_2088170981381730305.json, 音频生成/音频生成/真·最强开源音乐生成 minimaxmusic  suno之下第一人_2089988506549571586.json, 音频生成/音频生成/音乐生成 海螺 Music 3_2088110025138069505.json, 音频生成/音频生成/音乐生成 海螺 Music 3_2088981046997118977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_170

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（音频生成/音频生成/【开源】MiniMax_Music3 音乐生成_2088147284696584193.json、音频生成/音频生成/【遇见AI】Minimax Music 3开源音乐模型，最长支持5分钟_2088855416225755138.json、音频生成/音频生成/文字生歌曲 MiniMax Music_2090725556378750978.json、音频生成/音频生成/海螺Minimax Music3_2088170981381730305.json、音频生成/音频生成/真·最强开源音乐生成 minimaxmusic  suno之下第一人_2089988506549571586.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ComfySwitchNode` —— 4/7 个有
- `VAEDecodeAudioTiled` —— 4/7 个有
- `Float` —— 3/7 个有
- `PreviewAudio` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `Text` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 7 | 100% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 7/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：发现KSampler但没有VAEDecode
