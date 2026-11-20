---
name: unknown_workflow_controlnet_video_lora_15
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.580857
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageResizeKJv2, LoadImage, MaskToImage, MemoryCleaner, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewAny, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy sam3GetObjectIds, easy sam3ModelLoader, easy sam3VideoModelExtraConfig, easy sam3VideoSegmentation, easy sam3Visualization]
problems: []
missing: []
members: [图片生成/图生图/空白工作流_2029100592844513281.json, 平台全量/Wan2.2 Animate动作迁移 人物替换----1分钟长视频-不偏移、不变色、人物一致性_2015849698275368961.json, 平台全量/Wan2.2 Animate长视频人物替换-效果好缺陷少_2050497160684285953.json, 平台全量/wan2.2-animate-长视频高质量角色替换_2057646481527623681.json, 数字人/数字人/wan-2.2-人物替换-V2_2058802119330852865.json, 数字人/数字人/wan-2.2-人物替换-V3_2059239614648508418.json, 视频生成/图生视频/wan-2.2-人物替换-V5_2067889293686820865.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_15

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/空白工作流_2029100592844513281.json、平台全量/Wan2.2 Animate动作迁移 人物替换----1分钟长视频-不偏移、不变色、人物一致性_2015849698275368961.json、平台全量/Wan2.2 Animate长视频人物替换-效果好缺陷少_2050497160684285953.json、平台全量/wan2.2-animate-长视频高质量角色替换_2057646481527623681.json、数字人/数字人/wan-2.2-人物替换-V2_2058802119330852865.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 7 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskToImage`
- `MemoryCleaner`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewAny`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy sam3GetObjectIds`
- `easy sam3ModelLoader`
- `easy sam3VideoModelExtraConfig`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`

**可变部分**（部分 workflow 才有）：
- `ImageBlend` —— 6/7 个有
- `Int` —— 6/7 个有
- `Primitive integer [Crystools]` —— 5/7 个有
- `SimpleMath+` —— 5/7 个有
- `ZML_AnyTypeSwitchFive` —— 5/7 个有
- `ImpactSwitch` —— 2/7 个有
- `SDPoseOODLoader` —— 2/7 个有
- `SDPoseOODProcessor` —— 2/7 个有
- `SeedVR2` —— 2/7 个有
- `SeedVR2BlockSwap` —— 2/7 个有
- `SeedVR2ExtraArgs` —— 2/7 个有
- `YOLOModelLoader` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `DuckHideNode` —— 1/7 个有
- `GoogleTranslator` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `String` —— 1/7 个有
- `WanVideoLoraSelect` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
