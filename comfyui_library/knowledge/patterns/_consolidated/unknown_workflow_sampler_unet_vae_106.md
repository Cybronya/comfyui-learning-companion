---
name: unknown_workflow_sampler_unet_vae_106
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8072
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/Minimax_music_3 歌曲生成工作流_2089703825241366530.json, 音频生成/音频生成/Munimax+Music+_2095313021102026754.json, 音频生成/音频生成/MusicCreation(音乐创作)-MinimaxMusic_2109862183365599233.json, 音频生成/音频生成/audio_minimax_music_3_2088057881949196289.json, 音频生成/音频生成/audio_minimax_music_3_2088165410591035394.json, 音频生成/音频生成/audio_minimax_music_3_2089996070670655489.json, 音频生成/音频生成/minimax-music-3_2088169557298077698.json, 音频生成/音频生成/minimax音乐生成_2090253540622168065.json, 音频生成/音频生成/格式化音乐生成MiniMax-music3_2092316113559441410.json, 音频生成/音频生成/音乐生成器：minimax_music_3音乐生成_2092150851132542977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_106

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（音频生成/音频生成/Minimax_music_3 歌曲生成工作流_2089703825241366530.json、音频生成/音频生成/Munimax+Music+_2095313021102026754.json、音频生成/音频生成/MusicCreation(音乐创作)-MinimaxMusic_2109862183365599233.json、音频生成/音频生成/audio_minimax_music_3_2088057881949196289.json、音频生成/音频生成/audio_minimax_music_3_2088165410591035394.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `KSampler`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SeedNode` —— 9/10 个有
- `ComfySwitchNode` —— 8/10 个有
- `VAEDecodeAudioTiled` —— 8/10 个有
- `PrimitiveFloat` —— 3/10 个有
- `JjkText` —— 2/10 个有
- `FloatConstant` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `Textbox` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 10 | 100% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 10/10 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：发现KSampler但没有VAEDecode
