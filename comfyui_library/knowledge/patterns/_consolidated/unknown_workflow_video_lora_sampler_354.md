---
name: unknown_workflow_video_lora_sampler_354
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.523125
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Comfyui教学第五期-动作迁移_Wan-animate_2010172877395464194.json, 平台全量/KJ版  Wan Animate2.2主体替换（无限时长）_1972982632000655362.json, 平台全量/SeC整合版：3.WanAnimate 主体替换(手动)2.0_1986448638467600385.json, 平台全量/SeC整合版：6.WanAnimate 人物A的动作+B的表情混合迁移_1986448840238759938.json, 平台全量/Wan Animate2.2 主体不变只变背景_1971803048211378177.json, 平台全量/Wan Animate2.2 替换主体，保留背景_1988619047652737026.json, 平台全量/Wan Animate2.2 替换背景 需点选主体_1972736005038100482.json, 数字人/数字人/Wan Animate2.2 主体替换2_1970810037335695361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_354

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/Comfyui教学第五期-动作迁移_Wan-animate_2010172877395464194.json、平台全量/KJ版  Wan Animate2.2主体替换（无限时长）_1972982632000655362.json、平台全量/SeC整合版：3.WanAnimate 主体替换(手动)2.0_1986448638467600385.json、平台全量/SeC整合版：6.WanAnimate 人物A的动作+B的表情混合迁移_1986448840238759938.json、平台全量/Wan Animate2.2 主体不变只变背景_1971803048211378177.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 8 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 7/8 个有
- `DownloadAndLoadSAM2Model` —— 7/8 个有
- `FaceMaskFromPoseKeypoints` —— 7/8 个有
- `ImageConcatMulti` —— 7/8 个有
- `ImageCropByMaskAndResize` —— 7/8 个有
- `PixelPerfectResolution` —— 7/8 个有
- `PointsEditor` —— 7/8 个有
- `Sam2Segmentation` —— 7/8 个有
- `WanVideoTextEncodeCached` —— 7/8 个有
- `CR Prompt Text` —— 5/8 个有
- `JWInteger` —— 5/8 个有
- `Anything Everywhere` —— 4/8 个有
- `GrowMask` —— 4/8 个有
- `ImageFromBatch+` —— 4/8 个有
- `Manual XY Entry Info` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `WanVideoEncode` —— 4/8 个有
- `WanVideoUni3C_ControlnetLoader` —— 4/8 个有
- `WanVideoUni3C_embeds` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `INTConstant` —— 3/8 个有
- `WanVideoContextOptions` —— 3/8 个有
- `Display Any (rgthree)` —— 2/8 个有
- `InvertMask` —— 2/8 个有
- `CLIPLoader` —— 1/8 个有
- `CLIPTextEncode` —— 1/8 个有
- `DrawViTPose` —— 1/8 个有
- `OnnxDetectionModelLoader` —— 1/8 个有
- `PoseAndFaceDetection` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `RunningHub Deepcleaner` —— 1/8 个有
- `WanVideoTextEmbedBridge` —— 1/8 个有
- `easy sam3ModelLoader` —— 1/8 个有
- `easy sam3VideoSegmentation` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
