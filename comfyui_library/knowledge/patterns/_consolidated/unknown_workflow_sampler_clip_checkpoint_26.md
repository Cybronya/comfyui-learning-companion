---
name: unknown_workflow_sampler_clip_checkpoint_26
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.686333
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfySwitchNode, EmptyLatentAudio, JsonExtractString, KSampler, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, SaveAudioMP3, StringReplace, TextGenerate, VAEDecodeAudio]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/极速纯音乐生成 Stable Audio 3_2096940154840764418.json, 音频生成/音频生成/超快纯音乐生成stable audio 3_2058029063868084225.json, 音频生成/音频生成/音乐模型stable_audio_3_medium_2061789894426578945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_26

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/极速纯音乐生成 Stable Audio 3_2096940154840764418.json、音频生成/音频生成/超快纯音乐生成stable audio 3_2058029063868084225.json、音频生成/音频生成/音乐模型stable_audio_3_medium_2061789894426578945.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `EmptyLatentAudio`
- `JsonExtractString`
- `KSampler`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`
- `StringReplace`
- `TextGenerate`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 2/3 个有
- `CustomCombo` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy string` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 60 | 60 - 60 | 3 | 100% |
| 高度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | lcm | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 60，观测区间 60 - 60，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
