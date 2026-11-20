---
name: unknown_workflow_lora_sampler_unet_63
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8398
common_nodes: [CLIPLoader, GetImageSize, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SkipLayerGuidanceDiTSimple, TextEncodeMOSSImageEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MOSS Image 单图_多图 编辑_2115834115940507650.json, 图片生成/图生图/MOSS Image 单图编辑_2115255529105874945.json, 图片生成/图生图/MOSS_Image_单图编辑_2115317200344145922.json, 图片生成/图生图/MOSS多图参考编辑_2116064786747322370.json, 图片生成/图生图/MOSS多图参考编辑_2116674769302147073.json, 图片生成/图生图/moss image-edit-图像编辑_2115603254800371714.json, 图片生成/图生图/moss-图像编辑流-8步_2115992063287316481.json, 图片生成/图生图/moss-图像编辑流_2115952535369510913.json, 图片生成/图生图/基于MOSS多图参考编辑_2115999755930259457.json, 平台全量/2026-11-03 Moss-Image-t2i 图像编辑_2117100189843542017.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_63

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/MOSS Image 单图_多图 编辑_2115834115940507650.json、图片生成/图生图/MOSS Image 单图编辑_2115255529105874945.json、图片生成/图生图/MOSS_Image_单图编辑_2115317200344145922.json、图片生成/图生图/MOSS多图参考编辑_2116064786747322370.json、图片生成/图生图/MOSS多图参考编辑_2116674769302147073.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `TextEncodeMOSSImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 9/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `JjkText` —— 6/10 个有
- `ImageCompare` —— 2/10 个有
- `EmptyLatentImage` —— 1/10 个有
- `ModelSamplingAuraFlow` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 40 | 10 | 74% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 10 | 74% |
| 采样算法 | er_sde | - | 10 | 60% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 40，10 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，10 个样本
- 采样算法 最常用 er_sde，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
