---
name: unknown_workflow_lora_sampler_unet_2
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.747437
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [PIP_图像联结, LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
members: [图片生成/图生图/2100138204581163009.json, 图片生成/图生图/2102092053311217665.json, 图片生成/图生图/2102102116562198530.json, 图片生成/图生图/2102105687684902913.json, 图片生成/图生图/2102246195535110146.json, 图片生成/图生图/2102285939048542210.json, 图片生成/图生图/2102339848425263105.json, 图片生成/图生图/2102436317866057730.json, 图片生成/图生图/2102442398138851329.json, 图片生成/图生图/2102456917401624577.json, 图片生成/图生图/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2107392595335925762.json, 图片生成/文生图/FireRed-Image-Edit 单图、双图编辑 万能图像编辑  超强图片编辑_2027222768265203714.json, 图片生成/文生图/一键换衣_2076039591257264130.json, 视频生成/图生视频/1985628103055683586.json, 视频生成/图生视频/2073634953857953794.json, 视频生成/图生视频/1986279887705178114.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/2100138204581163009.json、图片生成/图生图/2102092053311217665.json、图片生成/图生图/2102102116562198530.json、图片生成/图生图/2102105687684902913.json、图片生成/图生图/2102246195535110146.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 11/16 个有
- `PIP_图像联结` —— 11/16 个有
- `LayerUtility: ImageReel` —— 10/16 个有
- `LayerUtility: ImageReelComposit` —— 10/16 个有
- `Anything Everywhere3` —— 1/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `PrimitiveInt` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `Text Concatenate` —— 1/16 个有
- `easy imageRemBg` —— 1/16 个有
- `easy seed` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 16 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 94% |
| 调度器 | simple | - | 16 | 81% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，16 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 94%
- 调度器 最常用 simple，16 个样本，一致性 81%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（10/16 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：PIP_图像联结、LayerUtility: ImageReel、LayerUtility: ImageReelComposit
