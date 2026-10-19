---
name: unknown_workflow_video_sampler_vae_23
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.907
common_nodes: [GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2019998989524934657.json, 视频生成/图生视频/1950137059535183873.json, 视频生成/图生视频/1951966233606434817.json, 视频生成/图生视频/1979786128704311297.json, 视频生成/图生视频/1981252954491617282.json, 视频生成/图生视频/1979812385382895618.json, 视频生成/图生视频/1979805991325831170.json, 视频生成/图生视频/1974477475709366273.json, 视频生成/图生视频/1975403680918843394.json, 视频生成/图生视频/1976126127594975233.json, 视频生成/图生视频/1974460906073665538.json, 视频生成/图生视频/1953401583553925122.json, 视频生成/图生视频/1982464473032212482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2019998989524934657.json、视频生成/图生视频/1950137059535183873.json、视频生成/图生视频/1951966233606434817.json、视频生成/图生视频/1979786128704311297.json、视频生成/图生视频/1981252954491617282.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `WanVideoSetLoRAs` —— 12/13 个有
- `WanVideoTorchCompileSettings` —— 12/13 个有
- `PrimitiveInt` —— 10/13 个有
- `CR Text` —— 9/13 个有
- `SimpleMath+` —— 9/13 个有
- `WanVideoLoraSelect` —— 8/13 个有
- `CLIPVisionLoader` —— 6/13 个有
- `ShowText|pysssss` —— 6/13 个有
- `WanVideoClipVisionEncode` —— 6/13 个有
- `AILab_MiniCPM_4_V_Advanced` —— 5/13 个有
- `ImageBatchMultiple+` —— 5/13 个有
- `WanVideoContextOptions` —— 4/13 个有
- `WanVideoEncodeLatentBatch` —— 4/13 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/13 个有
- `GIMMVFI_interpolate` —— 3/13 个有
- `ImageFromBatch+` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `VHS_LoadVideo` —— 2/13 个有
- `VHS_VideoInfo` —— 2/13 个有
- `AILab_QwenVL` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `RH_Nano_Banana_Image2Image` —— 1/13 个有
- `SaveImage` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
