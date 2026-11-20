---
name: image_to_image_controlnet_lora_sampler_3
type: Image To Image
frequency: 12
level: strong
coverage: 0.923167
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX真人照片转二次元【升级版更像本人】_1902541568551858178.json, 图片生成/图生图/flux万物转3d_1912796444883939329.json, 图片生成/图生图/flux优化动漫转真人_1932578311178743810.json, 图片生成/图生图/【动漫转真人】Flux+CN线稿+深度动漫转真人模特+修脸_1915997617510354945.json, 图片生成/图生图/万物转 3D 卡通 Flux 模型_1912873534123667457.json, 图片生成/图生图/动漫转真人工作流_1926867070372450305.json, 图片生成/文生图/flux万物转吉卜力_1912153719977508866.json, 平台全量/Flux动漫转真人_1933607759705198593.json, 平台全量/flux万物转像素风_1918749097765830658.json, 平台全量/flux真人转动漫_1911706295106502658.json, 平台全量/万物转国风工笔画_1909908422291091457.json, 平台全量/照片转水墨画_1909309956460584961.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/FLUX真人照片转二次元【升级版更像本人】_1902541568551858178.json、图片生成/图生图/flux万物转3d_1912796444883939329.json、图片生成/图生图/flux优化动漫转真人_1932578311178743810.json、图片生成/图生图/【动漫转真人】Flux+CN线稿+深度动漫转真人模特+修脸_1915997617510354945.json、图片生成/图生图/万物转 3D 卡通 Flux 模型_1912873534123667457.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingPreprocessor` —— 11/12 个有
- `FaceDetailer` —— 11/12 个有
- `Get Image Size` —— 11/12 个有
- `ModelSamplingFlux` —— 11/12 个有
- `ReduxAdvanced` —— 11/12 个有
- `SAMLoader` —— 11/12 个有
- `SeedSelector` —— 11/12 个有
- `UltralyticsDetectorProvider` —— 11/12 个有
- `easy imageColorMatch` —— 11/12 个有
- `OpenposePreprocessor` —— 9/12 个有
- `ApplyPulidFlux` —— 7/12 个有
- `ImageScaleToMegapixels` —— 7/12 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 7/12 个有
- `PulidEvaClipLoader` —— 7/12 个有
- `PulidFluxInsightFaceLoader` —— 7/12 个有
- `PulidFluxModelLoader` —— 7/12 个有
- `UpscaleModelLoader` —— 7/12 个有
- `easy cleanGpuUsed` —— 5/12 个有
- `ImageScaleToTotalPixels` —— 4/12 个有
- `TilePreprocessor` —— 4/12 个有
- `AIO_Preprocessor` —— 1/12 个有
- `CLIPVisionEncode` —— 1/12 个有
- `ConditioningConcat` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `LineartStandardPreprocessor` —— 1/12 个有
- `StyleModelApply` —— 1/12 个有
- `WD14Tagger|pysssss` —— 1/12 个有
- `easy clearCacheAll` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.3 - 0.6 | 12 | 78% |
| 采样步数 | 20 | 20 - 30 | 12 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 0.925 | 0.8 - 1 | 12 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.3 - 0.6，12 个样本
- 采样步数 中位数 20，观测区间 20 - 30，12 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 0.925，观测区间 0.8 - 1，12 个样本，取值集中（一致性 93%）
