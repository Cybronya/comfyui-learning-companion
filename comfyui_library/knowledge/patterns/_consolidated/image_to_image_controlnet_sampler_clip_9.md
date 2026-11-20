---
name: image_to_image_controlnet_sampler_clip_9
type: Image To Image
frequency: 5
level: weak
coverage: 0.7706
common_nodes: [Automatic CFG, BOPBTL_LoadRestoreOldPhotosModel, BOPBTL_LoadScratchMaskModel, BOPBTL_RestoreOldPhotos, BOPBTL_ScratchMask, CLIPTextEncode, CheckpointLoaderSimple, ComfyUI_Image_Round__ImageCropAdvanced, ComfyUI_Image_Round__ImageRoundAdvanced, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, DepthAnythingV2Preprocessor, DisplayText_Zho, DownloadAndLoadFlorence2Model, Florence2Run, ImageScaleToMegapixels, KSampler, LoadImage, PreviewImage, ReActorFaceSwap, SaveImage, VAEDecode, VAEEncode, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/旧照片修复上色_1915821202013618177.json, 平台全量/新版-老照片高清修复上色工作流_1894984830163746817.json, 平台全量/老照片修复 Old Photo Restoration XL_1844779688131727362.json, 平台全量/自用老照片修复上色——人物老照片修复_1913694811394666497.json, 视频生成/图生视频/老照片修复去划痕上色复活版V3_1882724771069677569.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/旧照片修复上色_1915821202013618177.json、平台全量/新版-老照片高清修复上色工作流_1894984830163746817.json、平台全量/老照片修复 Old Photo Restoration XL_1844779688131727362.json、平台全量/自用老照片修复上色——人物老照片修复_1913694811394666497.json、视频生成/图生视频/老照片修复去划痕上色复活版V3_1882724771069677569.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `Automatic CFG`
- `BOPBTL_LoadRestoreOldPhotosModel`
- `BOPBTL_LoadScratchMaskModel`
- `BOPBTL_RestoreOldPhotos`
- `BOPBTL_ScratchMask`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyUI_Image_Round__ImageCropAdvanced`
- `ComfyUI_Image_Round__ImageRoundAdvanced`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `DisplayText_Zho`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `ImageScaleToMegapixels`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReActorFaceSwap`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Apply Multi-ControlNet` —— 4/5 个有
- `CR Multi-ControlNet Stack` —— 4/5 个有
- `ConstrainImage|pysssss` —— 4/5 个有
- `ControlNetApply` —— 4/5 个有
- `FaceRestoreCFWithModel` —— 4/5 个有
- `FaceRestoreModelLoader` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageGenResolutionFromImage` —— 4/5 个有
- `ImageResizeKJ` —— 4/5 个有
- `ImageScale` —— 4/5 个有
- `ImageToMask` —— 4/5 个有
- `LineArtPreprocessor` —— 4/5 个有
- `MaskToImage` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `Zoe-DepthMapPreprocessor` —— 4/5 个有
- `workflow>Overlay` —— 4/5 个有
- `CreateShapeMask` —— 2/5 个有
- `DownloadAndLoadLivePortraitModels` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `GrowMaskWithBlur` —— 2/5 个有
- `LivePortraitComposite` —— 2/5 个有
- `LivePortraitCropper` —— 2/5 个有
- `LivePortraitLoadCropper` —— 2/5 个有
- `LivePortraitLoadMediaPipeCropper` —— 2/5 个有
- `LivePortraitProcess` —— 2/5 个有
- `LivePortraitRetargeting` —— 2/5 个有
- `MaskPreview+` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `workflow/Overlay` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 6 - 30 | 5 | 62% |
| Prompt 约束强度(CFG) | 7 | 2 - 7 | 5 | 67% |
| 采样算法 | dpmpp_2m | - | 5 | 80% |
| 调度器 | karras | - | 5 | 100% |
| 重绘幅度 | 0.1 | 0.1 - 0.8 | 5 | 0% |
| ControlNet 权重 | 1 | 0.4 - 1 | 5 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 6 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 2 - 7，5 个样本
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 80%
- 调度器 最常用 karras，5 个样本，一致性 100%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 0.8，5 个样本，取值分散，一致性仅 0%
- ControlNet 权重 中位数 1，观测区间 0.4 - 1，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
