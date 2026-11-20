---
name: unknown_workflow_lora_sampler_checkpoint_12
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.733
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, CR Overlay Text, CR Text, CR Text Replace, CheckpointLoaderSimple, DuckHideNode, Easy_QwenEdit2509, Fast Groups Muter (rgthree), GetNode, HAIGC_LoadImagesFromZip, HAIGC_SaveImagesToZip, ImageScaleToTotalPixels, JDCN_StringToList, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewAny, ProcessString, RHUploadZip, ResizeLongestToNode, SaveImage, SetNode, ShowText|pysssss, String, Text Concatenate, Time String (WLSH), UNETLoader, VAEDecode, VAELoader, easy int, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, string_util_Str]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/WF 图片编辑 AIO V23 P3T1 Zip批量多图单指令编辑_2034214259604856834.json, 图片生成/文生图/图片编辑 AIO V23 P1T1 单图单指令 ZIP保存_2028646206754267138.json, 图片生成/文生图/图片编辑 AIO V23 P1T3 单图多指令 ZIP保存_2034187035010932737.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/WF 图片编辑 AIO V23 P3T1 Zip批量多图单指令编辑_2034214259604856834.json、图片生成/文生图/图片编辑 AIO V23 P1T1 单图单指令 ZIP保存_2028646206754267138.json、图片生成/文生图/图片编辑 AIO V23 P1T3 单图多指令 ZIP保存_2034187035010932737.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `CR Overlay Text`
- `CR Text`
- `CR Text Replace`
- `CheckpointLoaderSimple`
- `DuckHideNode`
- `Easy_QwenEdit2509`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `HAIGC_LoadImagesFromZip`
- `HAIGC_SaveImagesToZip`
- `ImageScaleToTotalPixels`
- `JDCN_StringToList`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `ProcessString`
- `RHUploadZip`
- `ResizeLongestToNode`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `String`
- `Text Concatenate`
- `Time String (WLSH)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `string_util_Str`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `ImageBlur` —— 2/3 个有
- `ImpactImageBatchToImageList` —— 2/3 个有
- `ImpactMakeImageBatch` —— 2/3 个有
- `LayerUtility: ImageBlendAdvance V2` —— 2/3 个有
- `SelectImages` —— 2/3 个有
- `Text` —— 2/3 个有
- `1hew_ImageListToBatch` —— 1/3 个有
- `Float` —— 1/3 个有
- `ImageConcatFromBatch` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `VHS_GetImageCount` —— 1/3 个有
- `YANC.FormatDatetimeString` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
