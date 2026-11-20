---
name: text_to_image_lora_sampler_clip_93
type: Text To Image
frequency: 14
level: weak
coverage: 0.874714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 PE模特换装超清放大版，图生图高清画质提升工作流_2102856922788622338.json, 图片生成/图生图/Qwen Image 2.1图片编辑加角色定妆照，图生图角色一致性设计方案_2103556787147460610.json, 图片生成/图生图/Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514.json, 图片生成/图生图/qwen image2.1加速版三图图生图 多张输入精准改图_2108703420906565633.json, 图片生成/图生图/qwen image2.1加速版三图图生图｜多图编辑高效出图_2108440932126380034.json, 图片生成/图生图/qwen image2.1加速版双图图生图｜高效图像编辑出图_2108450269943132161.json, 图片生成/图生图/一站式AI短剧资产生成全能工作流（人物三视图，场景生成）_2115104250727583745.json, 图片生成/图生图/超美资产设计_2114188619610152962.json, 图片生成/图生图/超美资产设计_2116690984644988929.json, 图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json, 图片生成/文生图/文生图Qwen Image 2.1 PE加速版，角色设计文生图高质量方案_2106832611799814145.json, 图片生成/文生图/文生图Qwen_Image_2.1_PE加速版，角色设计文生图高质量方案_2110543311986577410.json, 图片生成/文生图/超美资产设计~~~_2110392866790002690.json, 视频生成/图生视频/超美资产设计~~~_2116342042778488833.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 PE模特换装超清放大版，图生图高清画质提升工作流_2102856922788622338.json、图片生成/图生图/Qwen Image 2.1图片编辑加角色定妆照，图生图角色一致性设计方案_2103556787147460610.json、图片生成/图生图/Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514.json、图片生成/图生图/qwen image2.1加速版三图图生图 多张输入精准改图_2108703420906565633.json、图片生成/图生图/qwen image2.1加速版三图图生图｜多图编辑高效出图_2108440932126380034.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 13/14 个有
- `SeedVR2LoadDiTModel` —— 13/14 个有
- `SeedVR2LoadVAEModel` —— 13/14 个有
- `SeedVR2VideoUpscaler` —— 13/14 个有
- `CR Prompt Text` —— 11/14 个有
- `ComfySwitchNode` —— 11/14 个有
- `Fast Groups Bypasser (rgthree)` —— 11/14 个有
- `INTConstant` —— 11/14 个有
- `LoadImage` —— 11/14 个有
- `QwenPERewriteT8` —— 11/14 个有
- `ResolutionSelector` —— 11/14 个有
- `Image Comparer (rgthree)` —— 9/14 个有
- `JjkText` —— 9/14 个有
- `QwenImage21Cache` —— 9/14 个有
- `solarL_SaveImagesToZip` —— 9/14 个有
- `孤海注释` —— 7/14 个有
- `easy cleanGpuUsed` —— 6/14 个有
- `easy showAnything` —— 6/14 个有
- `CR Text` —— 5/14 个有
- `忽略多组孤海` —— 5/14 个有
- `EmptyImage` —— 3/14 个有
- `PrimitiveStringMultiline` —— 3/14 个有
- `ResizeAndPadImage` —— 3/14 个有
- `Seed (rgthree)` —— 3/14 个有
- `Any Switch (rgthree)` —— 2/14 个有
- `Int` —— 2/14 个有
- `MuyeTextEditOutput` —— 2/14 个有
- `ImageStitch` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 14 | 0% |
| 高度 | 80 | 80 - 1920 | 14 | 0% |
| 采样步数 | 4 | 4 - 25 | 14 | 7% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 14 | 48% |
| 采样算法 | er_sde | - | 14 | 64% |
| 调度器 | beta | - | 14 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，14 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，14 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 25，14 个样本，取值分散，一致性仅 7%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，14 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 er_sde，14 个样本，一致性 64%
- 调度器 最常用 beta，14 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（16/14 个样本）：Steps较低可能导致细节不足
