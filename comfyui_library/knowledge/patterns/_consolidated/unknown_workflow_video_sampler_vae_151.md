---
name: unknown_workflow_video_sampler_vae_151
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.936
common_nodes: [DWPreprocessor, ImageBlend, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1935150460091179009.json, 视频生成/图生视频/1948012807525662721.json, 视频生成/图生视频/1935591885543243777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_151

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1935150460091179009.json、视频生成/图生视频/1948012807525662721.json、视频生成/图生视频/1935591885543243777.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `DWPreprocessor`
- `ImageBlend`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy imageConcat` —— 2/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有
- `Evaluate Integers` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoMagCache` —— 1/3 个有
- `WanVideoTeaCache` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
