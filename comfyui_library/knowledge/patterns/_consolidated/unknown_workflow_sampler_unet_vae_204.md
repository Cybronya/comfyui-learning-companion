---
name: unknown_workflow_sampler_unet_vae_204
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.703333
common_nodes: [CLIPLoader, ComfySwitchNode, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecodeAudio, VAEDecodeAudioTiled, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/Minimax-Music3 音乐生成神器 开源版！带官方skill自动优化节点_2089299030575771650.json, 音频生成/音频生成/Minimax-Music3开源版_2092083462328111106.json, 音频生成/音频生成/MinimaxMusic3 音乐生成器_2089599054853533698.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_204

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/Minimax-Music3 音乐生成神器 开源版！带官方skill自动优化节点_2089299030575771650.json、音频生成/音频生成/Minimax-Music3开源版_2092083462328111106.json、音频生成/音频生成/MinimaxMusic3 音乐生成器_2089599054853533698.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CR Text` —— 2/3 个有
- `DapaoMusic3CaptionPromptNode` —— 2/3 个有
- `PrimitiveString` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `easy saveText` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
