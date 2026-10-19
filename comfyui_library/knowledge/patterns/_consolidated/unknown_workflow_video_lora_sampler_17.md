---
name: unknown_workflow_video_lora_sampler_17
type: Unknown Workflow
frequency: 33
level: moderate
coverage: 0.575394
common_nodes: [BBoxYOLO, BatchCount+, CLIPVisionLoader, CR Text, CheckpointLoaderSimple, DrawViTPose, ImageBatch, ImageFromBatch, ImageResizeKJv2, ImpactSwitch, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, LazySwitch2way, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, RepeatImageBatch, SDPoseDrawKeypoints, SDPoseKeypointExtractor, VHS_LoadVideo, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, YOLOModelLoader, easy anythingIndexSwitch, easy boolean, easy compare, easy float, easy imageSize, easy int, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/2052262207102177281.json, 视频生成/图生视频/Action Transfer 视频动作迁移 Animate_2096773886733021185.json, 视频生成/图生视频/2071942874186477570.json, 视频生成/图生视频/Animate 动作迁移+表情+手部一致性 三种模式切换可多人_2092922363200495617.json, 视频生成/图生视频/2067865822789455873.json, 视频生成/图生视频/2067572288576376834.json, 视频生成/图生视频/2082104573845663745.json, 视频生成/图生视频/AnimateV9动作迁移人物动作模仿_2091532232967151618.json, 视频生成/图生视频/Animate动作迁移V9（plus)_2088492819714498561.json, 视频生成/图生视频/2067158640880078849.json, 视频生成/图生视频/Animate动作迁移V9（自动尺寸）PLUS_2083515980403265537.json, 视频生成/图生视频/Animate动作迁移V9（自动尺寸）_优化版V1_2087512134681980930.json, 视频生成/图生视频/Animate动作迁移V9（自动尺寸）优化版V2_2087495748442214401.json, 视频生成/图生视频/2063224518570758145.json, 视频生成/图生视频/2063576371754000385.json, 视频生成/图生视频/2065412383627112450.json, 视频生成/图生视频/2066779159443107841.json, 视频生成/图生视频/2066883170611585025.json, 视频生成/图生视频/2067591708271013889.json, 视频生成/图生视频/2067591863569309697.json, 视频生成/图生视频/Coze_Drive_动作迁移_V9_608x1088_固定版_2094292856751083522.json, 视频生成/图生视频/Wan2.2-Animate-Move&Mix-V1_2101929816374206466.json, 视频生成/图生视频/2054929094915174402.json, 视频生成/图生视频/1948362216455188482.json, 视频生成/图生视频/2056283340306735106.json, 视频生成/图生视频/2075410824641990657.json, 视频生成/图生视频/2051928447810846722.json, 视频生成/图生视频/2065796439602720769.json, 视频生成/图生视频/2045493013840928770.json, 视频生成/图生视频/2052770687701528577.json, 视频生成/图生视频/2060202203054432257.json, 视频生成/图生视频/2081637987401687042.json, 视频生成/图生视频/2080519359495237633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 33 个 workflow 归纳得出（视频生成/图生视频/2052262207102177281.json、视频生成/图生视频/Action Transfer 视频动作迁移 Animate_2096773886733021185.json、视频生成/图生视频/2071942874186477570.json、视频生成/图生视频/Animate 动作迁移+表情+手部一致性 三种模式切换可多人_2092922363200495617.json、视频生成/图生视频/2067865822789455873.json…）

- **类型**：Unknown Workflow
- **样本数**：33
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 33 个 workflow 都包含：
- `BBoxYOLO`
- `BatchCount+`
- `CLIPVisionLoader`
- `CR Text`
- `CheckpointLoaderSimple`
- `DrawViTPose`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch1way`
- `LazySwitch2way`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `RHHiddenNodes`
- `RepeatImageBatch`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy anythingIndexSwitch`
- `easy boolean`
- `easy compare`
- `easy float`
- `easy imageSize`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 32/33 个有
- `GetNode` —— 31/33 个有
- `SetNode` —— 31/33 个有
- `WanVideoEncode` —— 31/33 个有
- `WanVideoUni3C_ControlnetLoader` —— 31/33 个有
- `WanVideoUni3C_embeds` —— 31/33 个有
- `easy cleanGpuUsed` —— 31/33 个有
- `CompressImages` —— 29/33 个有
- `VideoCombineNode` —— 29/33 个有
- `ZML_AnyTypeSwitchFiveBoolean` —— 28/33 个有
- `BodyRatioMapperProportionTransfer` —— 26/33 个有
- `BodyRatioMapperSDPoseRender` —— 26/33 个有
- `ImageScaleToTotalPixels` —— 26/33 个有
- `Bool` —— 22/33 个有
- `PreviewImage` —— 17/33 个有
- `LayerUtility: ColorImage V2` —— 15/33 个有
- `孤海注释` —— 15/33 个有
- `SimpleMath+` —— 10/33 个有
- `easy showAnything` —— 8/33 个有
- `DownloadAndLoadNLFModel` —— 7/33 个有
- `NLFPredict` —— 7/33 个有
- `PoseDetectionVitPoseToDWPose` —— 7/33 个有
- `RenderNLFPoses` —— 7/33 个有
- `SaveImage` —— 7/33 个有
- `TT_img_enc` —— 7/33 个有
- `Any Switch (rgthree)` —— 2/33 个有
- `AnyBooleanSwitch` —— 2/33 个有
- `BlockifyMask` —— 2/33 个有
- `DownloadAndLoadSAM2Model` —— 2/33 个有
- `DrawMaskOnImage` —— 2/33 个有
- `Fast Groups Bypasser (rgthree)` —— 2/33 个有
- `GrowMaskWithBlur` —— 2/33 个有
- `MemoryCleaner` —— 2/33 个有
- `PrimitiveBoolean` —— 2/33 个有
- `Sam2Segmentation` —— 2/33 个有
- `CM_FloatToInt` —— 1/33 个有
- `easy sam3ModelLoader` —— 1/33 个有
- `easy sam3VideoSegmentation` —— 1/33 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
