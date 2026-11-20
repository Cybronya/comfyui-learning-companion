---
name: unknown_workflow_sampler_clip_unet_252
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8734
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSamplerAdvanced, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch]
problems: []
missing: []
members: [图片生成/图生图/F2Klein手部细节修复 局部重绘_高清放大_2064525984380051457.json, 图片生成/图生图/修手 细节修复 局部重绘 高清放大_2064141358033629185.json, 图片生成/图生图/修手_细节修复_局部重绘_高清放大_2064181510172925954.json, 图片生成/图生图/真人质感 模糊变清晰 蓝神版 Klein_2061023863017918465.json, 图片生成/图生图/高清修复  高清放大  模糊图片变清晰  图像清晰修复_2062450732946771969.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_252

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/F2Klein手部细节修复 局部重绘_高清放大_2064525984380051457.json、图片生成/图生图/修手 细节修复 局部重绘 高清放大_2064141358033629185.json、图片生成/图生图/修手_细节修复_局部重绘_高清放大_2064181510172925954.json、图片生成/图生图/真人质感 模糊变清晰 蓝神版 Klein_2061023863017918465.json、图片生成/图生图/高清修复  高清放大  模糊图片变清晰  图像清晰修复_2062450732946771969.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSamplerAdvanced`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `GrowMaskWithBlur` —— 3/5 个有
- `ImpactInt` —— 3/5 个有
- `LayerUtility: CropByMask V2` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LayerUtility: ImageScaleRestore V2` —— 3/5 个有
- `LayerUtility: RestoreCropBox` —— 3/5 个有
- `Mask Fill Holes` —— 3/5 个有
- `MaskPreview+` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | sa_solver | - | 5 | 100% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，5 个样本，一致性 100%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 100%
