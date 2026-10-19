---
name: unknown_workflow_video_lora_sampler_892
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.91
common_nodes: [ImageResizeKJv2, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1948023695982899201.json, 视频生成/图生视频/1945823469433221121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_892

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1948023695982899201.json、视频生成/图生视频/1945823469433221121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoSetRadialAttention` —— 1/2 个有
- `WanVideoVACEEncode` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
