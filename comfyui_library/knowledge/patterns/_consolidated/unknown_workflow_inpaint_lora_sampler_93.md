---
name: unknown_workflow_inpaint_lora_sampler_93
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8015
common_nodes: [Anything Everywhere3, CLIPTextEncode, CM_IntToNumber, CM_NumberToInt, CM_NumberUnaryOperation, CheckpointLoaderSimple, ColorMatch, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), Florence2ModelLoader, Florence2Run, GrowMaskWithBlur, INPAINT_ApplyFooocusInpaint, INPAINT_InpaintWithModel, INPAINT_LoadFooocusInpaint, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, Image Comparer (rgthree), ImageAndMaskPreview, ImageResizeKJ, ImageToMask, InpaintModelConditioning, Int, JWImageResizeByLongerSide, KSampler, LayerUtility: CropByMask, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewImage, ResizeMask, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy imageSize, easy mathInt]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万物移除工作流（移除物体、去水印等）_1901931679923986433.json, 平台全量/人物消失万物移除去水印等各种消失工作流_1904444729029791746.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_93

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/万物移除工作流（移除物体、去水印等）_1901931679923986433.json、平台全量/人物消失万物移除去水印等各种消失工作流_1904444729029791746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `CM_NumberUnaryOperation`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `GrowMaskWithBlur`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LayerUtility: CropByMask`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `ResizeMask`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy mathInt`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 67% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.55 | - | 2 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 0.55，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
