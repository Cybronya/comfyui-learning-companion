---
name: unknown_workflow_inpaint_upscale_lora_4
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.614333
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GetNode, ImageConcanate, ImageCrop, ImageResize+, ImageScale, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, InspyrenetRembg, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorPicker, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, ReActorRestoreFace, SaveImage, SetNode, StyleModelApply, StyleModelLoader, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy imageScaleDownToSize, easy imageSize]
problems: []
missing: []
members: [平台全量/2071501913450962945.json, 平台全量/strict-person-replace-v3-openapi-clean_2071850404291366914.json, 平台全量/固定人物换指定场景工作流_1867460387758129153.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/2071501913450962945.json、平台全量/strict-person-replace-v3-openapi-clean_2071850404291366914.json、平台全量/固定人物换指定场景工作流_1867460387758129153.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GetNode`
- `ImageConcanate`
- `ImageCrop`
- `ImageResize+`
- `ImageScale`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InspyrenetRembg`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `ReActorRestoreFace`
- `SaveImage`
- `SetNode`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageScaleDownToSize`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ReActorFaceSwap` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 20 - 28 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.15 | 3 | 93% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.72 - 1 | 3 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，观测区间 20 - 28，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.15，3 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.72 - 1，3 个样本，取值集中（一致性 85%）
