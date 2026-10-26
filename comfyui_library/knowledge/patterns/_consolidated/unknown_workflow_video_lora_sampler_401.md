---
name: unknown_workflow_video_lora_sampler_401
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.731833
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, ImageConcatMulti, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/4V商用版本 支持 运镜，切镜头，武术，跳舞，侧面迁移，_2093353108847030274.json, 视频生成/图生视频/Animate最强—人物姿态迁移！！--双人视频--单人视频！！_1978005827682455554.json, 视频生成/图生视频/Wan-Animate人物替换V3_1989226857599995905.json, 视频生成/图生视频/Wan-Animate人物替换V3_2002723614807998465.json, 视频生成/图生视频/Wan-Animate人物替换_1988762483311652866.json, 视频生成/图生视频/Wan-Animate人物替换遮罩版V3_2001920042348494850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_401

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/4V商用版本 支持 运镜，切镜头，武术，跳舞，侧面迁移，_2093353108847030274.json、视频生成/图生视频/Animate最强—人物姿态迁移！！--双人视频--单人视频！！_1978005827682455554.json、视频生成/图生视频/Wan-Animate人物替换V3_1989226857599995905.json、视频生成/图生视频/Wan-Animate人物替换V3_2002723614807998465.json、视频生成/图生视频/Wan-Animate人物替换_1988762483311652866.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `GetImageSizeAndCount` —— 5/6 个有
- `ImageFromBatch` —— 5/6 个有
- `Int` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 5/6 个有
- `LayerUtility: PurgeVRAM V2` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `BBoxesToSAM2` —— 4/6 个有
- `CM_IntToFloat` —— 4/6 个有
- `DownloadAndLoadQwenModel` —— 4/6 个有
- `LayerMask: SAM2Ultra` —— 4/6 个有
- `MaskPreview+` —— 4/6 个有
- `QwenVLDetection` —— 4/6 个有
- `RHHiddenNodes` —— 4/6 个有
- `SeCModelLoader` —— 4/6 个有
- `SeCVideoSegmentation` —— 4/6 个有
- `BlockifyMask` —— 3/6 个有
- `DrawMaskOnImage` —— 3/6 个有
- `GrowMask` —— 3/6 个有
- `ImpactInt` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `GemmaAPITextEncode` —— 1/6 个有
- `ShellAgentPluginSaveAudios` —— 1/6 个有
- `Textbox` —— 1/6 个有
- `VHS_VideoInfo` —— 1/6 个有
- `WanVideoTorchCompileSettings` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
