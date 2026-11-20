---
name: unknown_workflow_upscale_sampler_clip_43
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8605
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Base 文生图+高清放大 开源基础版_2016384209975255041.json, 图片生成/文生图/Z-Image-Base 文生图直出4K-最新写实派王者_2016306937016619010.json, 图片生成/文生图/Z-Image-Base 新模型懂你，文生图 直出4K_2016563209741799426.json, 图片生成/文生图/Z-Image-Turbo文生图4k版_1994058459186397185.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image-Base 文生图+高清放大 开源基础版_2016384209975255041.json、图片生成/文生图/Z-Image-Base 文生图直出4K-最新写实派王者_2016306937016619010.json、图片生成/文生图/Z-Image-Base 新模型懂你，文生图 直出4K_2016563209741799426.json、图片生成/文生图/Z-Image-Turbo文生图4k版_1994058459186397185.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `DapaoImageRatioLimitNode` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `RH_Captioner_Pro` —— 1/4 个有
- `SDXL Resolutions (JPS)` —— 1/4 个有
- `Text` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 8 - 50 | 4 | 51% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 4 | 59% |
| 采样算法 | res_multistep | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 35，观测区间 8 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，4 个样本
- 采样算法 最常用 res_multistep，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
