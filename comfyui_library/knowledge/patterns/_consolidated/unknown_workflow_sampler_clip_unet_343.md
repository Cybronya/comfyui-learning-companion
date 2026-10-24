---
name: unknown_workflow_sampler_clip_unet_343
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.714
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, HAIGC_LoadImagesFromZip, HAIGC_SaveImagesToZip, ImageFromBatch+, ImageListToBatch+, KSampler, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image批量图生图洗图zip打包下载_2010271901716848641.json, 图片生成/图生图/Z-image批量图生图洗图zip打包下载_2012719418110906370.json, 图片生成/图生图/Z-image批量洗图（zip打包）_2011621342914813953.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_343

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image批量图生图洗图zip打包下载_2010271901716848641.json、图片生成/图生图/Z-image批量图生图洗图zip打包下载_2012719418110906370.json、图片生成/图生图/Z-image批量洗图（zip打包）_2011621342914813953.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `HAIGC_LoadImagesFromZip`
- `HAIGC_SaveImagesToZip`
- `ImageFromBatch+`
- `ImageListToBatch+`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.55 | 0.55 - 0.55 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.55，观测区间 0.55 - 0.55，3 个样本，取值集中（一致性 100%）
