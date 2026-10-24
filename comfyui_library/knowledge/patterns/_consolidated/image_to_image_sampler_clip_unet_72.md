---
name: image_to_image_sampler_clip_unet_72
type: Image To Image
frequency: 6
level: moderate
coverage: 0.9375
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Krea + Redux 风格迁移工作流_1951121711959879682.json, 图片生成/图生图/Flux Krea 高质量洗图｜图生图_1951092819534487554.json, 图片生成/图生图/Flux Krea图生图_1951057726677917698.json, 图片生成/图生图/Flux+Krea +redux风格迁移_2058127140952035329.json, 图片生成/图生图/Flux图生图 新版Joycaption反推_1945130454674755585.json, 图片生成/图生图/Flux图生图（新版Joycaption反推）_1930696459295850498.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux Krea + Redux 风格迁移工作流_1951121711959879682.json、图片生成/图生图/Flux Krea 高质量洗图｜图生图_1951092819534487554.json、图片生成/图生图/Flux Krea图生图_1951057726677917698.json、图片生成/图生图/Flux+Krea +redux风格迁移_2058127140952035329.json、图片生成/图生图/Flux图生图 新版Joycaption反推_1945130454674755585.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 5/6 个有
- `easy imageConcat` —— 4/6 个有
- `ImageScaleDownToSize` —— 3/6 个有
- `JJC_JoyCaption` —— 3/6 个有
- `RH_Translator` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `CLIPVisionLoader` —— 2/6 个有
- `ReduxAdvanced` —— 2/6 个有
- `StyleModelLoader` —— 2/6 个有
- `LatentUpscale` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 0.6 | 0.3 - 1 | 6 | 54% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 0.6，观测区间 0.3 - 1，6 个样本
