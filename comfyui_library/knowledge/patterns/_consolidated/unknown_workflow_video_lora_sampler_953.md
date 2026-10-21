---
name: unknown_workflow_video_lora_sampler_953
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CreateCFGScheduleFloatList, Float to Int, Int, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/WAN2.2-文生视频_2018966000456175618.json, 视频生成/文生视频/1952158294372765697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_953

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/WAN2.2-文生视频_2018966000456175618.json、视频生成/文生视频/1952158294372765697.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `Float to Int`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadWav2VecModel` —— 1/2 个有
- `Float` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MathExpression_UTK` —— 1/2 个有
- `MultiTalkModelLoader` —— 1/2 个有
- `MultiTalkWav2VecEmbeds` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `RH_GetAudioDuration` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
