---
name: unknown_workflow_lora_clip_unet_9
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.988833
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/z-image-t控油+高清放大+增强细节_2022814596637134850.json, 图片生成/图生图/人物荒诞抽象特写_2034543447280984065.json, 图片生成/图生图/纸雕qwen编辑_2006298270800285697.json, 图片生成/图生图/美式卡通肖像漫画-荒诞特写_2049022001309814786.json, 图片生成/图生图/荒诞特写：造物主_2032835612440535042.json, 视频生成/图生视频/一键荒诞特写_2034914535194238977.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/z-image-t控油+高清放大+增强细节_2022814596637134850.json、图片生成/图生图/人物荒诞抽象特写_2034543447280984065.json、图片生成/图生图/纸雕qwen编辑_2006298270800285697.json、图片生成/图生图/美式卡通肖像漫画-荒诞特写_2049022001309814786.json、图片生成/图生图/荒诞特写：造物主_2032835612440535042.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `VAEEncode` —— 5/6 个有
- `TextEncodeQwenImageEditPlus` —— 4/6 个有
- `KSampler` —— 1/6 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/6 个有
- `scale` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 83% |
| Prompt 约束强度(CFG) | 5 | 1 - 9 | 6 | 54% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 9，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 67%
