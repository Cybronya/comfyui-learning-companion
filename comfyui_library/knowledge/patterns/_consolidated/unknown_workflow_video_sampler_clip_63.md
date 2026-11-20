---
name: unknown_workflow_video_sampler_clip_63
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9501
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1-i2v-360度旋转_1899839551614115842.json, 视频生成/图生视频/wan2.1-i2v-图生视频_1862829335932547073.json, 视频生成/图生视频/wan2.1-i2v-飞天特效_1899833123503222786.json, 视频生成/图生视频/wan2.1_1936400345864245250.json, 视频生成/图生视频/万相图生视频国风变装-戏服_1915350081669894146.json, 视频生成/图生视频/图生视频_大摆锤舞蹈_1952209693416566785.json, 视频生成/图生视频/图生视频_大摆锤舞蹈_1955172596662898690.json, 视频生成/图生视频/拉近眼睛镜头万相图生视48工作流_1938430134720593922.json, 视频生成/图生视频/缩小到地球万相图生视50工作流_1938457014647324673.json, 视频生成/图生视频/跳踢倒50_1940619360874508289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/wan2.1-i2v-360度旋转_1899839551614115842.json、视频生成/图生视频/wan2.1-i2v-图生视频_1862829335932547073.json、视频生成/图生视频/wan2.1-i2v-飞天特效_1899833123503222786.json、视频生成/图生视频/wan2.1_1936400345864245250.json、视频生成/图生视频/万相图生视频国风变装-戏服_1915350081669894146.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 9/10 个有
- `UpscaleModelLoader` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `ImageUpscaleWithModel` —— 6/10 个有
- `easy cleanGpuUsed` —— 6/10 个有
- `ImageSmartSharpen+` —— 5/10 个有
- `LayerUtility: PurgeVRAM` —— 5/10 个有
- `WanVideoExperimentalArgs` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `ImageScaleToMegapixels` —— 4/10 个有
- `PreviewImage` —— 3/10 个有
- `ImageResize+` —— 2/10 个有
- `Upscale Model Loader` —— 2/10 个有
- `CLIPVisionLoader` —— 1/10 个有
- `ImageResizeKJ` —— 1/10 个有
- `ImageScale` —— 1/10 个有
- `KEEP_ModelLoader` —— 1/10 个有
- `KEEP_ProcessImageSequence` —— 1/10 个有
- `PrimitiveBoolean` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `VHS_VideoInfo` —— 1/10 个有
- `WanVideoSLG` —— 1/10 个有
- `WanVideoVRAMManagement` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
