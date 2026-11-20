---
name: unknown_workflow_lora_sampler_unet_186
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.928
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-edit-2509-袜子迁移_1993141793747386370.json, 图片生成/图生图/qwen-edit-2509万物迁移2.0_1989172412551925762.json, 图片生成/图生图/qwen-edit-2509模特电商换装换物品换袜子电商产品图更换替换_2011512690249830401.json, 图片生成/图生图/qwen-edit-2511-换装迁移_2006598879860494338.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_186

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen-edit-2509-袜子迁移_1993141793747386370.json、图片生成/图生图/qwen-edit-2509万物迁移2.0_1989172412551925762.json、图片生成/图生图/qwen-edit-2509模特电商换装换物品换袜子电商产品图更换替换_2011512690249830401.json、图片生成/图生图/qwen-edit-2511-换装迁移_2006598879860494338.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `CR Text` —— 3/4 个有
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `图像缩放V2_孤海` —— 3/4 个有
- `Bookmark (rgthree)` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `MaskFillHoles` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 4 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | res_2s | - | 4 | 75% |
| 调度器 | bong_tangent | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 res_2s，4 个样本，一致性 75%
- 调度器 最常用 bong_tangent，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
