---
name: unknown_workflow_sampler_unet_vae_231
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.76575
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, Label (rgthree), LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-2.1 五视图-透明背景_2103379501370658818.json, 图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json, 图片生成/图生图/Qwen-2.1cos角色生活自拍_2104713076036689921.json, 图片生成/图生图/Qwen-2.1多格漫画。_2104722627184128002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_231

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-2.1 五视图-透明背景_2103379501370658818.json、图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json、图片生成/图生图/Qwen-2.1cos角色生活自拍_2104713076036689921.json、图片生成/图生图/Qwen-2.1多格漫画。_2104722627184128002.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/4 个有
- `MultiTextConcatenate` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `CR Prompt List` —— 1/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有
- `PreviewAny` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 25 | 25 - 40 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
