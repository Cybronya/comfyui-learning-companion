---
name: unknown_workflow_lora_sampler_clip_305
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9055
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen绘本故事出图+配音_1955973376605126657.json, 图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_305

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen绘本故事出图+配音_1955973376605126657.json、图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `IndexTTSNode` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有
- `Text` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17 | - | 2 | 24% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，样本不足，未给区间，2 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
