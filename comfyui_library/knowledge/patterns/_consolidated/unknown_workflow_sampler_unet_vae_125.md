---
name: unknown_workflow_sampler_unet_vae_125
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.840667
common_nodes: [CLIPLoader, CR Prompt Text, ComfySwitchNode, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, Float, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecodeAudio, VAEDecodeAudioTiled, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/MiniMax Music音乐生成-自动提示词_2088510242186416129.json, 音频生成/音频生成/MiniMax Music音乐生成_2088133517992620034.json, 音频生成/音频生成/MiniMax Music音乐生成_2088219988443357186.json, 音频生成/音频生成/MiniMax Music音乐生成_2088243433164075009.json, 音频生成/音频生成/MiniMax Music音乐生成_2088329185046654978.json, 音频生成/音频生成/MiniMax Music音乐生成_2088620802592825345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_125

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（音频生成/音频生成/MiniMax Music音乐生成-自动提示词_2088510242186416129.json、音频生成/音频生成/MiniMax Music音乐生成_2088133517992620034.json、音频生成/音频生成/MiniMax Music音乐生成_2088219988443357186.json、音频生成/音频生成/MiniMax Music音乐生成_2088243433164075009.json、音频生成/音频生成/MiniMax Music音乐生成_2088329185046654978.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `Float`
- `KSampler`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `SeedNode`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAEDecodeAudioTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MultiTextConcatenate` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `RH_Utils` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `TextConcatenator` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 32 | 6 | 98% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 32，6 个样本，取值集中（一致性 98%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
