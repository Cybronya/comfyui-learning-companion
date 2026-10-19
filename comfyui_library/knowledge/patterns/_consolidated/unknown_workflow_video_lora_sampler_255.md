---
name: unknown_workflow_video_lora_sampler_255
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.678375
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, INTConstant, Int, LayerUtility: PurgeVRAM V2, LoadImage, SetNode, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2030683109536043010.json, 视频生成/图生视频/2007757058510168066.json, 视频生成/图生视频/2000895108826398721.json, 视频生成/图生视频/1999108736645988353.json, 视频生成/图生视频/2013783129579851778.json, 视频生成/图生视频/2046453872159367169.json, 视频生成/图生视频/2032725036360011777.json, 视频生成/图生视频/1985123438920683522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_255

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2030683109536043010.json、视频生成/图生视频/2007757058510168066.json、视频生成/图生视频/2000895108826398721.json、视频生成/图生视频/1999108736645988353.json、视频生成/图生视频/2013783129579851778.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `SetNode`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 7/8 个有
- `WanVideoLoraSelectMulti` —— 7/8 个有
- `DrawViTPose` —— 6/8 个有
- `Florence2Run` —— 6/8 个有
- `GroundingDinoModelLoader (segment anything2)` —— 6/8 个有
- `OnnxDetectionModelLoader` —— 6/8 个有
- `PoseAndFaceDetection` —— 6/8 个有
- `RHHiddenNodes` —— 6/8 个有
- `RH_Captioner` —— 6/8 个有
- `SDPoseOODLoader` —— 6/8 个有
- `SDPoseOODProcessor` —— 6/8 个有
- `ShowText|pysssss` —— 6/8 个有
- `Text Concatenate` —— 6/8 个有
- `Wan_video_prompt_generator` —— 6/8 个有
- `YOLOModelLoader` —— 6/8 个有
- `ImageUpscaleWithModel` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `UpscaleModelLoader` —— 4/8 个有
- `FlashVSRNode` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有
- `easy rangeInt` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
