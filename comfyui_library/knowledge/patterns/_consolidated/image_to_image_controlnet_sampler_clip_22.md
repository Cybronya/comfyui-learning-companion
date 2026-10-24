---
name: image_to_image_controlnet_sampler_clip_22
type: Image To Image
frequency: 2
level: weak
coverage: 0.7665
common_nodes: [Automatic CFG, BOPBTL_LoadRestoreOldPhotosModel, BOPBTL_LoadScratchMaskModel, BOPBTL_RestoreOldPhotos, BOPBTL_ScratchMask, CLIPTextEncode, CR Apply Multi-ControlNet, CR Multi-ControlNet Stack, CheckpointLoaderSimple, ComfyUI_Image_Round__ImageCropAdvanced, ComfyUI_Image_Round__ImageRoundAdvanced, ConstrainImage|pysssss, ControlNetApply, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, DepthAnythingV2Preprocessor, DisplayText_Zho, DownloadAndLoadFlorence2Model, FaceRestoreCFWithModel, FaceRestoreModelLoader, Florence2Run, GetNode, Image Comparer (rgthree), ImageGenResolutionFromImage, ImageResizeKJ, ImageScale, ImageScaleToMegapixels, ImageToMask, KSampler, LineArtPreprocessor, LoadImage, MaskToImage, PreviewImage, ReActorFaceSwap, SaveImage, SetNode, VAEDecode, VAEEncode, Zoe-DepthMapPreprocessor, easy cleanGpuUsed, workflow>Overlay]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/旧照片修复上色_1915821202013618177.json, 视频生成/图生视频/老照片修复去划痕上色复活版V3_1882724771069677569.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/旧照片修复上色_1915821202013618177.json、视频生成/图生视频/老照片修复去划痕上色复活版V3_1882724771069677569.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `Automatic CFG`
- `BOPBTL_LoadRestoreOldPhotosModel`
- `BOPBTL_LoadScratchMaskModel`
- `BOPBTL_RestoreOldPhotos`
- `BOPBTL_ScratchMask`
- `CLIPTextEncode`
- `CR Apply Multi-ControlNet`
- `CR Multi-ControlNet Stack`
- `CheckpointLoaderSimple`
- `ComfyUI_Image_Round__ImageCropAdvanced`
- `ComfyUI_Image_Round__ImageRoundAdvanced`
- `ConstrainImage|pysssss`
- `ControlNetApply`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `DisplayText_Zho`
- `DownloadAndLoadFlorence2Model`
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `Florence2Run`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageGenResolutionFromImage`
- `ImageResizeKJ`
- `ImageScale`
- `ImageScaleToMegapixels`
- `ImageToMask`
- `KSampler`
- `LineArtPreprocessor`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `ReActorFaceSwap`
- `SaveImage`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `Zoe-DepthMapPreprocessor`
- `easy cleanGpuUsed`
- `workflow>Overlay`

**可变部分**（部分 workflow 才有）：
- `CreateShapeMask` —— 1/2 个有
- `DownloadAndLoadLivePortraitModels` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `LivePortraitComposite` —— 1/2 个有
- `LivePortraitCropper` —— 1/2 个有
- `LivePortraitLoadCropper` —— 1/2 个有
- `LivePortraitLoadMediaPipeCropper` —— 1/2 个有
- `LivePortraitProcess` —— 1/2 个有
- `LivePortraitRetargeting` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.1 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
