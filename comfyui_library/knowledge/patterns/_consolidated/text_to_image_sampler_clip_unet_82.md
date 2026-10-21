---
name: text_to_image_sampler_clip_unet_82
type: Text To Image
frequency: 6
level: moderate
coverage: 0.842667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2基础文生图_2070504244750405634.json, 图片生成/文生图/Krea2基础文生图（提示词扩写）_2070539846480912385.json, 图片生成/文生图/Z-iamge文生图批量版_2009171371842084866.json, 图片生成/文生图/Z-image 多图生成_2021773113834344449.json, 图片生成/文生图/Z-image批量文生图_2008069205383450626.json, 图片生成/文生图/全自动krea2文生图_2070721265224216578.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_82

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Krea2基础文生图_2070504244750405634.json、图片生成/文生图/Krea2基础文生图（提示词扩写）_2070539846480912385.json、图片生成/文生图/Z-iamge文生图批量版_2009171371842084866.json、图片生成/文生图/Z-image 多图生成_2021773113834344449.json、图片生成/文生图/Z-image批量文生图_2008069205383450626.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `PromptBatchQueue` —— 3/6 个有
- `RH_LLMAPI_Pro_Node` —— 3/6 个有
- `TTResolutionSelector` —— 3/6 个有
- `HAIGC_SaveImagesToZip` —— 2/6 个有
- `llama_cpp_instruct_adv` —— 2/6 个有
- `llama_cpp_model_loader` —— 2/6 个有
- `llama_cpp_parameters` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1104 | 6 | 65% |
| 高度 | 992 | 512 - 1536 | 6 | 50% |
| 采样步数 | 9 | 8 - 10 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1104，6 个样本
- 高度 中位数 992，观测区间 512 - 1536，6 个样本
- 采样步数 中位数 9，观测区间 8 - 10，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
