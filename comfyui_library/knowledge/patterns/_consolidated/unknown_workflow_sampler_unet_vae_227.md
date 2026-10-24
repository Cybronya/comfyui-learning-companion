---
name: unknown_workflow_sampler_unet_vae_227
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.667
common_nodes: [CLIPLoader, DrawMaskOnImage, EmptyLatentImage, GetNode, KSampler, LoadImage, PreviewImage, QwenImage21Cache, ResizeImageMaskNode, ResolutionSelector, SaveImage, SaveImageAdvanced, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 元素移除_2101986892471431170.json, 图片生成/图生图/Qwen Image 2.1 扩图_2101987076421021697.json, 图片生成/图生图/Qwen Image 2.1 扩图_2102016833665724417.json, 图片生成/图生图/Qwen Image 2.1 扩图工作流_2102621542323675137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_227

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 元素移除_2101986892471431170.json、图片生成/图生图/Qwen Image 2.1 扩图_2101987076421021697.json、图片生成/图生图/Qwen Image 2.1 扩图_2102016833665724417.json、图片生成/图生图/Qwen Image 2.1 扩图工作流_2102621542323675137.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `QwenImage21Cache`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `ImagePadForOutpaint` —— 3/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `ResizeMask` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 50 | 50 - 50 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 50 - 50，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
