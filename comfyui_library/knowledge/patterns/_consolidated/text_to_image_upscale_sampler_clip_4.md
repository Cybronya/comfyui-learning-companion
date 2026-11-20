---
name: text_to_image_upscale_sampler_clip_4
type: Text To Image
frequency: 14
level: moderate
coverage: 0.795786
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json, 图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json, 图片生成/文生图/Krea2 lora+高清放大基础工作流_2089602538793422849.json, 图片生成/文生图/Krea2基础生图+ SeedVR 4K 超清放大_2082094625946431490.json, 图片生成/文生图/Z-Image短剧拍档支持场景和角色_2055879009824722945.json, 图片生成/文生图/Z-image文生图+直逼真实摄影+最新seedvr2高清放大工作流_1994801677821730818.json, 图片生成/文生图/z_image 角色资产制作+如梦似幻 超绝美感+SEEDVR2放大_2112395440854487041.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色（私用）_2105937314986946562.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色_2098950780144410625.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色_2099062438128869377.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色【AI创客训练营】画布功能_角色_2114192879651479553.json, 图片生成/文生图/瑶光 zimage出图_2056391963225706497.json, 视频生成/文生视频/极致电影4K美学-Krea2基础生图++SeedVR+4K+超清放大-极氪白白酱_2082122814294937602.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json、图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json、图片生成/文生图/Krea2 lora+高清放大基础工作流_2089602538793422849.json、图片生成/文生图/Krea2基础生图+ SeedVR 4K 超清放大_2082094625946431490.json、图片生成/文生图/Z-Image短剧拍档支持场景和角色_2055879009824722945.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 12/14 个有
- `Image Comparer (rgthree)` —— 12/14 个有
- `LoraLoaderModelOnly` —— 12/14 个有
- `PreviewImage` —— 12/14 个有
- `Fast Groups Bypasser (rgthree)` —— 9/14 个有
- `CR Text` —— 7/14 个有
- `ConditioningZeroOut` —— 6/14 个有
- `EmptyImage` —— 4/14 个有
- `CR Prompt Text` —— 3/14 个有
- `GetNode` —— 2/14 个有
- `Lora Loader Stack (rgthree)` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `Int` —— 1/14 个有
- `TTResolutionSelector` —— 1/14 个有
- `easy promptLine` —— 1/14 个有
- `孤海注释` —— 1/14 个有
- `忽略多组孤海` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 512 - 2048 | 14 | 69% |
| 高度 | 1920 | 512 - 1920 | 14 | 72% |
| 采样步数 | 8 | 8 - 10 | 14 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | res_2s_ode | - | 14 | 57% |
| 调度器 | kl_optimal | - | 14 | 57% |
| 重绘幅度 | 1 | 0.58 - 1 | 14 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 512 - 2048，14 个样本
- 高度 中位数 1920，观测区间 512 - 1920，14 个样本
- 采样步数 中位数 8，观测区间 8 - 10，14 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s_ode，14 个样本，一致性 57%
- 调度器 最常用 kl_optimal，14 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.58 - 1，14 个样本，取值集中（一致性 89%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
