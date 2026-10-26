---
name: unknown_workflow_sampler_79
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.862
common_nodes: [Image Comparer (rgthree), ImageBatchRepeatInterleaving, ImageFromBatch+, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, easy imageSizeBySide]
problems: []
missing: []
members: [图片生成/图生图/图像高清修复Flash VSR FAST_1983357876649521153.json, 图片生成/图生图/图像高清修复Flash VSR SM 48G运行版_1983358618496081922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_79

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图像高清修复Flash VSR FAST_1983357876649521153.json、图片生成/图生图/图像高清修复Flash VSR SM 48G运行版_1983358618496081922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageBatchRepeatInterleaving`
- `ImageFromBatch+`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 1/2 个有
- `FlashVSR_SM_KSampler` —— 1/2 个有
- `FlashVSR_SM_Model` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.21546e+09 | - | 1 | 100% |
| Prompt 约束强度(CFG) | randomize | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 1.21546e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
