---
name: unknown_workflow_lora_sampler_clip_229
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.877
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Replace, EmptySD3LatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/各式写真生成器_2052206066884202498.json, 图片生成/文生图/摄影扭蛋机_zip_2053515891534512130.json, 图片生成/文生图/萌男摇摇乐_2052015200747962369.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_229

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/各式写真生成器_2052206066884202498.json、图片生成/文生图/摄影扭蛋机_zip_2053515891534512130.json、图片生成/文生图/萌男摇摇乐_2052015200747962369.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Replace`
- `EmptySD3LatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 2/3 个有
- `easy int` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `DuckHideNode` —— 1/3 个有
- `HAIGC_SaveImagesToZip` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RegexExtract` —— 1/3 个有
- `easy getNode` —— 1/3 个有
- `easy setNode` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
