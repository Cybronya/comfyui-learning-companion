---
name: unknown_workflow_video_upscale_sampler_23
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4445
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Display Int (rgthree), DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageSizeAndCount, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy int]
problems: []
missing: []
members: [视频生成/图生视频/视频生成-MiniMax_H3-参考生视频_2084163650293686273.json, 视频生成/文生视频/视频生成-MiniMax_H3-首尾帧生视频_2084190567281549314.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/视频生成-MiniMax_H3-参考生视频_2084163650293686273.json、视频生成/文生视频/视频生成-MiniMax_H3-首尾帧生视频_2084190567281549314.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：44%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Display Int (rgthree)`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2TorchCompileSettings`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
