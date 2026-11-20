---
name: unknown_workflow_video_lora_sampler_460
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.445
common_nodes: [CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PlaySound|pysssss, PoseAndFaceDetection, PreviewImage, Seed (rgthree), SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/qy-简化_2035638502787911682.json, 视频生成/图生视频/啊癫【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2062892652022030338.json, 视频生成/图生视频/图生视频-【丝滑变装】-【动作迁移】-【人物替换】Wan2.2 Animate 分段队列_2063193185219858434.json, 视频生成/图生视频/美女穿搭一键换衣 变装 +动作迁移 +动作模仿_2066425187536564226.json, 视频生成/图生视频/自用 人物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2026672367019237377.json, 视频生成/图生视频/顶级视频换人（变装跳舞专用）_2099576921075052545.json, 视频生成/文生视频/【丝滑变装】&【动作迁移】&【人物替换】_2100616978972102658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_460

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/qy-简化_2035638502787911682.json、视频生成/图生视频/啊癫【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2062892652022030338.json、视频生成/图生视频/图生视频-【丝滑变装】-【动作迁移】-【人物替换】Wan2.2 Animate 分段队列_2063193185219858434.json、视频生成/图生视频/美女穿搭一键换衣 变装 +动作迁移 +动作模仿_2066425187536564226.json、视频生成/图生视频/自用 人物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2026672367019237377.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PlaySound|pysssss`
- `PoseAndFaceDetection`
- `PreviewImage`
- `Seed (rgthree)`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `WanVideoContextOptions` —— 6/7 个有
- `YOLOModelLoader` —— 6/7 个有
- `BBoxYOLO` —— 5/7 个有
- `BlockifyMask` —— 5/7 个有
- `BodyRatioMapperSDPoseRender` —— 5/7 个有
- `CheckpointLoaderSimple` —— 5/7 个有
- `DrawMaskOnImage` —— 5/7 个有
- `GrowMaskWithBlur` —— 5/7 个有
- `ImageBlend` —— 5/7 个有
- `MaskToImage` —— 5/7 个有
- `SDPoseKeypointExtractor` —— 5/7 个有
- `SegmentQueueRunner` —— 5/7 个有
- `WanVideoEncode` —— 5/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 5/7 个有
- `WanVideoUni3C_embeds` —— 5/7 个有
- `CLIPTextEncode` —— 4/7 个有
- `LayerUtility: PurgeVRAM V2` —— 4/7 个有
- `SAM3_Detect` —— 4/7 个有
- `FastUnsharpSharpen` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `SDPoseOODLoader` —— 2/7 个有
- `SDPoseOODProcessor` —— 2/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `ImageFlip` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `RTXVideoSuperResolution` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `Text` —— 1/7 个有
- `easy framesEditor` —— 1/7 个有
- `easy sam3GetObjectIds` —— 1/7 个有
- `easy sam3GetObjectMask` —— 1/7 个有
- `easy sam3ModelLoader` —— 1/7 个有
- `easy sam3VideoModelExtraConfig` —— 1/7 个有
- `easy sam3VideoSegmentation` —— 1/7 个有
- `easy sam3Visualization` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
