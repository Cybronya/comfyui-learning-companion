---
name: text_to_image_upscale_lora_sampler_11
type: Text To Image
frequency: 12
level: moderate
coverage: 0.738583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/小红书 FireRed-V1.1虚拟换装_2041129593666539522.json, 图片生成/文生图/AI代码侠土豆 瑶光电商图专用_换产品_衣服_2034897021122908162.json, 图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json, 图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json, 图片生成/文生图/Krea2 lora+高清放大基础工作流_2089602538793422849.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色（私用）_2105937314986946562.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色_2098950780144410625.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色_2099062438128869377.json, 图片生成/文生图/瑶光 zimage出图_2056391963225706497.json, 图片生成/文生图/电商图专用_换产品_衣服_2039333002022490113.json, 图片生成/文生图/电商图专用_换产品_衣服_2041164747680260098.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/小红书 FireRed-V1.1虚拟换装_2041129593666539522.json、图片生成/文生图/AI代码侠土豆 瑶光电商图专用_换产品_衣服_2034897021122908162.json、图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json、图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json、图片生成/文生图/Krea2 lora+高清放大基础工作流_2089602538793422849.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 10/12 个有
- `ImageScaleToTotalPixels` —— 8/12 个有
- `ConditioningZeroOut` —— 7/12 个有
- `INTConstant` —— 7/12 个有
- `Image Comparer (rgthree)` —— 7/12 个有
- `PreviewImage` —— 6/12 个有
- `CR Text` —— 5/12 个有
- `GetNode` —— 5/12 个有
- `SetNode` —— 5/12 个有
- `TTResolutionSelector` —— 5/12 个有
- `LoadImage` —— 4/12 个有
- `Text` —— 4/12 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/12 个有
- `easy imageSizeBySide` —— 4/12 个有
- `EmptyImage` —— 3/12 个有
- `ImageResize+` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 512 - 1080 | 12 | 67% |
| 高度 | 1920 | 512 - 1920 | 12 | 48% |
| 采样步数 | 8 | 8 - 8 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | res_2s_ode | - | 12 | 42% |
| 调度器 | kl_optimal | - | 12 | 42% |
| 重绘幅度 | 1 | 0.58 - 1 | 12 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 512 - 1080，12 个样本
- 高度 中位数 1920，观测区间 512 - 1920，12 个样本，取值分散，一致性仅 48%
- 采样步数 中位数 8，观测区间 8 - 8，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s_ode，12 个样本，一致性 42%
- 调度器 最常用 kl_optimal，12 个样本，一致性 42%
- 重绘幅度 中位数 1，观测区间 0.58 - 1，12 个样本，取值集中（一致性 88%）
- 高发问题（17/12 个样本）：Steps较低可能导致细节不足
