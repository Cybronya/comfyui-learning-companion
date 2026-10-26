---
name: unknown_workflow_sampler_unet_vae_160
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.461714
common_nodes: [CLIPLoader, CM_IntUnaryOperation, GetImageSizeAndCount, GetNode, ImageBatchMulti, ImageLoader, ImageScaleToTotalPixels, KSampler, MemoryCleaner, PreviewImage, SaveImage, SetNode, SimpleMath+, StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy anythingInversedSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-Qwen-Image-2.1_2104090966184517633.json, 图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-qwen-edit-2511_2085948961461985282.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2104076531101425666.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2105574372848263169.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2108011209747423234.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-qwen-edit-2511_2006056375931113474.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-qwen-edit-2511_2066055878555791360.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_160

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-Qwen-Image-2.1_2104090966184517633.json、图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-qwen-edit-2511_2085948961461985282.json、图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2104076531101425666.json、图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2105574372848263169.json、图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2108011209747423234.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CM_IntUnaryOperation`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchMulti`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `MemoryCleaner`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy anythingInversedSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 6/7 个有
- `llama_cpp_model_loader` —— 6/7 个有
- `llama_cpp_parameters` —— 6/7 个有
- `EmptyImage` —— 5/7 个有
- `EmptyLatentImage` —— 5/7 个有
- `ImpactInt` —— 4/7 个有
- `TextEncodeQwenImage21` —— 4/7 个有
- `TextGenerateLTX2Prompt` —— 4/7 个有
- `CFGNorm` —— 3/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `ModelSamplingAuraFlow` —— 3/7 个有
- `TextEncodeQwenImageEditPlus` —— 3/7 个有
- `VAEEncode` —— 3/7 个有
- `Qwen3VL_Advanced` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `ResolutionSelector` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 40 | 10 - 40 | 7 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 10 - 40，7 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
