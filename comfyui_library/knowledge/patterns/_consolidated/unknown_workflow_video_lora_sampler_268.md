---
name: unknown_workflow_video_lora_sampler_268
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5608
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/主体替换WanAnimate（KJ版）_1969609216258416642.json, 平台全量/动作迁移（plus加时长版）人物替换Wan Animate2.2主体混合mix魔改加速版V1_2047224605890318337.json, 数字人/数字人/dnf_scail.json_2081553214935228418.json, 视频生成/图生视频/WanAnimate 姿势参考（KJ版）_1969999696024510466.json, 视频生成/图生视频/WanAnimate_去油版_1969228156349673474.json, 视频生成/图生视频/视频编辑视频转绘视频主体替换Wan-Animate（KJ）_1969558465037410306.json, 视频生成/图生视频/（KJ版）主体替换WanAnimate_1969378063396073473.json, 视频生成/图生视频/（KJ版）姿势参考WanAnimate_1969410370047799298.json, 视频生成/图生视频/（KJ版）姿势参考WanAnimate_1970135564894826498.json, 视频生成/文生视频/Wan Animate2.2非人类主体混合mix提示词加强+葫芦娃SAM2加速版V4（无限时长）_1969371914298925058.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_268

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/主体替换WanAnimate（KJ版）_1969609216258416642.json、平台全量/动作迁移（plus加时长版）人物替换Wan Animate2.2主体混合mix魔改加速版V1_2047224605890318337.json、数字人/数字人/dnf_scail.json_2081553214935228418.json、视频生成/图生视频/WanAnimate 姿势参考（KJ版）_1969999696024510466.json、视频生成/图生视频/WanAnimate_去油版_1969228156349673474.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 9/10 个有
- `DrawMaskOnImage` —— 9/10 个有
- `GrowMask` —— 9/10 个有
- `MathExpression|pysssss` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `PreviewImage` —— 8/10 个有
- `WanVideoSetLoRAs` —— 8/10 个有
- `LayerMask: LoadSegmentAnythingModels` —— 7/10 个有
- `LayerMask: SegmentAnythingUltra V3` —— 7/10 个有
- `WanVideoContextOptions` —— 7/10 个有
- `ImageFromBatch` —— 6/10 个有
- `Int` —— 5/10 个有
- `Textbox` —— 5/10 个有
- `GetImageSizeAndCount` —— 4/10 个有
- `ImpactInt` —— 4/10 个有
- `PixelPerfectResolution` —— 4/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `JWInteger` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `Anything Everywhere3` —— 2/10 个有
- `DF_Int_to_Float` —— 2/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `RMBG` —— 2/10 个有
- `WanVideoEncode` —— 2/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/10 个有
- `WanVideoUni3C_embeds` —— 2/10 个有
- `Anything Everywhere` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `DownloadAndLoadSAM2Model` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `RH_Captioner` —— 1/10 个有
- `Sam2Segmentation` —— 1/10 个有
- `ShowText` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy promptConcat` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
