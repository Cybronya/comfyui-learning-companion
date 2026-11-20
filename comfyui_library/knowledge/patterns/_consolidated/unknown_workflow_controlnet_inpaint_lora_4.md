---
name: unknown_workflow_controlnet_inpaint_lora_4
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.545333
common_nodes: [AIO_Preprocessor, Anything Everywhere3, CFGNorm, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DetailTransfer, DifferentialDiffusion, GetNode, INPAINT_MaskedFill, ImageBlend, ImageConcatMulti, ImageScale, ImageSmartSharpen+, InpaintModelConditioning, KSampler, LBMSampler, LayerColor: Brightness & Contrast, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadLBMModel, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, RH_LLMAPI_NODE, RH_Translator, RebatchLatents, RepeatLatentBatch, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageRemBg, easy seed, easy textSwitch, ttN concat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Cosplay换背景+打光-qwen edit+ibm_1969199998082707458.json, 图片生成/图生图/背景替换_2036002458442407937.json, 图片生成/图生图/😯换背景-主体置换参考背景-原图IBM打光-qwen edit+ibm_1974055419339517954.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Cosplay换背景+打光-qwen edit+ibm_1969199998082707458.json、图片生成/图生图/背景替换_2036002458442407937.json、图片生成/图生图/😯换背景-主体置换参考背景-原图IBM打光-qwen edit+ibm_1974055419339517954.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailTransfer`
- `DifferentialDiffusion`
- `GetNode`
- `INPAINT_MaskedFill`
- `ImageBlend`
- `ImageConcatMulti`
- `ImageScale`
- `ImageSmartSharpen+`
- `InpaintModelConditioning`
- `KSampler`
- `LBMSampler`
- `LayerColor: Brightness & Contrast`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadLBMModel`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `RebatchLatents`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageRemBg`
- `easy seed`
- `easy textSwitch`
- `ttN concat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
