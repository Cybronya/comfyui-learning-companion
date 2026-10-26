---
name: unknown_workflow_video_lora_sampler_1021
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7765
common_nodes: [CreateCFGScheduleFloatList, Fast Groups Bypasser (rgthree), GetImageSizeAndCount, INTConstant, ImageFromBatch, ImageListToImageBatch, Int, LoadWanVideoT5TextEncoder, RIFE VFI, SaveImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 文生视频高动态质量--(Palingenesis版)_1972223829290446850.json, 视频生成/文生视频/Work-Fisher_Wan2.2-T2V增强版_1971802147362893826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1021

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 文生视频高动态质量--(Palingenesis版)_1972223829290446850.json、视频生成/文生视频/Work-Fisher_Wan2.2-T2V增强版_1971802147362893826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageFromBatch`
- `ImageListToImageBatch`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `RIFE VFI`
- `SaveImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text` —— 1/2 个有
- `WanVideoScheduler` —— 1/2 个有
- `WanVideoSigmaToStep` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
