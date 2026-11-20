---
name: image_to_image_controlnet_sampler_clip_6
type: Image To Image
frequency: 5
level: strong
coverage: 0.8454
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Bypasser (rgthree), ImpactImageBatchToImageList, ImpactInt, KSampler, LayerUtility: PurgeVRAM, LoadImage, ModelPatchLoader, Mute / Bypass Repeater (rgthree), PreviewImage, QwenImageDiffsynthControlnet, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/251225001.010.Z-image批量强控洗图，下载到本地换备用节点_2004230957110620162.json, 图片生成/图生图/Z-image批量4张图洗图+强控流_2008253153619218433.json, 图片生成/图生图/Z-image批量洗图+姿态控制_1999117660967272449.json, 图片生成/图生图/Z-image批量洗图+姿态控制【傲雪AIGC 】_1998990561690443777.json, 图片生成/图生图/🤖Z-image小钢炮批量洗图+强控流_1997854052056764417.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/251225001.010.Z-image批量强控洗图，下载到本地换备用节点_2004230957110620162.json、图片生成/图生图/Z-image批量4张图洗图+强控流_2008253153619218433.json、图片生成/图生图/Z-image批量洗图+姿态控制_1999117660967272449.json、图片生成/图生图/Z-image批量洗图+姿态控制【傲雪AIGC 】_1998990561690443777.json、图片生成/图生图/🤖Z-image小钢炮批量洗图+强控流_1997854052056764417.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Bypasser (rgthree)`
- `ImpactImageBatchToImageList`
- `ImpactInt`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelPatchLoader`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactMakeImageBatch` —— 4/5 个有
- `Any Switch (rgthree)` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `Qwen3VL_Advanced` —— 3/5 个有
- `RH_LLMAPI_NODE` —— 3/5 个有
- `DapaoImageAspectRatioResizeNode` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `Grok_Chat` —— 2/5 个有
- `PrimitiveString` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `Float` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `Qwen3VL_ExtraOptions` —— 1/5 个有
- `VHS_LoadImagesPath` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 5 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
