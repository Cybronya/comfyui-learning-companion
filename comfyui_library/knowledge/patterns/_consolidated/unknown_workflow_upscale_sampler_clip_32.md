---
name: unknown_workflow_upscale_sampler_clip_32
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.848
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxSamplerParams+, Image Comparer (rgthree), SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/高清放大4K_2092084125342724098.json, 图片生成/图生图/高清放大4K_2092528398777282562.json, 图片生成/文生图/FLUX-fp8出图-高清放大_2004950309392838658.json, 图片生成/文生图/高清放大4K_2015373674332823554.json, 图片生成/文生图/高清放大4K_2091148212773146625.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/高清放大4K_2092084125342724098.json、图片生成/图生图/高清放大4K_2092528398777282562.json、图片生成/文生图/FLUX-fp8出图-高清放大_2004950309392838658.json、图片生成/文生图/高清放大4K_2015373674332823554.json、图片生成/文生图/高清放大4K_2091148212773146625.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxSamplerParams+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `LoraLoader` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
