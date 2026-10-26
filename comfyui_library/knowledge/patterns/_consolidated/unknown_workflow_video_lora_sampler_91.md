---
name: unknown_workflow_video_lora_sampler_91
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.672412
common_nodes: [AudioSeparation, BlockifyMask, CLIPVisionLoader, DownloadAndLoadWav2VecModel, DrawMaskOnImage, GetNode, GrowMask, ImageResizeKJv2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_Captioner, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy promptConcat]
problems: []
missing: []
members: [数字人/数字人/动作迁移，运镜模仿_1970665673569562625.json, 数字人/数字人/影视二创换脸自用-30s_1986605939723825153.json, 数字人/数字人/影视二创换脸自用_1986392976899403777.json, 数字人/数字人/影视二创换脸自用_1989908159244455937.json, 数字人/数字人/指定人物替换，指定角色替换，WanAnimate，对口型_1970655852627697666.json, 数字人/数字人/最强王炸—电商人物角色替换🤩_1971904577454993410.json, 数字人/数字人/视频局部重绘  参考重绘 Wan2.2 KJ加速_2060936779016003585.json, 视频生成/图生视频/Animate人物角色替换_1970083557895008257.json, 视频生成/图生视频/Animate最强角色替换_1978476869785899009.json, 视频生成/图生视频/人物角色替换Animate_1971412866429599745.json, 视频生成/图生视频/动作迁移  WanAnimate-KJ-V2 优化—加速_1975168158174679041.json, 视频生成/图生视频/多人物替换，优化 指定角色替换，加速 WanAnimate-KJ-V2 Infinite对口型校对_1975168163258175490.json, 视频生成/图生视频/指定人物替换 指定服装替换 Wan2.2 KJ加速 无惧切镜头SEC遮罩_1977316291763675138.json, 视频生成/图生视频/换人，角色替换，WanAnimate，对口型_2037208657041035265.json, 视频生成/图生视频/电商版-视频人物替换 +口型校对_1977681903191056385.json, 视频生成/图生视频/视频人物替换 Wan Animate KJ V2 Infinite口型校对_1975168167381217282.json, 视频生成/图生视频/运镜迁移Uni3c  Wan Animate  KJ-V2 加速优化版_1973741910089142274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_91

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（数字人/数字人/动作迁移，运镜模仿_1970665673569562625.json、数字人/数字人/影视二创换脸自用-30s_1986605939723825153.json、数字人/数字人/影视二创换脸自用_1986392976899403777.json、数字人/数字人/影视二创换脸自用_1989908159244455937.json、数字人/数字人/指定人物替换，指定角色替换，WanAnimate，对口型_1970655852627697666.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 17 个 workflow 都包含：
- `AudioSeparation`
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RH_Captioner`
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
- `easy cleanGpuUsed`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 16/17 个有
- `DWPreprocessor` —— 15/17 个有
- `FaceMaskFromPoseKeypoints` —— 15/17 个有
- `ImageCropByMaskAndResize` —— 15/17 个有
- `PixelPerfectResolution` —— 15/17 个有
- `Anything Everywhere` —— 13/17 个有
- `INTConstant` —— 13/17 个有
- `MaskToImage` —— 13/17 个有
- `SaveAudio` —— 13/17 个有
- `Text` —— 13/17 个有
- `LayerMask: LoadSegmentAnythingModels` —— 8/17 个有
- `LayerMask: SegmentAnythingUltra V3` —— 8/17 个有
- `PointsEditor` —— 7/17 个有
- `DownloadAndLoadSAM2Model` —— 6/17 个有
- `GetImageSizeAndCount` —— 6/17 个有
- `ImageFromBatch` —— 6/17 个有
- `Sam2Segmentation` —— 6/17 个有
- `SeCModelLoader` —— 6/17 个有
- `SeCVideoSegmentation` —— 6/17 个有
- `WanVideoEncode` —— 5/17 个有
- `WanVideoUni3C_ControlnetLoader` —— 5/17 个有
- `WanVideoUni3C_embeds` —— 5/17 个有
- `CR Text` —— 4/17 个有
- `EmptyImage` —— 4/17 个有
- `ImageConcatMulti` —— 4/17 个有
- `ImpactInt` —— 4/17 个有
- `ClothesSegment` —— 2/17 个有
- `DrawViTPose` —— 2/17 个有
- `OnnxDetectionModelLoader` —— 2/17 个有
- `PoseAndFaceDetection` —— 2/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
