---
name: unknown_workflow_video_lora_sampler_674
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.58625
common_nodes: [CreateScheduleFloatList, GetImageRangeFromBatch, GetLatentSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageResizeKJv2, PreviewAny, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddExtraLatent, WanVideoAddPusaNoise, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSigmaToStep, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Pusa_extension_loop 循环放大_1964706031962046466.json, 平台全量/Pusa_extension_once 一次扩展工作流_1964689032544440322.json, 视频生成/文生视频/PUSA+VACE视频延长_1967482692935749633.json, 视频生成/文生视频/Pusa视频延长_1964993314611187714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_674

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Pusa_extension_loop 循环放大_1964706031962046466.json、平台全量/Pusa_extension_once 一次扩展工作流_1964689032544440322.json、视频生成/文生视频/PUSA+VACE视频延长_1967482692935749633.json、视频生成/文生视频/Pusa视频延长_1964993314611187714.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateScheduleFloatList`
- `GetImageRangeFromBatch`
- `GetLatentSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJv2`
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
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V` —— 2/4 个有
- `CLIPLoader` —— 2/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `WanVideoTextEmbedBridge` —— 2/4 个有
- `WanVideoTinyVAELoader` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `WanVideoVACEModelSelect` —— 1/4 个有
- `easy forLoopEnd` —— 1/4 个有
- `easy forLoopStart` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
