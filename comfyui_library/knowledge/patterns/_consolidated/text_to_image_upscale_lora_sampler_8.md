---
name: text_to_image_upscale_lora_sampler_8
type: Text To Image
frequency: 9
level: weak
coverage: 0.731444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json, 图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json, 图片生成/文生图/Krea2-真人角色4K文生图_2095131210359074818.json, 图片生成/文生图/Krea2美学视觉文生图加SeedVR2高清出图工作流，文生图高质量文本到图像_2107579414744752130.json, 图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json, 图片生成/文生图/Qwen Image 2.1角色设计参考表，四视图多角度角色一致性文生图_2102832066093215745.json, 图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json, 图片生成/文生图/文生图Qwen Image 2.1 PE加速版，角色设计文生图高质量方案_2106832611799814145.json, 视频生成/文生视频/Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_8

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json、图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json、图片生成/文生图/Krea2-真人角色4K文生图_2095131210359074818.json、图片生成/文生图/Krea2美学视觉文生图加SeedVR2高清出图工作流，文生图高质量文本到图像_2107579414744752130.json、图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
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
- `INTConstant` —— 8/9 个有
- `PreviewImage` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `GetNode` —— 6/9 个有
- `JjkText` —— 6/9 个有
- `ResolutionSelector` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `solarL_SaveImagesToZip` —— 6/9 个有
- `CR Prompt Text` —— 5/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `QwenImage21Cache` —— 5/9 个有
- `TextEncodeQwenImage21` —— 5/9 个有
- `孤海注释` —— 5/9 个有
- `ConditioningZeroOut` —— 4/9 个有
- `Seed (rgthree)` —— 4/9 个有
- `Anything Everywhere3` —— 3/9 个有
- `LayerUtility: TextJoin` —— 3/9 个有
- `TextGenerateLTX2Prompt` —— 3/9 个有
- `easy setNode` —— 3/9 个有
- `ComfySwitchNode` —— 2/9 个有
- `EmptyImage` —— 2/9 个有
- `QwenPERewriteT8` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `QZ_ResolutionPreset` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 9 | 0% |
| 高度 | 80 | 80 - 1920 | 9 | 0% |
| 采样步数 | 4 | 4 - 9 | 9 | 62% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 9 | 52% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，9 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，9 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 9，9 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，9 个样本
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
