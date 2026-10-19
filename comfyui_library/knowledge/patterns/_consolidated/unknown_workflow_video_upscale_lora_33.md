---
name: unknown_workflow_video_upscale_lora_33
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6545
common_nodes: [Batch Make (mtb), CR Text, CreateCFGScheduleFloatList, GetNode, INTConstant, ImageUpscaleWithModelBatched, KEEP_ModelLoader, KEEP_ProcessImageSequence, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, PreviewAny, RH_LLMAPI_NODE, RIFE VFI, SetNode, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEasyCache, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: [Batch Make (mtb), CR Text, KEEP_ModelLoader, KEEP_ProcessImageSequence, LayerUtility: PurgeVRAM V2, RIFE VFI, easy cleanGpuUsed, easy clearCacheAll]
members: [视频生成/图生视频/1977031736406233089.json, 视频生成/文生视频/1977028133595553793.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1977031736406233089.json、视频生成/文生视频/1977028133595553793.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `Batch Make (mtb)`
- `CR Text`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `INTConstant`
- `ImageUpscaleWithModelBatched`
- `KEEP_ModelLoader`
- `KEEP_ProcessImageSequence`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `PreviewAny`
- `RH_LLMAPI_NODE`
- `RIFE VFI`
- `SetNode`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `ConcatTextOfUtils` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PDImageResizeV3` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Nano_Banana_Image2Image` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Batch Make (mtb)、CR Text、KEEP_ModelLoader、KEEP_ProcessImageSequence、LayerUtility: PurgeVRAM V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
