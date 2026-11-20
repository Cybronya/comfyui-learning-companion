---
name: unknown_workflow_video_lora_sampler_1087
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.898
common_nodes: [CLIPVisionLoader, CM_IntToFloat, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveInt, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy int]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频+自动提示词扩写_1954168086414934018.json, 视频生成/图生视频/Wan2.2图生视频（最新优化版）_1987880762861137921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1087

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频+自动提示词扩写_1954168086414934018.json、视频生成/图生视频/Wan2.2图生视频（最新优化版）_1987880762861137921.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V_Advanced` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `FlashVSRNode` —— 1/2 个有
- `Int` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
