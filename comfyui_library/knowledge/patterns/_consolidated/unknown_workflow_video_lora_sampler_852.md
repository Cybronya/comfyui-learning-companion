---
name: unknown_workflow_video_lora_sampler_852
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.717
common_nodes: [FloatToSigmas, GetNode, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, StringToFloatList, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1956984735042867201.json, 视频生成/图生视频/1954777743701491714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_852

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1956984735042867201.json、视频生成/图生视频/1954777743701491714.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `FloatToSigmas`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `StringToFloatList`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ADE_CameraPoseAdvanced` —— 1/2 个有
- `CameraPoseVisualizer` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `String Literal` —— 1/2 个有
- `WanVideoFunCameraEmbeds` —— 1/2 个有
- `easy globalSeed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
