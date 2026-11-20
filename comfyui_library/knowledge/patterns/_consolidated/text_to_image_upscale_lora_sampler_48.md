---
name: text_to_image_upscale_lora_sampler_48
type: Text To Image
frequency: 6
level: strong
coverage: 0.862667
common_nodes: [CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-影楼级人像 细节增强 提示词自动优化_2036434441282785282.json, 图片生成/文生图/Zimage 直出真实感网红图片 林耀3.18_2034176377439653889.json, 图片生成/文生图/zimage（梦幻）_2053013074277355522.json, 图片生成/文生图/【古装精品短剧】文生图 _ 场景角色_2054379116278886401.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色_2052651394800336898.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色_2057377135022661634.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image-影楼级人像 细节增强 提示词自动优化_2036434441282785282.json、图片生成/文生图/Zimage 直出真实感网红图片 林耀3.18_2034176377439653889.json、图片生成/文生图/zimage（梦幻）_2053013074277355522.json、图片生成/文生图/【古装精品短剧】文生图 _ 场景角色_2054379116278886401.json、图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色_2052651394800336898.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `SeedVR2LoadDiTModel` —— 5/6 个有
- `SeedVR2LoadVAEModel` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `LoadImage` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `llama_cpp_instruct_adv` —— 2/6 个有
- `llama_cpp_model_loader` —— 2/6 个有
- `ClipLoaderGGUF` —— 1/6 个有
- `ImpactConditionalBranch` —— 1/6 个有
- `PDRatioSelector` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `Text` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1080 | 6 | 87% |
| 高度 | 1920 | 1280 - 1920 | 6 | 87% |
| 采样步数 | 8 | 8 - 10 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 6 | 96% |
| 采样算法 | res_2s_ode | - | 6 | 67% |
| 调度器 | kl_optimal | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1080，6 个样本，取值集中（一致性 87%）
- 高度 中位数 1920，观测区间 1280 - 1920，6 个样本，取值集中（一致性 87%）
- 采样步数 中位数 8，观测区间 8 - 10，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，6 个样本，取值集中（一致性 96%）
- 采样算法 最常用 res_2s_ode，6 个样本，一致性 67%
- 调度器 最常用 kl_optimal，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
