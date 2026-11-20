---
name: unknown_workflow_sampler_unet_vae_217
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.839
common_nodes: [CLIPLoader, EmptyImage, EmptyLatentImage, GetImageSizeAndCount, ImpactInt, KSampler, SaveImage, SetNode, StringFunction|pysssss, Text Multiline, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json, 图片生成/文生图/生图-文生图自动-Qwen-Image-2.1_2103831634712809474.json, 图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2103796350319157249.json, 图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2108745240646602753.json, 图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2110189318915575810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_217

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json、图片生成/文生图/生图-文生图自动-Qwen-Image-2.1_2103831634712809474.json、图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2103796350319157249.json、图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2108745240646602753.json、图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2110189318915575810.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImpactInt`
- `KSampler`
- `SaveImage`
- `SetNode`
- `StringFunction|pysssss`
- `Text Multiline`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `llama_cpp_parameters` —— 2/5 个有
- `DapaoImageRatioLimitNode` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 50 | 50 - 50 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 50 - 50，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
