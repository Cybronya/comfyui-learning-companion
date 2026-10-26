---
name: unknown_workflow_video_upscale_lora_41
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.667
common_nodes: [Any Switch (rgthree), CLIPVisionLoader, CM_IntToFloat, CR Integer To String, CR String To Number, CR Text, CropFace, DWPreprocessor, Display Any (rgthree), FaceMaskFromPoseKeypoints, Fast Groups Muter (rgthree), Float, GetImageSize, GetImageSize+, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageFromBatch+, ImageResizeKJ, ImageResizeKJv2, ImageScale, ImageUpscaleWithModelBatched, LayerUtility: PurgeVRAM V2, LoadImage, MathExpression|pysssss, PixelPerfectResolution, PreviewImage, RIFE VFI, ReActorFaceSwap, SetNode, ShowText|pysssss, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy anythingIndexSwitch, easy imageIndexSwitch, easy int]
problems: []
missing: []
members: [视频生成/图生视频/角色替换 _ 动作迁移 _ 图生视频 Wan2.2 Animate V4_2027691887594835969.json, 视频生成/图生视频/角色替换 _ 动作迁移 _ 图生视频 Wan2.2 Animate_2020368444805357570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_41

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/角色替换 _ 动作迁移 _ 图生视频 Wan2.2 Animate V4_2027691887594835969.json、视频生成/图生视频/角色替换 _ 动作迁移 _ 图生视频 Wan2.2 Animate_2020368444805357570.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `CR Integer To String`
- `CR String To Number`
- `CR Text`
- `CropFace`
- `DWPreprocessor`
- `Display Any (rgthree)`
- `FaceMaskFromPoseKeypoints`
- `Fast Groups Muter (rgthree)`
- `Float`
- `GetImageSize`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageUpscaleWithModelBatched`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MathExpression|pysssss`
- `PixelPerfectResolution`
- `PreviewImage`
- `RIFE VFI`
- `ReActorFaceSwap`
- `SetNode`
- `ShowText|pysssss`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy imageIndexSwitch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 1/2 个有
- `ImageHistogramMatch+` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoLoraSelectMulti` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
