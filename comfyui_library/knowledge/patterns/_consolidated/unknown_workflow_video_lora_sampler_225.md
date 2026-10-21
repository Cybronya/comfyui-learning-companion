---
name: unknown_workflow_video_lora_sampler_225
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.600333
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: [int _O]
members: [视频生成/图生视频/2004522934133817346.json, 视频生成/图生视频/2029116870359519233.json, 视频生成/图生视频/2020345629322518529.json, 视频生成/图生视频/2046604886866927617.json, 视频生成/图生视频/2059509696591122433.json, 视频生成/图生视频/1980236223493136385.json, 视频生成/图生视频/1983085978363568129.json, 视频生成/图生视频/1974839339156901889.json, 视频生成/文生视频/1975351604679413761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_225

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2004522934133817346.json、视频生成/图生视频/2029116870359519233.json、视频生成/图生视频/2020345629322518529.json、视频生成/图生视频/2046604886866927617.json、视频生成/图生视频/2059509696591122433.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `MathExpression|pysssss` —— 8/9 个有
- `ImageConcatMulti` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `ImageFromBatch` —— 6/9 个有
- `ImpactInt` —— 6/9 个有
- `BlockifyMask` —— 5/9 个有
- `DownloadAndLoadSAM2Model` —— 5/9 个有
- `DrawMaskOnImage` —— 5/9 个有
- `GrowMask` —— 5/9 个有
- `Sam2Segmentation` —— 5/9 个有
- `Textbox` —— 5/9 个有
- `GetImageSizeAndCount` —— 3/9 个有
- `CM_IntToFloat` —— 2/9 个有
- `CR Text` —— 2/9 个有
- `ImageFromBatch+` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `WanVideoLoraSelect` —— 2/9 个有
- `easy int` —— 2/9 个有
- `int _O` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：int _O
