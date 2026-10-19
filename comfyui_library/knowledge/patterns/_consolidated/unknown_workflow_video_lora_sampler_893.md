---
name: unknown_workflow_video_lora_sampler_893
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7685
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoVRAMManagement]
problems: []
missing: []
members: [视频生成/图生视频/1927430164823564289.json, 视频生成/图生视频/1922720148057198593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_893

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1927430164823564289.json、视频生成/图生视频/1922720148057198593.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/2 个有
- `LoadWanVideoClipTextEncoder` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoControlEmbeds` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoPhantomEmbeds` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
