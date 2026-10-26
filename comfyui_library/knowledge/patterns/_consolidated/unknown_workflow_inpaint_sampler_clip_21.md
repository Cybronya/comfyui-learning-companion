---
name: unknown_workflow_inpaint_sampler_clip_21
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8438
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DeepTranslatorTextNode, DualCLIPLoader, FluxGuidance, GetImageSize+, ImageConcanate, ImageCrop+, ImageResizeKJ, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerStyle: ColorOverlay V2, LayerUtility: ColorImage V2, LoadImage, PreviewImage, SaveImage, StyleModelLoader, Switch any [Crystools], UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX FILL自动遮罩换装_1956561807777431554.json, 图片生成/图生图/【丙丙版哪吒】最强换头术，太乙真人换哪吒_1898375384982081537.json, 图片生成/图生图/【很强】电商产品迁移指定场景细节版_1942158807361601537.json, 图片生成/图生图/【电商】产品迁移指定场景plus完美细节版_1904379336580046850.json, 图片生成/图生图/【电商】电商产品指定场景【手机壳版】_1904358996265050114.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX FILL自动遮罩换装_1956561807777431554.json、图片生成/图生图/【丙丙版哪吒】最强换头术，太乙真人换哪吒_1898375384982081537.json、图片生成/图生图/【很强】电商产品迁移指定场景细节版_1942158807361601537.json、图片生成/图生图/【电商】产品迁移指定场景plus完美细节版_1904379336580046850.json、图片生成/图生图/【电商】电商产品指定场景【手机壳版】_1904358996265050114.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LayerUtility: ColorPicker` —— 4/5 个有
- `MaskPreview+` —— 4/5 个有
- `MaskToImage` —— 4/5 个有
- `JjkText` —— 3/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/5 个有
- `LayerUtility: CropByMask V2` —— 3/5 个有
- `LayerUtility: ImageScaleRestore V2` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ReduxAdvanced` —— 3/5 个有
- `TeaCache` —— 3/5 个有
- `InpaintCrop` —— 2/5 个有
- `InpaintStitch` —— 2/5 个有
- `LayerMask: ObjectDetectorYOLO8` —— 2/5 个有
- `LayerMask: SAM2Ultra` —— 2/5 个有
- `LayerUtility: GetImageSize` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `AddMask` —— 1/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `LayerMask: PersonMaskUltra` —— 1/5 个有
- `LayerMask: PersonMaskUltra V2` —— 1/5 个有
- `LayerUtility: CropByMask` —— 1/5 个有
- `LayerUtility: RestoreCropBox` —— 1/5 个有
- `Mask Threshold Region` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `SubtractMask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26 | 25 - 26 | 5 | 98% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 2 | 5 | 79% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 26，观测区间 25 - 26，5 个样本，取值集中（一致性 98%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 2，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
