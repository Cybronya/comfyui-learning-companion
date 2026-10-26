---
name: unknown_workflow_controlnet_sampler_clip_7
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8588
common_nodes: [CLIPLoader, CLIPTextEncode, CannyEdgePreprocessor, DepthAnythingV2Preprocessor, EmptySD3LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image_controlnet_2056259479821438978.json, 图片生成/文生图/Z-Image_turbo控制ControlNet-2601_2020760393320243201.json, 图片生成/文生图/Z-Image_turbo控制图像姿势_2041507138564005890.json, 图片生成/文生图/Z-Image_turbo控制姿态ControlNe_2038525013095092225.json, 图片生成/文生图/Z-Image_turbo造像模型线性&深度预处理器工作流_2050112161892052994.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-Image_controlnet_2056259479821438978.json、图片生成/文生图/Z-Image_turbo控制ControlNet-2601_2020760393320243201.json、图片生成/文生图/Z-Image_turbo控制图像姿势_2041507138564005890.json、图片生成/文生图/Z-Image_turbo控制姿态ControlNe_2038525013095092225.json、图片生成/文生图/Z-Image_turbo造像模型线性&深度预处理器工作流_2050112161892052994.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `DepthAnythingV2Preprocessor`
- `EmptySD3LatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `CR Text` —— 1/5 个有
- `Get Image Size` —— 1/5 个有
- `HEDPreprocessor` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_multistep | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
