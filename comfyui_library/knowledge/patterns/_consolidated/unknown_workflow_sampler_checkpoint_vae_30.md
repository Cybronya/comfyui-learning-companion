---
name: unknown_workflow_sampler_checkpoint_vae_30
type: Unknown Workflow
frequency: 4
level: strong
coverage: 1
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyAceStepLatentAudio, KSampler, ModelSamplingSD3, PreviewAudio, TextEncodeAceStepAudio, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/Ace-step 音乐生成_1926228432416370689.json, 音频生成/音频生成/Ace-step_纯音乐快速生成工作流_1965832137704386561.json, 音频生成/音频生成/ace step生成音乐_2010334449979891713.json, 音频生成/音频生成/视频生成-生成背景音乐_2012683689955696641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_30

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Ace-step 音乐生成_1926228432416370689.json、音频生成/音频生成/Ace-step_纯音乐快速生成工作流_1965832137704386561.json、音频生成/音频生成/ace step生成音乐_2010334449979891713.json、音频生成/音频生成/视频生成-生成背景音乐_2012683689955696641.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyAceStepLatentAudio`
- `KSampler`
- `ModelSamplingSD3`
- `PreviewAudio`
- `TextEncodeAceStepAudio`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `SaveAudioMP3` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `VAEDecode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | res_multistep | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：发现KSampler但没有VAEDecode
