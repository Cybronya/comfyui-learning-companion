---
name: unknown_workflow_sampler_unet_vae_178
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.786625
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/audio_minimax_music_3_Comfy官方工作流_2088632634527277058.json, 音频生成/音频生成/audio_minimax_music_3带时长参数控制_2088062682548232193.json, 音频生成/音频生成/minimax music3 文生音乐_2088358998398558210.json, 音频生成/音频生成/minimax-music-3_2088169557298077698.json, 音频生成/音频生成/minimax音乐生成_2090253540622168065.json, 音频生成/音频生成/【开源】MiniMax_Music3 音乐生成_2088147284696584193.json, 音频生成/音频生成/格式化音乐生成MiniMax-music3_2092316113559441410.json, 音频生成/音频生成/海螺Minimax Music3_2088170981381730305.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_178

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（音频生成/音频生成/audio_minimax_music_3_Comfy官方工作流_2088632634527277058.json、音频生成/音频生成/audio_minimax_music_3带时长参数控制_2088062682548232193.json、音频生成/音频生成/minimax music3 文生音乐_2088358998398558210.json、音频生成/音频生成/minimax-music-3_2088169557298077698.json、音频生成/音频生成/minimax音乐生成_2090253540622168065.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 8 个 workflow 都包含：
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
- `ComfySwitchNode` —— 7/8 个有
- `VAEDecodeAudioTiled` —— 7/8 个有
- `Float` —— 4/8 个有
- `MuyeTextEditOutput` —— 2/8 个有
- `Text` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 8 | 100% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 8/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：发现KSampler但没有VAEDecode
