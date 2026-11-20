---
name: unknown_workflow_sampler_unet_vae_208
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.828714
common_nodes: [CLIPLoader, EmptyImage, GetImageSizeAndCount, KSampler, SaveImage, SetNode, StringFunction|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json, 图片生成/文生图/生图-文生图自动-Qwen-Image-2.1_2103831634712809474.json, 图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2103796350319157249.json, 图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2108745240646602753.json, 图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2110189318915575810.json, 平台全量/生图-文生图(角色白底图四视图)-Moss_2120439612547096577.json, 平台全量/生图-文生图自动-Moss_2120439602023591937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_208

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json、图片生成/文生图/生图-文生图自动-Qwen-Image-2.1_2103831634712809474.json、图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2103796350319157249.json、图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2108745240646602753.json、图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2110189318915575810.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyImage`
- `GetImageSizeAndCount`
- `KSampler`
- `SaveImage`
- `SetNode`
- `StringFunction|pysssss`
- `Text Multiline`
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
- `EmptyLatentImage` —— 5/7 个有
- `ImpactInt` —— 5/7 个有
- `TextEncodeQwenImage21` —— 5/7 个有
- `TextGenerateLTX2Prompt` —— 5/7 个有
- `GetNode` —— 4/7 个有
- `llama_cpp_instruct_adv` —— 4/7 个有
- `llama_cpp_model_loader` —— 4/7 个有
- `llama_cpp_parameters` —— 4/7 个有
- `RH_LLMAPI_NODE` —— 3/7 个有
- `CLIPTextEncode` —— 2/7 个有
- `DapaoImageRatioLimitNode` —— 2/7 个有
- `EmptyFlux2LatentImage` —— 2/7 个有
- `MOSSMergePreset` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `SkipLayerGuidanceDiTSimple` —— 2/7 个有
- `TextGenerate` —— 2/7 个有
- `easy imageRemBg` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 50 | 50 - 50 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 7 | 43% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 50 - 50，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，7 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
