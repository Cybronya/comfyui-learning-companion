---
name: unknown_workflow_inpaint_sampler_clip_36
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.850667
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DeepTranslatorTextNode, DualCLIPLoader, FluxGuidance, GetImageSize+, ImageConcanate, ImageCrop+, ImageResizeKJ, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerStyle: ColorOverlay V2, LayerUtility: ColorImage V2, LoadImage, PreviewImage, SaveImage, StyleModelLoader, Switch any [Crystools], UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX FILL自动遮罩换装_1956561807777431554.json, 图片生成/图生图/【丙丙版哪吒】最强换头术，太乙真人换哪吒_1898375384982081537.json, 图片生成/图生图/【很强】电商产品迁移指定场景细节版_1942158807361601537.json, 图片生成/图生图/【电商】产品迁移指定场景plus完美细节版_1904379336580046850.json, 图片生成/图生图/【电商】电商产品指定场景【手机壳版】_1904358996265050114.json, 平台全量/【趣味】【飞翔鲸】王炸！FLUX+ACE++换头_1890052281759571970.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FLUX FILL自动遮罩换装_1956561807777431554.json、图片生成/图生图/【丙丙版哪吒】最强换头术，太乙真人换哪吒_1898375384982081537.json、图片生成/图生图/【很强】电商产品迁移指定场景细节版_1942158807361601537.json、图片生成/图生图/【电商】产品迁移指定场景plus完美细节版_1904379336580046850.json、图片生成/图生图/【电商】电商产品指定场景【手机壳版】_1904358996265050114.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskGrow`
- `LayerStyle: ColorOverlay V2`
- `LayerUtility: ColorImage V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelLoader`
- `Switch any [Crystools]`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ColorPicker` —— 4/6 个有
- `LayerUtility: CropByMask V2` —— 4/6 个有
- `LayerUtility: ImageScaleRestore V2` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `MaskPreview+` —— 4/6 个有
- `MaskToImage` —— 4/6 个有
- `ReduxAdvanced` —— 4/6 个有
- `JjkText` —— 3/6 个有
- `LayerMask: ObjectDetectorYOLO8` —— 3/6 个有
- `LayerMask: SAM2Ultra` —— 3/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/6 个有
- `TeaCache` —— 3/6 个有
- `Display Any (rgthree)` —— 2/6 个有
- `InpaintCrop` —— 2/6 个有
- `InpaintStitch` —— 2/6 个有
- `LayerMask: PersonMaskUltra` —— 2/6 个有
- `LayerUtility: GetImageSize` —— 2/6 个有
- `LayerUtility: RestoreCropBox` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `AddMask` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerMask: PersonMaskUltra V2` —— 1/6 个有
- `LayerUtility: CropByMask` —— 1/6 个有
- `Mask Threshold Region` —— 1/6 个有
- `PowerfulMaskCrop` —— 1/6 个有
- `SubtractMask` —— 1/6 个有
- `easy sam3ImageSegmentation` —— 1/6 个有
- `easy sam3ModelLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25.5 | 25 - 26 | 6 | 98% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 2 | 6 | 76% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25.5，观测区间 25 - 26，6 个样本，取值集中（一致性 98%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 2，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
