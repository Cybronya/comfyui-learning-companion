---
name: unknown_workflow_video_lora_sampler_493
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.539333
common_nodes: [Anything Everywhere, BlockifyMask, CLIPVisionLoader, CR Prompt Text, Display Any (rgthree), DrawMaskOnImage, DrawViTPose, GetNode, ImageConcatMulti, ImageFromBatch+, ImageResizeKJv2, JWImageExtractFromBatch, JWInteger, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/[众馨]角色替换V7  SAM3遮罩_2018495014267002882.json, 平台全量/sam3一句话人物替换(长视频)_1993676469306146818.json, 平台全量/一句话替换视频中的人物_1991148338110136321.json, 平台全量/一句话替换视频中的人物_1992132613513039874.json, 视频生成/图生视频/WanAnimate_Sam3 精准替换角色_1996398131812114433.json, 视频生成/图生视频/超精准sam3人物替换，视频主体替换 生成速度快 效果好_2011830823506419713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_493

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/[众馨]角色替换V7  SAM3遮罩_2018495014267002882.json、平台全量/sam3一句话人物替换(长视频)_1993676469306146818.json、平台全量/一句话替换视频中的人物_1991148338110136321.json、平台全量/一句话替换视频中的人物_1992132613513039874.json、视频生成/图生视频/WanAnimate_Sam3 精准替换角色_1996398131812114433.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 6 个 workflow 都包含：
- `Anything Everywhere`
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `Display Any (rgthree)`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWImageExtractFromBatch`
- `JWInteger`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
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

**可变部分**（部分 workflow 才有）：
- `Manual XY Entry Info` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `Evaluate Integers` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `ImageBatch` —— 4/6 个有
- `Int` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `RH_Translator` —— 4/6 个有
- `RepeatImageBatch` —— 4/6 个有
- `easy sam3ModelLoader` —— 4/6 个有
- `easy sam3VideoSegmentation` —— 4/6 个有
- `easy sam3Visualization` —— 4/6 个有
- `MathExpressionNode` —— 3/6 个有
- `ZML_IntegerFloatConverter` —— 3/6 个有
- `GrowMask` —— 1/6 个有
- `LayerMask: SAM2VideoUltra` —— 1/6 个有
- `LoadSAM3Model` —— 1/6 个有
- `MaskListToMaskBatch` —— 1/6 个有
- `PointsEditor` —— 1/6 个有
- `SAM3Segmentation` —— 1/6 个有
- `Sa2VANodeTpl` —— 1/6 个有
- `easy imageBatchToImageList` —— 1/6 个有
- `easy imageListToImageBatch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
