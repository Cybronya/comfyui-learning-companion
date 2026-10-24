---
name: unknown_workflow_upscale_sampler_clip_25
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.8495
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/002.Qwen编辑之王001.lora文生图.json_2034472907614724097.json, 图片生成/文生图/2031265164120559617.json, 图片生成/文生图/AA--8步加速-Zimage-base-蒸馏加速lora+超清放大_2026691270235660289.json, 图片生成/文生图/AA--加速版-Z-image Base Meancache加速+seedVR2超清放大_2019376193790808065.json, 图片生成/文生图/AA--文生图-Qwen-Image-2512-文生图+SeedVR2放大_2006397025637638146.json, 图片生成/文生图/Z-Image_Base+SeedVR2 （BF16版模型）高清放大RH在线工作流_2017118139036737537.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/002.Qwen编辑之王001.lora文生图.json_2034472907614724097.json、图片生成/文生图/2031265164120559617.json、图片生成/文生图/AA--8步加速-Zimage-base-蒸馏加速lora+超清放大_2026691270235660289.json、图片生成/文生图/AA--加速版-Z-image Base Meancache加速+seedVR2超清放大_2019376193790808065.json、图片生成/文生图/AA--文生图-Qwen-Image-2512-文生图+SeedVR2放大_2006397025637638146.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `INTConstant` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `ImageScaleBy` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `MeanCache_ZImage` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有
- `ModelSamplingZImage` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 8 - 50 | 6 | 11% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 6 | 40% |
| 采样算法 | euler | - | 6 | 33% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 8 - 50，6 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，6 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
