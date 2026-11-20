---
name: unknown_workflow_sampler_unet_vae_204
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.832571
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1 文生图 影视美学_2101866960572211201.json, 图片生成/文生图/Qwen image 2.1 文生图-V1_2101852626458599426.json, 图片生成/文生图/Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657.json, 图片生成/文生图/Qwen image 2.1 文生图（提示词增强）_2101808005967867905.json, 图片生成/文生图/Qwen-Image-2.1 文生图增强版_2116371963533946882.json, 图片生成/文生图/Qwenimage2.1 文生图工作流_2101837000008622081.json, 数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_204

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1 文生图 影视美学_2101866960572211201.json、图片生成/文生图/Qwen image 2.1 文生图-V1_2101852626458599426.json、图片生成/文生图/Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657.json、图片生成/文生图/Qwen image 2.1 文生图（提示词增强）_2101808005967867905.json、图片生成/文生图/Qwen-Image-2.1 文生图增强版_2116371963533946882.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 6/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `LoadImage` —— 3/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `SaveImageAdvanced` —— 2/7 个有
- `StringConcatenate` —— 2/7 个有
- `BatchImagesNode` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `QwenImage21Cache` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 50 | 25 - 50 | 7 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 25 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
