---
name: text_to_image_upscale_lora_sampler_63
type: Text To Image
frequency: 4
level: strong
coverage: 0.78975
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1多合一文生图图生图处理工具_2102471938563207170.json, 图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json, 图片生成/文生图/Qwen Image 2.1角色设计参考表，四视图多角度角色一致性文生图_2102832066093215745.json, 视频生成/文生视频/Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1多合一文生图图生图处理工具_2102471938563207170.json、图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json、图片生成/文生图/Qwen Image 2.1角色设计参考表，四视图多角度角色一致性文生图_2102832066093215745.json、视频生成/文生视频/Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `LayerUtility: TextJoin` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有
- `easy setNode` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `EmptyImage` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
