---
name: text_to_image_sampler_clip_unet_65
type: Text To Image
frequency: 10
level: strong
coverage: 0.8216
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2文生图+SeedVR2高清放大_2079590934051901442.json, 图片生成/文生图/Qwen3超强图片反推_2043616761685221378.json, 图片生成/文生图/Z-Image + 4K超清放大_1995496468943396865.json, 图片生成/文生图/Z-Image+lora测试工作流_2027762368310157313.json, 图片生成/文生图/Z-Image-跑场景图-v3.0_2044237946076794881.json, 图片生成/文生图/Z-Image-跑场景图-v4.0_2044957910106640386.json, 图片生成/文生图/Z-Image-跑场景图_2037100091957317634.json, 图片生成/文生图/Z-image-Art 文生图+高清放大_2017835536668434434.json, 图片生成/文生图/Z-image绝世美女人物一致性lora和工作流，高清美女图适合抖音、快手等自媒体平台_1995357519012880385.json, 图片生成/文生图/小而美图像模型：文生图_1995813775376789506.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_65

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Krea2文生图+SeedVR2高清放大_2079590934051901442.json、图片生成/文生图/Qwen3超强图片反推_2043616761685221378.json、图片生成/文生图/Z-Image + 4K超清放大_1995496468943396865.json、图片生成/文生图/Z-Image+lora测试工作流_2027762368310157313.json、图片生成/文生图/Z-Image-跑场景图-v3.0_2044237946076794881.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `SeedVR2LoadDiTModel` —— 9/10 个有
- `SeedVR2LoadVAEModel` —— 9/10 个有
- `SeedVR2VideoUpscaler` —— 9/10 个有
- `Image Comparer (rgthree)` —— 8/10 个有
- `ImageScaleBy` —— 8/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `ImpactInt` —— 5/10 个有
- `PrimitiveInt` —— 2/10 个有
- `JoinStringMulti` —— 1/10 个有
- `KepStringLiteral` —— 1/10 个有
- `LoraLoader` —— 1/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `TextInputNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 10 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1500 | 720 - 1920 | 10 | 68% |
| 高度 | 1180 | 1080 - 1920 | 10 | 74% |
| LoRA 模型强度 | 2.1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，10 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1500，观测区间 720 - 1920，10 个样本
- 高度 中位数 1180，观测区间 1080 - 1920，10 个样本
