---
name: text_to_image_inpaint_sampler_clip_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.732333
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, InpaintModelConditioning, KSampler, LayerColor: AutoAdjustV2, LayerColor: HSV, LayerMask: MaskBoxDetect, LayerMask: MaskPreview, LayerMask: MaskStroke, LayerMask: ShadowHighlightMaskV2, LayerMask: YoloV8Detect, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: GetImageSize, LayerUtility: ImageAutoCrop V3, LayerUtility: ImageBlend V2, LayerUtility: ImageBlendAdvance V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LayerUtility: Seed, LoadImage, PreviewImage, SaveImage, ShowText|pysssss, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键给照片加上相框氛围感_1906648409602707457.json, 图片生成/图生图/照片与相框融合版工作流_2005570185358700546.json, 图片生成/图生图/精讲版（葫芦娃开源）照片变相框融合版工作流_1906178794665725954.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键给照片加上相框氛围感_1906648409602707457.json、图片生成/图生图/照片与相框融合版工作流_2005570185358700546.json、图片生成/图生图/精讲版（葫芦娃开源）照片变相框融合版工作流_1906178794665725954.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `InpaintModelConditioning`
- `KSampler`
- `LayerColor: AutoAdjustV2`
- `LayerColor: HSV`
- `LayerMask: MaskBoxDetect`
- `LayerMask: MaskPreview`
- `LayerMask: MaskStroke`
- `LayerMask: ShadowHighlightMaskV2`
- `LayerMask: YoloV8Detect`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: GetImageSize`
- `LayerUtility: ImageAutoCrop V3`
- `LayerUtility: ImageBlend V2`
- `LayerUtility: ImageBlendAdvance V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LayerUtility: Seed`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: LoadSegmentAnythingModels` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/3 个有
- `LayerUtility: AnyRerouter` —— 2/3 个有
- `LayerUtility: ChoiceTextPreset` —— 2/3 个有
- `LayerUtility: TextBox` —— 2/3 个有
- `LayerUtility: TextJoinV2` —— 2/3 个有
- `LayerUtility: TextPreseter` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `DF_Text_Box` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image To Mask` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `KSampler (Efficient)` —— 1/3 个有
- `LayerMask: LoadFlorence2Model` —— 1/3 个有
- `LayerMask: ObjectDetectorFL2` —— 1/3 个有
- `LayerMask: SAM2Ultra` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PMRF` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `preview_mask` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 12 | 12 - 20 | 3 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.67 | 0.67 - 1 | 3 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 12，观测区间 12 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.67，观测区间 0.67 - 1，3 个样本，取值集中（一致性 80%）
