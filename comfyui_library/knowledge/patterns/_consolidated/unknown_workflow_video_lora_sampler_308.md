---
name: unknown_workflow_video_lora_sampler_308
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.505333
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetNode, GrowMask, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2049085267893555202.json, 平台全量/Animate Wan2.2视频换装工作流_1983864192195297281.json, 平台全量/Animate低配版set自动抠图_2007570467749634050.json, 平台全量/Wan2.1_1998875316565237761.json, 平台全量/Wan2.2 Animate_Wan2.1 影视人物替换_2008805512766296066.json, 平台全量/Wan2.4_1998866448049131522.json, 平台全量/Wan2.5_1998873107249123329.json, 平台全量/wan2.3_1998872337804054529.json, 平台全量/自用wan2.2_1998477831229308930.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_308

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2049085267893555202.json、平台全量/Animate Wan2.2视频换装工作流_1983864192195297281.json、平台全量/Animate低配版set自动抠图_2007570467749634050.json、平台全量/Wan2.1_1998875316565237761.json、平台全量/Wan2.2 Animate_Wan2.1 影视人物替换_2008805512766296066.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 9 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GrowMask`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
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
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `VHS_VideoInfo` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 7/9 个有
- `GetImageSizeAndCount` —— 7/9 个有
- `ImageFromBatch` —— 7/9 个有
- `Int` —— 7/9 个有
- `SeCModelLoader` —— 7/9 个有
- `SeCVideoSegmentation` —— 7/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `easy showAnything` —— 7/9 个有
- `PointsEditor` —— 6/9 个有
- `PrimitiveInt` —— 6/9 个有
- `easy imageSwitch` —— 6/9 个有
- `ImageBlend` —— 5/9 个有
- `WanVideoExperimentalArgs` —— 5/9 个有
- `WanVideoSLG` —— 5/9 个有
- `WanVideoVACEEncode` —— 5/9 个有
- `WanVideoVACEStartToEndFrame` —— 5/9 个有
- `LayerMask: SegformerB2ClothesUltra` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `JWInteger` —— 2/9 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/9 个有
- `EmptyImage` —— 1/9 个有
- `GIMMVFI_interpolate` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `PlaySound|pysssss` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
