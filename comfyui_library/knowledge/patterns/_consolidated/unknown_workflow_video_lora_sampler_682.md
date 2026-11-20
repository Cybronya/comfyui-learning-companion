---
name: unknown_workflow_video_lora_sampler_682
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85575
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, GetImageSize, GrowMaskWithBlur, ImageCompositeMasked, ImageConcanate, ImageFromBatch+, ImageMirror, ImpactSwitch, InvertMask, JWInteger, KSamplerAdvanced, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2VideoUltra, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingSD3, PDIMAGE_LongerSize, PathchSageAttentionKJ, PreviewImage, RebatchImages, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo]
problems: []
missing: []
members: [平台全量/Wan2.2 Vace主体替换视频生视频加速版V1_1950024468905287681.json, 平台全量/🦖Wan2.2 Vace视频换主体_1957619452634394626.json, 视频生成/图生视频/Wan2.2 Vace主体替换视频生视频加速版V1_1957475437662367746.json, 视频生成/图生视频/wan2.2图片跳舞视频转绘视频主体替换（Vace+自动提示词）_1958077284689334273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_682

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Wan2.2 Vace主体替换视频生视频加速版V1_1950024468905287681.json、平台全量/🦖Wan2.2 Vace视频换主体_1957619452634394626.json、视频生成/图生视频/Wan2.2 Vace主体替换视频生视频加速版V1_1957475437662367746.json、视频生成/图生视频/wan2.2图片跳舞视频转绘视频主体替换（Vace+自动提示词）_1958077284689334273.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `GetImageSize`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageMirror`
- `ImpactSwitch`
- `InvertMask`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2VideoUltra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingSD3`
- `PDIMAGE_LongerSize`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RebatchImages`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `InspyrenetRembg` —— 3/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `ShowText` —— 3/4 个有
- `easy promptConcat` —— 3/4 个有
- `SimpleMath+` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
