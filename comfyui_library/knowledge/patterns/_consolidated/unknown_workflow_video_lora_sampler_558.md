---
name: unknown_workflow_video_lora_sampler_558
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7492
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json, 图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json, 平台全量/Wan Animate V2+SeC视频角色替换_2058762900847812610.json, 平台全量/Wan Animate视频换背景_2059962221534474241.json, 平台全量/Wan2.2 Animate 高质量视频换背景_2010992426214760449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_558

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json、图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json、平台全量/Wan Animate V2+SeC视频角色替换_2058762900847812610.json、平台全量/Wan Animate视频换背景_2059962221534474241.json、平台全量/Wan2.2 Animate 高质量视频换背景_2010992426214760449.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SeCModelLoader`
- `SeCVideoSegmentation`
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
- `GetImageSizeAndCount` —— 4/5 个有
- `GrowMaskWithBlur` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `DrawViTPose` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `ImageCompositeMasked` —— 3/5 个有
- `ImageFromBatch` —— 3/5 个有
- `ImageResize+` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `VHS_VideoInfo` —— 3/5 个有
- `WanVideoContextOptions` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `AILab_QwenVL` —— 2/5 个有
- `EmptyImage` —— 2/5 个有
- `LayerMask: MaskInvert` —— 2/5 个有
- `MaskToImage` —— 2/5 个有
- `PDIMAGE_LongerSize` —— 2/5 个有
- `PointsEditor` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `TTP_text_mix` —— 2/5 个有
- `TextInput_` —— 2/5 个有
- `ACE_ImageFaceCrop` —— 1/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `ClothesSegment` —— 1/5 个有
- `CoordinatePlotter` —— 1/5 个有
- `GrowMask` —— 1/5 个有
- `ImageRepeat` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
