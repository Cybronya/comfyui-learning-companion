---
name: unknown_workflow_lora_sampler_clip_155
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8515
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize, Image Comparer (rgthree), KSampler, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, PanoramaViewerNode, PreviewImage, SaveImage, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, ZNGB_Equirect360ToViews, easy positive, easy showAnything, llama_cpp_clean_states, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_unload_model]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1-Aiden-360全景生成_2080345693348261890.json, 图片生成/文生图/1-Aiden-360全景生成_2096836824219086850.json, 图片生成/文生图/360度全景场景生成  Qwen2512 文生图_2081679129409310722.json, 图片生成/文生图/全景图生成 360度 生图_2082880184562307074.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_155

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1-Aiden-360全景生成_2080345693348261890.json、图片生成/文生图/1-Aiden-360全景生成_2096836824219086850.json、图片生成/文生图/360度全景场景生成  Qwen2512 文生图_2081679129409310722.json、图片生成/文生图/全景图生成 360度 生图_2082880184562307074.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PanoramaViewerNode`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZNGB_Equirect360ToViews`
- `easy positive`
- `easy showAnything`
- `llama_cpp_clean_states`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_unload_model`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 3/4 个有
- `忽略多组孤海` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.45 | 0.45 - 0.45 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 0.45，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
