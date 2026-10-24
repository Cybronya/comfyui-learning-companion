---
name: text_to_image_sampler_clip_unet_104
type: Text To Image
frequency: 7
level: strong
coverage: 0.986
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: []
missing: []
members: [图片生成/文生图/（fg-Lora）Z-image Engineer V4-文生图V2（3000步）_2028626642955935746.json, 图片生成/文生图/（小情绪版）Z-image文生图V1_1999752612872417281.json, 图片生成/文生图/（自用-zhenzhen）Z-image-turbo文生图2K版_2019482059055566849.json, 图片生成/文生图/（自用）成人摄影Z-image文生图2K版_1993954086909313026.json, 图片生成/文生图/（贞贞-小情绪版）Z-image文生图V1_1999750941198909441.json, 图片生成/文生图/（贞贞Lora）Z-image Engineer V4& Flow Dop文生图V2（11000步）_2028503409036365825.json, 图片生成/文生图/（贞贞Lora）Z-image同丹不同配方Lora对比测试_1996261458461736961.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_104

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/（fg-Lora）Z-image Engineer V4-文生图V2（3000步）_2028626642955935746.json、图片生成/文生图/（小情绪版）Z-image文生图V1_1999752612872417281.json、图片生成/文生图/（自用-zhenzhen）Z-image-turbo文生图2K版_2019482059055566849.json、图片生成/文生图/（自用）成人摄影Z-image文生图2K版_1993954086909313026.json、图片生成/文生图/（贞贞-小情绪版）Z-image文生图V1_1999750941198909441.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 6/7 个有
- `CLIPLoader` —— 5/7 个有
- `ClipLoaderGGUF` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `DuckHideNode` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `PDIMAGE_LongerSize` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有
- `TT_img_enc_v2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1920 | 1080 - 1920 | 7 | 73% |
| 高度 | 1080 | 1080 - 1920 | 7 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 1080 - 1920，7 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，7 个样本
