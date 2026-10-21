---
name: unknown_workflow_lora_sampler_clip_172
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9565
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoader, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/2023308170269036545.json, 图片生成/文生图/文生图-Qwen2512-6步-模板_2023584055270313986.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_172

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/2023308170269036545.json、图片生成/文生图/文生图-Qwen2512-6步-模板_2023584055270313986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMulti` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RunningHub_ZImageI2L_Loader` —— 1/2 个有
- `RunningHub_ZImageI2L_LoraGenerator` —— 1/2 个有
- `RunningHub_ZImageI2L_Saver` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | - | 2 | 21% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1.05 | - | 2 | 95% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 28，样本不足，未给区间，2 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1.05，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
