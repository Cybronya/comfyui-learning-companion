---
name: text_to_image_upscale_sampler_clip_8
type: Text To Image
frequency: 12
level: moderate
coverage: 0.86325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Zimage-文生图+高清修复_2011971976901955585.json, 图片生成/文生图/Zimage_瑶光_2095722755646902273.json, 图片生成/文生图/Zimage图像修复放大_2045420770012172290.json, 图片生成/文生图/zimage图像修复放大_2032377992323801090.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色（私用）_2105937314986946562.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色_2098950780144410625.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色_2099062438128869377.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色【AI创客训练营】画布功能_角色_2114192879651479553.json, 图片生成/文生图/人物资产图_2111020921766109185.json, 图片生成/文生图/人物资产图一键生成 角色设定文生图处理生成工具_2113023431720656897.json, 图片生成/文生图/文生图写真创作工作流+4K出图_2082314053673902082.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Zimage-文生图+高清修复_2011971976901955585.json、图片生成/文生图/Zimage_瑶光_2095722755646902273.json、图片生成/文生图/Zimage图像修复放大_2045420770012172290.json、图片生成/文生图/zimage图像修复放大_2032377992323801090.json、图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 10/12 个有
- `Fast Groups Bypasser (rgthree)` —— 9/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `INTConstant` —— 8/12 个有
- `ImageScaleToTotalPixels` —— 8/12 个有
- `PreviewImage` —— 8/12 个有
- `CR Text` —— 7/12 个有
- `ConditioningZeroOut` —— 4/12 个有
- `ImageScaleBy` —— 4/12 个有
- `EmptyImage` —— 3/12 个有
- `Text` —— 3/12 个有
- `JjkText` —— 2/12 个有
- `solarL_SaveImagesToZip` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `CLIPLoaderGGUF` —— 1/12 个有
- `EmptySD3LatentImage` —— 1/12 个有
- `LoadImage` —— 1/12 个有
- `MemoryCleaner` —— 1/12 个有
- `Resolution` —— 1/12 个有
- `ResolutionSelector` —— 1/12 个有
- `easy promptList` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 9 | 12 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 12 | 18% |
| 采样算法 | res_2s_ode | - | 12 | 50% |
| 调度器 | kl_optimal | - | 12 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1080 | 80 - 1280 | 12 | 59% |
| 高度 | 1920 | 80 - 1920 | 12 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 9，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，12 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 res_2s_ode，12 个样本，一致性 50%
- 调度器 最常用 kl_optimal，12 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 80 - 1280，12 个样本
- 高度 中位数 1920，观测区间 80 - 1920，12 个样本
- 高发问题（15/12 个样本）：Steps较低可能导致细节不足
