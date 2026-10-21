---
name: unknown_workflow_upscale_clip_unet
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.870333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Base 文生图直出4K-最新写实派王者_2016306937016619010.json, 图片生成/文生图/Z-Image-Turbo文生图4k版_1994058459186397185.json, 图片生成/文生图/Z-image-base 兼顾 Z-image-turbo lora 双采样工作流_2067512561997795329.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Image-Base 文生图直出4K-最新写实派王者_2016306937016619010.json、图片生成/文生图/Z-Image-Turbo文生图4k版_1994058459186397185.json、图片生成/文生图/Z-image-base 兼顾 Z-image-turbo lora 双采样工作流_2067512561997795329.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `Text` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `CLIPLoaderGGUF` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `Lora Loader Stack (rgthree)` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 3 | 1 - 8 | 3 | 26% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 24，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 8，3 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
