---
name: unknown_workflow_video_lora_sampler_441
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9622
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1980926100463337474.json, 视频生成/图生视频/1952803879810494466.json, 视频生成/图生视频/1963047092535136257.json, 视频生成/图生视频/1956285826319699969.json, 视频生成/图生视频/1978365294227906562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_441

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1980926100463337474.json、视频生成/图生视频/1952803879810494466.json、视频生成/图生视频/1963047092535136257.json、视频生成/图生视频/1956285826319699969.json、视频生成/图生视频/1978365294227906562.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
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
- `SimpleMath+` —— 2/5 个有
- `WanVideoContextOptions` —— 2/5 个有
- `WanVideoEncodeLatentBatch` —— 2/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `WanVideoScheduler` —— 1/5 个有
- `WanVideoSigmaToStep` —— 1/5 个有
- `easy float` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
