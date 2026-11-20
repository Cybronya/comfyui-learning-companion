---
name: image_to_image_lora_sampler_clip_97
type: Image To Image
frequency: 4
level: strong
coverage: 0.6625
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetNode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein_万物精修&老照片修复_2070354521028653057.json, 图片生成/图生图/Flux2-klein万物电商产品精修&老照片修复_2073958493895348225.json, 图片生成/图生图/动漫转真人-完美复刻_2047659471861719042.json, 平台全量/Flux2-klein万物电商产品精修&老照片修复_2074050014644629506.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_97

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2-klein_万物精修&老照片修复_2070354521028653057.json、图片生成/图生图/Flux2-klein万物电商产品精修&老照片修复_2073958493895348225.json、图片生成/图生图/动漫转真人-完美复刻_2047659471861719042.json、平台全量/Flux2-klein万物电商产品精修&老照片修复_2074050014644629506.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CR Text Input Switch` —— 3/4 个有
- `CR Text Input Switch (4 way)` —— 3/4 个有
- `ImageColorMatch+` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `mxSlider` —— 3/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `Lora Loader Stack (rgthree)` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.6 - 1 | 4 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，4 个样本，取值集中（一致性 81%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
