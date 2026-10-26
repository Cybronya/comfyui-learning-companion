---
name: unknown_workflow_video_lora_sampler_573
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.926
common_nodes: [Int, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1-图生视频_1949678146162446337.json, 视频生成/图生视频/Wan2.2图生视频-Kijai优化版-极速优化版_1950213842141929473.json, 视频生成/图生视频/Wan2.2图生视频-Kijai优化版_1950147247079079938.json, 视频生成/图生视频/Wan2.2图生视频-Kijai版-课程专用_1950140877723361281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_573

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.1-图生视频_1949678146162446337.json、视频生成/图生视频/Wan2.2图生视频-Kijai优化版-极速优化版_1950213842141929473.json、视频生成/图生视频/Wan2.2图生视频-Kijai优化版_1950147247079079938.json、视频生成/图生视频/Wan2.2图生视频-Kijai版-课程专用_1950140877723361281.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `WanVideoSetBlockSwap` —— 3/4 个有
- `WanVideoSetLoRAs` —— 3/4 个有
- `WanVideoTextEncode` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `CreateCFGScheduleFloatList` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `StringToFloatList` —— 1/4 个有
- `WanVideoApplyNAG` —— 1/4 个有
- `WanVideoEasyCache` —— 1/4 个有
- `WanVideoEnhanceAVideo` —— 1/4 个有
- `WanVideoExperimentalArgs` —— 1/4 个有
- `WanVideoSLG` —— 1/4 个有
- `WanVideoTextEncodeSingle` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
