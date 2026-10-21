---
name: text_to_image_sampler_clip_unet_51
type: Text To Image
frequency: 9
level: strong
coverage: 0.826
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, PreviewImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/手机壁纸批量生成_2070683280311152641.json, 图片生成/文生图/手机壁纸批量生成_2071070906801283073.json, 图片生成/文生图/手机壁纸批量生成_2071084050814685186.json, 图片生成/文生图/手机壁纸量产机_2063857665717133314.json, 图片生成/文生图/最佳中文汉字生成_2075055838858928129.json, 图片生成/文生图/桌面壁纸批量生成_2070681246564446210.json, 图片生成/文生图/桌面壁纸批量生成_2071071853019492353.json, 图片生成/文生图/桌面壁纸批量生成_2071084913327165441.json, 图片生成/文生图/电脑桌面壁纸量产机_2063856244808568833.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_51

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/手机壁纸批量生成_2070683280311152641.json、图片生成/文生图/手机壁纸批量生成_2071070906801283073.json、图片生成/文生图/手机壁纸批量生成_2071084050814685186.json、图片生成/文生图/手机壁纸量产机_2063857665717133314.json、图片生成/文生图/最佳中文汉字生成_2075055838858928129.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SaveImagesToZip` —— 8/9 个有
- `PromptBatchQueue` —— 8/9 个有
- `RH_LLMAPI_NODE` —— 8/9 个有
- `RepeatLatentBatch` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 960 | 720 - 1920 | 9 | 63% |
| 高度 | 1088 | 960 - 1984 | 9 | 69% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 960，观测区间 720 - 1920，9 个样本
- 高度 中位数 1088，观测区间 960 - 1984，9 个样本
