---
name: text_to_image_lora_sampler_clip_196
type: Text To Image
frequency: 4
level: moderate
coverage: 0.6955
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate, easy cleanGpuUsed, CR Text, Evaluate Strings, easy anythingIndexSwitch, CR Latent Batch Size]
members: [图片生成/文生图/1959956985607303170.json, 图片生成/文生图/1960945431024996353.json, 图片生成/文生图/1965105754103533569.json, 图片生成/文生图/1970170024373743617.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_196

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1959956985607303170.json、图片生成/文生图/1960945431024996353.json、图片生成/文生图/1965105754103533569.json、图片生成/文生图/1970170024373743617.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 3/4 个有
- `CR Text Concatenate` —— 3/4 个有
- `FluxResolutionNode` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `CR Latent Batch Size` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Evaluate Strings` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.4 - 1 | 4 | 69% |
| LoRA 文本强度 | 1.01 | 0.4 - 1.01 | 4 | 69% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 800 | 4 | 79% |
| 高度 | 512 | 512 - 1200 | 4 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.4 - 1，4 个样本
- LoRA 文本强度 中位数 1.01，观测区间 0.4 - 1.01，4 个样本
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 800，4 个样本
- 高度 中位数 512，观测区间 512 - 1200，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、easy cleanGpuUsed、CR Text、Evaluate Strings、easy anythingIndexSwitch
