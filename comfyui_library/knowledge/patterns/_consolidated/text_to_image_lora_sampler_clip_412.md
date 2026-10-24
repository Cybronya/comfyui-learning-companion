---
name: text_to_image_lora_sampler_clip_412
type: Text To Image
frequency: 4
level: strong
coverage: 0.81875
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, FluxResolutionNode, JjkText, KSampler, LoraLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-图生图-支持文案输入-极速版_1960977962109743106.json, 图片生成/图生图/自己用：以图生图-Qwen-Edit_1965220654645694466.json, 图片生成/文生图/Qwen-Edit-以图生图_1965105754103533569.json, 图片生成/文生图/Qwen-文生图（极速版）_1960945431024996353.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_412

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-图生图-支持文案输入-极速版_1960977962109743106.json、图片生成/图生图/自己用：以图生图-Qwen-Edit_1965220654645694466.json、图片生成/文生图/Qwen-Edit-以图生图_1965105754103533569.json、图片生成/文生图/Qwen-文生图（极速版）_1960945431024996353.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `JjkText`
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
- `CR Text Concatenate` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `Int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `easy textSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1.01 | 1.01 - 1.01 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1.01，观测区间 1.01 - 1.01，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
