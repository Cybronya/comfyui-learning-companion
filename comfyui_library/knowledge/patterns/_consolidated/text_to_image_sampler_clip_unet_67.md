---
name: text_to_image_sampler_clip_unet_67
type: Text To Image
frequency: 7
level: moderate
coverage: 0.862286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima-Base 动漫艺术_2057379324319326210.json, 图片生成/文生图/Anima-Base1.0 动漫文生图_2067514380631240706.json, 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json, 图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2067497247423680513.json, 图片生成/文生图/Anima_base+1.0+文生图_2069591838113226754.json, 图片生成/文生图/Anima动漫文生图_2057367708785790977.json, 图片生成/文生图/anima_base 1.0 文生图_1888839342318870529.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_67

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Anima-Base 动漫艺术_2057379324319326210.json、图片生成/文生图/Anima-Base1.0 动漫文生图_2067514380631240706.json、图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2057295897054236673.json、图片生成/文生图/Anima-Base1.0 动漫文生图（提示词指南）_2067497247423680513.json、图片生成/文生图/Anima_base+1.0+文生图_2069591838113226754.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/7 个有
- `JjkText` —— 4/7 个有
- `RH_Translator` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `CR Text Concatenate` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `LoadImage` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1920 | 7 | 68% |
| 高度 | 1080 | 1024 - 2048 | 7 | 66% |
| 采样步数 | 35 | 30 - 40 | 7 | 87% |
| Prompt 约束强度(CFG) | 4.5 | 4 - 5 | 7 | 91% |
| 采样算法 | er_sde | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1920，7 个样本
- 高度 中位数 1080，观测区间 1024 - 2048，7 个样本
- 采样步数 中位数 35，观测区间 30 - 40，7 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4 - 5，7 个样本，取值集中（一致性 91%）
- 采样算法 最常用 er_sde，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
