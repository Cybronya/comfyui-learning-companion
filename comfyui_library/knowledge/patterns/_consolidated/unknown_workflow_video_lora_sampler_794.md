---
name: unknown_workflow_video_lora_sampler_794
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9675
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, ImpactSwitch, LoadWanVideoT5TextEncoder, RH_LLMAPI_NODE, SeargePromptText, ShowText, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.2 图生视频（优化版）_1951564039392579586.json, 视频生成/文生视频/Wan 2.2 文生视频（优化版）_1951554035532902402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_794

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2 图生视频（优化版）_1951564039392579586.json、视频生成/文生视频/Wan 2.2 文生视频（优化版）_1951554035532902402.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `ImpactSwitch`
- `LoadWanVideoT5TextEncoder`
- `RH_LLMAPI_NODE`
- `SeargePromptText`
- `ShowText`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
