---
name: unknown_workflow_video_lora_sampler_154
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.525917
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ImageResizeKJv2, Int, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMaskV2, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Scail-2-多参工作流。原创：肥猴和WUWU_2070429204839223298.json, 数字人/数字人/电商商用Scail-2 高级版工作流【多图 + 多角色参考 + 动作迁移 + 背景替换】-肥猴&wuwu版_2067262704208932866.json, 视频生成/图生视频/SCAIL2！动作迁移！角色替换！多图参考！影视二创！_2070337569765814273.json, 视频生成/图生视频/Scail-2   动作替换版_2073277807773446146.json, 视频生成/图生视频/Scail-2 高阶工作流Plus V3版【一键长视频 + 多图参考 + 动作迁移 + 背景替换】_2068175109889806337.json, 视频生成/图生视频/Scail-2 高阶工作流Plus V3版【一键长视频 + 多图参考 + 动作迁移 + 背景替换】_2068602751445200897.json, 视频生成/图生视频/Scail-2 高阶工作流Plus V3版肥猴【多图参考 + 动作迁移 + 背景替换】_2068667240626614274.json, 视频生成/图生视频/Scail-2 高阶工作流Plus版 v1.5 【多图 + 多角色参考 + 动作迁移 + 背景替换】_2067873915053101058.json, 视频生成/图生视频/Scail-2-工作流。动作迁移_2073070381749063682.json, 视频生成/图生视频/scail2-动作迁移，单_多图参考_2070686802167549953.json, 视频生成/图生视频/【阿良绘】多角色替换 _ Scail2高级工作流 （长视频+动作捕捉+多角色替换）_2074674360849354753.json, 视频生成/图生视频/阿良绘Scail2测试-长视频071_2073289160070545408.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_154

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Scail-2-多参工作流。原创：肥猴和WUWU_2070429204839223298.json、数字人/数字人/电商商用Scail-2 高级版工作流【多图 + 多角色参考 + 动作迁移 + 背景替换】-肥猴&wuwu版_2067262704208932866.json、视频生成/图生视频/SCAIL2！动作迁移！角色替换！多图参考！影视二创！_2070337569765814273.json、视频生成/图生视频/Scail-2   动作替换版_2073277807773446146.json、视频生成/图生视频/Scail-2 高阶工作流Plus V3版【一键长视频 + 多图参考 + 动作迁移 + 背景替换】_2068175109889806337.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ImageBatchMulti` —— 11/12 个有
- `PrimitiveBoolean` —— 11/12 个有
- `AutoRefCollage` —— 10/12 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 10/12 个有
- `FastGroupsBypassSwitch` —— 10/12 个有
- `GetNode` —— 10/12 个有
- `INTConstant` —— 10/12 个有
- `LoadNLFModel` —— 10/12 个有
- `NLFPredict` —— 10/12 个有
- `OnnxDetectionModelLoader` —— 10/12 个有
- `PoseDetectionVitPoseToDWPose` —— 10/12 个有
- `RenderNLFPoses` —— 10/12 个有
- `SDPoseKeypointExtractor` —— 10/12 个有
- `Seed (rgthree)` —— 10/12 个有
- `SetNode` —— 10/12 个有
- `WanAnimatePlus ClipVisionEncode V2` —— 10/12 个有
- `WanVideoTextEncodeCached` —— 10/12 个有
- `ComfySwitchNodeV2` —— 9/12 个有
- `ImageBatchMultiV2` —— 9/12 个有
- `WanVideoTorchCompileSettings` —— 9/12 个有
- `Fast Groups Bypasser (rgthree)` —— 8/12 个有
- `PlaySound|pysssss` —— 8/12 个有
- `InvertBoolean` —— 7/12 个有
- `Label (rgthree)` —— 5/12 个有
- `Any Switch (rgthree)` —— 3/12 个有
- `CR Text` —— 3/12 个有
- `GetImageSize` —— 3/12 个有
- `SimpleMath+` —— 3/12 个有
- `ImageFromBatch` —— 2/12 个有
- `JjkText` —— 2/12 个有
- `WanAnimatePlus ClipVisionEncode` —— 2/12 个有
- `WanAnimatePlus TextEncodeCached` —— 2/12 个有
- `WanVideoContextOptions` —— 2/12 个有
- `easy int` —— 2/12 个有
- `easy seed` —— 2/12 个有
- `Image Blank` —— 1/12 个有
- `ImageCompositeMasked` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `RepeatImageBatch` —— 1/12 个有
- `SAM3_TrackToMask` —— 1/12 个有
- `WanAnimatePlus ContextOptions` —— 1/12 个有
- `easy ifElse` —— 1/12 个有
- `孤海注释` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
