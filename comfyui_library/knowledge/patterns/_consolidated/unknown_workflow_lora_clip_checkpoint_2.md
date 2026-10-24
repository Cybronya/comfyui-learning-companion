---
name: unknown_workflow_lora_clip_checkpoint_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DepthAnythingV2Preprocessor, DetailerForEach, FaceAnalysisModels, FaceSegmentation, Fast Groups Bypasser (rgthree), GrowMaskWithBlur, HSLColorNode, Image Comparer (rgthree), LayerColor: Brightness & Contrast, LayerColor: Color of Shadow & Highlight, LayerColor: ColorTemperature, LayerFilter: FilmV2, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader|pysssss, MaskComposite, MaskToSEGS, Masks Combine Regions, ReroutePrimitive|pysssss, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/一键人像精修磨皮工作流_1927274632234303489.json, 图片生成/图生图/一键人像精修磨皮工作流，快速增加皮肤质感_1923632531608883201.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键人像精修磨皮工作流_1927274632234303489.json、图片生成/图生图/一键人像精修磨皮工作流，快速增加皮肤质感_1923632531608883201.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DepthAnythingV2Preprocessor`
- `DetailerForEach`
- `FaceAnalysisModels`
- `FaceSegmentation`
- `Fast Groups Bypasser (rgthree)`
- `GrowMaskWithBlur`
- `HSLColorNode`
- `Image Comparer (rgthree)`
- `LayerColor: Brightness & Contrast`
- `LayerColor: Color of Shadow & Highlight`
- `LayerColor: ColorTemperature`
- `LayerFilter: FilmV2`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader|pysssss`
- `MaskComposite`
- `MaskToSEGS`
- `Masks Combine Regions`
- `ReroutePrimitive|pysssss`
- `SaveImage`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
