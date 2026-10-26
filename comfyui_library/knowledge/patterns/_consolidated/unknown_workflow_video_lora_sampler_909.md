---
name: unknown_workflow_video_lora_sampler_909
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9445
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageSizeAndCount, INTConstant, ImageMaskScaleAs_UTK, ImageScaleByAspectRatio_UTK, LoadImage, LoadWanVideoT5TextEncoder, PurgeVRAM_UTK, QwenLoader, ShowText|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoPromptExtender, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan22_图生视频及首尾帧_终极版_1952800839192743937.json, 视频生成/图生视频/wan2.2_图生视频及首尾帧_终极版【gen全能视频Si】_1960937886998827010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_909

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan22_图生视频及首尾帧_终极版_1952800839192743937.json、视频生成/图生视频/wan2.2_图生视频及首尾帧_终极版【gen全能视频Si】_1960937886998827010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageMaskScaleAs_UTK`
- `ImageScaleByAspectRatio_UTK`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PurgeVRAM_UTK`
- `QwenLoader`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoPromptExtender`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
