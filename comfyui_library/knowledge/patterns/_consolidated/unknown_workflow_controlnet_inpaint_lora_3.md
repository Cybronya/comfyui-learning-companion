---
name: unknown_workflow_controlnet_inpaint_lora_3
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.569
common_nodes: [ACN_AdvancedControlNetApply_v2, AIO_Preprocessor, Anything Everywhere, Anything Everywhere3, CLIPTextEncodeFlux, CM_IntToBool, CR String To Number, CR Text, CR Text Concatenate, CXH_Florence2Run, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetLoader, DetailerForEach, DifferentialDiffusion, DownloadAndLoadFlorence2Model, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImpactConditionalBranch, InpaintCrop, InpaintModelConditioning, InpaintStitch, Int, KSampler, LTXVPromptEnhancer, LTXVPromptEnhancerLoader, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, MaskToSEGS, PreviewImage, RH_Captioner, RH_Translator, RepeatLatentBatch, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, StringConstant, SubtractMask, VAEDecode, easy imageChooser]
problems: []
missing: []
members: [图片生成/图生图/FLux局部重绘 脸部一致+人物服装换装_1921221516183404545.json, 图片生成/文生图/【商业级】Flxu局部重绘人像处理篇V2（多功能、全自动）_1919189783527231490.json, 图片生成/文生图/局部重绘人像处理（多功能、全自动）_1945748479278981121.json, 视频生成/文生视频/局部重绘人像处理（多功能、全自动）_1942785187778334721.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLux局部重绘 脸部一致+人物服装换装_1921221516183404545.json、图片生成/文生图/【商业级】Flxu局部重绘人像处理篇V2（多功能、全自动）_1919189783527231490.json、图片生成/文生图/局部重绘人像处理（多功能、全自动）_1945748479278981121.json、视频生成/文生视频/局部重绘人像处理（多功能、全自动）_1942785187778334721.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 4 个 workflow 都包含：
- `ACN_AdvancedControlNetApply_v2`
- `AIO_Preprocessor`
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncodeFlux`
- `CM_IntToBool`
- `CR String To Number`
- `CR Text`
- `CR Text Concatenate`
- `CXH_Florence2Run`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DetailerForEach`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactConditionalBranch`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `Int`
- `KSampler`
- `LTXVPromptEnhancer`
- `LTXVPromptEnhancerLoader`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MaskToSEGS`
- `PreviewImage`
- `RH_Captioner`
- `RH_Translator`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `StringConstant`
- `SubtractMask`
- `VAEDecode`
- `easy imageChooser`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 4 | 100% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
