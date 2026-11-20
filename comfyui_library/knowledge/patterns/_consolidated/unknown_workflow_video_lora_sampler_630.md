---
name: unknown_workflow_video_lora_sampler_630
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4524
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, FastGroupsBypassSwitch, GetNode, ImageFromBatch, ImageResizeKJv2, Int, LoadImage, PreviewImage, PrimitiveBoolean, SAM3_VideoTrack, SCAIL2ColoredMaskV2, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode V2, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/【阿良绘】多角色替换 _ Scail2高级工作流 （长视频+动作捕捉+多角色替换）_2074674360849354753.json, 视频生成/图生视频/【阿良绘】角色+指定动作+背景替换V3+_+Scail2高级工作流+（角色背景+参考动作）_2081659907098636289.json, 视频生成/图生视频/【阿良绘】角色+指定动作V2 _ Scail2高级工作流 （角色+指定动作🔧）_2075472358017687554.json, 视频生成/图生视频/【阿良绘】角色稳定替换 _ Scail2高级工作流 （长视频+角色替换+姿势保持）_2074344791734837250.json, 视频生成/图生视频/阿良绘Scail2测试-长视频071_2073289160070545408.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_630

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/【阿良绘】多角色替换 _ Scail2高级工作流 （长视频+动作捕捉+多角色替换）_2074674360849354753.json、视频生成/图生视频/【阿良绘】角色+指定动作+背景替换V3+_+Scail2高级工作流+（角色背景+参考动作）_2081659907098636289.json、视频生成/图生视频/【阿良绘】角色+指定动作V2 _ Scail2高级工作流 （角色+指定动作🔧）_2075472358017687554.json、视频生成/图生视频/【阿良绘】角色稳定替换 _ Scail2高级工作流 （长视频+角色替换+姿势保持）_2074344791734837250.json、视频生成/图生视频/阿良绘Scail2测试-长视频071_2073289160070545408.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `FastGroupsBypassSwitch`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `PreviewImage`
- `PrimitiveBoolean`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `SetNode`
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
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AutoRefCollage` —— 4/5 个有
- `Image Blank` —— 4/5 个有
- `ImageCompositeMasked` —— 4/5 个有
- `InvertBoolean` —— 4/5 个有
- `RepeatImageBatch` —— 4/5 个有
- `SAM3_TrackToMask` —— 4/5 个有
- `easy seed` —— 4/5 个有
- `Any Switch (rgthree)` —— 3/5 个有
- `ComfySwitchNodeV2` —— 3/5 个有
- `BatchImagesNode` —— 2/5 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `LoadNLFModel` —— 2/5 个有
- `NLFPredict` —— 2/5 个有
- `OnnxDetectionModelLoader` —— 2/5 个有
- `PoseDetectionVitPoseToDWPose` —— 2/5 个有
- `RenderNLFPoses` —— 2/5 个有
- `SDPoseKeypointExtractor` —— 2/5 个有
- `WanAnimatePlus ContextOptions` —— 2/5 个有
- `WanAnimatePlus LoraSelect` —— 2/5 个有
- `WanAnimatePlus SCAIL_2 TwoPhase Settings` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `ImageBatchMultiV2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
