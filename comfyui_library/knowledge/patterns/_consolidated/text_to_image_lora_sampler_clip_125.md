---
name: text_to_image_lora_sampler_clip_125
type: Text To Image
frequency: 7
level: strong
coverage: 0.818714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [easy seed, Image Compare (mtb)]
members: [图片生成/图生图/2102471938563207170.json, 图片生成/图生图/2102650761531445250.json, 图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json, 图片生成/文生图/Qwen Image 2.1角色设计参考表，四视图多角度角色一致性文生图_2102832066093215745.json, 图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json, 图片生成/文生图/文生图Qwen Image 2.1 PE加速版，角色设计文生图高质量方案_2106832611799814145.json, 视频生成/文生视频/Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2102471938563207170.json、图片生成/图生图/2102650761531445250.json、图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json、图片生成/文生图/Qwen Image 2.1角色设计参考表，四视图多角度角色一致性文生图_2102832066093215745.json、图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 6/7 个有
- `SeedVR2LoadVAEModel` —— 6/7 个有
- `SeedVR2VideoUpscaler` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `CR Prompt Text` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `TextGenerateLTX2Prompt` —— 5/7 个有
- `Anything Everywhere3` —— 4/7 个有
- `GetNode` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `ComfySwitchNode` —— 3/7 个有
- `LayerUtility: TextJoin` —— 3/7 个有
- `Seed (rgthree)` —— 3/7 个有
- `easy setNode` —— 3/7 个有
- `LoadImage` —— 2/7 个有
- `QwenPERewriteT8` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `Image Compare (mtb)` —— 1/7 个有
- `SaveImageAdvanced` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy seed、Image Compare (mtb)
