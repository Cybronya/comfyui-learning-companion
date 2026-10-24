---
name: unknown_workflow_video_lora_sampler_169
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.660091
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-Animate-视频换脸+换装+动作模仿+迁移跳舞_1993696432154755073.json, 视频生成/图生视频/Wan2.2Animate+DWPose动作模仿工作流！墙裂推荐！表情精准迁移_2038302872932192257.json, 视频生成/图生视频/Wan2.2图生视频人物替换动作迁移_2028365300059611138.json, 视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052450080971603969.json, 视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052663395060600834.json, 视频生成/图生视频/Wan2.7+视频换脸  换头换发型+真实自然+视频换脸+人物角色替换+虚拟美女模特_2061612628442705921.json, 视频生成/图生视频/人物换脸 图生视频_2001188538823606273.json, 视频生成/图生视频/人物替换，SAM3自动分割_2046159964988776450.json, 视频生成/图生视频/人物角色替换_2062336789762895874.json, 视频生成/图生视频/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上）_1988865006097797121.json, 视频生成/图生视频/高清视频换脸换发型+自定时长+真实自然+视频换脸+人物角色替换 (1)_2069968810341396482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_169

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-Animate-视频换脸+换装+动作模仿+迁移跳舞_1993696432154755073.json、视频生成/图生视频/Wan2.2Animate+DWPose动作模仿工作流！墙裂推荐！表情精准迁移_2038302872932192257.json、视频生成/图生视频/Wan2.2图生视频人物替换动作迁移_2028365300059611138.json、视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052450080971603969.json、视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052663395060600834.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 10/11 个有
- `DrawMaskOnImage` —— 10/11 个有
- `GrowMask` —— 10/11 个有
- `JWInteger` —— 10/11 个有
- `WanVideoLoraSelectMulti` —— 10/11 个有
- `CR Text` —— 9/11 个有
- `ImageConcatMulti` —— 9/11 个有
- `Int` —— 9/11 个有
- `LayerMask: SegformerB2ClothesUltra` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/11 个有
- `MathExpression|pysssss` —— 9/11 个有
- `PreviewImage` —— 9/11 个有
- `VHS_VideoInfo` —— 9/11 个有
- `LayerUtility: PurgeVRAM V2` —— 8/11 个有
- `MemoryCleaner` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LoadVideo` —— 1/11 个有
- `RH_AlibabaWan27VideoEdit` —— 1/11 个有
- `RMBG` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `SaveVideo` —— 1/11 个有
- `TT_img_enc_v2` —— 1/11 个有
- `Text` —— 1/11 个有
- `VHS_VideoInfoLoaded` —— 1/11 个有
- `WanVideoLoraSelect` —— 1/11 个有
- `easy framesEditor` —— 1/11 个有
- `easy sam3ModelLoader` —— 1/11 个有
- `easy sam3VideoModelExtraConfig` —— 1/11 个有
- `easy sam3VideoSegmentation` —— 1/11 个有
- `easy sam3Visualization` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
