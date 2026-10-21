---
name: unknown_workflow_sampler_clip_unet_154
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85875
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxSamplerParams+, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX-fp8出图-高清放大_2004950309392838658.json, 图片生成/文生图/文生图生成精美的手工设计图_1892852557050777602.json, 图片生成/文生图/高清放大4K_2015373674332823554.json, 图片生成/文生图/高清放大4K_2091148212773146625.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_154

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX-fp8出图-高清放大_2004950309392838658.json、图片生成/文生图/文生图生成精美的手工设计图_1892852557050777602.json、图片生成/文生图/高清放大4K_2015373674332823554.json、图片生成/文生图/高清放大4K_2091148212773146625.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxSamplerParams+`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `UltimateSDUpscale` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `LoadImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `LoraLoader` —— 1/4 个有
- `Note _O` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
