---
name: unknown_workflow_video_sampler_vae_82
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9385
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 Fusion X 图生视频_1949673530895540225.json, 视频生成/图生视频/fusionx 动漫视频 图生视频_1947087609853685762.json, 视频生成/图生视频/wan2.1-FusionX+NAG超高清图生视频_1936289758157115393.json, 视频生成/图生视频/wan2.1FusionX超高清图生视频_1934598793851510785.json, 视频生成/图生视频/高清图生视频工作流-Wan fusionX_1937875802723913730.json, 视频生成/图生视频/龙明wan2.1 图生视频fusionX+NAG_1935009209383886850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_82

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 Fusion X 图生视频_1949673530895540225.json、视频生成/图生视频/fusionx 动漫视频 图生视频_1947087609853685762.json、视频生成/图生视频/wan2.1-FusionX+NAG超高清图生视频_1936289758157115393.json、视频生成/图生视频/wan2.1FusionX超高清图生视频_1934598793851510785.json、视频生成/图生视频/高清图生视频工作流-Wan fusionX_1937875802723913730.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 4/6 个有
- `GIMMVFI_interpolate` —— 4/6 个有
- `ImageResizeKJ` —— 4/6 个有
- `ImageScaleToMegapixels` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `UpscaleModelLoader` —— 3/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `Note Plus (mtb)` —— 2/6 个有
- `ImageSmartSharpen+` —— 1/6 个有
- `LoadImageFromUrl` —— 1/6 个有
- `LoadWanVideoClipTextEncoder` —— 1/6 个有
- `WanVideoClipVisionEncode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
