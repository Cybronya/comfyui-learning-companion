---
name: unknown_workflow_sampler_unet_vae_85
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.782444
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1文生图_2101860458935439362.json, 图片生成/文生图/Qwen image 2.1文生图_2102442182849421314.json, 图片生成/文生图/Qwen image 2.1文生图_2102591785762639873.json, 图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json, 图片生成/文生图/Qwen-Image-2.1 ComfyUI 原生工作流示例_2101898468049645569.json, 图片生成/文生图/Qwen-Image-2.1 文生图_2102343034200477698.json, 图片生成/文生图/Qwen-Image-2.1 文生图_2102996517320740865.json, 图片生成/文生图/Qwen-Image-2.1-T2I_2102034536937902081.json, 图片生成/文生图/Qwen-image2.1文生图工作流_2101888147331305473.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_85

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1文生图_2101860458935439362.json、图片生成/文生图/Qwen image 2.1文生图_2102442182849421314.json、图片生成/文生图/Qwen image 2.1文生图_2102591785762639873.json、图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json、图片生成/文生图/Qwen-Image-2.1 ComfyUI 原生工作流示例_2101898468049645569.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextGenerateLTX2Prompt` —— 5/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `Text` —— 3/9 个有
- `孤海注释` —— 3/9 个有
- `easy showAnything` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `TextGenerate` —— 1/9 个有
- `easy promptList` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 25 - 50 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 9 | 100% |
| 高度 | 1024 | 1024 - 1024 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 25 - 50，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
