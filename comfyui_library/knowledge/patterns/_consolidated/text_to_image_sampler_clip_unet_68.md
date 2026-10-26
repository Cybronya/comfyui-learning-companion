---
name: text_to_image_sampler_clip_unet_68
type: Text To Image
frequency: 10
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/（fg-Lora）Z-image Engineer V4-文生图V2（3000步）_2028626642955935746.json, 图片生成/文生图/（小情绪版）Z-image文生图V1_1999752612872417281.json, 图片生成/文生图/（自用-zhenzhen）Z-image-turbo文生图2K版_2019482059055566849.json, 图片生成/文生图/（自用）成人摄影Z-image文生图2K版_1993954086909313026.json, 图片生成/文生图/（贞贞-小情绪版）Z-Image 文生图V1_2001331257915080706.json, 图片生成/文生图/（贞贞-小情绪版）Z-image文生图V1_1999750941198909441.json, 图片生成/文生图/（贞贞Lora）Z-image Engineer V4& Flow Dop文生图V2（11000步）_2028503409036365825.json, 图片生成/文生图/（贞贞Lora）Z-image文生图V2（11000步）_1996234333444775938.json, 图片生成/文生图/（贞贞Lora）Z-image文生图V2（24000步）_1996258756096835586.json, 图片生成/文生图/（贞贞Lora）Z-image文生图V2（4500步）_1994676967016439809.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_68

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/（fg-Lora）Z-image Engineer V4-文生图V2（3000步）_2028626642955935746.json、图片生成/文生图/（小情绪版）Z-image文生图V1_1999752612872417281.json、图片生成/文生图/（自用-zhenzhen）Z-image-turbo文生图2K版_2019482059055566849.json、图片生成/文生图/（自用）成人摄影Z-image文生图2K版_1993954086909313026.json、图片生成/文生图/（贞贞-小情绪版）Z-Image 文生图V1_2001331257915080706.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `easy promptLine` —— 9/10 个有
- `CLIPLoader` —— 8/10 个有
- `ClipLoaderGGUF` —— 2/10 个有
- `DuckHideNode` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有
- `TT_img_enc_v2` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1500 | 1080 - 1920 | 10 | 72% |
| 高度 | 1500 | 1080 - 1920 | 10 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1500，观测区间 1080 - 1920，10 个样本
- 高度 中位数 1500，观测区间 1080 - 1920，10 个样本
