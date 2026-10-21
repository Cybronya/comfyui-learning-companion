---
name: unknown_workflow_lora_sampler_clip_128
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.853333
common_nodes: [CLIPLoaderGGUF, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Int, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/文生图/Zimage随机美少女抽卡机【无限出图模式】_2059903175817252865.json, 图片生成/文生图/z-image真实人像（带反推和扩写）_2064352102926868481.json, 图片生成/文生图/美女孵蛋器 V3升级版【无限模式】_2073460891844177921.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_128

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Zimage随机美少女抽卡机【无限出图模式】_2059903175817252865.json、图片生成/文生图/z-image真实人像（带反推和扩写）_2064352102926868481.json、图片生成/文生图/美女孵蛋器 V3升级版【无限模式】_2073460891844177921.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Int`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `DapaoImageAspectRatioResizeNode` —— 2/3 个有
- `DapaoImageRatioLimitNode` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `DapaoImageWatermarkNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 864 | 864 - 1024 | 3 | 92% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 12 | 3 | 29% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 864，观测区间 864 - 1024，3 个样本，取值集中（一致性 92%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 12，3 个样本，取值分散，一致性仅 29%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
