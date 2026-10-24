---
name: unknown_workflow_lora_clip_unet_3
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.861364
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptySD3LatentImage, JDCN_StringToList, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图+自动优化提示词_2060877486279450626.json, 图片生成/文生图/文生图（自动优化提示词，全内容）_2059980038669422593.json, 图片生成/文生图/美学文生图_2037917835934048258.json, 图片生成/文生图/美学文生图_2038170383051923457.json, 图片生成/文生图/美学文生图_2038945200831209473.json, 图片生成/文生图/自动提示词文生图V1.1_2065419266714849281.json, 图片生成/文生图/自动提示词文生图V1.1_2075057029013655554.json, 图片生成/文生图/超级美学文生图，自动提示词美化_2044012198627905537.json, 图片生成/文生图/雅致美学文生图V1.1_2050555900452192257.json, 图片生成/文生图/高雅美学扭蛋机_2049685786714488834.json, 图片生成/文生图/🦄Z-image扭蛋文生图 🎯天下无腰_2062502101711933441.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/文生图+自动优化提示词_2060877486279450626.json、图片生成/文生图/文生图（自动优化提示词，全内容）_2059980038669422593.json、图片生成/文生图/美学文生图_2037917835934048258.json、图片生成/文生图/美学文生图_2038170383051923457.json、图片生成/文生图/美学文生图_2038945200831209473.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `JDCN_StringToList`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 9/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `llama_cpp_instruct_adv` —— 9/11 个有
- `llama_cpp_model_loader` —— 9/11 个有
- `llama_cpp_parameters` —— 7/11 个有
- `CR Text Replace` —— 6/11 个有
- `llama_cpp_clean_states` —— 6/11 个有
- `LoadImage` —— 5/11 个有
- `RHHiddenNodes` —— 5/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `easy int` —— 3/11 个有
- `CFGNorm` —— 2/11 个有
- `KSamplerAdvanced` —— 2/11 个有
- `RH_LLMAPI_NODE` —— 2/11 个有
- `easy showAnything` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 9 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 11 | 0% |
| 采样算法 | euler_ancestral | - | 11 | 55% |
| 调度器 | simple | - | 11 | 45% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，9 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，11 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler_ancestral，11 个样本，一致性 55%
- 调度器 最常用 simple，11 个样本，一致性 45%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
