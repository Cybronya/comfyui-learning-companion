---
name: unknown_workflow_video_lora_sampler_424
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7644
common_nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy globalSeed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频性价比极致加速_1959896744446341122.json, 视频生成/图生视频/wan2.2-fun-镜头控制_1956984735042867201.json, 视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_1963202515145822209.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_1965041345570197506.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速_1959889034724192257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_424

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频性价比极致加速_1959896744446341122.json、视频生成/图生视频/wan2.2-fun-镜头控制_1956984735042867201.json、视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_1963202515145822209.json、视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_1965041345570197506.json、视频生成/文生视频/Wan2.2文生视频性价比极致加速_1959889034724192257.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy globalSeed`

**可变部分**（部分 workflow 才有）：
- `FloatToSigmas` —— 4/5 个有
- `StringToFloatList` —— 4/5 个有
- `WanVideoContextOptions` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `WanVideoSetRadialAttention` —— 4/5 个有
- `easy seed` —— 4/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `WanVideoImageToVideoEncode` —— 3/5 个有
- `WanVideoEmptyEmbeds` —— 2/5 个有
- `ADE_CameraPoseAdvanced` —— 1/5 个有
- `AILab_MiniCPM_4_V` —— 1/5 个有
- `CameraPoseVisualizer` —— 1/5 个有
- `LoadVideo` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `ShowText` —— 1/5 个有
- `WanVideoFunCameraEmbeds` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有
- `WanVideoScheduler` —— 1/5 个有
- `WanVideoSigmaToStep` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
