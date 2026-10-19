---
name: text_to_image_sampler_clip_unet_7
type: Text To Image
frequency: 9
level: moderate
coverage: 0.894222
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Text Multiline, LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1951065960218304513.json, 图片生成/文生图/1951153128769040386.json, 图片生成/文生图/1951218791621570562.json, 图片生成/文生图/1951794471434399745.json, 图片生成/文生图/1953071206398365698.json, 图片生成/文生图/1953481264051441666.json, 图片生成/文生图/1962669092442386433.json, 图片生成/文生图/1968285554058113025.json, 图片生成/文生图/F.1 在线生图-文生图_1873981103047315457.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1951065960218304513.json、图片生成/文生图/1951153128769040386.json、图片生成/文生图/1951218791621570562.json、图片生成/文生图/1951794471434399745.json、图片生成/文生图/1953071206398365698.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 6/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `Text Multiline` —— 4/9 个有
- `FluxGuidance` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `ApplyFBCacheAndSkipBlocks` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1280 | 9 | 81% |
| 高度 | 1536 | 720 - 1920 | 9 | 67% |
| 采样步数 | 20 | 10 - 30 | 9 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 9 | 39% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1280，9 个样本，取值集中（一致性 81%）
- 高度 中位数 1536，观测区间 720 - 1920，9 个样本
- 采样步数 中位数 20，观测区间 10 - 30，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、LayerUtility: PurgeVRAM V2
