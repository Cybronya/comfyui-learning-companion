---
name: unknown_workflow_video_lora_sampler_155
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.533909
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ImageResizeKJv2, Int, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMaskV2, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Scail-2-多参工作流。原创：肥猴和WUWU_2070429204839223298.json, 视频生成/图生视频/SCAIL2！动作迁移！角色替换！多图参考！影视二创！_2070337569765814273.json, 视频生成/图生视频/Scail-2   动作替换版_2073277807773446146.json, 视频生成/图生视频/Scail-2 高阶工作流Plus V3版【一键长视频 + 多图参考 + 动作迁移 + 背景替换】_2068175109889806337.json, 视频生成/图生视频/Scail-2 高阶工作流Plus V3版【一键长视频 + 多图参考 + 动作迁移 + 背景替换】_2068602751445200897.json, 视频生成/图生视频/Scail-2 高阶工作流Plus V3版肥猴【多图参考 + 动作迁移 + 背景替换】_2068667240626614274.json, 视频生成/图生视频/Scail-2 高阶工作流Plus版 v1.5 【多图 + 多角色参考 + 动作迁移 + 背景替换】_2067873915053101058.json, 视频生成/图生视频/Scail-2-工作流。动作迁移_2073070381749063682.json, 视频生成/图生视频/scail2-动作迁移，单_多图参考_2070686802167549953.json, 视频生成/图生视频/【阿良绘】多角色替换 _ Scail2高级工作流 （长视频+动作捕捉+多角色替换）_2074674360849354753.json, 视频生成/图生视频/阿良绘Scail2测试-长视频071_2073289160070545408.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_155

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Scail-2-多参工作流。原创：肥猴和WUWU_2070429204839223298.json、视频生成/图生视频/SCAIL2！动作迁移！角色替换！多图参考！影视二创！_2070337569765814273.json、视频生成/图生视频/Scail-2   动作替换版_2073277807773446146.json、视频生成/图生视频/Scail-2 高阶工作流Plus V3版【一键长视频 + 多图参考 + 动作迁移 + 背景替换】_2068175109889806337.json、视频生成/图生视频/Scail-2 高阶工作流Plus V3版【一键长视频 + 多图参考 + 动作迁移 + 背景替换】_2068602751445200897.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ConvertOpenPoseKeypointsToDWPose` —— 10/11 个有
- `ImageBatchMulti` —— 10/11 个有
- `LoadNLFModel` —— 10/11 个有
- `NLFPredict` —— 10/11 个有
- `OnnxDetectionModelLoader` —— 10/11 个有
- `PoseDetectionVitPoseToDWPose` —— 10/11 个有
- `PrimitiveBoolean` —— 10/11 个有
- `RenderNLFPoses` —— 10/11 个有
- `SDPoseKeypointExtractor` —— 10/11 个有
- `WanAnimatePlus ClipVisionEncode V2` —— 10/11 个有
- `AutoRefCollage` —— 9/11 个有
- `ComfySwitchNodeV2` —— 9/11 个有
- `FastGroupsBypassSwitch` —— 9/11 个有
- `GetNode` —— 9/11 个有
- `INTConstant` —— 9/11 个有
- `ImageBatchMultiV2` —— 9/11 个有
- `Seed (rgthree)` —— 9/11 个有
- `SetNode` —— 9/11 个有
- `WanVideoTextEncodeCached` —— 9/11 个有
- `WanVideoTorchCompileSettings` —— 8/11 个有
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `InvertBoolean` —— 7/11 个有
- `PlaySound|pysssss` —— 7/11 个有
- `Label (rgthree)` —— 5/11 个有
- `Any Switch (rgthree)` —— 3/11 个有
- `GetImageSize` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `ImageFromBatch` —— 2/11 个有
- `JjkText` —— 2/11 个有
- `SimpleMath+` —— 2/11 个有
- `WanAnimatePlus TextEncodeCached` —— 2/11 个有
- `easy int` —— 2/11 个有
- `easy seed` —— 2/11 个有
- `Image Blank` —— 1/11 个有
- `ImageCompositeMasked` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `RepeatImageBatch` —— 1/11 个有
- `SAM3_TrackToMask` —— 1/11 个有
- `WanAnimatePlus ClipVisionEncode` —— 1/11 个有
- `WanAnimatePlus ContextOptions` —— 1/11 个有
- `WanVideoContextOptions` —— 1/11 个有
- `easy ifElse` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
