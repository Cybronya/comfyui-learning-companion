---
name: unknown_workflow_video_lora_sampler_917
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.972
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/ani全能视频S + lightx2v基础工作流_1946201158950248449.json, 视频生成/图生视频/ani全能视频S-图生视频-wan_1945006395668484098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_917

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/ani全能视频S + lightx2v基础工作流_1946201158950248449.json、视频生成/图生视频/ani全能视频S-图生视频-wan_1945006395668484098.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy imageScaleDownToSize` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
