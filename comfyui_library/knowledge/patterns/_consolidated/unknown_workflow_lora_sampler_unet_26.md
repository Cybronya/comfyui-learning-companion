---
name: unknown_workflow_lora_sampler_unet_26
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.889167
common_nodes: [CLIPLoader, CR Text, CR Text Replace, EmptySD3LatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/绅士美学文生图快速出图_2100549454419025922.json, 图片生成/文生图/绅士美学文生图快速出图_2100570247014215682.json, 图片生成/文生图/绅士美学文生图快速出图_2103299027126276098.json, 图片生成/文生图/绅士美学文生图快速出图_2104853569731125249.json, 视频生成/图生视频/2045119996459749378.json, 视频生成/图生视频/2041990716972343297.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_26

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/绅士美学文生图快速出图_2100549454419025922.json、图片生成/文生图/绅士美学文生图快速出图_2100570247014215682.json、图片生成/文生图/绅士美学文生图快速出图_2103299027126276098.json、图片生成/文生图/绅士美学文生图快速出图_2104853569731125249.json、视频生成/图生视频/2045119996459749378.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `CR Text Replace`
- `EmptySD3LatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `llama_cpp_clean_states` —— 4/6 个有
- `CFGNorm` —— 2/6 个有
- `GetImageSize` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `TextEncodeQwenImageEditPlus` —— 2/6 个有
- `CustomAddLabel` —— 1/6 个有
- `Int` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 6 - 9 | 6 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 67% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 6 - 9，6 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 67%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（10/6 个样本）：Steps较低可能导致细节不足
