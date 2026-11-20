---
name: unknown_workflow_video_clip_checkpoint
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.889125
common_nodes: [BiRefNet_Hugo, BiRefNet_ModelLoader_Zho, BiRefNet_Zho, CR Text, ChinesePrompt_Mix, EG_ZZ_TMTX, GrowMaskWithBlur, Image Comparer (rgthree), InspyrenetRembg, JoinImageWithAlpha, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerMask: LoadSegmentAnythingModels, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, LayerMask: SegmentAnythingUltra V3, LayerMask: TransparentBackgroundUltra, LayerUtility: ColorPicker, LayerUtility: ImageCombineAlpha, LayerUtility: ImageRemoveAlpha, LoadImage, LoadRembgByBiRefNetModel, Mask Invert, MaskPreview+, RH_Translator, RembgByBiRefNet, SDMatteApply, SaveImage, easy sam3ImageSegmentation, easy sam3ModelLoader, easy sam3Visualization]
problems: []
missing: []
members: [图片生成/图生图/万物皆可抠_八种方案抠图合集--附指引及模型介绍_2057711935738695682.json, 图片生成/图生图/抠图多方案工作流多方案合集_附指引及模型介绍_2026.5.10更新_2083565368009912321.json, 图片生成/图生图/抠图多方案工作流多方案合集_附指引及模型介绍_2086633510139424770.json, 图片生成/图生图/抠图多方案工作流多方案合集_附指引及模型介绍_2090280388886351874.json, 图片生成/图生图/抠图多方案工作流多方案合集_附指引及模型介绍_2095718642699821057.json, 图片生成/图生图/超级抠图多方案工作流合集_2053039140375146497.json, 平台全量/抠图多方案工作流多方案合集 附指引及模型介绍 2026.5.10更新_1975489906623516673.json, 平台全量/抠图多方案工作流（共十一中方案按需选择开启）_2100861466747424769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/万物皆可抠_八种方案抠图合集--附指引及模型介绍_2057711935738695682.json、图片生成/图生图/抠图多方案工作流多方案合集_附指引及模型介绍_2026.5.10更新_2083565368009912321.json、图片生成/图生图/抠图多方案工作流多方案合集_附指引及模型介绍_2086633510139424770.json、图片生成/图生图/抠图多方案工作流多方案合集_附指引及模型介绍_2090280388886351874.json、图片生成/图生图/抠图多方案工作流多方案合集_附指引及模型介绍_2095718642699821057.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BiRefNet_Hugo`
- `BiRefNet_ModelLoader_Zho`
- `BiRefNet_Zho`
- `CR Text`
- `ChinesePrompt_Mix`
- `EG_ZZ_TMTX`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `InspyrenetRembg`
- `JoinImageWithAlpha`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerMask: TransparentBackgroundUltra`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageCombineAlpha`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoadRembgByBiRefNetModel`
- `Mask Invert`
- `MaskPreview+`
- `RH_Translator`
- `RembgByBiRefNet`
- `SDMatteApply`
- `SaveImage`
- `easy sam3ImageSegmentation`
- `easy sam3ModelLoader`
- `easy sam3Visualization`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 7/8 个有
- `CheckpointLoaderSimple` —— 7/8 个有
- `Fast Groups Muter (rgthree)` —— 7/8 个有
- `SAM3_Detect` —— 7/8 个有
- `DrawMaskOnImage` —— 6/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `SAM3PointCollector` —— 6/8 个有
- `SAM3Propagate` —— 6/8 个有
- `SAM3VideoModelLoader` —— 6/8 个有
- `SAM3VideoOutput` —— 6/8 个有
- `SAM3VideoSegmentation` —— 6/8 个有
- `VHS_LoadVideo` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `easy cleanGpuUsed` —— 6/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
