---
name: unknown_workflow_lora_sampler_unet_262
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.839
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), ImageAndMaskPreview, ImageConcanate, KSampler, LayerMask: RmBgUltra V2, LayerUtility: CropByMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEdit_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2509，社区Lora，主体换背景_1987846769604276226.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，融图_1987512527364009986.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_262

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2509，社区Lora，主体换背景_1987846769604276226.json、图片生成/图生图/Qwen Edit 2509，社区Lora，融图_1987512527364009986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `KSampler`
- `LayerMask: RmBgUltra V2`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEdit_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 1/2 个有
- `ImageRemoveAlpha+` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LayerUtility: ColorImage V2` —— 1/2 个有
- `LayerUtility: CropBoxResolve` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance V2` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance V3` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
