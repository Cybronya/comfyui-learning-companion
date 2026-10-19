---
name: unknown_workflow_sampler_unet_vae_67
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7312
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, UNETLoader, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/1-Aiden-MiniMax_Music3测试工作流！！！_2088008118289653761.json, 音频生成/音频生成/A-18 MiniMax Music 3 文生音频 主题+歌词 歌曲直出_2107488878654480385.json, 音频生成/音频生成/MiniMax Music 3 - 音乐生成-支持提示词-歌词_2088208847331745794.json, 音频生成/音频生成/MiniMax Music 3 AI音乐歌曲创作工作流2608_2094013038423793665.json, 音频生成/音频生成/MiniMax Music 3 文生音乐工作流｜为自己的爱情定制专属情歌！_2092788025477656578.json, 音频生成/音频生成/MiniMax Music 3 文生音乐工作流｜为自己的爱情定制专属情歌！_2109801992737615874.json, 音频生成/音频生成/MiniMax Music 3 文生音频_2088066476321361922.json, 音频生成/音频生成/MiniMax Music-音乐生成_2088831784896258049.json, 音频生成/音频生成/MiniMax Music3 文生歌曲工作流 带时长参数控制注释版_2088143069853077505.json, 音频生成/音频生成/MiniMax Music音乐生成_2089190873136459777.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_67

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（音频生成/音频生成/1-Aiden-MiniMax_Music3测试工作流！！！_2088008118289653761.json、音频生成/音频生成/A-18 MiniMax Music 3 文生音频 主题+歌词 歌曲直出_2107488878654480385.json、音频生成/音频生成/MiniMax Music 3 - 音乐生成-支持提示词-歌词_2088208847331745794.json、音频生成/音频生成/MiniMax Music 3 AI音乐歌曲创作工作流2608_2094013038423793665.json、音频生成/音频生成/MiniMax Music 3 文生音乐工作流｜为自己的爱情定制专属情歌！_2092788025477656578.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `KSampler`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 9/10 个有
- `VAEDecodeAudioTiled` —— 8/10 个有
- `ComfySwitchNode` —— 7/10 个有
- `SeedNode` —— 7/10 个有
- `Float` —— 6/10 个有
- `PreviewAudio` —— 4/10 个有
- `孤海注释` —— 4/10 个有
- `CR Prompt Text` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `MuyeTextEditOutput` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `JjkText` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `RHLLMChatNode` —— 1/10 个有
- `easy seed` —— 1/10 个有

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
