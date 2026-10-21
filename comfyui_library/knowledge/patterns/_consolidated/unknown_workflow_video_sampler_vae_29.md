---
name: unknown_workflow_video_sampler_vae_29
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.91275
common_nodes: [GetImageSize, INTConstant, Image Blank, ImageCompositeMasked, ImageResizeKJ, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [Image Blank, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, String Literal, GetImageSize+]
members: [视频生成/图生视频/1923407399171125249.json, 视频生成/图生视频/1923698037238263809.json, 视频生成/图生视频/1909082788321239041.json, 视频生成/图生视频/1909078127585468418.json, 视频生成/图生视频/1933797677106946049.json, 视频生成/图生视频/1923226071490359297.json, 视频生成/图生视频/1923186184321683457.json, 视频生成/图生视频/1927603788339634178.json, 视频生成/文生视频/1933086733389139969.json, 视频生成/文生视频/1945819044681576449.json, 视频生成/文生视频/Self Forcing-VACE-七组实践_2072999742382317568.json, 视频生成/文生视频/lightx2v-V2-VACE-七组实践_2072999693577396224.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_29

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1923407399171125249.json、视频生成/图生视频/1923698037238263809.json、视频生成/图生视频/1909082788321239041.json、视频生成/图生视频/1909078127585468418.json、视频生成/图生视频/1933797677106946049.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
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
- `WanVideoTorchCompileSettings` —— 11/12 个有
- `String Literal` —— 10/12 个有
- `WanVideoSLG` —— 10/12 个有
- `WanVideoTeaCache` —— 10/12 个有
- `WanVideoVACEEncode` —— 10/12 个有
- `ImageConcanate` —— 7/12 个有
- `ImagePadKJ` —— 6/12 个有
- `LayerUtility: PurgeVRAM` —— 6/12 个有
- `LayerUtility: PurgeVRAM V2` —— 6/12 个有
- `RH_Captioner` —— 6/12 个有
- `WanVideoVACEModelSelect` —— 6/12 个有
- `easy ifElse` —— 6/12 个有
- `easy showAnything` —— 6/12 个有
- `AIO_Preprocessor` —— 4/12 个有
- `GetImageSize+` —— 4/12 个有
- `GetImageSizeAndCount` —— 4/12 个有
- `GrowMaskWithBlur` —— 4/12 个有
- `InpaintPreprocessor` —— 4/12 个有
- `MaskToImage` —— 4/12 个有
- `VHS_LoadVideo` —— 4/12 个有
- `WanVideoLoraSelect` —— 4/12 个有
- `WanVideoVACEStartToEndFrame` —— 4/12 个有
- `KepStringLiteral` —— 2/12 个有
- `WanVideoEncode` —— 2/12 个有
- `WanVideoFreeInitArgs` —— 2/12 个有
- `WanVideoPhantomEmbeds` —— 2/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Image Blank、LayerMask: LoadFlorence2Model、LayerMask: ObjectDetectorFL2、LayerMask: SAM2Ultra、LayerUtility: PurgeVRAM
