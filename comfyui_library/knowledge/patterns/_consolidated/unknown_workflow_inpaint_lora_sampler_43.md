---
name: unknown_workflow_inpaint_lora_sampler_43
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.964
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, DF_Text_Box, DualCLIPLoader, FeatheredMask, GrowMask, INPAINT_ApplyFooocusInpaint, INPAINT_InpaintWithModel, INPAINT_LoadFooocusInpaint, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, Image Blend by Mask, Image Comparer (rgthree), KSampler (Efficient), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, SaveImage, UNETLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/手动可操控移除物体_1909082607488016385.json, 平台全量/物品消除_1897227310834077697.json, 平台全量/物品消除_2075519752872742913.json, 平台全量/🦄万物消除，手动遮罩涂抹🎯天下无腰_2035007127311355905.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/手动可操控移除物体_1909082607488016385.json、平台全量/物品消除_1897227310834077697.json、平台全量/物品消除_2075519752872742913.json、平台全量/🦄万物消除，手动遮罩涂抹🎯天下无腰_2035007127311355905.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DF_Text_Box`
- `DualCLIPLoader`
- `FeatheredMask`
- `GrowMask`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `Image Blend by Mask`
- `Image Comparer (rgthree)`
- `KSampler (Efficient)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | 0.6 - 0.6 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 4 | 100% |
| 采样算法 | dpmpp_sde | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.6，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
