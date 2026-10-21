---
name: unknown_workflow_lora_sampler_clip_169
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, NunchakuQwenImageDiTLoader, NunchakuQwenImageLoraStack, SDXLEmptyLatentSizePicker+, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [SDXLEmptyLatentSizePicker+, easy promptConcat]
members: [图片生成/文生图/1982787768378109953.json, 图片生成/文生图/图片用这个_2023321341348290562.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_169

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1982787768378109953.json、图片生成/文生图/图片用这个_2023321341348290562.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `NunchakuQwenImageDiTLoader`
- `NunchakuQwenImageLoraStack`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 1/2 个有
- `NunchakuQwenImageLoraLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | kl_optimal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | disable | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 kl_optimal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：SDXLEmptyLatentSizePicker+、easy promptConcat
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
