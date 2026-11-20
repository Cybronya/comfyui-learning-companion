---
name: unknown_workflow_video_lora_sampler_816
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.604
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, MaskToImage, PointsEditor, PreviewImage, PrimitiveStringMultiline, SetNode, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy float]
problems: []
missing: []
members: [平台全量/[AI小兵哥]wan2_2_Animate-长视频画遮罩去字幕去水印工作流_1978458264746790913.json, 平台全量/去字幕工作流_2050467383827017729.json, 平台全量/🦖wan2.2_去字幕去水印工作流_2052571007172521985.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_816

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/[AI小兵哥]wan2_2_Animate-长视频画遮罩去字幕去水印工作流_1978458264746790913.json、平台全量/去字幕工作流_2050467383827017729.json、平台全量/🦖wan2.2_去字幕去水印工作流_2052571007172521985.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `MaskToImage`
- `PointsEditor`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SetNode`
- `VHS_DuplicateMasks`
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
- `easy float`

**可变部分**（部分 workflow 才有）：
- `SomethingToString` —— 2/3 个有
- `VHS_SelectImages` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `VAELoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
