---
name: unknown_workflow_sampler_unet_vae_248
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8705
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【qwen2.1短剧资产】图生角色设定图（(目前只支持真人▏无PE）_2102180346572922881.json, 图片生成/图生图/【遇见AI】qwen image 2.1图生图和图片参考基础流_2101841464891367425.json, 图片生成/图生图/一键抠图背景移除-qwen image 2.1_2112444591415848961.json, 图片生成/图生图/换装-Qwen Image 2.1-图像编辑_2101859929576534017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_248

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【qwen2.1短剧资产】图生角色设定图（(目前只支持真人▏无PE）_2102180346572922881.json、图片生成/图生图/【遇见AI】qwen image 2.1图生图和图片参考基础流_2101841464891367425.json、图片生成/图生图/一键抠图背景移除-qwen image 2.1_2112444591415848961.json、图片生成/图生图/换装-Qwen Image 2.1-图像编辑_2101859929576534017.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ImageCompare` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `easy boolean` —— 1/4 个有
- `easy float` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
