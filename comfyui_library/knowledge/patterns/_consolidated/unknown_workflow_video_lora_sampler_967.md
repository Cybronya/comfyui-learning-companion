---
name: unknown_workflow_video_lora_sampler_967
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.681
common_nodes: [Bjornulf_ShowFloat, Bjornulf_ShowInt, BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GrowMaskWithBlur, ImageFromBatch, LayerUtility: ImageBlend, LayerUtility: PurgeVRAM V2, LoadImage, Mask Invert, MathExpression|pysssss, OnnxDetectionModelLoader, PlaySound|pysssss, PointsEditor, PoseAndFaceDetection, PreviewImage, SeCModelLoader, SeCVideoSegmentation, SystemNotification|pysssss, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/3D人物替换（测试版）_1983855894943404033.json, 平台全量/角色迁移 (Sec遮罩KJ手动)_1984100501258174466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_967

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/3D人物替换（测试版）_1983855894943404033.json、平台全量/角色迁移 (Sec遮罩KJ手动)_1984100501258174466.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowFloat`
- `Bjornulf_ShowInt`
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `ImageFromBatch`
- `LayerUtility: ImageBlend`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `Mask Invert`
- `MathExpression|pysssss`
- `OnnxDetectionModelLoader`
- `PlaySound|pysssss`
- `PointsEditor`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SystemNotification|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 1/2 个有
- `Float` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `Seed_` —— 1/2 个有
- `Text` —— 1/2 个有
- `ToFloat` —— 1/2 个有
- `easy seed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
