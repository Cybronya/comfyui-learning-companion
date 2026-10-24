---
name: text_to_image_sampler_clip_vae_32
type: Text To Image
frequency: 4
level: strong
coverage: 0.95825
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, NunchakuFluxDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux-kontext一箭双雕文生图_1947462711925952514.json, 图片生成/文生图/双节棍文生图_1934093892570501121.json, 图片生成/文生图/新手-基础工作流-长clip_1951451403174752257.json, 图片生成/文生图/波西米亚卡牌风格 FLUX  Nunchaku_1943499738438397954.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_32

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/flux-kontext一箭双雕文生图_1947462711925952514.json、图片生成/文生图/双节棍文生图_1934093892570501121.json、图片生成/文生图/新手-基础工作流-长clip_1951451403174752257.json、图片生成/文生图/波西米亚卡牌风格 FLUX  Nunchaku_1943499738438397954.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `NunchakuFluxLoraLoader` —— 2/4 个有
- `GoogleTranslateCLIPTextEncodeNode` —— 1/4 个有
- `LongCLIPTextEncodeFlux` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1024 | 4 | 86% |
| 高度 | 1152 | 768 - 1536 | 4 | 75% |
| 采样步数 | 20 | 10 - 25 | 4 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1024，4 个样本，取值集中（一致性 86%）
- 高度 中位数 1152，观测区间 768 - 1536，4 个样本
- 采样步数 中位数 20，观测区间 10 - 25，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
