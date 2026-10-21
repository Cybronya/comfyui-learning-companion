---
name: unknown_workflow_upscale_sampler_clip_6
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.845
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen-2512文生图(Yihan AIGC)_2018677340422807553.json, 图片生成/文生图/Z-Image-Base 文生图+高清放大 开源基础版_2016384209975255041.json, 图片生成/文生图/Z-Image-Base 新模型懂你，文生图 直出4K_2016563209741799426.json, 图片生成/文生图/Z-image-base 文生图_2016300269142806530.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen-2512文生图(Yihan AIGC)_2018677340422807553.json、图片生成/文生图/Z-Image-Base 文生图+高清放大 开源基础版_2016384209975255041.json、图片生成/文生图/Z-Image-Base 新模型懂你，文生图 直出4K_2016563209741799426.json、图片生成/文生图/Z-image-base 文生图_2016300269142806530.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ImageScaleBy`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `DapaoImageRatioLimitNode` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `Image Filter Adjustments` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `RH_Captioner_Pro` —— 1/4 个有
- `SDXL Resolutions (JPS)` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 21 - 50 | 4 | 65% |
| Prompt 约束强度(CFG) | 4 | 3 - 4 | 4 | 88% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，观测区间 21 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 3 - 4，4 个样本，取值集中（一致性 88%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
