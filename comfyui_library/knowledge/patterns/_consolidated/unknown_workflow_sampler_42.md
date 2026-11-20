---
name: unknown_workflow_sampler_42
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.835
common_nodes: [ColorCorrectOfUtils, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetImageRangeFromBatch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/flashvsr图像超清放大画质提升_2068998849661853698.json, 图片生成/图生图/flashvsr图片超清放大图片画质调整图片比例裁剪_2067511226749513730.json, 图片生成/图生图/flashvsr超清放大+画质调整 +比例裁剪_2063135348976349186.json, 图片生成/图生图/图像高清放大+画质调整+按比例裁剪_2059539851397128193.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_42

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flashvsr图像超清放大画质提升_2068998849661853698.json、图片生成/图生图/flashvsr图片超清放大图片画质调整图片比例裁剪_2067511226749513730.json、图片生成/图生图/flashvsr超清放大+画质调整 +比例裁剪_2063135348976349186.json、图片生成/图生图/图像高清放大+画质调整+按比例裁剪_2059539851397128193.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `ColorCorrectOfUtils`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetImageRangeFromBatch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.25358e+09 | 2.60432e+07 - 1.59813e+09 | 4 | 40% |
| Prompt 约束强度(CFG) | randomize | - | 4 | 100% |
| 采样算法 | 2 | 2 - 2 | 4 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.25358e+09，观测区间 2.60432e+07 - 1.59813e+09，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 最常用 randomize，4 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，4 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.59813e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
