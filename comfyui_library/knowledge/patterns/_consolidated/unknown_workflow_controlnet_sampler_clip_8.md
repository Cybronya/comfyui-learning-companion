---
name: unknown_workflow_controlnet_sampler_clip_8
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8615
common_nodes: [CLIPLoader, CLIPTextEncode, CannyEdgePreprocessor, DepthAnythingV2Preprocessor, EmptySD3LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image_controlnet_2056259479821438978.json, 图片生成/文生图/Z-Image_turbo控制ControlNet-2601_2020760393320243201.json, 图片生成/文生图/Z-Image_turbo控制图像姿势_2041507138564005890.json, 图片生成/文生图/Z-Image_turbo控制姿态ControlNe_2038525013095092225.json, 图片生成/文生图/Z-Image_turbo造像模型线性&深度预处理器工作流_2050112161892052994.json, 平台全量/Z-Image_turbo控制 姿势迁移ControlNet 精准控制2.1版动作复制_2021066048845389826.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image_controlnet_2056259479821438978.json、图片生成/文生图/Z-Image_turbo控制ControlNet-2601_2020760393320243201.json、图片生成/文生图/Z-Image_turbo控制图像姿势_2041507138564005890.json、图片生成/文生图/Z-Image_turbo控制姿态ControlNe_2038525013095092225.json、图片生成/文生图/Z-Image_turbo造像模型线性&深度预处理器工作流_2050112161892052994.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
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
- `DWPreprocessor` —— 5/6 个有
- `GetImageSize` —— 5/6 个有
- `CR Text` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `Get Image Size` —— 1/6 个有
- `HEDPreprocessor` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `Qwen3_VQA` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_multistep | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
