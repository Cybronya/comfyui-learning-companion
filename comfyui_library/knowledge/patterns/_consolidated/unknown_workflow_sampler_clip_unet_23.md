---
name: unknown_workflow_sampler_clip_unet_23
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.813111
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy imageSplitGrid, easy imagesSplitImage]
members: [图片生成/文生图/1906689471180419073.json, 图片生成/文生图/1907035068605292545.json, 图片生成/文生图/1907048220537544706.json, 图片生成/文生图/1908549630693679105.json, 图片生成/文生图/1908700798354599938.json, 图片生成/文生图/1908846681855504386.json, 图片生成/文生图/1910653440345997314.json, 图片生成/文生图/1925132068681150465.json, 图片生成/文生图/1943617599785607170.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_23

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1906689471180419073.json、图片生成/文生图/1907035068605292545.json、图片生成/文生图/1907048220537544706.json、图片生成/文生图/1908549630693679105.json、图片生成/文生图/1908700798354599938.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/9 个有
- `PreviewImage` —— 6/9 个有
- `easy imageSplitGrid` —— 5/9 个有
- `easy imagesSplitImage` —— 5/9 个有
- `RH_Translator` —— 2/9 个有
- `CheckpointLoaderSimple` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `JjkShowText` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `UltimateSDUpscale` —— 1/9 个有
- `UpscaleModelLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 2048 | 9 | 60% |
| 高度 | 1152 | 512 - 1728 | 9 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 2048，9 个样本
- 高度 中位数 1152，观测区间 512 - 1728，9 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageSplitGrid、easy imagesSplitImage
