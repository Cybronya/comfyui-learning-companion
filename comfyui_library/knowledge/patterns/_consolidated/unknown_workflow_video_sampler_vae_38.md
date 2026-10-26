---
name: unknown_workflow_video_sampler_vae_38
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9264
common_nodes: [GetImageSize, INTConstant, Image Blank, ImageCompositeMasked, ImageResizeKJ, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/CausVid-3步720P单图参考(Wan2.1&MoviiGen&Skyreels)_1923407399171125249.json, 视频生成/图生视频/CausVid-3步720P多图参考(Wan2.1&MoviiGen&Skyreels)_1923698037238263809.json, 视频生成/图生视频/WAN-VACE(双图参考)_1909082788321239041.json, 视频生成/图生视频/WAN-VACE(图像参考)_1909078127585468418.json, 视频生成/图生视频/fusionxPhantom两图融合_1933797677106946049.json, 视频生成/图生视频/单图参考(Wan2.1-VACE-14B)_1923226071490359297.json, 视频生成/图生视频/多图参考(Wan2.1-VACE-14B)_1923186184321683457.json, 视频生成/图生视频/多图融合-Phantom-Wan-14B_1927603788339634178.json, 视频生成/文生视频/Self Forcing-VACE-七组实践_1933086733389139969.json, 视频生成/文生视频/lightx2v-V2-VACE-七组实践_1945819044681576449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_38

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/CausVid-3步720P单图参考(Wan2.1&MoviiGen&Skyreels)_1923407399171125249.json、视频生成/图生视频/CausVid-3步720P多图参考(Wan2.1&MoviiGen&Skyreels)_1923698037238263809.json、视频生成/图生视频/WAN-VACE(双图参考)_1909082788321239041.json、视频生成/图生视频/WAN-VACE(图像参考)_1909078127585468418.json、视频生成/图生视频/fusionxPhantom两图融合_1933797677106946049.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `GetImageSize`
- `INTConstant`
- `Image Blank`
- `ImageCompositeMasked`
- `ImageResizeKJ`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `String Literal` —— 8/10 个有
- `WanVideoSLG` —— 8/10 个有
- `WanVideoTeaCache` —— 8/10 个有
- `WanVideoVACEEncode` —— 8/10 个有
- `ImageConcanate` —— 5/10 个有
- `WanVideoVACEModelSelect` —— 5/10 个有
- `ImagePadKJ` —— 4/10 个有
- `LayerUtility: PurgeVRAM` —— 4/10 个有
- `LayerUtility: PurgeVRAM V2` —— 4/10 个有
- `RH_Captioner` —— 4/10 个有
- `easy ifElse` —— 4/10 个有
- `easy showAnything` —— 4/10 个有
- `WanVideoLoraSelect` —— 3/10 个有
- `AIO_Preprocessor` —— 2/10 个有
- `GetImageSize+` —— 2/10 个有
- `GetImageSizeAndCount` —— 2/10 个有
- `GrowMaskWithBlur` —— 2/10 个有
- `InpaintPreprocessor` —— 2/10 个有
- `KepStringLiteral` —— 2/10 个有
- `MaskToImage` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `WanVideoEncode` —— 2/10 个有
- `WanVideoPhantomEmbeds` —— 2/10 个有
- `WanVideoVACEStartToEndFrame` —— 2/10 个有
- `WanVideoFreeInitArgs` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
