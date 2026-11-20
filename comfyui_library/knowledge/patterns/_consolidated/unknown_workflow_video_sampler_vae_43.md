---
name: unknown_workflow_video_sampler_vae_43
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9422
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/分镜小工具 _ 图生视频_1940804451999629313.json, 视频生成/图生视频/B2-wan2.1 720p- MagCache加速版图生视频FusionX+NAG_1934577756585795586.json, 视频生成/图生视频/B2-wan2.1 720p图生视频FusionX+NAG_1934068571276533761.json, 视频生成/图生视频/FX超级图生视频_1934656036613595137.json, 视频生成/图生视频/fusionx 动漫视频 图生视频_1947087609853685762.json, 视频生成/图生视频/wan2.1FusionX超高清图生视频_1934598793851510785.json, 视频生成/图生视频/图生视频FusionX+NAG_1934129997869142017.json, 视频生成/图生视频/图生视频（WanFusionX）（魔方）_1948023695982899201.json, 视频生成/图生视频/首+尾帧视频转绘（FusionX_VACE无V）(魔方)_1945823469433221121.json, 视频生成/图生视频/首帧+视频转绘(WanFusionX_VACE)（魔方）_1948012807525662721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_43

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/分镜小工具 _ 图生视频_1940804451999629313.json、视频生成/图生视频/B2-wan2.1 720p- MagCache加速版图生视频FusionX+NAG_1934577756585795586.json、视频生成/图生视频/B2-wan2.1 720p图生视频FusionX+NAG_1934068571276533761.json、视频生成/图生视频/FX超级图生视频_1934656036613595137.json、视频生成/图生视频/fusionx 动漫视频 图生视频_1947087609853685762.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoImageToVideoEncode` —— 8/10 个有
- `PreviewImage` —— 7/10 个有
- `ImageResizeKJ` —— 5/10 个有
- `ImageResizeKJv2` —— 5/10 个有
- `WanVideoMagCache` —— 4/10 个有
- `JWInteger` —— 3/10 个有
- `WanVideoExperimentalArgs` —— 3/10 个有
- `WanVideoLoraSelect` —— 3/10 个有
- `WanVideoTorchCompileSettings` —— 3/10 个有
- `WanVideoVACEModelSelect` —— 3/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `WanVideoVACEEncode` —— 2/10 个有
- `DWPreprocessor` —— 1/10 个有
- `DepthAnythingPreprocessor` —— 1/10 个有
- `Evaluate Integers` —— 1/10 个有
- `GetImageSizeAndCount` —— 1/10 个有
- `ImageBlend` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `WanVideoSetRadialAttention` —— 1/10 个有
- `WanVideoVACEStartToEndFrame` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
