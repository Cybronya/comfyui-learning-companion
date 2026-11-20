---
name: unknown_workflow_lora_sampler_unet_356
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [CR Text, Compare, CompressImages, FromListGet1Image, ImageConcanate, ImageConcatMulti, ImageListToImageBatch, ImpactSwitch, Int, IntToString, InversionDemoLazySwitch, LayerUtility: ImageScaleByAspectRatio V2, List Length, LoadImage, MergeImageLists, Multi Text Merge, ProcessString, RH_LLMAPI_NODE, RunningHub Deepcleaner, SaveImage, TextInput_, easy forLoopEnd, easy forLoopStart, easy imageConcat, easy mathInt, easy promptConcat, easy promptLine, easy promptReplace, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/发朋友圈专用——穿搭大师 Pro 多视角OOTD_2010534563256209410.json, 平台全量/穿搭大师 Pro 多视角OOTD_2010404234423963650.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_356

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/发朋友圈专用——穿搭大师 Pro 多视角OOTD_2010534563256209410.json、平台全量/穿搭大师 Pro 多视角OOTD_2010404234423963650.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `Compare`
- `CompressImages`
- `FromListGet1Image`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageListToImageBatch`
- `ImpactSwitch`
- `Int`
- `IntToString`
- `InversionDemoLazySwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `List Length`
- `LoadImage`
- `MergeImageLists`
- `Multi Text Merge`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `RunningHub Deepcleaner`
- `SaveImage`
- `TextInput_`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageConcat`
- `easy mathInt`
- `easy promptConcat`
- `easy promptLine`
- `easy promptReplace`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `CR Overlay Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `QwenMultiangleCameraNode` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | ['1037', 0] | - | 1 | 100% |
| 高度 | ['1036', 0] | - | 1 | 100% |
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
