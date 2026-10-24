---
name: text_to_image_upscale_sampler_clip_15
type: Text To Image
frequency: 8
level: moderate
coverage: 0.875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问最新文生图模型 2512_2006387159393112065.json, 图片生成/文生图/强力模型Z-image，活人感图片生成_1993860368776757249.json, 图片生成/文生图/熊猫哥AIGC_Zimage_文生图+高清放大_2054039924533407745.json, 图片生成/文生图/短剧主角生成工作流ZImage+Kook瑶光lora_2053108617959755777.json, 图片生成/文生图/短剧剧情设计工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053083458406236162.json, 视频生成/图生视频/【最佳短剧生成】支持场景 _ 角色_2098744968851578881.json, 视频生成/图生视频/【短剧最佳助手】支持场景 _ 角色_2067180332339785729.json, 视频生成/图生视频/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/千问最新文生图模型 2512_2006387159393112065.json、图片生成/文生图/强力模型Z-image，活人感图片生成_1993860368776757249.json、图片生成/文生图/熊猫哥AIGC_Zimage_文生图+高清放大_2054039924533407745.json、图片生成/文生图/短剧主角生成工作流ZImage+Kook瑶光lora_2053108617959755777.json、图片生成/文生图/短剧剧情设计工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053083458406236162.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 7/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `CR Text` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `FastFilmGrain` —— 3/8 个有
- `INTConstant` —— 3/8 个有
- `LayerColor: BrightnessContrastV2` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `MuyeTextEditOutput` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `FluxResolutionNode` —— 1/8 个有
- `easy ifElse` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 512 - 1920 | 8 | 64% |
| 高度 | 1920 | 512 - 1920 | 8 | 66% |
| 采样步数 | 8 | 4 - 10 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | res_2s_ode | - | 8 | 38% |
| 调度器 | kl_optimal | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 512 - 1920，8 个样本
- 高度 中位数 1920，观测区间 512 - 1920，8 个样本
- 采样步数 中位数 8，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s_ode，8 个样本，一致性 38%
- 调度器 最常用 kl_optimal，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
