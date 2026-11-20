---
name: unknown_workflow_video_lora_sampler_988
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.957
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, Florence2ModelLoader, Florence2Run, GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageResizeKJv2, ImageStitch, InspyrenetRembgAdvanced, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageRemoveAlpha, LoadImage, RHHiddenNodes, ShowText|pysssss, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, intToFloat _O]
problems: []
missing: []
members: [平台全量/wan2.2视频替换人物背景不改变 V1_1965333926627655682.json, 平台全量/多角色替换+动作迁移 搞笑恶搞+ 多遮罩模式控制 Wan2.2 Animate_2006883230821130241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_988

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/wan2.2视频替换人物背景不改变 V1_1965333926627655682.json、平台全量/多角色替换+动作迁移 搞笑恶搞+ 多遮罩模式控制 Wan2.2 Animate_2006883230821130241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageStitch`
- `InspyrenetRembgAdvanced`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEmbedBridge`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `intToFloat _O`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
