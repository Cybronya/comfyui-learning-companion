---
name: unknown_workflow_video_upscale_lora_13
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96475
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageUpscaleWithModel, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, PreviewImage, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/万相图生视频国风变装-戏服_1915350081669894146.json, 视频生成/图生视频/图生视频_大摆锤舞蹈_1952209693416566785.json, 视频生成/图生视频/图生视频_大摆锤舞蹈_1955172596662898690.json, 视频生成/文生视频/图生视频_大摆锤舞蹈_1965243729651093506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_13

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/万相图生视频国风变装-戏服_1915350081669894146.json、视频生成/图生视频/图生视频_大摆锤舞蹈_1952209693416566785.json、视频生成/图生视频/图生视频_大摆锤舞蹈_1955172596662898690.json、视频生成/文生视频/图生视频_大摆锤舞蹈_1965243729651093506.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `CLIPVisionLoader` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `ImageSmartSharpen+` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `WanVideoExperimentalArgs` —— 1/4 个有
- `WanVideoSLG` —— 1/4 个有
- `WanVideoVRAMManagement` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
