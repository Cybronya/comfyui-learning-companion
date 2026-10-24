---
name: unknown_workflow_upscale_sampler_vae
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.771
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetImageRangeFromBatch, Image Comparer (rgthree), JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/FlashVSR&SeedVR2图像高清放大修复_1996917572320825346.json, 图片生成/文生图/FalshVSR&SeedVR2.5 4k图片高清修复_1995374682880847874.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_vae

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FlashVSR&SeedVR2图像高清放大修复_1996917572320825346.json、图片生成/文生图/FalshVSR&SeedVR2.5 4k图片高清修复_1995374682880847874.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetImageRangeFromBatch`
- `Image Comparer (rgthree)`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.77816e+08 | - | 2 | 87% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 9.77816e+08，样本不足，未给区间，2 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.10843e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
