---
name: image_to_image_controlnet_face_detailer_lora
type: Image To Image
frequency: 7
level: strong
coverage: 0.922857
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FaceDetailer, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SAMLoader, SaveImage, StyleModelLoader, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX真人照片转二次元【升级版更像本人】_1902541568551858178.json, 图片生成/图生图/flux万物转3d_1912796444883939329.json, 图片生成/图生图/flux优化动漫转真人_1932578311178743810.json, 图片生成/图生图/【动漫转真人】Flux+CN线稿+深度动漫转真人模特+修脸_1915997617510354945.json, 图片生成/图生图/万物转 3D 卡通 Flux 模型_1912873534123667457.json, 图片生成/图生图/动漫转真人工作流_1926867070372450305.json, 图片生成/文生图/flux万物转吉卜力_1912153719977508866.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_face_detailer_lora

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX真人照片转二次元【升级版更像本人】_1902541568551858178.json、图片生成/图生图/flux万物转3d_1912796444883939329.json、图片生成/图生图/flux优化动漫转真人_1932578311178743810.json、图片生成/图生图/【动漫转真人】Flux+CN线稿+深度动漫转真人模特+修脸_1915997617510354945.json、图片生成/图生图/万物转 3D 卡通 Flux 模型_1912873534123667457.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FaceDetailer`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingPreprocessor` —— 6/7 个有
- `Get Image Size` —— 6/7 个有
- `ModelSamplingFlux` —— 6/7 个有
- `OpenposePreprocessor` —— 6/7 个有
- `ReduxAdvanced` —— 6/7 个有
- `SeedSelector` —— 6/7 个有
- `easy imageColorMatch` —— 6/7 个有
- `ApplyPulidFlux` —— 4/7 个有
- `PulidEvaClipLoader` —— 4/7 个有
- `PulidFluxInsightFaceLoader` —— 4/7 个有
- `PulidFluxModelLoader` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `ImageScaleToMegapixels` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 3/7 个有
- `TilePreprocessor` —— 3/7 个有
- `UpscaleModelLoader` —— 3/7 个有
- `AIO_Preprocessor` —— 1/7 个有
- `CLIPVisionEncode` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `StyleModelApply` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.4 - 0.6 | 7 | 83% |
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 0.9 | 0.8 - 1 | 7 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.4 - 0.6，7 个样本，取值集中（一致性 83%）
- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 0.9，观测区间 0.8 - 1，7 个样本，取值集中（一致性 93%）
