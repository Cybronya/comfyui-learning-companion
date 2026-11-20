---
name: text_to_image_sampler_clip_checkpoint_7
type: Text To Image
frequency: 12
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/SDXL文生图基础 by Mae_1965622186373468162.json, 图片生成/文生图/SDXL文生图工作流_2110984780241260546.json, 图片生成/文生图/SD_1971226483622658049.json, 图片生成/文生图/XL文生图基础款_1946346552236339202.json, 图片生成/文生图/Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209.json, 图片生成/文生图/chai·文生图工作流_1904438332934520833.json, 图片生成/文生图/clip简易图片_2108889381011550210.json, 图片生成/文生图/controlnet文生图SD_2096536231768317953.json, 图片生成/文生图/generate_image_2069748514313293826.json, 图片生成/文生图/jiami_test_2040045480884838401.json, 图片生成/文生图/new01_2046592687888928769.json, 图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/SDXL文生图基础 by Mae_1965622186373468162.json、图片生成/文生图/SDXL文生图工作流_2110984780241260546.json、图片生成/文生图/SD_1971226483622658049.json、图片生成/文生图/XL文生图基础款_1946346552236339202.json、图片生成/文生图/Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/12 个有
- `FaceRestoreCFWithModel` —— 1/12 个有
- `FaceRestoreModelLoader` —— 1/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有
- `PathchSageAttentionKJ` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1920 | 12 | 57% |
| 高度 | 1024 | 512 - 1536 | 12 | 68% |
| 采样步数 | 20 | 10 - 30 | 12 | 74% |
| Prompt 约束强度(CFG) | 7.765 | 1 - 8 | 12 | 59% |
| 采样算法 | euler | - | 12 | 58% |
| 调度器 | simple | - | 12 | 42% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1920，12 个样本
- 高度 中位数 1024，观测区间 512 - 1536，12 个样本
- 采样步数 中位数 20，观测区间 10 - 30，12 个样本
- Prompt 约束强度(CFG) 中位数 7.765，观测区间 1 - 8，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 58%
- 调度器 最常用 simple，12 个样本，一致性 42%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
