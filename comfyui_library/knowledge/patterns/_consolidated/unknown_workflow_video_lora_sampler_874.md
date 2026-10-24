---
name: unknown_workflow_video_lora_sampler_874
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8785
common_nodes: [GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveInt, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/丝滑转场+首尾帧—Wan2.2 SmoothMix_1981250536429314050.json, 视频生成/图生视频/首尾帧Wan2.2SmoothMix高动态首尾帧_1979812422854807553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_874

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/丝滑转场+首尾帧—Wan2.2 SmoothMix_1981250536429314050.json、视频生成/图生视频/首尾帧Wan2.2SmoothMix高动态首尾帧_1979812422854807553.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `ImageBatchMultiple+` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `TextBox` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
