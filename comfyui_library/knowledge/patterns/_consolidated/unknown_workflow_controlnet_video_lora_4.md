---
name: unknown_workflow_controlnet_video_lora_4
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.833235
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, Fast Groups Bypasser (rgthree), GetImageSizeAndCount, ImageResizeKJv2, ImpactInt, JWInteger, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/Wan-Animate_视频动作迁移到参考图-B站UP主@好奇漫步_2003755593414418433.json, 平台全量/animate动作迁移，口型保持，镜头控制_1995745340076724226.json, 平台全量/带劲抖解压版~跟着视频跳舞-色彩保持不变~V3_2027094482008674306.json, 平台全量/开源最强人物姿态迁移Animate V2【原图背景】_1977712629550567425.json, 数字人/数字人/人物姿势迁移_1999053777653071873.json, 视频生成/图生视频/Animate-原图背景版-人物姿态迁移V2_1987930419398119426.json, 视频生成/图生视频/Animate-原图背景版-人物姿态迁移V2_2015387238657433602.json, 视频生成/图生视频/Animate-原图背景版-人物姿态迁移V2_2026954923237183490.json, 视频生成/图生视频/WAN 2.2 Animate人物姿态迁移（720P+30帧+9：16+）_1992946454725672962.json, 视频生成/图生视频/Wan2.2 Animate带口型+运镜动作迁移（图片跳舞）_1981708814372225026.json, 视频生成/图生视频/Wan2.2 最强效果Animate 视频人物姿态迁移V2升级版(保留原图背景）15S稳如老狗_1980606139123585025.json, 视频生成/图生视频/【推荐】Animate-原图背景版-人物姿态迁移V2_2009584371598102530.json, 视频生成/图生视频/人物姿态迁移V2 原图背景_1979145028213837826.json, 视频生成/图生视频/动作迁移老11_2015053987497648129.json, 视频生成/图生视频/带劲抖~Animate-原图背景版-人物姿态迁移V2_2041179422866284546.json, 视频生成/图生视频/🤩Animate最强王炸—人物姿态迁移V2【原图背景】🤩_1975078330166849538.json, 视频生成/图生视频/🤩Animate最强王炸—人物姿态迁移【原图背景】_1969605920248504321.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_4

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（平台全量/Wan-Animate_视频动作迁移到参考图-B站UP主@好奇漫步_2003755593414418433.json、平台全量/animate动作迁移，口型保持，镜头控制_1995745340076724226.json、平台全量/带劲抖解压版~跟着视频跳舞-色彩保持不变~V3_2027094482008674306.json、平台全量/开源最强人物姿态迁移Animate V2【原图背景】_1977712629550567425.json、数字人/数字人/人物姿势迁移_1999053777653071873.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 17 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `ImpactInt`
- `JWInteger`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
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
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 16/17 个有
- `LayerUtility: PurgeVRAM` —— 16/17 个有
- `SetNode` —— 16/17 个有
- `DrawViTPose` —— 14/17 个有
- `OnnxDetectionModelLoader` —— 14/17 个有
- `PoseAndFaceDetection` —— 14/17 个有
- `ImageConcatMulti` —— 10/17 个有
- `WanVideoLoraSelect` —— 7/17 个有
- `TT_img_enc_v2` —— 4/17 个有
- `FaceMaskFromPoseKeypoints` —— 3/17 个有
- `ImageCropByMaskAndResize` —— 3/17 个有
- `PixelPerfectResolution` —— 3/17 个有
- `SaveImage` —— 3/17 个有
- `DWPreprocessor` —— 2/17 个有
- `DuckHideNode` —— 2/17 个有
- `Note Plus (mtb)` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `ColorMatch` —— 1/17 个有
- `Image Resize To Width` —— 1/17 个有
- `ImageMirror` —— 1/17 个有
- `ImpactSwitch` —— 1/17 个有
- `LayerUtility: PurgeVRAM V2` —— 1/17 个有
- `LoadAudio` —— 1/17 个有
- `RHHiddenNodes` —— 1/17 个有
- `SimpleCondition+` —— 1/17 个有
- `WanVideoContextOptions` —— 1/17 个有
- `easy float` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
