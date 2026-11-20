---
name: unknown_workflow_video_lora_sampler_911
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.546
common_nodes: [Anything Everywhere, BlockifyMask, CLIPVisionLoader, CR Prompt Text, Display Any (rgthree), DrawMaskOnImage, DrawViTPose, Evaluate Integers, GetImageSize, GetNode, ImageBatch, ImageConcatMulti, ImageFromBatch+, ImageResizeKJv2, Int, JWImageExtractFromBatch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, PrimitiveFloat, RepeatImageBatch, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization]
problems: []
missing: []
members: [视频生成/图生视频/WanAnimate_Sam3 精准替换角色_1996398131812114433.json, 视频生成/图生视频/超精准sam3人物替换，视频主体替换 生成速度快 效果好_2011830823506419713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_911

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WanAnimate_Sam3 精准替换角色_1996398131812114433.json、视频生成/图生视频/超精准sam3人物替换，视频主体替换 生成速度快 效果好_2011830823506419713.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `Display Any (rgthree)`
- `DrawMaskOnImage`
- `DrawViTPose`
- `Evaluate Integers`
- `GetImageSize`
- `GetNode`
- `ImageBatch`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `Int`
- `JWImageExtractFromBatch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `PrimitiveFloat`
- `RepeatImageBatch`
- `SetNode`
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
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`

**可变部分**（部分 workflow 才有）：
- `Manual XY Entry Info` —— 1/2 个有
- `MathExpressionNode` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ZML_IntegerFloatConverter` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
