---
name: unknown_workflow_video_sampler_vae_60
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.910625
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImageResize+, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1924712621050613761.json, 视频生成/图生视频/1912568927808094209.json, 视频生成/图生视频/1918282117372121090.json, 视频生成/图生视频/1914979935533105154.json, 视频生成/图生视频/1920112646744641537.json, 视频生成/图生视频/1920718476594315266.json, 视频生成/图生视频/1913886030926180353.json, 视频生成/图生视频/1905171860894437377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_60

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1924712621050613761.json、视频生成/图生视频/1912568927808094209.json、视频生成/图生视频/1918282117372121090.json、视频生成/图生视频/1914979935533105154.json、视频生成/图生视频/1920112646744641537.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResize+`
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
- `LoadWanVideoClipTextEncoder` —— 6/8 个有
- `WanVideoExperimentalArgs` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `WanVideoEnhanceAVideo` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `WanVideoVRAMManagement` —— 4/8 个有
- `CLIPVisionLoader` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `Note Plus (mtb)` —— 3/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/8 个有
- `GIMMVFI_interpolate` —— 1/8 个有
- `ImageFromBatch+` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `Upscale Model Loader` —— 1/8 个有
- `WanVideoVACEModelSelect` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
