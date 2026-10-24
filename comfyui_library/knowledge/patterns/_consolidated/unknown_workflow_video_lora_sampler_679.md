---
name: unknown_workflow_video_lora_sampler_679
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPVisionLoader, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoUniAnimateDWPoseDetector, WanVideoUniAnimatePoseInput, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/极速万物跳舞Fusionx+Lightx2v+MagCache万相wan2.1万物跳舞打拳30帧流畅_1914138516001910786.json, 视频生成/图生视频/跳舞转绘_1921566992392978434.json, 视频生成/图生视频/🦖wan Unianimate_1934795083336065026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_679

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/极速万物跳舞Fusionx+Lightx2v+MagCache万相wan2.1万物跳舞打拳30帧流畅_1914138516001910786.json、视频生成/图生视频/跳舞转绘_1921566992392978434.json、视频生成/图生视频/🦖wan Unianimate_1934795083336065026.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoUniAnimateDWPoseDetector`
- `WanVideoUniAnimatePoseInput`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTeaCache` —— 2/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/3 个有
- `GIMMVFI_interpolate` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `VHS_VideoInfoLoaded` —— 1/3 个有
- `WanVideoExperimentalArgs` —— 1/3 个有
- `WanVideoMagCache` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
