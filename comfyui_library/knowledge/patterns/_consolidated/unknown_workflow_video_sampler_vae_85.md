---
name: unknown_workflow_video_sampler_vae_85
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.768833
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Fun-V1.1-InP首尾帧(Wan2.1)_1905144833516965890.json, 视频生成/图生视频/WAN2.1 首尾帧 生成视频_1919985178293239809.json, 视频生成/图生视频/Wan2.1-KJ首尾帧图生视频_1911321308582608897.json, 视频生成/图生视频/Wan2.1官方首尾帧FLF2V14b_1918282117372121090.json, 视频生成/图生视频/【Wan2.1系列】FLF2V首尾帧生成视频工作流_1920112646744641537.json, 视频生成/图生视频/【Wan2.1系列】首尾帧生成视频之Fun V1.1 Inp模型 _ 一键生成创意视频！_1920718476594315266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_85

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Fun-V1.1-InP首尾帧(Wan2.1)_1905144833516965890.json、视频生成/图生视频/WAN2.1 首尾帧 生成视频_1919985178293239809.json、视频生成/图生视频/Wan2.1-KJ首尾帧图生视频_1911321308582608897.json、视频生成/图生视频/Wan2.1官方首尾帧FLF2V14b_1918282117372121090.json、视频生成/图生视频/【Wan2.1系列】FLF2V首尾帧生成视频工作流_1920112646744641537.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `WanVideoExperimentalArgs` —— 5/6 个有
- `ImageResize+` —— 4/6 个有
- `LoadWanVideoClipTextEncoder` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `CLIPVisionLoader` —— 2/6 个有
- `ImageResizeKJ` —— 2/6 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `GIMMVFI_interpolate` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `WanVideoVRAMManagement` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
