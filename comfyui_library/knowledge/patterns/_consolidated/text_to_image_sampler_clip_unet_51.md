---
name: text_to_image_sampler_clip_unet_51
type: Text To Image
frequency: 12
level: moderate
coverage: 0.831
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2基础文生图（提示词扩写）_2070539846480912385.json, 图片生成/文生图/Z-iamge文生图批量版_2009171371842084866.json, 图片生成/文生图/Z-image 多图生成_2021773113834344449.json, 图片生成/文生图/Z-image多图生成（抖音）_2044693320726745089.json, 图片生成/文生图/Z-image批量文生图_2008069205383450626.json, 图片生成/文生图/boogu turbo批量文生图_2070386922110930945.json, 图片生成/文生图/boogu turbo文生图批量版_2070336788392144897.json, 图片生成/文生图/boogu turbo文生图批量版_2070422555663622146.json, 图片生成/文生图/boogu turbo文生图批量版_2070469626550644737.json, 图片生成/文生图/boogu全自动文生图工作流_2071823346756575234.json, 图片生成/文生图/krea2全自动文生图工作流_2071823380147425281.json, 图片生成/文生图/krea2全自动文生图工作流_2095743937389621250.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_51

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Krea2基础文生图（提示词扩写）_2070539846480912385.json、图片生成/文生图/Z-iamge文生图批量版_2009171371842084866.json、图片生成/文生图/Z-image 多图生成_2021773113834344449.json、图片生成/文生图/Z-image多图生成（抖音）_2044693320726745089.json、图片生成/文生图/Z-image批量文生图_2008069205383450626.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 12 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `PromptBatchQueue` —— 8/12 个有
- `easy showAnything` —— 8/12 个有
- `HAIGC_SaveImagesToZip` —— 7/12 个有
- `llama_cpp_instruct_adv` —— 4/12 个有
- `llama_cpp_model_loader` —— 4/12 个有
- `llama_cpp_parameters` —— 4/12 个有
- `Any Switch (rgthree)` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `LoadImage` —— 3/12 个有
- `RH_LLMAPI_Pro_Node` —— 3/12 个有
- `ResolutionSelector` —— 3/12 个有
- `ConditioningKrea2Rebalance` —— 2/12 个有
- `MuyeTextEditOutput` —— 1/12 个有
- `TTResolutionSelector` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1664 | 12 | 64% |
| 高度 | 1504 | 512 - 1536 | 12 | 59% |
| 采样步数 | 8 | 4 - 10 | 12 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1664，12 个样本
- 高度 中位数 1504，观测区间 512 - 1536，12 个样本
- 采样步数 中位数 8，观测区间 4 - 10，12 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（8/12 个样本）：Steps较低可能导致细节不足
