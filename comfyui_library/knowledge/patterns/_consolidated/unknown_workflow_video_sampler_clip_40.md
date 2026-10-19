---
name: unknown_workflow_video_sampler_clip_40
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.964417
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1899839551614115842.json, 视频生成/图生视频/1862829335932547073.json, 视频生成/图生视频/1899833123503222786.json, 视频生成/图生视频/1936400345864245250.json, 视频生成/图生视频/2012905954114805761.json, 视频生成/图生视频/万相-图像360度旋转工作流_1907252963578896386.json, 视频生成/图生视频/2053025337801494530.json, 视频生成/图生视频/2053031421186457601.json, 视频生成/图生视频/1915350081669894146.json, 视频生成/图生视频/1938430134720593922.json, 视频生成/图生视频/1938457014647324673.json, 视频生成/图生视频/1940619360874508289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1899839551614115842.json、视频生成/图生视频/1862829335932547073.json、视频生成/图生视频/1899833123503222786.json、视频生成/图生视频/1936400345864245250.json、视频生成/图生视频/2012905954114805761.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 11/12 个有
- `WanVideoExperimentalArgs` —— 9/12 个有
- `DownloadAndLoadGIMMVFIModel` —— 8/12 个有
- `GIMMVFI_interpolate` —— 8/12 个有
- `ImageUpscaleWithModel` —— 8/12 个有
- `WanVideoEnhanceAVideo` —— 8/12 个有
- `easy cleanGpuUsed` —— 8/12 个有
- `Upscale Model Loader` —— 6/12 个有
- `UpscaleModelLoader` —— 6/12 个有
- `ImageResizeKJ` —— 5/12 个有
- `ImageSmartSharpen+` —— 5/12 个有
- `LayerUtility: PurgeVRAM` —— 5/12 个有
- `WanVideoSLG` —— 5/12 个有
- `WanVideoTorchCompileSettings` —— 5/12 个有
- `FILM VFI` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 4/12 个有
- `ImageScaleToMegapixels` —— 4/12 个有
- `TextInput_` —— 4/12 个有
- `CLIPVisionLoader` —— 1/12 个有
- `ImageScale` —— 1/12 个有
- `KEEP_ModelLoader` —— 1/12 个有
- `KEEP_ProcessImageSequence` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `PrimitiveBoolean` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有
- `VHS_VideoInfo` —— 1/12 个有
- `WanVideoVRAMManagement` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
