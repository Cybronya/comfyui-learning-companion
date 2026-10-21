---
name: unknown_workflow_sampler_unet_vae_158
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.827
common_nodes: [CLIPLoader, ComfySwitchNode, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecodeAudio, VAEDecodeAudioTiled, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/MiniMax Music音乐生成_自动谱曲连接版_v4_2090433735576608769.json, 音频生成/音频生成/Minimax Music3 音乐创作（用法指南）_2088106169742221313.json, 音频生成/音频生成/Minimax Music3文生音频工作流_2088271615460208642.json, 音频生成/音频生成/Minimax+音乐3生成音乐_2089683699175612418.json, 音频生成/音频生成/Minimax-Music3 音乐生成神器 开源版！_2090322547391946753.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_158

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/MiniMax Music音乐生成_自动谱曲连接版_v4_2090433735576608769.json、音频生成/音频生成/Minimax Music3 音乐创作（用法指南）_2088106169742221313.json、音频生成/音频生成/Minimax Music3文生音频工作流_2088271615460208642.json、音频生成/音频生成/Minimax+音乐3生成音乐_2089683699175612418.json、音频生成/音频生成/Minimax-Music3 音乐生成神器 开源版！_2090322547391946753.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `KSampler`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `SeedNode`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAEDecodeAudioTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/5 个有
- `PreviewAudio` —— 2/5 个有
- `Float` —— 1/5 个有
- `JoinStrings` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `SomethingToString` —— 1/5 个有
- `孤海注释` —— 1/5 个有

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
