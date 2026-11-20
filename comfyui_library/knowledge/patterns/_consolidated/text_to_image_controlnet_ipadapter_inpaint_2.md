---
name: text_to_image_controlnet_ipadapter_inpaint_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.757333
common_nodes: [ACN_AdvancedControlNetApply_v2, AIO_Preprocessor, Anything Everywhere3, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSize+, ImageResize+, ImageScale, ImageUpscaleWithModel, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UnetLoaderGGUF, UpscaleModelLoader, VAEDecode, VAELoader, easy imageInsetCrop, easy ipadapterApply, easy makeImageForICLora]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【自定义姿势】超强人物一致性_1937323234260107266.json, 图片生成/图生图/【自定义姿势】超强人物一致性，无需lora！太强了_1925181871607771137.json, 图片生成/图生图/最强人物更换姿势100%一致性_1936612047746420737.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_inpaint_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【自定义姿势】超强人物一致性_1937323234260107266.json、图片生成/图生图/【自定义姿势】超强人物一致性，无需lora！太强了_1925181871607771137.json、图片生成/图生图/最强人物更换姿势100%一致性_1936612047746420737.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `ACN_AdvancedControlNetApply_v2`
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize+`
- `ImageResize+`
- `ImageScale`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UnetLoaderGGUF`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`
- `easy ipadapterApply`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `ApplyInstantID` —— 2/3 个有
- `ChinesePrompt_Mix` —— 2/3 个有
- `CropFaces` —— 2/3 个有
- `DetectFaces` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `InstantIDFaceAnalysis` —— 2/3 个有
- `InstantIDModelLoader` —— 2/3 个有
- `MaskComposite` —— 2/3 个有
- `MaskFastGrow` —— 2/3 个有
- `SetLatentNoiseMask` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `WarpFacesBack` —— 2/3 个有
- `easy imageColorMatch` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 600 | 600 - 600 | 3 | 100% |
| 高度 | 904 | 904 - 904 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 600，观测区间 600 - 600，3 个样本，取值集中（一致性 100%）
- 高度 中位数 904，观测区间 904 - 904，3 个样本，取值集中（一致性 100%）
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
