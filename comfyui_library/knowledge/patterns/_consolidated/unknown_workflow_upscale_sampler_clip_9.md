---
name: unknown_workflow_upscale_sampler_clip_9
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.906364
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageResizeKJv2, ImageScaleBy, ImageUpscaleWithModel, KSampler, LatentNoised, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, SaveImage, Seed (rgthree), ShowText|pysssss, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/图片质感修复 细节增强 I2I+高清修复+去除AI感 Z-image+_2086630330550804481.json, 图片生成/图生图/细节增强 I2I+高清修复+去除AI感 Z-image+_2084816177175556098.json, 图片生成/图生图/细节增强+I2I+高清修复+去除AI感+Z-image+_2088063933524566017.json, 图片生成/图生图/细节增强+I2I+高清修复+去除AI感+Z-image+_2091700703575236610.json, 图片生成/图生图/细节增强+I2I+高清修复+去除AI感+Z-image+_2091832452590424065.json, 图片生成/图生图/细节增强_I2I+高清修复+去除AI感_Z-image+_2084909208365002754.json, 图片生成/图生图/细节增强_I2I+高清修复+去除AI感_Z-image+_2084913885353701377.json, 图片生成/图生图/细节增强_I2I+高清修复+去除AI感_Z-image+_2088520442444341249.json, 图片生成/图生图/细节增强_Z-image I2I 高清修复 去除AI感_2006290972799406082.json, 图片生成/图生图/细节增强_高清放大修复+去除AI感_Z-image_SeedVR2_2077568734268583938.json, 图片生成/图生图/细节增强_高清放大修复+去除AI感_Z-image_SeedVR2_2077933739077885954.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/图片质感修复 细节增强 I2I+高清修复+去除AI感 Z-image+_2086630330550804481.json、图片生成/图生图/细节增强 I2I+高清修复+去除AI感 Z-image+_2084816177175556098.json、图片生成/图生图/细节增强+I2I+高清修复+去除AI感+Z-image+_2088063933524566017.json、图片生成/图生图/细节增强+I2I+高清修复+去除AI感+Z-image+_2091700703575236610.json、图片生成/图生图/细节增强+I2I+高清修复+去除AI感+Z-image+_2091832452590424065.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LatentNoised`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UpscaleModelLoader` —— 9/11 个有
- `Upscale Model Loader` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 3 - 3 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 0.15 | 0.15 - 0.15 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 11/11 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 3，观测区间 3 - 3，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 0.15，观测区间 0.15 - 0.15，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
- 高发问题（11/11 个样本）：发现KSampler但没有VAEDecode
