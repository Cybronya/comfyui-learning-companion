---
name: image_to_image_controlnet_ipadapter_inpaint
type: Image To Image
frequency: 4
level: strong
coverage: 0.7235
common_nodes: [AV_VAELoader, Any Switch (rgthree), BNK_CLIPTextEncodeAdvanced, CLIPVisionLoader, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, DepthAnythingPreprocessor, FaceDetailer, FeatheredMask, IPAdapterFaceID, IPAdapterModelLoader, ImageBlend, ImageResize+, ImageUpscaleWithModel, InpaintPreprocessor, InvertMask, KSampler, KSampler Config (rgthree), LayerColor: ColorAdapter, LayerMask: SegmentAnythingUltra, LoadImage, Mask Gaussian Region, MaskPreview+, PrepImageForClipVision, PreviewImage, SAMLoader, SaveImage, StringFunction|pysssss, Text Concatenate, TextInput_, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAEEncodeForInpaint, WD14Tagger|pysssss]
problems: []
missing: []
members: [平台全量/一键换背景_1778254813151158273.json, 平台全量/一键换装_1778255145872711682.json, 平台全量/一键换装换发型换背景_1778255908640448514.json, 平台全量/一键换装换背景_1778255604654071810.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_inpaint

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/一键换背景_1778254813151158273.json、平台全量/一键换装_1778255145872711682.json、平台全量/一键换装换发型换背景_1778255908640448514.json、平台全量/一键换装换背景_1778255604654071810.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `AV_VAELoader`
- `Any Switch (rgthree)`
- `BNK_CLIPTextEncodeAdvanced`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `DepthAnythingPreprocessor`
- `FaceDetailer`
- `FeatheredMask`
- `IPAdapterFaceID`
- `IPAdapterModelLoader`
- `ImageBlend`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `InpaintPreprocessor`
- `InvertMask`
- `KSampler`
- `KSampler Config (rgthree)`
- `LayerColor: ColorAdapter`
- `LayerMask: SegmentAnythingUltra`
- `LoadImage`
- `Mask Gaussian Region`
- `MaskPreview+`
- `PrepImageForClipVision`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `StringFunction|pysssss`
- `Text Concatenate`
- `TextInput_`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeForInpaint`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `Zoe_DepthAnythingPreprocessor` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.925 | 0.85 - 1 | 4 | 92% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | dpmpp_sde | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 0.75 | 0.7 - 0.8 | 4 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.925，观测区间 0.85 - 1，4 个样本，取值集中（一致性 92%）
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.7 - 0.8，4 个样本，取值集中（一致性 93%）
