---
name: unknown_workflow_video_lora_sampler_145
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.636214
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConvertOpenPoseKeypointsToDWPose, INTConstant, ImageBatchMulti, ImageBatchMultiV2, ImageResizeKJv2, Int, LoadImage, LoadNLFModel, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PreviewImage, RenderNLFPoses, SAM3_VideoTrack, SCAIL2ColoredMaskV2, SDPoseKeypointExtractor, Seed (rgthree), VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode V2, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus VAELoader, WanVideoTextEncodeCached]
problems: []
missing: []
members: [图片生成/图生图/Scail-2-多参工作流。原创：肥猴和WUWU_2070429204839223298.json, 平台全量/GS-Scail-2 动作迁移+人物替换_2072951527395913729.json, 平台全量/Scail-2 高阶工作流Plus V3.2版【长视频 + 多图参考 + 动作迁移 + 背景替换】_2071133720278552578.json, 平台全量/奶龙 (1)_2117921056794177537.json, 平台全量/奶龙_2117809037038407681.json, 平台全量/最强舞蹈工作流_2112449073562345473.json, 平台全量/最强舞蹈工作流_2112450386337554434.json, 视频生成/图生视频/SCAIL2！动作迁移！角色替换！多图参考！影视二创！_2070337569765814273.json, 视频生成/图生视频/Scail-2   动作替换版_2073277807773446146.json, 视频生成/图生视频/Scail-2 高阶工作流Plus V3版【一键长视频 + 多图参考 + 动作迁移 + 背景替换】_2068175109889806337.json, 视频生成/图生视频/Scail-2 高阶工作流Plus V3版【一键长视频 + 多图参考 + 动作迁移 + 背景替换】_2068602751445200897.json, 视频生成/图生视频/Scail-2 高阶工作流Plus V3版肥猴【多图参考 + 动作迁移 + 背景替换】_2068667240626614274.json, 视频生成/图生视频/Scail-2-工作流。动作迁移_2073070381749063682.json, 视频生成/图生视频/scail2-动作迁移，单_多图参考_2070686802167549953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_145

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Scail-2-多参工作流。原创：肥猴和WUWU_2070429204839223298.json、平台全量/GS-Scail-2 动作迁移+人物替换_2072951527395913729.json、平台全量/Scail-2 高阶工作流Plus V3.2版【长视频 + 多图参考 + 动作迁移 + 背景替换】_2071133720278552578.json、平台全量/奶龙 (1)_2117921056794177537.json、平台全量/奶龙_2117809037038407681.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConvertOpenPoseKeypointsToDWPose`
- `INTConstant`
- `ImageBatchMulti`
- `ImageBatchMultiV2`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `LoadNLFModel`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PreviewImage`
- `RenderNLFPoses`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `SDPoseKeypointExtractor`
- `Seed (rgthree)`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode V2`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus SamplerFromSettings`
- `WanAnimatePlus SamplerSettings`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus VAELoader`
- `WanVideoTextEncodeCached`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNodeV2` —— 13/14 个有
- `PrimitiveBoolean` —— 13/14 个有
- `Fast Groups Bypasser (rgthree)` —— 12/14 个有
- `WanVideoTorchCompileSettings` —— 11/14 个有
- `FastGroupsBypassSwitch` —— 8/14 个有
- `GetNode` —— 8/14 个有
- `PlaySound|pysssss` —— 8/14 个有
- `SetNode` —— 8/14 个有
- `AutoRefCollage` —— 7/14 个有
- `CR Text` —— 6/14 个有
- `GetImageSize` —— 6/14 个有
- `Label (rgthree)` —— 6/14 个有
- `InvertBoolean` —— 5/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/14 个有
- `Any Switch (rgthree)` —— 3/14 个有
- `ImageUpscaleWithModelBatched` —— 3/14 个有
- `RIFE VFI` —— 3/14 个有
- `UpscaleModelLoader` —— 3/14 个有
- `WanAnimatePlus ContextOptions` —— 3/14 个有
- `JjkText` —— 1/14 个有
- `ManualRefCollage` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `VRAMCleanup` —— 1/14 个有
- `WanVideoEncode` —— 1/14 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/14 个有
- `WanVideoUni3C_embeds` —— 1/14 个有
- `easy ifElse` —— 1/14 个有
- `孤海注释` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
