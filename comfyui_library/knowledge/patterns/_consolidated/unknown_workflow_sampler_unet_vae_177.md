---
name: unknown_workflow_sampler_unet_vae_177
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.743125
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/MiniMax Music3 I 开源音乐新王_2088579603374895106.json, 音频生成/音频生成/MiniMax_Music3-音乐生成_2090004883062747138.json, 音频生成/音频生成/Minimax Music 3音乐生成工作流_2088093007462617089.json, 音频生成/音频生成/Minimax Music3 音乐创作（用法指南）_2088106169742221313.json, 音频生成/音频生成/Minimax Music3文生音频工作流_2088271615460208642.json, 音频生成/音频生成/Minimax+音乐3生成音乐_2089683699175612418.json, 音频生成/音频生成/Minimax-Music3 音乐生成神器 开源版！_2090322547391946753.json, 音频生成/音频生成/Minimax-Music3 音乐生成神器 开源版！带官方skill自动优化节点_2089299030575771650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_177

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（音频生成/音频生成/MiniMax Music3 I 开源音乐新王_2088579603374895106.json、音频生成/音频生成/MiniMax_Music3-音乐生成_2090004883062747138.json、音频生成/音频生成/Minimax Music 3音乐生成工作流_2088093007462617089.json、音频生成/音频生成/Minimax Music3 音乐创作（用法指南）_2088106169742221313.json、音频生成/音频生成/Minimax Music3文生音频工作流_2088271615460208642.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：74%

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
- `PrimitiveFloat` —— 4/8 个有
- `CR Text` —— 3/8 个有
- `孤海注释` —— 3/8 个有
- `DapaoMusic3CaptionPromptNode` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PreviewAudio` —— 1/8 个有
- `PrimitiveString` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `String` —— 1/8 个有
- `Text` —— 1/8 个有
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
