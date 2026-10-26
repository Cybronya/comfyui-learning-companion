---
name: unknown_workflow_video_lora_sampler_580
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83425
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频性价比极致加速_1959896744446341122.json, 视频生成/图生视频/wan2.2 图生图_1995404196142833665.json, 视频生成/文生视频/1022对比测试_1981324716671664130.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_1965041345570197506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_580

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频性价比极致加速_1959896744446341122.json、视频生成/图生视频/wan2.2 图生图_1995404196142833665.json、视频生成/文生视频/1022对比测试_1981324716671664130.json、视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_1965041345570197506.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
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
- `FloatToSigmas` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `String Literal` —— 3/4 个有
- `StringToFloatList` —— 3/4 个有
- `WanVideoSetRadialAttention` —— 3/4 个有
- `easy globalSeed` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `INTConstant` —— 2/4 个有
- `WanVideoContextOptions` —— 2/4 个有
- `WanVideoScheduler` —— 2/4 个有
- `WanVideoSigmaToStep` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `CLIPVisionLoader` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `Int` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `WanVideoClipVisionEncode` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
