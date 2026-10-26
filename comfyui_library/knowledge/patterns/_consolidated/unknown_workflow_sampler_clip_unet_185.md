---
name: unknown_workflow_sampler_clip_unet_185
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.868286
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelPatchLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Z-Image ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1997645811326586881.json, 图片生成/图生图/59.tonnie-ZImage-CN控制_2009057459750572033.json, 图片生成/图生图/66.tonnie-Zimage controlnet2.1深度洗图_2009444441521659906.json, 图片生成/图生图/Z-IMAGE+Controlnet_2004837379913515010.json, 图片生成/图生图/Z-Image+CN2.0洗图神器_2000462790190133250.json, 图片生成/图生图/Z-Image+CN2.1All In One_2003517827271303169.json, 图片生成/文生图/快速生图三剑客：Z-Image、ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1996753267008884738.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_185

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Z-Image ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1997645811326586881.json、图片生成/图生图/59.tonnie-ZImage-CN控制_2009057459750572033.json、图片生成/图生图/66.tonnie-Zimage controlnet2.1深度洗图_2009444441521659906.json、图片生成/图生图/Z-IMAGE+Controlnet_2004837379913515010.json、图片生成/图生图/Z-Image+CN2.0洗图神器_2000462790190133250.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 6/7 个有
- `QwenImageDiffsynthControlnet` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `AILab_QwenVL` —— 4/7 个有
- `Label (rgthree)` —— 4/7 个有
- `PreviewAny` —— 4/7 个有
- `GetImageSize` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `Canny` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `PixelPerfectResolution` —— 2/7 个有
- `Qwen3_VQA` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `ImageSharpen` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `ZImageFunControlnet` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 10 | 7 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | res_multistep | - | 7 | 57% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 10，7 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
