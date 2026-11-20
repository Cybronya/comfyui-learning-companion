---
name: unknown_workflow_controlnet_inpaint_lora_18
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.686
common_nodes: [ACN_ControlNetLoaderAdvanced, AIO_Preprocessor, Anything Everywhere, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, DualCLIPLoader, FaceRestoreCFWithModel, FaceRestoreModelLoader, FluxGuidance, GetNode, GoogleTranslateTextNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageCompositeMasked, ImageResizeKJ, ImpactSwitch, InpaintModelConditioning, InspyrenetRembgAdvanced, InvertMask, KSamplerAdvanced //Inspire, LayerMask: MaskPreview, LayerMask: SegformerClothesPipelineLoader, LayerMask: SegformerUltraV2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskComposite, PreviewImage, SaveImage, SetNode, Textbox, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/最强PS，还原您的美，风格随意换_1949824833317158913.json, 平台全量/锦鲤汉服修图专用_1891531316368723970.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/最强PS，还原您的美，风格随意换_1949824833317158913.json、平台全量/锦鲤汉服修图专用_1891531316368723970.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_ControlNetLoaderAdvanced`
- `AIO_Preprocessor`
- `Anything Everywhere`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `DualCLIPLoader`
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `FluxGuidance`
- `GetNode`
- `GoogleTranslateTextNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageResizeKJ`
- `ImpactSwitch`
- `InpaintModelConditioning`
- `InspyrenetRembgAdvanced`
- `InvertMask`
- `KSamplerAdvanced //Inspire`
- `LayerMask: MaskPreview`
- `LayerMask: SegformerClothesPipelineLoader`
- `LayerMask: SegformerUltraV2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskComposite`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `Textbox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 30 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
