---
name: unknown_workflow_lora_sampler_unet_163
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.86225
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEdit_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2509，提示词改图_1987504679863169026.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，主体换背景_1987846769604276226.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，去掉光影_1987518092307795970.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，融图_1987512527364009986.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_163

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2509，提示词改图_1987504679863169026.json、图片生成/图生图/Qwen Edit 2509，社区Lora，主体换背景_1987846769604276226.json、图片生成/图生图/Qwen Edit 2509，社区Lora，去掉光影_1987518092307795970.json、图片生成/图生图/Qwen Edit 2509，社区Lora，融图_1987512527364009986.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `KSampler`
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
- `ImageAndMaskPreview` —— 2/4 个有
- `LayerMask: RmBgUltra V2` —— 2/4 个有
- `LayerUtility: CropByMask` —— 2/4 个有
- `GetImageSize+` —— 1/4 个有
- `ImageRemoveAlpha+` —— 1/4 个有
- `InvertMask` —— 1/4 个有
- `LayerUtility: ColorImage V2` —— 1/4 个有
- `LayerUtility: CropBoxResolve` —— 1/4 个有
- `LayerUtility: ImageBlendAdvance V2` —— 1/4 个有
- `LayerUtility: ImageBlendAdvance V3` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 4 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
