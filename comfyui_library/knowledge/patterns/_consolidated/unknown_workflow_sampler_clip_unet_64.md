---
name: unknown_workflow_sampler_clip_unet_64
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.932
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/1949869161797345281.json, 图片生成/文生图/1951288327628599298.json, 图片生成/文生图/1952013936583495682.json, 图片生成/文生图/1952185609727234050.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_64

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1949869161797345281.json、图片生成/文生图/1951288327628599298.json、图片生成/文生图/1952013936583495682.json、图片生成/文生图/1952185609727234050.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `JanusImage2Text` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `LoadJanusModel` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 924 | 768 - 1200 | 4 | 80% |
| 高度 | 1360 | 1024 - 1920 | 4 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 924，观测区间 768 - 1200，4 个样本，取值集中（一致性 80%）
- 高度 中位数 1360，观测区间 1024 - 1920，4 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
