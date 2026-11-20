---
name: text_to_image_sampler_clip_unet_176
type: Text To Image
frequency: 4
level: strong
coverage: 0.9755
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: []
missing: []
members: [图片生成/文生图/（自用）成人摄影Z-image文生图2K版_1993954086909313026.json, 图片生成/文生图/（贞贞-小情绪版）Z-image文生图V1_1999750941198909441.json, 图片生成/文生图/（贞贞Lora）Z-image Engineer V4& Flow Dop文生图V2（11000步）_2028503409036365825.json, 图片生成/文生图/（贞贞Lora）Z-image同丹不同配方Lora对比测试_1996261458461736961.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_176

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/（自用）成人摄影Z-image文生图2K版_1993954086909313026.json、图片生成/文生图/（贞贞-小情绪版）Z-image文生图V1_1999750941198909441.json、图片生成/文生图/（贞贞Lora）Z-image Engineer V4& Flow Dop文生图V2（11000步）_2028503409036365825.json、图片生成/文生图/（贞贞Lora）Z-image同丹不同配方Lora对比测试_1996261458461736961.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `AddLabel` —— 1/4 个有
- `ClipLoaderGGUF` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `PDIMAGE_LongerSize` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有
- `TT_img_enc_v2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1920 | 1080 - 1920 | 4 | 79% |
| 高度 | 1080 | 1080 - 1920 | 4 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 1080 - 1920，4 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，4 个样本
