---
name: text_to_image_upscale_sampler_clip_23
type: Text To Image
frequency: 5
level: strong
coverage: 0.846
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image绝世美女人物一致性lora和工作流，高清美女图适合抖音、快手等自媒体平台_1995357519012880385.json, 图片生成/文生图/Zimage_瑶光_2095722755646902273.json, 图片生成/文生图/zimage图像修复放大_2032377992323801090.json, 图片生成/文生图/小而美图像模型：文生图_1995813775376789506.json, 图片生成/文生图/阿里开源 Z-IMAGE 图像生成模型 + SeedVR2洗图高清放大工作流_1994282214103990274.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image绝世美女人物一致性lora和工作流，高清美女图适合抖音、快手等自媒体平台_1995357519012880385.json、图片生成/文生图/Zimage_瑶光_2095722755646902273.json、图片生成/文生图/zimage图像修复放大_2032377992323801090.json、图片生成/文生图/小而美图像模型：文生图_1995813775376789506.json、图片生成/文生图/阿里开源 Z-IMAGE 图像生成模型 + SeedVR2洗图高清放大工作流_1994282214103990274.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleBy`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImpactInt` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Text` —— 2/5 个有
- `JoinStringMulti` —— 1/5 个有
- `KepStringLiteral` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 720 - 1920 | 5 | 66% |
| 高度 | 1280 | 1080 - 1920 | 5 | 74% |
| 采样步数 | 10 | 8 - 10 | 5 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 720 - 1920，5 个样本
- 高度 中位数 1280，观测区间 1080 - 1920，5 个样本
- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
