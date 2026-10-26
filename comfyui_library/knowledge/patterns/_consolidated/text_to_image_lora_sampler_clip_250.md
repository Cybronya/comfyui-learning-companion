---
name: text_to_image_lora_sampler_clip_250
type: Text To Image
frequency: 8
level: strong
coverage: 0.882125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Turbo官方8步图像编辑 高效改图方案_2109720316372152321.json, 图片生成/图生图/Qwen Image 2.1 Turbo扣印章电子版，图生图精准抠章一键出图_2114509350621507586.json, 图片生成/图生图/Qwen Image 2.1 turbo光影迁移 图生图处理生成工具_2113004334173741057.json, 图片生成/图生图/Qwen Image 2.1图片编辑工作流，简洁高效的图生图处理方案_2105792533245808642.json, 图片生成/图生图/Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626.json, 图片生成/图生图/Qwen image 2.1 turbo扣印章提取电子版｜图生图证件材料神器_2114302718364962818.json, 图片生成/图生图/Qwen image 2.1 turbo扣印章电子版｜图生图秒变电子印章件_2114300959450034178.json, 图片生成/图生图/Qwen image 2.1文生编辑抠图一体 透明图像处理方案_2110350738932191233.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_250

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Turbo官方8步图像编辑 高效改图方案_2109720316372152321.json、图片生成/图生图/Qwen Image 2.1 Turbo扣印章电子版，图生图精准抠章一键出图_2114509350621507586.json、图片生成/图生图/Qwen Image 2.1 turbo光影迁移 图生图处理生成工具_2113004334173741057.json、图片生成/图生图/Qwen Image 2.1图片编辑工作流，简洁高效的图生图处理方案_2105792533245808642.json、图片生成/图生图/Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/8 个有
- `SaveImageAdvanced` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `KSamplerSelect` —— 5/8 个有
- `ManualSigmas` —— 5/8 个有
- `SamplerCustom` —— 5/8 个有
- `ComfySwitchNode` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `QwenImage21Cache` —— 4/8 个有
- `ResolutionSelector` —— 4/8 个有
- `BRIA_RMBG_ModelLoader_Zho` —— 3/8 个有
- `BRIA_RMBG_Zho` —— 3/8 个有
- `FluxKontextImageScale` —— 3/8 个有
- `PrimitiveBoolean` —— 3/8 个有
- `QwenPERewriteT8` —— 3/8 个有
- `easy promptConcat` —— 3/8 个有
- `Change Channel Count` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `VOSR2ModelLoader` —— 2/8 个有
- `VOSR2Upscale` —— 2/8 个有
- `Int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
