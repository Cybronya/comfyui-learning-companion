---
name: text_to_image_sampler_clip_unet_43
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9457
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image-De-Turbo文生图_1997688531524980738.json, 图片生成/文生图/Z-Image-De文生图(Z-Image脱蒸馏版-效果更好)_1997646136397729793.json, 图片生成/文生图/Z-Image-De文生图_1997873304331517954.json, 图片生成/文生图/Z-Image-Engineer-V4--文生图_2028091411702222850.json, 图片生成/文生图/Z-Image-Turbo + Lora 文生图_2008180292552495105.json, 图片生成/文生图/Z-image D-OPSD文生图_2057839881359020034.json, 图片生成/文生图/Z-image Qwen3 4B Vs Qwen3 4b Z-image Engineer V4_2027773457253011458.json, 图片生成/文生图/Z-image-Turbo电影质感文生图_2056911427314737153.json, 图片生成/文生图/Z-image-turbo Vs flow-dpo对比_2026971124013207554.json, 图片生成/文生图/Z-image-turbo Vs flow-dpo对比工作流 林耀2.27_2027214097611231233.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_43

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Z-Image-De-Turbo文生图_1997688531524980738.json、图片生成/文生图/Z-Image-De文生图(Z-Image脱蒸馏版-效果更好)_1997646136397729793.json、图片生成/文生图/Z-Image-De文生图_1997873304331517954.json、图片生成/文生图/Z-Image-Engineer-V4--文生图_2028091411702222850.json、图片生成/文生图/Z-Image-Turbo + Lora 文生图_2008180292552495105.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 9/10 个有
- `CR Prompt Text` —— 7/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `easy seed` —— 5/10 个有
- `AddLabel` —— 3/10 个有
- `ImageConcanate` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `CLIPLoaderGGUF` —— 2/10 个有
- `Int` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `Qwen3_VQA` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1920 | 10 | 77% |
| 高度 | 1920 | 1080 - 1920 | 10 | 86% |
| 采样步数 | 10 | 10 - 30 | 10 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 10 | 53% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1920，10 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，10 个样本，取值集中（一致性 86%）
- 采样步数 中位数 10，观测区间 10 - 30，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
