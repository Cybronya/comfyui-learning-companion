---
name: unknown_workflow_controlnet_video_lora_18
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.952429
common_nodes: [CLIPVisionLoader, DWPreprocessor, GetImageSizeAndCount, ImageConcatMulti, JoinStrings, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PixelPerfectResolution, PrimitiveStringMultiline, RH_Captioner, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/WAN-AnimateV2_1980263044716670978.json, 平台全量/动作模仿（更加融入环境）_1995702836300230658.json, 平台全量/🦖WAN-Animate face and pose_1971404384703856641.json, 数字人/数字人/bl动作_2017570006296436738.json, 视频生成/图生视频/动作迁移+可多镜头+面部表情参考_1982728839811997698.json, 视频生成/图生视频/动作迁移+面部表情参考 (长视频版本）_1982639964624175105.json, 视频生成/图生视频/动作迁移+面部表情参考-WAN-AnimateV2_1971179799987265537.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_18

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/WAN-AnimateV2_1980263044716670978.json、平台全量/动作模仿（更加融入环境）_1995702836300230658.json、平台全量/🦖WAN-Animate face and pose_1971404384703856641.json、数字人/数字人/bl动作_2017570006296436738.json、视频生成/图生视频/动作迁移+可多镜头+面部表情参考_1982728839811997698.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `JoinStrings`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PixelPerfectResolution`
- `PrimitiveStringMultiline`
- `RH_Captioner`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawViTPose` —— 6/7 个有
- `OnnxDetectionModelLoader` —— 6/7 个有
- `PoseAndFaceDetection` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `easy int` —— 5/7 个有
- `LayerUtility: ColorImage V2` —— 3/7 个有
- `LayerUtility: ImageBlend` —— 3/7 个有
- `easy anythingIndexSwitch` —— 3/7 个有
- `Int` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `ApplyFaceProcessor` —— 1/7 个有
- `FaceMaskFromPoseKeypoints` —— 1/7 个有
- `FaceProcessorLoader` —— 1/7 个有
- `ImageListToImageBatch` —— 1/7 个有
- `ImpactImageBatchToImageList` —— 1/7 个有
- `LayerUtility: CropByMask V2` —— 1/7 个有
- `MasksToMaskList` —— 1/7 个有
- `MyOpenPoseNode` —— 1/7 个有
- `OpenposePreprocessor` —— 1/7 个有
- `VideoInputPreprocessor` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
