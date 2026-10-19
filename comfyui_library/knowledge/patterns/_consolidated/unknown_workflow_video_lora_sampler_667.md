---
name: unknown_workflow_video_lora_sampler_667
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.899
common_nodes: [LoadImage, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2065244368470106114.json, 视频生成/图生视频/2065243346691510273.json, 视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_667

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2065244368470106114.json、视频生成/图生视频/2065243346691510273.json、视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
