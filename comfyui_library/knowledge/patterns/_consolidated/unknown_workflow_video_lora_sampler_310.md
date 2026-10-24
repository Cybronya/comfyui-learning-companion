---
name: unknown_workflow_video_lora_sampler_310
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.597571
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan-Animate_V2-动作迁移自动版_1975030930718986242.json, 视频生成/图生视频/Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json, 视频生成/图生视频/Wan2.2-Animate加强版V2.0_1980113724029702145.json, 视频生成/图生视频/WanAnimate V2 主体替换（KJ版）_1977205841587773441.json, 视频生成/图生视频/WanAnimate V2 姿势参考（KJ版）_1977282428031115265.json, 视频生成/图生视频/舞蹈视频人物替换_1983085978363568129.json, 视频生成/图生视频/（KJ版）主体替换WanAnimate V2_1974839339156901889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_310

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan-Animate_V2-动作迁移自动版_1975030930718986242.json、视频生成/图生视频/Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json、视频生成/图生视频/Wan2.2-Animate加强版V2.0_1980113724029702145.json、视频生成/图生视频/WanAnimate V2 主体替换（KJ版）_1977205841587773441.json、视频生成/图生视频/WanAnimate V2 姿势参考（KJ版）_1977282428031115265.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 7 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `ImageResizeKJv2`
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
- `DownloadAndLoadSAM2Model` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `GrowMask` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `MathExpression|pysssss` —— 6/7 个有
- `Sam2Segmentation` —— 6/7 个有
- `ImageFromBatch` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `ImpactInt` —— 4/7 个有
- `Int` —— 4/7 个有
- `PreviewImage` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `GetImageSizeAndCount` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `ToFloat` —— 2/7 个有
- `GetImageSize+` —— 1/7 个有
- `GrowMaskWithBlur` —— 1/7 个有
- `ImageBlend` —— 1/7 个有
- `ImageRemoveBackground+` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有
- `RemBGSession+` —— 1/7 个有
- `Text` —— 1/7 个有
- `Textbox` —— 1/7 个有
- `WanVideoEncode` —— 1/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/7 个有
- `WanVideoUni3C_embeds` —— 1/7 个有
- `easy positive` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
