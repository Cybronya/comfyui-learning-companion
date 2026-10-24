---
name: unknown_workflow_video_lora_sampler_930
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.696
common_nodes: [AILab_MiniCPM_4_V, CLIPLoader, CLIPTextEncode, CreateScheduleFloatList, GetImageRangeFromBatch, GetLatentSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageConcatMulti, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, PreviewAny, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddExtraLatent, WanVideoAddPusaNoise, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSigmaToStep, WanVideoTextEmbedBridge, WanVideoTextEncodeCached, WanVideoTinyVAELoader, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/PUSA+VACE视频延长_1967482692935749633.json, 视频生成/文生视频/Pusa视频延长_1964993314611187714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_930

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/PUSA+VACE视频延长_1967482692935749633.json、视频生成/文生视频/Pusa视频延长_1964993314611187714.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
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
- `WanVideoVACEModelSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
