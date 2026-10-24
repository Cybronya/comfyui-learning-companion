---
name: unknown_workflow_sampler_unet_vae_175
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.849333
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1 文生图 影视美学_2101866960572211201.json, 图片生成/文生图/Qwen image 2.1 文生图-V1_2101852626458599426.json, 图片生成/文生图/Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657.json, 图片生成/文生图/Qwen image 2.1 文生图（提示词增强）_2101808005967867905.json, 图片生成/文生图/Qwenimage2.1 文生图工作流_2101837000008622081.json, 图片生成/文生图/qwen2.1 文生图_2102025901952299009.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_175

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1 文生图 影视美学_2101866960572211201.json、图片生成/文生图/Qwen image 2.1 文生图-V1_2101852626458599426.json、图片生成/文生图/Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657.json、图片生成/文生图/Qwen image 2.1 文生图（提示词增强）_2101808005967867905.json、图片生成/文生图/Qwenimage2.1 文生图工作流_2101837000008622081.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `StringConcatenate` —— 2/6 个有
- `LoadImage` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `SaveImageAdvanced` —— 1/6 个有
- `Text Multiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 6 | 90% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 50 | 30 - 50 | 6 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，6 个样本，取值集中（一致性 90%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 30 - 50，6 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
