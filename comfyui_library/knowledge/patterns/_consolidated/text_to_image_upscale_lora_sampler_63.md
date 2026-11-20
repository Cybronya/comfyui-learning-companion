---
name: text_to_image_upscale_lora_sampler_63
type: Text To Image
frequency: 5
level: weak
coverage: 0.8624
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, INTConstant, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima3-xingtong-lora_2066761395605164033.json, 图片生成/文生图/zimage（梦幻）_2053013074277355522.json, 图片生成/文生图/【古装精品短剧】文生图 _ 场景角色_2054379116278886401.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色_2052651394800336898.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色_2057377135022661634.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/anima3-xingtong-lora_2066761395605164033.json、图片生成/文生图/zimage（梦幻）_2053013074277355522.json、图片生成/文生图/【古装精品短剧】文生图 _ 场景角色_2054379116278886401.json、图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色_2052651394800336898.json、图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色_2057377135022661634.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `INTConstant`
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
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `PreviewAny` —— 2/5 个有
- `ImpactConditionalBranch` —— 1/5 个有
- `JoinStringMulti` —— 1/5 个有
- `PDRatioSelector` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RHLLMChatNode` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有
- `easy float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1920 | 5 | 73% |
| 高度 | 1920 | 1128 - 1920 | 5 | 82% |
| 采样步数 | 8 | 8 - 50 | 5 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 5 | 11% |
| 采样算法 | res_2s_ode | - | 5 | 80% |
| 调度器 | kl_optimal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1920，5 个样本
- 高度 中位数 1920，观测区间 1128 - 1920，5 个样本，取值集中（一致性 82%）
- 采样步数 中位数 8，观测区间 8 - 50，5 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，5 个样本，取值分散，一致性仅 11%
- 采样算法 最常用 res_2s_ode，5 个样本，一致性 80%
- 调度器 最常用 kl_optimal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
