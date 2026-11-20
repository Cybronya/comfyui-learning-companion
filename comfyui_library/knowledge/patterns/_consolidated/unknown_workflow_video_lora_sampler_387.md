---
name: unknown_workflow_video_lora_sampler_387
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.542125
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetNode, GrowMask, ImageConcatMulti, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-Animate加强版V2.0_1980113724029702145.json, 视频生成/图生视频/WanAnimate V2 主体替换（KJ版）_1977205841587773441.json, 视频生成/图生视频/WanAnimate V2 姿势参考（KJ版）_1977282428031115265.json, 视频生成/图生视频/动作迁移人物替换主体替换_2046604886866927617.json, 视频生成/图生视频/动作迁移人物替换主体替换_2059509696591122433.json, 视频生成/图生视频/舞蹈视频人物替换_1983085978363568129.json, 视频生成/图生视频/（KJ版）主体替换WanAnimate V2_1974839339156901889.json, 视频生成/文生视频/wan animate v2——优化版_1975351604679413761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_387

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-Animate加强版V2.0_1980113724029702145.json、视频生成/图生视频/WanAnimate V2 主体替换（KJ版）_1977205841587773441.json、视频生成/图生视频/WanAnimate V2 姿势参考（KJ版）_1977282428031115265.json、视频生成/图生视频/动作迁移人物替换主体替换_2046604886866927617.json、视频生成/图生视频/动作迁移人物替换主体替换_2059509696591122433.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 8 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 7/8 个有
- `ImageFromBatch` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `MathExpression|pysssss` —— 7/8 个有
- `Sam2Segmentation` —— 7/8 个有
- `Int` —— 6/8 个有
- `ImpactInt` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `Textbox` —— 3/8 个有
- `Anything Everywhere3` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `ToFloat` —— 2/8 个有
- `GetImageSizeAndCount` —— 1/8 个有
- `ImageBlend` —— 1/8 个有
- `ImageRemoveBackground+` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有
- `RemBGSession+` —— 1/8 个有
- `easy positive` —— 1/8 个有
- `int _O` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
