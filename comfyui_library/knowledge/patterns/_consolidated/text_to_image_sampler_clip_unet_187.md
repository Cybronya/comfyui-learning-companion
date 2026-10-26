---
name: text_to_image_sampler_clip_unet_187
type: Text To Image
frequency: 3
level: strong
coverage: 0.852667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, EmptyLatentImage, Int, JjkText, KSampler, RH_Translator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima_base+1.0+文生图 anima 动漫王者文生图_2057276484787720193.json, 图片生成/文生图/Anima_base+1.0+文生图_2069591838113226754.json, 图片生成/文生图/anima_base 1.0 文生图_1888839342318870529.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_187

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Anima_base+1.0+文生图 anima 动漫王者文生图_2057276484787720193.json、图片生成/文生图/Anima_base+1.0+文生图_2069591838113226754.json、图片生成/文生图/anima_base 1.0 文生图_1888839342318870529.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `Int`
- `JjkText`
- `KSampler`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 2048 | 2048 - 2048 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，观测区间 2048 - 2048，3 个样本，取值集中（一致性 100%）
