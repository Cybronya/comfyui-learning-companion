---
name: unknown_workflow_lora_clip_unet
type: Unknown Workflow
frequency: 41
level: moderate
coverage: 0.871585
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Replace, EmptySD3LatentImage, JDCN_StringToList, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/唯美抽卡文生图_2050836322817982466.json, 图片生成/文生图/地表最强美学文生图-使用自由灵活_2046146947014201345.json, 图片生成/文生图/墨幽Z-image欧亚纯欲私房人像_2065517075992498177.json, 图片生成/文生图/女频短剧古风角色设计工作流_2071324708490014722.json, 图片生成/文生图/小红书ins风文生图_2038522821722247169.json, 图片生成/文生图/批量洗图 一次9张图 Z-Image-Turbo 美学文生图_2045749943704489985.json, 图片生成/文生图/文生图 美女各种造型_2039952046241095682.json, 图片生成/文生图/文生图批量出图-各种时代风格均可_2040787252544020482.json, 图片生成/文生图/最受欢迎美学文生图-zip_2048628552379142145.json, 图片生成/文生图/最受欢迎美学文生图_2037071836214730753.json, 图片生成/文生图/最受欢迎美学文生图_2049489608165036034.json, 图片生成/文生图/最受欢迎美学文生图_2049507480018886657.json, 图片生成/文生图/最受欢迎美学文生图_2052369948986617858.json, 图片生成/文生图/最好看超梦幻终极高清美学文生图 2_2097488176058290177.json, 图片生成/文生图/最美丽的文生图_2043860608734470145.json, 图片生成/文生图/林荫青春 · 日系JK少女元气写真_2043960060086329346.json, 图片生成/文生图/生成不同姿势的文生图_2048561332487720961.json, 图片生成/文生图/绅士(猛男)必备美学文生图_2037379986608365569.json, 图片生成/文生图/绅士美学 文生图_2037852434311159810.json, 图片生成/文生图/绅士美学文生图- 邻家AI大女孩_2041959172656340994.json, 图片生成/文生图/绅士美学文生图V1.1_2065364992593063938.json, 图片生成/文生图/绅士美学文生图_2043164185919492097.json, 图片生成/文生图/绅士美学文生图_2043537507744223234.json, 图片生成/文生图/绅士美学文生图工作流_2038478405020160002.json, 图片生成/文生图/绅士美学文生图工作流_2038581767006851074.json, 图片生成/文生图/绅士美学文生图工作流_2067207382131892226.json, 图片生成/文生图/绅士美学文生图工作流_2112481300396466177.json, 图片生成/文生图/绅士美学文生图工作流_2112538158800916481.json, 图片生成/文生图/绅士美学文生图快速出图_2082099425329115138.json, 图片生成/文生图/绅士美学文生图快速出图_2100549454419025922.json, 图片生成/文生图/绅士美学文生图快速出图_2100570247014215682.json, 图片生成/文生图/绅士美学文生图快速出图_2103299027126276098.json, 图片生成/文生图/绅士美学文生图快速出图_2104853569731125249.json, 图片生成/文生图/绅士美学文生图，输入提示词和生成图片数量即可，绝美推荐！_2038437859195101186.json, 图片生成/文生图/绅士美学文生图，输入提示词和生成图片数量即可，绝美推荐！_2042047375442714625.json, 图片生成/文生图/绅士美学文生图，输入提示词和生成图片数量即可，绝美推荐！_2074692182715494401.json, 图片生成/文生图/网红美女模特小红书高质量洗图美学文生图 Z-Image-base+Z-Image-Turbo_2037344482659667970.json, 图片生成/文生图/美女文生图_2039512911617462274.json, 图片生成/文生图/美女素材文生图_2039711334178234370.json, 图片生成/文生图/美学文生图v1.2_2071115010402766849.json, 图片生成/文生图/金庸武侠_v2.1-krea_2071973773867311106.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet

> 由 `engine/knowledge_consolidation` 从 41 个 workflow 归纳得出（图片生成/文生图/唯美抽卡文生图_2050836322817982466.json、图片生成/文生图/地表最强美学文生图-使用自由灵活_2046146947014201345.json、图片生成/文生图/墨幽Z-image欧亚纯欲私房人像_2065517075992498177.json、图片生成/文生图/女频短剧古风角色设计工作流_2071324708490014722.json、图片生成/文生图/小红书ins风文生图_2038522821722247169.json…）

- **类型**：Unknown Workflow
- **样本数**：41
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 41 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Replace`
- `EmptySD3LatentImage`
- `JDCN_StringToList`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 40/41 个有
- `llama_cpp_clean_states` —— 39/41 个有
- `KSampler` —— 37/41 个有
- `Fast Groups Bypasser (rgthree)` —— 36/41 个有
- `llama_cpp_instruct_adv` —— 36/41 个有
- `llama_cpp_model_loader` —— 36/41 个有
- `llama_cpp_parameters` —— 36/41 个有
- `RH_LLMAPI_NODE` —— 5/41 个有
- `CFGNorm` —— 4/41 个有
- `KSamplerAdvanced` —— 4/41 个有
- `HAIGC_SaveImagesToZip` —— 3/41 个有
- `CompressImages` —— 2/41 个有
- `ImageListToBatch+` —— 1/41 个有
- `PreviewImage` —— 1/41 个有
- `PrimitiveBoolean` —— 1/41 个有
- `Text Concatenate` —— 1/41 个有
- `ZML_SwitchOutput` —— 1/41 个有
- `easy cleanGpuUsed` —— 1/41 个有
- `easy saveText` —— 1/41 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 6 - 9 | 37 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 41 | 0% |
| 采样算法 | euler_ancestral | - | 41 | 88% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 41 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 37 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 73/41 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 6 - 9，37 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，41 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler_ancestral，41 个样本，一致性 88%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，41 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，37 个样本，取值集中（一致性 100%）
- 高发问题（73/41 个样本）：Steps较低可能导致细节不足
