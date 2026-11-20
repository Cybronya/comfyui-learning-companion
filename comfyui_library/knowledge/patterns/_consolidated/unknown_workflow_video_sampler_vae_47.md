---
name: unknown_workflow_video_sampler_vae_47
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7651
common_nodes: [DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, ImageConcatMulti, ImageFromBatch+, ImageMirror, ImageRepeat, ImageResizeKJ, ImpactSwitch, JWInteger, LoadWanVideoT5TextEncoder, PreviewImage, VHS_LoadVideo, VHS_MergeImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/FusionX视频转绘_1934419083666354178.json, 平台全量/Lightx2v vace深度_姿势控制稳定双倍加速版视频转绘V1(脸部稳定)_1945809168936869889.json, 平台全量/Vace 14B超强双控双参考加速模式视频转绘V1_1924708002820255745.json, 平台全量/Vace14B ACC加速吉卜力风格转换视频转绘V1_1927644879114125313.json, 平台全量/姿势模仿视频-加速版FusionX稳定视频转绘_1934510153603436545.json, 视频生成/图生视频/FusionX controlnet控制稳定双倍加速版视频转绘_1933785528938450945.json, 视频生成/图生视频/FusionX+VACE深度_姿势控制稳定双倍加速版视频转绘V1_1933557560941395970.json, 视频生成/图生视频/VACE 1.3B正式版双重引导姿势_深度稳定加速版V1_1924678755254456322.json, 视频生成/图生视频/VACE 14B图像参考双重引导姿势及深度控制视频生视频V2_1922710757258006529.json, 视频生成/图生视频/VACE图像参考双重引导姿势及深度控制视频生视频V1_1907443729060532226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_47

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/FusionX视频转绘_1934419083666354178.json、平台全量/Lightx2v vace深度_姿势控制稳定双倍加速版视频转绘V1(脸部稳定)_1945809168936869889.json、平台全量/Vace 14B超强双控双参考加速模式视频转绘V1_1924708002820255745.json、平台全量/Vace14B ACC加速吉卜力风格转换视频转绘V1_1927644879114125313.json、平台全量/姿势模仿视频-加速版FusionX稳定视频转绘_1934510153603436545.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 10 个 workflow 都包含：
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageMirror`
- `ImageRepeat`
- `ImageResizeKJ`
- `ImpactSwitch`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_MergeImages`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `OpenposePreprocessor` —— 9/10 个有
- `WanVideoEnhanceAVideo` —— 9/10 个有
- `WanVideoExperimentalArgs` —— 9/10 个有
- `WanVideoSLG` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `Note Plus (mtb)` —— 8/10 个有
- `CR Prompt Text` —— 6/10 个有
- `WanVideoTeaCache` —— 6/10 个有
- `WanVideoVACEModelSelect` —— 5/10 个有
- `WanVideoLoraSelect` —— 4/10 个有
- `Blend` —— 3/10 个有
- `Note _O` —— 2/10 个有
- `DWPreprocessor` —— 1/10 个有
- `EasyControlGenerate` —— 1/10 个有
- `EasyControlLoadFlux` —— 1/10 个有
- `EasyControlLoadLora` —— 1/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `ImageBlend` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `PDIMAGE_LongerSize` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
