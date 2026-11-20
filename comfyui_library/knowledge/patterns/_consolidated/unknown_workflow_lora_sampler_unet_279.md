---
name: unknown_workflow_lora_sampler_unet_279
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.808667
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Qwen Image2.1——精准抠图丨移除遮挡丨完美PNG通道_2108501418909986817.json, 平台全量/人像精修-原生肌肤 qwen_image_2.1_1900186985972101122.json, 平台全量/心宝3S半透明材质抠图完美半透明PNG通道_2109898358209990658.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_279

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Qwen Image2.1——精准抠图丨移除遮挡丨完美PNG通道_2108501418909986817.json、平台全量/人像精修-原生肌肤 qwen_image_2.1_1900186985972101122.json、平台全量/心宝3S半透明材质抠图完美半透明PNG通道_2109898358209990658.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `StringToAnyNode` —— 2/3 个有
- `XinbaoImageStandardizer` —— 2/3 个有
- `easy boolean` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Replace` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 25 - 40 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 3 | 43% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 25 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，3 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
