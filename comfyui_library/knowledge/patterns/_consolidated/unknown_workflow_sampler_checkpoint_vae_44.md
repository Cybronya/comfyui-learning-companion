---
name: unknown_workflow_sampler_checkpoint_vae_44
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.933333
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyAceStepLatentAudio, KSampler, ModelSamplingSD3, TextEncodeAceStepAudio, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/乐器（音乐生成 速度快）_1944363862294450178.json, 音频生成/音频生成/视频生成-生成背景音乐_2003723447257735169.json, 音频生成/音频生成/视频生成-生成背景音乐_2012683689955696641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_44

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/乐器（音乐生成 速度快）_1944363862294450178.json、音频生成/音频生成/视频生成-生成背景音乐_2003723447257735169.json、音频生成/音频生成/视频生成-生成背景音乐_2012683689955696641.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyAceStepLatentAudio`
- `KSampler`
- `ModelSamplingSD3`
- `TextEncodeAceStepAudio`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `SaveAudioMP3` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 45 - 50 | 3 | 95% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 50，观测区间 45 - 50，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
