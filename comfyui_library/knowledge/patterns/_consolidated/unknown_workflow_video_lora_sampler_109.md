---
name: unknown_workflow_video_lora_sampler_109
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.643571
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetNode, GrowMask, ImageResizeKJv2, LoadImage, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy promptConcat]
problems: []
missing: []
members: [视频生成/图生视频/Animate人物角色替换_1970083557895008257.json, 视频生成/图生视频/Animate最强角色替换_1978476869785899009.json, 视频生成/图生视频/Wan2.2 Animate最强 视频人物角色替换V2版 15秒以上稳如老狗 工作流_1980483253431877633.json, 视频生成/图生视频/人物角色替换Animate    V2版_1979152858195070977.json, 视频生成/图生视频/人物角色替换Animate_1971412866429599745.json, 视频生成/图生视频/人物角色替换_2032500996332593153.json, 视频生成/图生视频/动作迁移  WanAnimate-KJ-V2 优化—加速_1975168158174679041.json, 视频生成/图生视频/多人物替换，优化 指定角色替换，加速 WanAnimate-KJ-V2 Infinite对口型校对_1975168163258175490.json, 视频生成/图生视频/指定人物替换 指定服装替换 Wan2.2 KJ加速 无惧切镜头SEC遮罩_1977316291763675138.json, 视频生成/图生视频/换人，角色替换，WanAnimate，对口型_2037208657041035265.json, 视频生成/图生视频/极品！！！全能视频S人物替换实现一致性 Animate V2_2039247939687686145.json, 视频生成/图生视频/电商版-视频人物替换 +口型校对_1977681903191056385.json, 视频生成/图生视频/视频人物替换 Wan Animate KJ V2 Infinite口型校对_1975168167381217282.json, 视频生成/图生视频/运镜迁移Uni3c  Wan Animate  KJ-V2 加速优化版_1973741910089142274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_109

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/Animate人物角色替换_1970083557895008257.json、视频生成/图生视频/Animate最强角色替换_1978476869785899009.json、视频生成/图生视频/Wan2.2 Animate最强 视频人物角色替换V2版 15秒以上稳如老狗 工作流_1980483253431877633.json、视频生成/图生视频/人物角色替换Animate    V2版_1979152858195070977.json、视频生成/图生视频/人物角色替换Animate_1971412866429599745.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 14 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `SimpleMath+`
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
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 13/14 个有
- `AudioSeparation` —— 11/14 个有
- `DownloadAndLoadWav2VecModel` —— 11/14 个有
- `MultiTalkModelLoader` —— 11/14 个有
- `MultiTalkWav2VecEmbeds` —— 11/14 个有
- `LayerMask: LoadSegmentAnythingModels` —— 10/14 个有
- `LayerMask: SegmentAnythingUltra V3` —— 10/14 个有
- `RH_Captioner` —— 10/14 个有
- `easy cleanGpuUsed` —— 10/14 个有
- `DWPreprocessor` —— 8/14 个有
- `FaceMaskFromPoseKeypoints` —— 8/14 个有
- `GetImageSizeAndCount` —— 8/14 个有
- `ImageCropByMaskAndResize` —— 8/14 个有
- `PixelPerfectResolution` —— 8/14 个有
- `Anything Everywhere` —— 7/14 个有
- `CR Text` —— 7/14 个有
- `EmptyImage` —— 7/14 个有
- `INTConstant` —— 7/14 个有
- `ImageConcatMulti` —— 7/14 个有
- `ImpactInt` —— 7/14 个有
- `MaskToImage` —— 7/14 个有
- `SaveAudio` —— 7/14 个有
- `Text` —— 7/14 个有
- `DrawViTPose` —— 6/14 个有
- `OnnxDetectionModelLoader` —— 6/14 个有
- `PoseAndFaceDetection` —— 6/14 个有
- `DownloadAndLoadSAM2Model` —— 4/14 个有
- `RH_LLMAPI_NODE` —— 4/14 个有
- `Sam2Segmentation` —— 4/14 个有
- `WanVideoEncode` —— 3/14 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/14 个有
- `WanVideoUni3C_embeds` —— 3/14 个有
- `ImageFromBatch` —— 2/14 个有
- `PointsEditor` —— 2/14 个有
- `SeCModelLoader` —— 2/14 个有
- `SeCVideoSegmentation` —— 2/14 个有
- `ClothesSegment` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `SaveAudioMP3` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
