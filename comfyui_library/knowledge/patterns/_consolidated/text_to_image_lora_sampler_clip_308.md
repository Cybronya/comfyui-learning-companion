---
name: text_to_image_lora_sampler_clip_308
type: Text To Image
frequency: 7
level: strong
coverage: 0.902286
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Replace, EmptyLatentImage, JDCN_StringToList, JjkText, KSampler, LoraLoaderModelOnly, ProcessString, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen2.1摆拍美学文生图，写实构图光影到极致_2112318313169776642.json, 图片生成/文生图/不同姿势文生图生成器 美少女写实多姿态处理工具_2114042179948732417.json, 图片生成/文生图/古风角色设计｜女频短剧人像写真文生图一键生成_2089772497628655617.json, 图片生成/文生图/摆拍美学文生图 摄影级构图画面直出高质量_2108983596869578754.json, 图片生成/文生图/摆拍美学文生图V1.1 摄影级构图画面直出_2109183810997932034.json, 图片生成/文生图/绅士美学文生图工作流｜美少女写实风一键出图氛围拉满_2112896790910554113.json, 图片生成/文生图/绅士美学文生图工作流｜美少女写实风快速出图_2100816563434770434.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_308

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen2.1摆拍美学文生图，写实构图光影到极致_2112318313169776642.json、图片生成/文生图/不同姿势文生图生成器 美少女写实多姿态处理工具_2114042179948732417.json、图片生成/文生图/古风角色设计｜女频短剧人像写真文生图一键生成_2089772497628655617.json、图片生成/文生图/摆拍美学文生图 摄影级构图画面直出高质量_2108983596869578754.json、图片生成/文生图/摆拍美学文生图V1.1 摄影级构图画面直出_2109183810997932034.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Replace`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `ModelSamplingAuraFlow` —— 4/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `llama_cpp_clean_states` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `QwenImage21Cache` —— 3/7 个有
- `ResolutionSelector` —— 3/7 个有
- `TextEncodeQwenImage21` —— 3/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（15/7 个样本）：Steps较低可能导致细节不足
