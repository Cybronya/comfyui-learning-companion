---
name: unknown_workflow_sampler_unet_vae_148
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.768778
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/Minimax-Music3开源版_2092083462328111106.json, 音频生成/音频生成/MinimaxH3-music3_2094205332569550850.json, 音频生成/音频生成/Minimax_music_3 歌曲生成工作流_2089703825241366530.json, 音频生成/音频生成/Munimax+Music+_2095313021102026754.json, 音频生成/音频生成/MusicCreation(音乐创作)-MinimaxMusic_2109862183365599233.json, 音频生成/音频生成/audio_minimax_music_3_2088057881949196289.json, 音频生成/音频生成/audio_minimax_music_3_2088165410591035394.json, 音频生成/音频生成/audio_minimax_music_3_2089996070670655489.json, 音频生成/音频生成/audio_minimax_music_3_2103383216622231553.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_148

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（音频生成/音频生成/Minimax-Music3开源版_2092083462328111106.json、音频生成/音频生成/MinimaxH3-music3_2094205332569550850.json、音频生成/音频生成/Minimax_music_3 歌曲生成工作流_2089703825241366530.json、音频生成/音频生成/Munimax+Music+_2095313021102026754.json、音频生成/音频生成/MusicCreation(音乐创作)-MinimaxMusic_2109862183365599233.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
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
- `SeedNode` —— 8/9 个有
- `ComfySwitchNode` —— 7/9 个有
- `VAEDecodeAudioTiled` —— 7/9 个有
- `PrimitiveFloat` —— 4/9 个有
- `JjkText` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `Float` —— 1/9 个有
- `FloatConstant` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `Textbox` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 9 | 100% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 9/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：发现KSampler但没有VAEDecode
