---
name: unknown_workflow_lora_sampler_clip_264
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.963
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, CR Text Replace, EmptyLatentImage, FlowMatchEulerDiscreteScheduler (Custom), JDCN_StringToList, KSamplerSelect, LayerUtility: PurgeVRAM V2, LazyCache, LoraLoaderModelOnly, ProcessString, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2, ShowText|pysssss, Text Concatenate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-Image 自动扩写 官方调度器皮肤纹理质感细腻_2007754698790543362.json, 图片生成/文生图/Z-Image 自动扩写 官方调度器皮肤纹理质感细腻_2002583225962774529.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_264

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-Image 自动扩写 官方调度器皮肤纹理质感细腻_2007754698790543362.json、图片生成/文生图/Z-Image 自动扩写 官方调度器皮肤纹理质感细腻_2002583225962774529.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `CR Text Replace`
- `EmptyLatentImage`
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `JDCN_StringToList`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LazyCache`
- `LoraLoaderModelOnly`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2`
- `ShowText|pysssss`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1476 | - | 2 | 61% |
| 高度 | 1476 | - | 2 | 61% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1476，样本不足，未给区间，2 个样本
- 高度 中位数 1476，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
