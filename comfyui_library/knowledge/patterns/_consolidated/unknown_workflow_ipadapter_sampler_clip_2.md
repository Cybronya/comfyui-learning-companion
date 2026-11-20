---
name: unknown_workflow_ipadapter_sampler_clip_2
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.78575
common_nodes: [ApplyFluxIPAdapter, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, ImageScale, LoadFluxIPAdapter, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/图生图/多图风格融合  Flux+IPAdapter_1915051485367889922.json, 图片生成/文生图/Flux+IPAdapter 文生同风格图片_1914704276978106370.json, 平台全量/Flux模型+IPAdapter-胖喵_1828743948205740033.json, 平台全量/图生图风格迁移（Flux+IPAdapter）_1828978179221450754.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/多图风格融合  Flux+IPAdapter_1915051485367889922.json、图片生成/文生图/Flux+IPAdapter 文生同风格图片_1914704276978106370.json、平台全量/Flux模型+IPAdapter-胖喵_1828743948205740033.json、平台全量/图生图风格迁移（Flux+IPAdapter）_1828978179221450754.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyFluxIPAdapter`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ImageScale`
- `LoadFluxIPAdapter`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `DisplayText_Zho` —— 1/4 个有
- `ImpactMakeImageBatch` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 896 | 504 - 1024 | 4 | 74% |
| 高度 | 1024 | 512 - 1024 | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 504 - 1024，4 个样本
- 高度 中位数 1024，观测区间 512 - 1024，4 个样本
