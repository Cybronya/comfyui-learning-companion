---
name: unknown_workflow_video_lora_sampler_103
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.686706
common_nodes: [Anything Everywhere, AudioSeparation, BlockifyMask, CLIPVisionLoader, DownloadAndLoadWav2VecModel, DrawMaskOnImage, GetNode, GrowMask, INTConstant, ImageResizeKJv2, LoadImage, MaskToImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_Captioner, SaveAudio, SetNode, SimpleMath+, Text, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy promptConcat]
problems: []
missing: []
members: [平台全量/Wan-animate 完美人物替换_1970655429825077250.json, 平台全量/影视游戏二创——首帧图人物替换最精准方案，游戏影视二创第二步V2_2012023405704388610.json, 平台全量/影视游戏二创——首帧图人物替换，游戏影视二创第二步_2008180291705249793.json, 平台全量/超好用🔥多人物替换-指定角色替换-口型校对-二创首选_2046531577512988674.json, 数字人/数字人/动作迁移，运镜模仿_1970665673569562625.json, 数字人/数字人/影视二创换脸自用-30s_1986605939723825153.json, 数字人/数字人/影视二创换脸自用_1986392976899403777.json, 数字人/数字人/影视二创换脸自用_1989908159244455937.json, 数字人/数字人/指定人物替换，指定角色替换，WanAnimate，对口型_1970655852627697666.json, 数字人/数字人/视频局部重绘  参考重绘 Wan2.2 KJ加速_2060936779016003585.json, 视频生成/图生视频/动作迁移  WanAnimate-KJ-V2 优化—加速_1975168158174679041.json, 视频生成/图生视频/多人物替换，优化 指定角色替换，加速 WanAnimate-KJ-V2 Infinite对口型校对_1975168163258175490.json, 视频生成/图生视频/指定人物替换 指定服装替换 Wan2.2 KJ加速 无惧切镜头SEC遮罩_1977316291763675138.json, 视频生成/图生视频/换人，角色替换，WanAnimate，对口型_2037208657041035265.json, 视频生成/图生视频/电商版-视频人物替换 +口型校对_1977681903191056385.json, 视频生成/图生视频/视频人物替换 Wan Animate KJ V2 Infinite口型校对_1975168167381217282.json, 视频生成/图生视频/运镜迁移Uni3c  Wan Animate  KJ-V2 加速优化版_1973741910089142274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_103

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（平台全量/Wan-animate 完美人物替换_1970655429825077250.json、平台全量/影视游戏二创——首帧图人物替换最精准方案，游戏影视二创第二步V2_2012023405704388610.json、平台全量/影视游戏二创——首帧图人物替换，游戏影视二创第二步_2008180291705249793.json、平台全量/超好用🔥多人物替换-指定角色替换-口型校对-二创首选_2046531577512988674.json、数字人/数字人/动作迁移，运镜模仿_1970665673569562625.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 17 个 workflow 都包含：
- `Anything Everywhere`
- `AudioSeparation`
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskToImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RH_Captioner`
- `SaveAudio`
- `SetNode`
- `SimpleMath+`
- `Text`
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
- `DWPreprocessor` —— 15/17 个有
- `FaceMaskFromPoseKeypoints` —— 15/17 个有
- `ImageCropByMaskAndResize` —— 15/17 个有
- `PixelPerfectResolution` —— 15/17 个有
- `easy showAnything` —— 15/17 个有
- `PointsEditor` —— 10/17 个有
- `DownloadAndLoadSAM2Model` —— 9/17 个有
- `ImageFromBatch` —— 9/17 个有
- `Sam2Segmentation` —— 9/17 个有
- `SeCModelLoader` —— 9/17 个有
- `SeCVideoSegmentation` —— 9/17 个有
- `WanVideoEncode` —— 7/17 个有
- `WanVideoUni3C_ControlnetLoader` —— 7/17 个有
- `WanVideoUni3C_embeds` —— 7/17 个有
- `LayerMask: LoadSegmentAnythingModels` —— 5/17 个有
- `LayerMask: SegmentAnythingUltra V3` —— 5/17 个有
- `ClothesSegment` —— 4/17 个有
- `GetImageSizeAndCount` —— 4/17 个有
- `DrawViTPose` —— 2/17 个有
- `Fast Groups Muter (rgthree)` —— 2/17 个有
- `OnnxDetectionModelLoader` —— 2/17 个有
- `PoseAndFaceDetection` —— 2/17 个有
- `VHS_VideoInfo` —— 2/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
