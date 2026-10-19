---
name: unknown_workflow_video_lora_sampler_330
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.874714
common_nodes: [Bjornulf_ShowJson, DWPreprocessor, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/1957679362386620417.json, 视频生成/图生视频/1953648697265586178.json, 视频生成/图生视频/1961001361997500417.json, 视频生成/图生视频/1963854925186961409.json, 视频生成/图生视频/1960782180505071617.json, 视频生成/文生视频/WAN_VACE_14B + CAUSVID + 视频姿态控制 【跳舞视频流程】- 视频课程配套_1931599157772136450.json, 视频生成/文生视频/1955515292903358465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_330

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1957679362386620417.json、视频生成/图生视频/1953648697265586178.json、视频生成/图生视频/1961001361997500417.json、视频生成/图生视频/1963854925186961409.json、视频生成/图生视频/1960782180505071617.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `Bjornulf_ShowJson`
- `DWPreprocessor`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `Display Int (rgthree)` —— 5/7 个有
- `EmptyImage` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `ImageScaleToMegapixels` —— 5/7 个有
- `MaskToImage` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `UpscaleModelLoader` —— 5/7 个有
- `VHS_SplitImages` —— 5/7 个有
- `WanVideoTeaCache` —— 5/7 个有
- `Int` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `WanVideoEasyCache` —— 2/7 个有
- `WanVideoEnhanceAVideo` —— 2/7 个有
- `AILab_MiniCPM_4_V` —— 1/7 个有
- `ImagePadKJ` —— 1/7 个有
- `WanVideoSetRadialAttention` —— 1/7 个有
- `WanVideoTorchCompileSettings` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
