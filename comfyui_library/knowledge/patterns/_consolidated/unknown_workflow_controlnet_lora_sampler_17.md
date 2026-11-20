---
name: unknown_workflow_controlnet_lora_sampler_17
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.954667
common_nodes: [AIO_Preprocessor, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.1-controlnet工作流_2088611300489392130.json, 图片生成/图生图/Flux.1+ controlnet工作流_2109991263348019202.json, 图片生成/文生图/F.1一键毛坯变精装工作流 Bot_LXX V3.0_1930576899993686018.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX.1-controlnet工作流_2088611300489392130.json、图片生成/图生图/Flux.1+ controlnet工作流_2109991263348019202.json、图片生成/文生图/F.1一键毛坯变精装工作流 Bot_LXX V3.0_1930576899993686018.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SetUnionControlNetType` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.6 | 0.38 - 0.6 | 3 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，观测区间 0.38 - 0.6，3 个样本，取值集中（一致性 80%）
