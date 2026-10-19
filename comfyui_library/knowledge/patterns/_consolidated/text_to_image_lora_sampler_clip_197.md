---
name: text_to_image_lora_sampler_clip_197
type: Text To Image
frequency: 4
level: strong
coverage: 0.781
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, easy cleanGpuUsed, ttN concat, CR Text Concatenate]
members: [图片生成/文生图/1965625145698209793.json, 图片生成/文生图/1970876758574698497.json, 图片生成/文生图/1975417957952172034.json, 图片生成/文生图/1988803647096098817.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_197

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1965625145698209793.json、图片生成/文生图/1970876758574698497.json、图片生成/文生图/1975417957952172034.json、图片生成/文生图/1988803647096098817.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ImpactSwitch` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `SaveImagePlus` —— 1/4 个有
- `ShowText` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy cleanGpuUsed、ttN concat、CR Text Concatenate
