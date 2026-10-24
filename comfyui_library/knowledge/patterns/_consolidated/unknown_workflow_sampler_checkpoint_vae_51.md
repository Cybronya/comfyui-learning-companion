---
name: unknown_workflow_sampler_checkpoint_vae_51
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyAceStepLatentAudio, KSampler, ModelSamplingSD3, SaveAudio, TextEncodeAceStepAudio, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/乐器（音乐生成 速度快）_1944363862294450178.json, 音频生成/音频生成/视频生成-生成背景音乐_2003723447257735169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_51

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/乐器（音乐生成 速度快）_1944363862294450178.json、音频生成/音频生成/视频生成-生成背景音乐_2003723447257735169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyAceStepLatentAudio`
- `KSampler`
- `ModelSamplingSD3`
- `SaveAudio`
- `TextEncodeAceStepAudio`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 47.5 | - | 2 | 95% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 47.5，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
