---
name: unknown_workflow_video_sampler_vae_65
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9405
common_nodes: [INTConstant, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/CausVid-3步720P参考编辑(Wan2.1&MoviiGen&Skyreels)_1923420902107566082.json, 平台全量/CausVid-3步720P控制+参考(Wan2.1&MoviiGen&Skyreels)_1923413100647600129.json, 平台全量/WAN-VACE（视频的参考编辑）_1909088194090905601.json, 平台全量/Wan14BT2VFusioniX-VACE-七组实践_1932278596193124353.json, 视频生成/图生视频/CausVid-3步720P单图参考(Wan2.1&MoviiGen&Skyreels)_1923407399171125249.json, 视频生成/图生视频/CausVid-3步720P多图参考(Wan2.1&MoviiGen&Skyreels)_1923698037238263809.json, 视频生成/文生视频/Self Forcing-VACE-七组实践_1933086733389139969.json, 视频生成/文生视频/lightx2v-V2-VACE-七组实践_1945819044681576449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_65

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/CausVid-3步720P参考编辑(Wan2.1&MoviiGen&Skyreels)_1923420902107566082.json、平台全量/CausVid-3步720P控制+参考(Wan2.1&MoviiGen&Skyreels)_1923413100647600129.json、平台全量/WAN-VACE（视频的参考编辑）_1909088194090905601.json、平台全量/Wan14BT2VFusioniX-VACE-七组实践_1932278596193124353.json、视频生成/图生视频/CausVid-3步720P单图参考(Wan2.1&MoviiGen&Skyreels)_1923407399171125249.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `INTConstant`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: LoadFlorence2Model` —— 7/8 个有
- `LayerMask: ObjectDetectorFL2` —— 7/8 个有
- `LayerMask: SAM2Ultra` —— 7/8 个有
- `RH_Captioner` —— 7/8 个有
- `WanVideoSLG` —— 7/8 个有
- `WanVideoTeaCache` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `String Literal` —— 6/8 个有
- `VHS_LoadVideo` —— 6/8 个有
- `WanVideoVACEModelSelect` —— 6/8 个有
- `GetImageSize` —— 5/8 个有
- `GrowMaskWithBlur` —— 5/8 个有
- `Image Blank` —— 5/8 个有
- `ImageCompositeMasked` —— 5/8 个有
- `InpaintPreprocessor` —— 5/8 个有
- `WanVideoLoraSelect` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `AIO_Preprocessor` —— 4/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `ImageConcanate` —— 4/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `LayerUtility: PurgeVRAM V2` —— 4/8 个有
- `easy ifElse` —— 4/8 个有
- `GetImageSize+` —— 3/8 个有
- `ImagePadKJ` —— 3/8 个有
- `MaskToImage` —— 3/8 个有
- `WanVideoVACEStartToEndFrame` —— 3/8 个有
- `GetNode` —— 1/8 个有
- `WanVideoFreeInitArgs` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
