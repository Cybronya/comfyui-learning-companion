---
name: unknown_workflow_inpaint_lora_sampler_37
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.840333
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GetImageSize+, InpaintCropImproved, InpaintModelConditioning, InpaintStitchImproved, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop, easy makeImageForICLora]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux万物迁移大件小件都能迁移_2054474666810585089.json, 图片生成/文生图/ACE++万物迁移换脸换产品工作流_2042897339244875777.json, 图片生成/文生图/ACE++万物迁移换脸换产品工作流_2043312251825819650.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux万物迁移大件小件都能迁移_2054474666810585089.json、图片生成/文生图/ACE++万物迁移换脸换产品工作流_2042897339244875777.json、图片生成/文生图/ACE++万物迁移换脸换产品工作流_2043312251825819650.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `InpaintCropImproved`
- `InpaintModelConditioning`
- `InpaintStitchImproved`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `GoogleTranslateTextNode` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageStitch` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `AutoCropFaces` —— 1/3 个有
- `ImageToMask` —— 1/3 个有
- `LayerMask: PersonMaskUltra` —— 1/3 个有
- `LayerUtility: CropByMask V2` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `遮罩比例扩展` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 3 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，3 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
