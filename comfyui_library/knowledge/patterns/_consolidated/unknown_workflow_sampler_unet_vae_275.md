---
name: unknown_workflow_sampler_unet_vae_275
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.79
common_nodes: [CLIPLoader, CR Text, CR Text Replace, EmptyLatentImage, JDCN_StringToList, KSampler, LoadImage, PrimitiveInt, ProcessString, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/Qwen2.1摆拍美学文生图极致_2111870447930400769.json, 图片生成/文生图/摆拍美学文生图V1.1_2108522154689122305.json, 图片生成/文生图/摆拍美学文生图_2108391724740595714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_275

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen2.1摆拍美学文生图极致_2111870447930400769.json、图片生成/文生图/摆拍美学文生图V1.1_2108522154689122305.json、图片生成/文生图/摆拍美学文生图_2108391724740595714.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `CR Text Replace`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LoadImage`
- `PrimitiveInt`
- `ProcessString`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
