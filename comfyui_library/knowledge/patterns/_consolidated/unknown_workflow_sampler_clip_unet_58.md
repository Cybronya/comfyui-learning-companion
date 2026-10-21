---
name: unknown_workflow_sampler_clip_unet_58
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.749556
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [ImageCrop+, easy imageSplitGrid, easy imagesSplitImage, LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1907499231920156674.json, 图片生成/文生图/1908149869620375554.json, 图片生成/文生图/1908549630693679105.json, 图片生成/文生图/1908700798354599938.json, 图片生成/文生图/1908846681855504386.json, 图片生成/文生图/1925132068681150465.json, 图片生成/文生图/1943617599785607170.json, 图片生成/文生图/1968322626772979714.json, 图片生成/文生图/文生四宫格图_2060284327476416514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_58

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1907499231920156674.json、图片生成/文生图/1908149869620375554.json、图片生成/文生图/1908549630693679105.json、图片生成/文生图/1908700798354599938.json、图片生成/文生图/1908846681855504386.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `EmptyLatentImage` —— 6/9 个有
- `easy imageSplitGrid` —— 5/9 个有
- `easy imagesSplitImage` —— 5/9 个有
- `FluxGuidance` —— 4/9 个有
- `ModelSamplingFlux` —— 4/9 个有
- `EmptySD3LatentImage` —— 3/9 个有
- `CheckpointLoaderSimple` —— 2/9 个有
- `UnetLoaderGGUF` —— 2/9 个有
- `ImageCrop+` —— 1/9 个有
- `LatentToWidthHeight` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2048 | 6 | 65% |
| 高度 | 1440 | 1024 - 1728 | 6 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2048，6 个样本
- 高度 中位数 1440，观测区间 1024 - 1728，6 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：ImageCrop+、easy imageSplitGrid、easy imagesSplitImage、LayerUtility: PurgeVRAM V2
