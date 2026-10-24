---
name: unknown_workflow_controlnet_sampler_clip_4
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8868
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/59.tonnie-ZImage-CN控制_2009057459750572033.json, 图片生成/图生图/66.tonnie-Zimage controlnet2.1深度洗图_2009444441521659906.json, 图片生成/图生图/ControlNet精准控制图像生成工作流_2069079255807512577.json, 图片生成/图生图/Z-Image_turbo造像模型线性&深度预处理器工作流_2050181630404378626.json, 图片生成/文生图/Qwen2511+Fun+ControlNet+1.0_2080490152702603265.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/59.tonnie-ZImage-CN控制_2009057459750572033.json、图片生成/图生图/66.tonnie-Zimage controlnet2.1深度洗图_2009444441521659906.json、图片生成/图生图/ControlNet精准控制图像生成工作流_2069079255807512577.json、图片生成/图生图/Z-Image_turbo造像模型线性&深度预处理器工作流_2050181630404378626.json、图片生成/文生图/Qwen2511+Fun+ControlNet+1.0_2080490152702603265.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `CannyEdgePreprocessor` —— 2/5 个有
- `DepthAnythingV2Preprocessor` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PreviewAny` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 5 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
