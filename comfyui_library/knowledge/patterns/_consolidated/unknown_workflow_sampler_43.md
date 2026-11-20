---
name: unknown_workflow_sampler_43
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.935
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetImageRangeFromBatch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/FlashVSR图像高清放大修复V1_1988299820123209730.json, 图片生成/图生图/FlashVsr高清_1998272321880227841.json, 图片生成/图生图/b-FlashVSR图像高清放大_1988961247645282305.json, 平台全量/FlashVSR图像高清放大_1991046562904252418.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_43

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FlashVSR图像高清放大修复V1_1988299820123209730.json、图片生成/图生图/FlashVsr高清_1998272321880227841.json、图片生成/图生图/b-FlashVSR图像高清放大_1988961247645282305.json、平台全量/FlashVSR图像高清放大_1991046562904252418.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetImageRangeFromBatch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageConcanate` —— 2/4 个有
- `Image Compare (mtb)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7.64483e+08 | 4.86353e+08 - 8.13826e+08 | 4 | 81% |
| Prompt 约束强度(CFG) | randomize | - | 4 | 100% |
| 采样算法 | 2 | 2 - 4 | 4 | 65% |
| 调度器 | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 7.64483e+08，观测区间 4.86353e+08 - 8.13826e+08，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 最常用 randomize，4 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 4，4 个样本
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，4 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 8.13826e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
