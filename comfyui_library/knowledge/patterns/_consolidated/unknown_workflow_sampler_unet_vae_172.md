---
name: unknown_workflow_sampler_unet_vae_172
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.794833
common_nodes: [CLIPLoader, ComfySwitchNode, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecodeAudio, VAEDecodeAudioTiled, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/反推提示词/音乐生成 海螺 Music 3_2088149749898764290.json, 数字人/数字人/MiniMax Music 3_2095916117280772098.json, 数字人/数字人/Minimax-Music3  音乐_2095365589534601218.json, 数字人/数字人/智能体制作好声音必备 minimax M3_2094801787873218562.json, 视频生成/图生视频/MiniMax+Music音乐生成_2089265743111213057.json, 音频生成/音频生成/Mini max  music生成音乐_2088925873197117441.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_172

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/音乐生成 海螺 Music 3_2088149749898764290.json、数字人/数字人/MiniMax Music 3_2095916117280772098.json、数字人/数字人/Minimax-Music3  音乐_2095365589534601218.json、数字人/数字人/智能体制作好声音必备 minimax M3_2094801787873218562.json、视频生成/图生视频/MiniMax+Music音乐生成_2089265743111213057.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
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
- `PreviewAudio` —— 3/6 个有
- `Float` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `PixaromaLabel` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy boolean` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 6 | 100% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
