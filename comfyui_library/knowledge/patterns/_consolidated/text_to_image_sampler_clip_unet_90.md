---
name: text_to_image_sampler_clip_unet_90
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7764
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy cleanGpuUsed, easy textSwitch]
members: [图片生成/文生图/1980137914665439234.json, 图片生成/文生图/Anima文生图精简版+全节点注释_2059139633056931841.json, 图片生成/文生图/QWEN3反推提示+Z-image图生图_1995786213816676354.json, 图片生成/文生图/QWEN3反推提示词+Z-image图生图123_1999891271516815361.json, 图片生成/文生图/文生图精简版+全节点注释_2067404118905409537.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_90

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1980137914665439234.json、图片生成/文生图/Anima文生图精简版+全节点注释_2059139633056931841.json、图片生成/文生图/QWEN3反推提示+Z-image图生图_1995786213816676354.json、图片生成/文生图/QWEN3反推提示词+Z-image图生图123_1999891271516815361.json、图片生成/文生图/文生图精简版+全节点注释_2067404118905409537.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL_Advanced` —— 3/5 个有
- `Int` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `easy textSwitch` —— 3/5 个有
- `PreviewImage` —— 1/5 个有
- `SeedVR2GGUF` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1024 - 1536 | 5 | 81% |
| 高度 | 1024 | 1024 - 1536 | 5 | 80% |
| 采样步数 | 28 | 10 - 40 | 5 | 50% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4.5 | 5 | 47% |
| 采样算法 | euler_ancestral | - | 5 | 40% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1024 - 1536，5 个样本，取值集中（一致性 81%）
- 高度 中位数 1024，观测区间 1024 - 1536，5 个样本
- 采样步数 中位数 28，观测区间 10 - 40，5 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、easy textSwitch
