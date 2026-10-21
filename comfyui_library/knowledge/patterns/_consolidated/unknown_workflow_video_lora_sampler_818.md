---
name: unknown_workflow_video_lora_sampler_818
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8305
common_nodes: [CR Text Concatenate, CR Text Replace, CreateCFGScheduleFloatList, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch+, ImageResizeKJ, ImpactSwitch, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], PrimitiveBoolean, RHHiddenNodes, RH_Captioner, SetNode, SimpleMath+, TextBox, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy ifElse, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1952617990284087298.json, 视频生成/图生视频/1952604203145474049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_818

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1952617990284087298.json、视频生成/图生视频/1952604203145474049.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text Concatenate`
- `CR Text Replace`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `ImpactSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `PrimitiveBoolean`
- `RHHiddenNodes`
- `RH_Captioner`
- `SetNode`
- `SimpleMath+`
- `TextBox`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy ifElse`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
