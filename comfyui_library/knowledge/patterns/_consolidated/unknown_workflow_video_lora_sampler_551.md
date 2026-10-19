---
name: unknown_workflow_video_lora_sampler_551
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.68
common_nodes: [AILab_MiniCPM_4_V, CLIPLoader, CLIPTextEncode, CreateScheduleFloatList, GetImageRangeFromBatch, GetLatentSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageConcatMulti, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, PreviewAny, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddExtraLatent, WanVideoAddPusaNoise, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSigmaToStep, WanVideoTextEmbedBridge, WanVideoTextEncodeCached, WanVideoTinyVAELoader, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: [LayerUtility: PurgeVRAM V2, SimpleMath+]
members: [视频生成/文生视频/1964993314611187714.json, 视频生成/文生视频/1967482692935749633.json, 视频生成/文生视频/PUSA+VACE视频延长_2072999575281246208.json, 视频生成/文生视频/Pusa视频延长_2072999589491548160.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_551

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1964993314611187714.json、视频生成/文生视频/1967482692935749633.json、视频生成/文生视频/PUSA+VACE视频延长_2072999575281246208.json、视频生成/文生视频/Pusa视频延长_2072999589491548160.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_MiniCPM_4_V`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateScheduleFloatList`
- `GetImageRangeFromBatch`
- `GetLatentSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `PreviewAny`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddExtraLatent`
- `WanVideoAddPusaNoise`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSigmaToStep`
- `WanVideoTextEmbedBridge`
- `WanVideoTextEncodeCached`
- `WanVideoTinyVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WanVideoVACEModelSelect` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、SimpleMath+
