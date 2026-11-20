---
name: image_to_image_lora_sampler_clip_90
type: Image To Image
frequency: 3
level: strong
coverage: 0.673333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetNode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein_万物精修&老照片修复_2070354521028653057.json, 图片生成/图生图/Flux2-klein万物电商产品精修&老照片修复_2073958493895348225.json, 图片生成/图生图/动漫转真人-完美复刻_2047659471861719042.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2-klein_万物精修&老照片修复_2070354521028653057.json、图片生成/图生图/Flux2-klein万物电商产品精修&老照片修复_2073958493895348225.json、图片生成/图生图/动漫转真人-完美复刻_2047659471861719042.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Input Switch` —— 2/3 个有
- `CR Text Input Switch (4 way)` —— 2/3 个有
- `ImageColorMatch+` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `mxSlider` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `Lora Loader Stack (rgthree)` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.6 - 1 | 3 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
