---
name: unknown_workflow_lora_clip_unet_2
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.881125
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Replace, EmptySD3LatentImage, JDCN_StringToList, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/唯美抽卡文生图_2050836322817982466.json, 图片生成/文生图/墨幽Z-image欧亚纯欲私房人像_2065517075992498177.json, 图片生成/文生图/女频短剧古风角色设计工作流_2071324708490014722.json, 图片生成/文生图/最受欢迎美学文生图_2037071836214730753.json, 图片生成/文生图/最好看超梦幻终极高清美学文生图 2_2097488176058290177.json, 图片生成/文生图/绅士美学文生图V1.1_2065364992593063938.json, 图片生成/文生图/绅士美学文生图工作流_2067207382131892226.json, 图片生成/文生图/绅士美学文生图快速出图_2082099425329115138.json, 图片生成/文生图/绅士美学文生图快速出图_2100549454419025922.json, 图片生成/文生图/绅士美学文生图快速出图_2100570247014215682.json, 图片生成/文生图/绅士美学文生图快速出图_2103299027126276098.json, 图片生成/文生图/绅士美学文生图快速出图_2104853569731125249.json, 图片生成/文生图/绅士美学文生图，输入提示词和生成图片数量即可，绝美推荐！_2074692182715494401.json, 图片生成/文生图/美学文生图v1.2_2071115010402766849.json, 图片生成/文生图/自动提示词文生图V1.1_2065419266714849281.json, 图片生成/文生图/自动提示词文生图V1.1_2075057029013655554.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/唯美抽卡文生图_2050836322817982466.json、图片生成/文生图/墨幽Z-image欧亚纯欲私房人像_2065517075992498177.json、图片生成/文生图/女频短剧古风角色设计工作流_2071324708490014722.json、图片生成/文生图/最受欢迎美学文生图_2037071836214730753.json、图片生成/文生图/最好看超梦幻终极高清美学文生图 2_2097488176058290177.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Replace`
- `EmptySD3LatentImage`
- `JDCN_StringToList`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_clean_states` —— 14/16 个有
- `KSampler` —— 11/16 个有
- `Fast Groups Bypasser (rgthree)` —— 10/16 个有
- `llama_cpp_instruct_adv` —— 10/16 个有
- `llama_cpp_model_loader` —— 10/16 个有
- `llama_cpp_parameters` —— 10/16 个有
- `RH_LLMAPI_NODE` —— 6/16 个有
- `CFGNorm` —— 5/16 个有
- `KSamplerAdvanced` —— 5/16 个有
- `HAIGC_SaveImagesToZip` —— 1/16 个有
- `LoadImage` —— 1/16 个有
- `Text Concatenate` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有
- `easy saveText` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 9 | 11 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 16 | 10% |
| 采样算法 | euler_ancestral | - | 16 | 62% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 16 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 9，11 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，16 个样本，取值分散，一致性仅 10%
- 采样算法 最常用 euler_ancestral，16 个样本，一致性 62%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，16 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（21/16 个样本）：Steps较低可能导致细节不足
