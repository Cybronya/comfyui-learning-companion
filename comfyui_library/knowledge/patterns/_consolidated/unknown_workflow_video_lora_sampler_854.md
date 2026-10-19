---
name: unknown_workflow_video_lora_sampler_854
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.973
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950030719999500290.json, 视频生成/图生视频/1952744719957880834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_854

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1950030719999500290.json、视频生成/图生视频/1952744719957880834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `GLM_Vision_ImageToPrompt` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `QwenLoader` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `Wan22PromptSelector` —— 1/2 个有
- `WanVideoPromptExtender` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
