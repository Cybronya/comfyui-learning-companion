---
name: unknown_workflow_sampler_4
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.856091
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, Get Image Size, GetImageRangeFromBatch, ImageCASharpening+, ImageResize+, ImpactMinMax, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, SaveImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch]
problems: []
missing: []
members: [图片生成/图生图/03-17-04-WAN2.1-图片高清放大-FlashVsr1.1+SeedVR2.5+TTP分块_2000041264647110658.json, 图片生成/图生图/2K图像超清放大工作流  浮云_1998297538107203585.json, 图片生成/图生图/一键8K图像超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1995018321785499649.json, 图片生成/图生图/图片高清放大修复FlashVSR+SeedVR2.5_2001462449176014850.json, 图片生成/图生图/最强8K图像超清放大工作流  浮云_1995307793727074305.json, 图片生成/图生图/最强8K图像高清超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1994746471113166850.json, 图片生成/图生图/最强8K图像高清超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1994991712038793217.json, 图片生成/图生图/漫剧专用 8K直出 极致细节_2045575557361967105.json, 图片生成/图生图/超强8K放大修复-极致细节，毫厘必现_1995113403595284482.json, 图片生成/图生图/（能力层调用）图像4K放大_2066692074161926145.json, 图片生成/图生图/（能力层调用）图像4K放大_2067512612836958210.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_4

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/03-17-04-WAN2.1-图片高清放大-FlashVsr1.1+SeedVR2.5+TTP分块_2000041264647110658.json、图片生成/图生图/2K图像超清放大工作流  浮云_1998297538107203585.json、图片生成/图生图/一键8K图像超清放大修复FlashVsr1.1+SeedVR2.5+TTP分块_1995018321785499649.json、图片生成/图生图/图片高清放大修复FlashVSR+SeedVR2.5_2001462449176014850.json、图片生成/图生图/最强8K图像超清放大工作流  浮云_1995307793727074305.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `Get Image Size`
- `GetImageRangeFromBatch`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 10/11 个有
- `Image Comparer (rgthree)` —— 9/11 个有
- `JWInteger` —— 8/11 个有
- `ImageConcanate` —— 6/11 个有
- `PreviewImage` —— 6/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.30362e+09 | 4.56375e+08 - 2.0998e+09 | 11 | 50% |
| Prompt 约束强度(CFG) | randomize | - | 11 | 100% |
| 采样算法 | 2 | 2 - 2 | 11 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 11 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.30362e+09，观测区间 4.56375e+08 - 2.0998e+09，11 个样本
- Prompt 约束强度(CFG) 最常用 randomize，11 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，11 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，11 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，11 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.0998e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
