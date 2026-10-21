---
name: unknown_workflow_upscale_sampler_clip_12
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.847667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), KSampler, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AA--加速版-Z-image Base Meancache加速+seedVR2超清放大_2019376193790808065.json, 图片生成/文生图/AA--文生图-Qwen-Image-2512-文生图+SeedVR2放大_2006397025637638146.json, 图片生成/文生图/Z-Image Turbo + LoRA 文生图高清放大2k直出工作流_2047129096592822273.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/AA--加速版-Z-image Base Meancache加速+seedVR2超清放大_2019376193790808065.json、图片生成/文生图/AA--文生图-Qwen-Image-2512-文生图+SeedVR2放大_2006397025637638146.json、图片生成/文生图/Z-Image Turbo + LoRA 文生图高清放大2k直出工作流_2047129096592822273.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `DF_Integer` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MeanCache_ZImage` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 3 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | res_multistep | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，3 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 res_multistep，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
