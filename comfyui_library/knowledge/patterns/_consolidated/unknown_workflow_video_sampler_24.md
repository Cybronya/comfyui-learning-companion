---
name: unknown_workflow_video_sampler_24
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.634857
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, INTConstant, ImageCropByMaskAndResize, LoadImage, PixelPerfectResolution, Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, SetNode, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, easy anythingIndexSwitch, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [平台全量/动作转换_1974670510976053250.json, 平台全量/动作迁移WanAnimate_1969415386640883714.json, 平台全量/多人提示词替换工作流wan2.2 mm_1975819490330021889.json, 平台全量/视频角色替换-动作迁移-面部表情_2008121907756929026.json, 视频生成/图生视频/CHARM-角色替换+动作迁移+面部表情-WanAnimate_1969347581694406657.json, 视频生成/图生视频/Wan2.2 Animate（动作迁移稳定版）长视频循环48G_1999709871861792770.json, 视频生成/图生视频/角色替换+动作迁移+面部表情 Wan2.2 Animate Sam2_1999438379999690753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_24

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/动作转换_1974670510976053250.json、平台全量/动作迁移WanAnimate_1969415386640883714.json、平台全量/多人提示词替换工作流wan2.2 mm_1975819490330021889.json、平台全量/视频角色替换-动作迁移-面部表情_2008121907756929026.json、视频生成/图生视频/CHARM-角色替换+动作迁移+面部表情-WanAnimate_1969347581694406657.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `INTConstant`
- `ImageCropByMaskAndResize`
- `LoadImage`
- `PixelPerfectResolution`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_Captioner`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 6/7 个有
- `DownloadAndLoadSAM2Model` —— 6/7 个有
- `DrawMaskOnImage` —— 6/7 个有
- `GrowMask` —— 6/7 个有
- `ImageResizeKJ` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `RMBG` —— 6/7 个有
- `Sam2Segmentation` —— 6/7 个有
- `WanVideoSetBlockSwap` —— 6/7 个有
- `DownloadAndLoadFlorence2Model` —— 5/7 个有
- `Florence2Run` —— 5/7 个有
- `Florence2toCoordinates` —— 5/7 个有
- `ImpactSwitch` —— 5/7 个有
- `LayerUtility: PurgeVRAM V2` —— 5/7 个有
- `PrimitiveString` —— 5/7 个有
- `RH_Translator` —— 5/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `WanVideoContextOptions` —— 4/7 个有
- `PointsEditor` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `WanVideoSLG` —— 3/7 个有
- `WanVideoTeaCache` —— 3/7 个有
- `BBoxesToSAM2` —— 1/7 个有
- `BatchCount+` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `DownloadAndLoadQwenModel` —— 1/7 个有
- `If ANY execute A else B` —— 1/7 个有
- `IfInnerExecute` —— 1/7 个有
- `ImageBatchGet` —— 1/7 个有
- `ImageBatchMulti` —— 1/7 个有
- `ImageFromBatch` —— 1/7 个有
- `Int` —— 1/7 个有
- `LayerMask: SAM2VideoUltra` —— 1/7 个有
- `OnnxDetectionModelLoader` —— 1/7 个有
- `PoseAndFaceDetection` —— 1/7 个有
- `QwenVLDetection` —— 1/7 个有
- `RepeatImageBatch` —— 1/7 个有
- `easy batchAnything` —— 1/7 个有
- `easy compare` —— 1/7 个有
- `easy forLoopEnd` —— 1/7 个有
- `easy forLoopStart` —— 1/7 个有
- `easy ifElse` —— 1/7 个有
- `easy int` —— 1/7 个有
- `easy mathInt` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
