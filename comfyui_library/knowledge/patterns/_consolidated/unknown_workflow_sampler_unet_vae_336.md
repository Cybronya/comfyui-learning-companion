---
name: unknown_workflow_sampler_unet_vae_336
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6365
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, Int, KSampler, MiniMaxMusic3TextEncode, PrimitiveStringMultiline, SaveAudioAdvanced, SaveText, SeedNode, UNETLoader, VAEDecodeAudio, VAELoader, easy showAnything, ttN int, 孤海注释, 忽略多组孤海]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/MiniMax Music 3-提示词助手+迷你音乐生成工作流_2088107679498723330.json, 音频生成/音频生成/MiniMax Music 3-提示词助手+迷你音乐生成工作流_2088480751586209793.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_336

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/MiniMax Music 3-提示词助手+迷你音乐生成工作流_2088107679498723330.json、音频生成/音频生成/MiniMax Music 3-提示词助手+迷你音乐生成工作流_2088480751586209793.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `Int`
- `KSampler`
- `MiniMaxMusic3TextEncode`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `SaveText`
- `SeedNode`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `easy showAnything`
- `ttN int`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 1/2 个有
- `Float` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `VAEDecodeAudioTiled` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.7 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
