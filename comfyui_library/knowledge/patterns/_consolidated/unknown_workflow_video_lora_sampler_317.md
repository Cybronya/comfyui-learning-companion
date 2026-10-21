---
name: unknown_workflow_video_lora_sampler_317
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.791714
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1959896744446341122.json, 视频生成/图生视频/1995404196142833665.json, 视频生成/文生视频/1022对比测试_1981324716671664130.json, 视频生成/文生视频/Wan2.2 V5-MoE Fast I2V for Characters_2072999497279774720.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V3_2072999534260953088.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-1022版_1981325230595629057.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-1030-非人_1984904372494680065.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_317

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1959896744446341122.json、视频生成/图生视频/1995404196142833665.json、视频生成/文生视频/1022对比测试_1981324716671664130.json、视频生成/文生视频/Wan2.2 V5-MoE Fast I2V for Characters_2072999497279774720.json、视频生成/文生视频/Wan2.2图生视频性价比极致加速V3_2072999534260953088.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
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
- `GetNode` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `String Literal` —— 6/7 个有
- `WanVideoSetRadialAttention` —— 6/7 个有
- `easy globalSeed` —— 6/7 个有
- `easy seed` —— 6/7 个有
- `Int` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `WanVideoScheduler` —— 5/7 个有
- `WanVideoSigmaToStep` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `FloatToSigmas` —— 3/7 个有
- `StringToFloatList` —— 3/7 个有
- `INTConstant` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `WanVideoClipVisionEncode` —— 1/7 个有
- `WanVideoContextOptions` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
