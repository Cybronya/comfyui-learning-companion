---
name: unknown_workflow_video_lora_sampler_186
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5397
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ImageResizeKJv2, Int, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMaskV2, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2070337569765814273.json, 视频生成/图生视频/2073277807773446146.json, 视频生成/图生视频/2068175109889806337.json, 视频生成/图生视频/2068602751445200897.json, 视频生成/图生视频/2068667240626614274.json, 视频生成/图生视频/2067873915053101058.json, 视频生成/图生视频/2073070381749063682.json, 视频生成/图生视频/2070686802167549953.json, 视频生成/图生视频/2074674360849354753.json, 视频生成/图生视频/2073289160070545408.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_186

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2070337569765814273.json、视频生成/图生视频/2073277807773446146.json、视频生成/图生视频/2068175109889806337.json、视频生成/图生视频/2068602751445200897.json、视频生成/图生视频/2068667240626614274.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus SamplerFromSettings`
- `WanAnimatePlus SamplerSettings`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConvertOpenPoseKeypointsToDWPose` —— 9/10 个有
- `ImageBatchMulti` —— 9/10 个有
- `LoadNLFModel` —— 9/10 个有
- `NLFPredict` —— 9/10 个有
- `OnnxDetectionModelLoader` —— 9/10 个有
- `PoseDetectionVitPoseToDWPose` —— 9/10 个有
- `PrimitiveBoolean` —— 9/10 个有
- `RenderNLFPoses` —— 9/10 个有
- `SDPoseKeypointExtractor` —— 9/10 个有
- `WanAnimatePlus ClipVisionEncode V2` —— 9/10 个有
- `AutoRefCollage` —— 8/10 个有
- `ComfySwitchNodeV2` —— 8/10 个有
- `FastGroupsBypassSwitch` —— 8/10 个有
- `GetNode` —— 8/10 个有
- `INTConstant` —— 8/10 个有
- `ImageBatchMultiV2` —— 8/10 个有
- `Seed (rgthree)` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `WanVideoTextEncodeCached` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `InvertBoolean` —— 6/10 个有
- `PlaySound|pysssss` —— 6/10 个有
- `Label (rgthree)` —— 4/10 个有
- `Any Switch (rgthree)` —— 3/10 个有
- `GetImageSize` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `ImageFromBatch` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `WanAnimatePlus TextEncodeCached` —— 2/10 个有
- `easy int` —— 2/10 个有
- `easy seed` —— 2/10 个有
- `Image Blank` —— 1/10 个有
- `ImageCompositeMasked` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `RepeatImageBatch` —— 1/10 个有
- `SAM3_TrackToMask` —— 1/10 个有
- `WanAnimatePlus ClipVisionEncode` —— 1/10 个有
- `WanAnimatePlus ContextOptions` —— 1/10 个有
- `WanVideoContextOptions` —— 1/10 个有
- `easy ifElse` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
