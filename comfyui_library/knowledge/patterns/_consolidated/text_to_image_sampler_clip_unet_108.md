---
name: text_to_image_sampler_clip_unet_108
type: Text To Image
frequency: 7
level: moderate
coverage: 0.920571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-image-edit-2059图像编辑_1973209775687208961.json, 图片生成/文生图/Z-Anime-动漫文生图_2049110641390129153.json, 图片生成/文生图/Z-image文生图_1994684914001977346.json, 图片生成/文生图/千问qwen-2512文生图（自定义尺寸）_2083196882171547649.json, 图片生成/文生图/文生图简单实用、真人、快速_2114370405342474242.json, 图片生成/文生图/极简中文生图工作流_2070152864193925122.json, 视频生成/文生视频/Boogu-Image Base 文生图工作流_2067856528262127617.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_108

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen-image-edit-2059图像编辑_1973209775687208961.json、图片生成/文生图/Z-Anime-动漫文生图_2049110641390129153.json、图片生成/文生图/Z-image文生图_1994684914001977346.json、图片生成/文生图/千问qwen-2512文生图（自定义尺寸）_2083196882171547649.json、图片生成/文生图/文生图简单实用、真人、快速_2114370405342474242.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

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
- `PreviewImage` —— 6/7 个有
- `TextEncodeQwenImageEditPlus` —— 2/7 个有
- `AIO_Preprocessor` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `ImageStitch` —— 1/7 个有
- `LoadImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1920 | 7 | 63% |
| 高度 | 1024 | 720 - 1288 | 7 | 83% |
| 采样步数 | 10 | 4 - 35 | 7 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 35% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1920，7 个样本
- 高度 中位数 1024，观测区间 720 - 1288，7 个样本，取值集中（一致性 83%）
- 采样步数 中位数 10，观测区间 4 - 35，7 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
