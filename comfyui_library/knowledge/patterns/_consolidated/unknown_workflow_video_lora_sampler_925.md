---
name: unknown_workflow_video_lora_sampler_925
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7935
common_nodes: [GetImageSize, INTConstant, Image Blank, ImageCompositeMasked, ImageResizeKJv2, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy ifElse]
problems: []
missing: [Image Blank, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, String Literal]
members: [视频生成/文生视频/1963899418183438337.json, 视频生成/文生视频/WAN2.2-AllInOne单图参考_2072999602976235520.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_925

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/1963899418183438337.json、视频生成/文生视频/WAN2.2-AllInOne单图参考_2072999602976235520.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize`
- `INTConstant`
- `Image Blank`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy ifElse`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Image Blank、LayerMask: LoadFlorence2Model、LayerMask: ObjectDetectorFL2、LayerMask: SAM2Ultra、LayerUtility: PurgeVRAM
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
