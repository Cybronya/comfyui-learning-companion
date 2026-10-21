---
name: unknown_workflow_lora_sampler_clip_89
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.81175
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CheckpointLoaderSimple, EmptyLatentImage, Int, InversionDemoLazyIndexSwitch, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Z-image Base+Turbo 双采样 文生图 高级工作流_2041740734788800513.json, 图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图 图生图洗图_2044650703913750529.json, 图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图_2052366719192186882.json, 图片生成/文生图/多样性超写实文生图_2052923543083597826.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_89

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image Base+Turbo 双采样 文生图 高级工作流_2041740734788800513.json、图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图 图生图洗图_2044650703913750529.json、图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图_2052366719192186882.json、图片生成/文生图/多样性超写实文生图_2052923543083597826.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Int`
- `InversionDemoLazyIndexSwitch`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `LayerFilter: HDREffects` —— 1/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 5.5 | 3 - 8 | 4 | 55% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |
| 宽度 | 992 | 960 - 1536 | 4 | 78% |
| 高度 | 1536 | 960 - 1536 | 4 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 5.5，观测区间 3 - 8，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 宽度 中位数 992，观测区间 960 - 1536，4 个样本
- 高度 中位数 1536，观测区间 960 - 1536，4 个样本，取值集中（一致性 82%）
