---
name: unknown_workflow_sampler_clip_unet_102
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7878
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Moss-image+Base文生图高质量加速版V2(Un版)_2112816236777267202.json, 图片生成/图生图/Moss-image+SFT文生图高质量加速版V2(Un版)_2112816043226918914.json, 图片生成/图生图/flux3_klein_多参考_2111077778098573313.json, 图片生成/文生图/FLUX3 Image Klein 文生图_2111346567927123970.json, 图片生成/文生图/FLUX3 Image Klein 文生图（修复版·中文繁体招牌王）_2111323705954623489.json, 图片生成/文生图/Moss-image Sft文生图_自动词优化版_2112493550918258689.json, 图片生成/文生图/Moss-image Sft文生图_自动词优化版_2112499136711979009.json, 图片生成/文生图/flux3-image-klein（文生图）_2110956174114910210.json, 图片生成/文生图/【遇见AI】flux3 image 蒸馏版文生图基础流_2111000814536978434.json, 图片生成/文生图/图像编辑 FLUX 3 Image Klein_2112063690060156930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_102

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Moss-image+Base文生图高质量加速版V2(Un版)_2112816236777267202.json、图片生成/图生图/Moss-image+SFT文生图高质量加速版V2(Un版)_2112816043226918914.json、图片生成/图生图/flux3_klein_多参考_2111077778098573313.json、图片生成/文生图/FLUX3 Image Klein 文生图_2111346567927123970.json、图片生成/文生图/FLUX3 Image Klein 文生图（修复版·中文繁体招牌王）_2111323705954623489.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 9/10 个有
- `PreviewAny` —— 6/10 个有
- `TextGenerate` —— 5/10 个有
- `LoadImage` —— 4/10 个有
- `MOSSImageBlockCacheT8` —— 2/10 个有
- `MOSSImagePromptEnhancerT8` —— 2/10 个有
- `ReferenceMultiLatent` —— 2/10 个有
- `BatchImagesNode` —— 1/10 个有
- `ComfySwitchNode` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20.5 | 15 - 50 | 10 | 47% |
| Prompt 约束强度(CFG) | 2 | 1 - 3.5 | 10 | 48% |
| 采样算法 | euler | - | 10 | 60% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20.5，观测区间 15 - 50，10 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 3.5，10 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
