---
name: unknown_workflow_controlnet_video_lora_4
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.784143
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2001008301930315778.json, 视频生成/图生视频/2001007812647976961.json, 视频生成/图生视频/2001114999428968450.json, 视频生成/图生视频/2000985576838922241.json, 视频生成/图生视频/2002262972904947714.json, 视频生成/图生视频/2000835179973406721.json, 视频生成/图生视频/2015270492097220610.json, 视频生成/图生视频/2007356620417798146.json, 视频生成/图生视频/2001530537791614977.json, 视频生成/图生视频/2001210850083995649.json, 视频生成/图生视频/2003735062367641602.json, 视频生成/图生视频/2004016053883682817.json, 视频生成/图生视频/2002389202262212609.json, 视频生成/图生视频/2000980028173283329.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2001008301930315778.json、视频生成/图生视频/2001007812647976961.json、视频生成/图生视频/2001114999428968450.json、视频生成/图生视频/2000985576838922241.json、视频生成/图生视频/2002262972904947714.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 12/14 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 9/14 个有
- `DWPreprocessor` —— 9/14 个有
- `SetNode` —— 9/14 个有
- `SimpleMath+` —— 9/14 个有
- `CR Prompt Text` —— 7/14 个有
- `FloatConstant` —— 7/14 个有
- `GetNode` —— 7/14 个有
- `JWInteger` —— 7/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/14 个有
- `MathExpression|pysssss` —— 7/14 个有
- `RunningHub Deepcleaner` —— 7/14 个有
- `PDIMAGE_LongerSize` —— 5/14 个有
- `WanVideoTorchCompileSettings` —— 5/14 个有
- `INTConstant` —— 4/14 个有
- `CR Text` —— 2/14 个有
- `DuckHideNode` —— 2/14 个有
- `Fast Bypasser (rgthree)` —— 2/14 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/14 个有
- `SaveImage` —— 2/14 个有
- `TT_img_enc` —— 2/14 个有
- `TT_img_enc_v2` —— 2/14 个有
- `easy int` —— 2/14 个有
- `Bookmark (rgthree)` —— 1/14 个有
- `CM_IntToFloat` —— 1/14 个有
- `CR SDXL Aspect Ratio` —— 1/14 个有
- `MemoryCleaner` —— 1/14 个有
- `TextBox` —— 1/14 个有
- `WanVideoLoraSelectMulti` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
