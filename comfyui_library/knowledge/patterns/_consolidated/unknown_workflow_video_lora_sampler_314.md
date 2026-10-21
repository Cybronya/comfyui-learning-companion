---
name: unknown_workflow_video_lora_sampler_314
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.606286
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1976670695512068097.json, 视频生成/图生视频/1977205841587773441.json, 视频生成/图生视频/1977282428031115265.json, 视频生成/图生视频/1977738504492961794.json, 视频生成/图生视频/1970425229413654530.json, 视频生成/图生视频/2062169414258221058.json, 视频生成/图生视频/2010634733373366273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_314

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1976670695512068097.json、视频生成/图生视频/1977205841587773441.json、视频生成/图生视频/1977282428031115265.json、视频生成/图生视频/1977738504492961794.json、视频生成/图生视频/1970425229413654530.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 7 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
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
- `DrawViTPose` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `GetImageSizeAndCount` —— 5/7 个有
- `GrowMask` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `INTConstant` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `MathExpression|pysssss` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `WanVideoEncode` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `GIMMVFI_interpolate` —— 2/7 个有
- `GetImageSize+` —— 2/7 个有
- `GrowMaskWithBlur` —— 2/7 个有
- `ImageBlend` —— 2/7 个有
- `ImageFromBatch` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `ToFloat` —— 2/7 个有
- `WanVideoContextOptions` —— 2/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/7 个有
- `WanVideoUni3C_embeds` —— 2/7 个有
- `Int` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SaveLatent` —— 1/7 个有
- `TT_img_enc_v2` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
