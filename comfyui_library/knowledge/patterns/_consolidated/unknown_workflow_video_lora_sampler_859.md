---
name: unknown_workflow_video_lora_sampler_859
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8115
common_nodes: [CreateCFGScheduleFloatList, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageSizeAndCount, INTConstant, LoadWanVideoT5TextEncoder, RH_LLMAPI_NODE, SetNode, ShowText, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy sleep]
problems: []
missing: [Primitive string multiline [Crystools], easy cleanGpuUsed, easy sleep]
members: [视频生成/图生视频/1975470690600136706.json, 视频生成/文生视频/1975486726921695233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_859

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1975470690600136706.json、视频生成/文生视频/1975486726921695233.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `RH_LLMAPI_NODE`
- `SetNode`
- `ShowText`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy sleep`

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `Primitive string multiline [Crystools]` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoScheduler` —— 1/2 个有
- `WanVideoSigmaToStep` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Primitive string multiline [Crystools]、easy cleanGpuUsed、easy sleep
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
