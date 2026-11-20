---
name: unknown_workflow_video_lora_sampler_244
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.510091
common_nodes: [CLIPVisionLoader, GetNode, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy boolean, easy float, easy int]
problems: []
missing: []
members: [视频生成/图生视频/Wan_Animate图+视频跳舞_2071251010294734850.json, 视频生成/图生视频/YJ-APP-WanAnimate-v2-骨骼匹配-动作迁移_2052769134831779841.json, 视频生成/图生视频/wan2.2-Animate-动作迁移长视频_2044091136876224513.json, 视频生成/图生视频/【最推荐，动作迁移高动态】WanAnimate动作迁移_2035636525664309249.json, 视频生成/图生视频/动作迁移5，横版竖版_2035886366013267970.json, 视频生成/图生视频/动作迁移V6.1+抖动版（表情、动作到位）_2040370994539405314.json, 视频生成/图生视频/动作迁移V7_lcc_2048275067708116994.json, 视频生成/图生视频/动作迁移_2039702221989875713.json, 视频生成/图生视频/动作迁移增强_2059259951234772993.json, 视频生成/图生视频/动漫动物跳舞工作流_2051611196058550273.json, 视频生成/图生视频/啊癫 动漫动物跳舞工作流_2051288649169420290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_244

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Wan_Animate图+视频跳舞_2071251010294734850.json、视频生成/图生视频/YJ-APP-WanAnimate-v2-骨骼匹配-动作迁移_2052769134831779841.json、视频生成/图生视频/wan2.2-Animate-动作迁移长视频_2044091136876224513.json、视频生成/图生视频/【最推荐，动作迁移高动态】WanAnimate动作迁移_2035636525664309249.json、视频生成/图生视频/动作迁移5，横版竖版_2035886366013267970.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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
- `easy boolean`
- `easy float`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 10/11 个有
- `DownloadAndLoadNLFModel` —— 10/11 个有
- `DrawViTPose` —— 10/11 个有
- `ImageBatch` —— 10/11 个有
- `LazySwitch1way` —— 10/11 个有
- `NLFPredict` —— 10/11 个有
- `PoseDetectionVitPoseToDWPose` —— 10/11 个有
- `RenderNLFPoses` —— 10/11 个有
- `RepeatImageBatch` —— 10/11 个有
- `VHS_VideoInfo` —— 10/11 个有
- `YOLOModelLoader` —— 10/11 个有
- `easy anythingIndexSwitch` —— 10/11 个有
- `easy mathInt` —— 10/11 个有
- `PreviewImage` —— 9/11 个有
- `RHHiddenNodes` —— 9/11 个有
- `CR Text` —— 8/11 个有
- `ImpactSwitch` —— 7/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/11 个有
- `MemoryCleaner` —— 7/11 个有
- `easy compare` —— 7/11 个有
- `easy imageSize` —— 7/11 个有
- `BBoxYOLO` —— 5/11 个有
- `CheckpointLoaderSimple` —— 5/11 个有
- `LazySwitch2way` —— 5/11 个有
- `SDPoseDrawKeypoints` —— 5/11 个有
- `SDPoseKeypointExtractor` —— 5/11 个有
- `SDPoseOODLoader` —— 5/11 个有
- `SDPoseOODProcessor` —— 5/11 个有
- `VRAMReserver` —— 5/11 个有
- `Bool` —— 4/11 个有
- `CompressImages` —— 4/11 个有
- `VideoCombineNode` —— 4/11 个有
- `WanVideoEncode` —— 4/11 个有
- `WanVideoUni3C_ControlnetLoader` —— 4/11 个有
- `WanVideoUni3C_embeds` —— 4/11 个有
- `ZML_AnyTypeSwitchFiveBoolean` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `AddNoise` —— 2/11 个有
- `ArchAi3D_Qwen_Encoder` —— 2/11 个有
- `GrowMask` —— 2/11 个有
- `ImageFilterMedianBlur` —— 2/11 个有
- `KSamplerVariationsWithNoise+` —— 2/11 个有
- `LLMLoader` —— 2/11 个有
- `LMStudioPrompt` —— 2/11 个有
- `LatentBlend` —— 2/11 个有
- `LatentRotate` —— 2/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `RH_AlibabaWan27ImageEditPro` —— 2/11 个有
- `RH_Kling25_I2V_FirstLastFrame` —— 2/11 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 2/11 个有
- `RH_YouchuanImageToVideo` —— 2/11 个有
- `SamplerCustom` —— 2/11 个有
- `TorchCompileModel` —— 2/11 个有
- `BodyRatioMapperProportionTransfer` —— 1/11 个有
- `BodyRatioMapperSDPoseRender` —— 1/11 个有
- `DF_Int_to_Float` —— 1/11 个有
- `Display Any (rgthree)` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有
- `Text` —— 1/11 个有
- `easy imageColorMatch` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
