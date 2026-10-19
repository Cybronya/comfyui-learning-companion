---
name: unknown_workflow_video_sampler_5
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.64175
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, INTConstant, ImageCropByMaskAndResize, ImageResizeKJ, LoadImage, PixelPerfectResolution, Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, SetNode, ShowText|pysssss, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/CHARM-动作迁移+面部表情-WanAnimate_1970806141703909377.json, 视频生成/图生视频/CHARM-角色替换+动作迁移+面部表情-WanAnimate_1969347581694406657.json, 视频生成/图生视频/1999709871861792770.json, 视频生成/图生视频/2011786789937221634.json, 视频生成/图生视频/1976525741590450177.json, 视频生成/图生视频/1971065537902059521.json, 视频生成/图生视频/1975054171986595841.json, 视频生成/图生视频/1983153039076958210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_5

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/CHARM-动作迁移+面部表情-WanAnimate_1970806141703909377.json、视频生成/图生视频/CHARM-角色替换+动作迁移+面部表情-WanAnimate_1969347581694406657.json、视频生成/图生视频/1999709871861792770.json、视频生成/图生视频/2011786789937221634.json、视频生成/图生视频/1976525741590450177.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `INTConstant`
- `ImageCropByMaskAndResize`
- `ImageResizeKJ`
- `LoadImage`
- `PixelPerfectResolution`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_Captioner`
- `SetNode`
- `ShowText|pysssss`
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

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 7/8 个有
- `DownloadAndLoadFlorence2Model` —— 7/8 个有
- `DownloadAndLoadSAM2Model` —— 7/8 个有
- `DrawMaskOnImage` —— 7/8 个有
- `Florence2Run` —— 7/8 个有
- `Florence2toCoordinates` —— 7/8 个有
- `GrowMask` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `ImpactSwitch` —— 7/8 个有
- `LayerUtility: PurgeVRAM V2` —— 7/8 个有
- `PrimitiveString` —— 7/8 个有
- `RH_Translator` —— 7/8 个有
- `RMBG` —— 7/8 个有
- `Sam2Segmentation` —— 7/8 个有
- `SimpleMath+` —— 7/8 个有
- `WanVideoSetBlockSwap` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `GetImageSizeAndCount` —— 6/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `WanVideoContextOptions` —— 6/8 个有
- `PreviewImage` —— 5/8 个有
- `PointsEditor` —— 4/8 个有
- `ImageFromBatch` —— 2/8 个有
- `WanVideoSLG` —— 2/8 个有
- `WanVideoTeaCache` —— 2/8 个有
- `BatchCount+` —— 1/8 个有
- `If ANY execute A else B` —— 1/8 个有
- `IfInnerExecute` —— 1/8 个有
- `ImageBatchMulti` —— 1/8 个有
- `OnnxDetectionModelLoader` —— 1/8 个有
- `PoseAndFaceDetection` —— 1/8 个有
- `RepeatImageBatch` —— 1/8 个有
- `easy batchAnything` —— 1/8 个有
- `easy compare` —— 1/8 个有
- `easy forLoopEnd` —— 1/8 个有
- `easy forLoopStart` —— 1/8 个有
- `easy ifElse` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy mathInt` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
