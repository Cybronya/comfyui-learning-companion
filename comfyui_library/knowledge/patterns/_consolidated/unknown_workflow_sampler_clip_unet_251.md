---
name: unknown_workflow_sampler_clip_unet_251
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8654
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ControlNet精准控制图像生成工作流_2069079255807512577.json, 图片生成/图生图/Qwen2509 人物姿态精准模仿_2015989123600883713.json, 图片生成/图生图/Qwen_模型补丁_DiffsynthControlnet_局部修复工作流1.0_1974478851558477825.json, 图片生成/图生图/Z-Image_turbo造像模型线性&深度预处理器工作流_2050181630404378626.json, 图片生成/文生图/Qwen2511+Fun+ControlNet+1.0_2080490152702603265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_251

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ControlNet精准控制图像生成工作流_2069079255807512577.json、图片生成/图生图/Qwen2509 人物姿态精准模仿_2015989123600883713.json、图片生成/图生图/Qwen_模型补丁_DiffsynthControlnet_局部修复工作流1.0_1974478851558477825.json、图片生成/图生图/Z-Image_turbo造像模型线性&深度预处理器工作流_2050181630404378626.json、图片生成/文生图/Qwen2511+Fun+ControlNet+1.0_2080490152702603265.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 4/5 个有
- `ModelPatchLoader` —— 4/5 个有
- `QwenImageDiffsynthControlnet` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `CannyEdgePreprocessor` —— 2/5 个有
- `DepthAnythingV2Preprocessor` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `InvertMask` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
