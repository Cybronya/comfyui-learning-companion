---
name: text_to_image_sampler_clip_unet_141
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7826
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2基础文生图（提示词扩写）_2070539846480912385.json, 图片生成/文生图/Z-iamge文生图批量版_2009171371842084866.json, 图片生成/文生图/Z-image 多图生成_2021773113834344449.json, 图片生成/文生图/Z-image多图生成（抖音）_2044693320726745089.json, 图片生成/文生图/Z-image批量文生图_2008069205383450626.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_141

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Krea2基础文生图（提示词扩写）_2070539846480912385.json、图片生成/文生图/Z-iamge文生图批量版_2009171371842084866.json、图片生成/文生图/Z-image 多图生成_2021773113834344449.json、图片生成/文生图/Z-image多图生成（抖音）_2044693320726745089.json、图片生成/文生图/Z-image批量文生图_2008069205383450626.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PromptBatchQueue` —— 4/5 个有
- `HAIGC_SaveImagesToZip` —— 3/5 个有
- `RH_LLMAPI_Pro_Node` —— 3/5 个有
- `MuyeTextEditOutput` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有
- `llama_cpp_instruct_adv` —— 1/5 个有
- `llama_cpp_model_loader` —— 1/5 个有
- `llama_cpp_parameters` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1664 | 5 | 66% |
| 高度 | 1472 | 512 - 1536 | 5 | 66% |
| 采样步数 | 10 | 8 - 10 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1664，5 个样本
- 高度 中位数 1472，观测区间 512 - 1536，5 个样本
- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
