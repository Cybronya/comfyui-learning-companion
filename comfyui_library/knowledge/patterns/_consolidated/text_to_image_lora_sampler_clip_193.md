---
name: text_to_image_lora_sampler_clip_193
type: Text To Image
frequency: 9
level: strong
coverage: 0.869667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 PE模特换装超清放大版，图生图高清画质提升工作流_2102856922788622338.json, 图片生成/图生图/Qwen Image 2.1图片编辑加角色定妆照，图生图角色一致性设计方案_2103556787147460610.json, 图片生成/图生图/Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514.json, 图片生成/图生图/qwen image2.1加速版三图图生图 多张输入精准改图_2108703420906565633.json, 图片生成/图生图/qwen image2.1加速版三图图生图｜多图编辑高效出图_2108440932126380034.json, 图片生成/图生图/qwen image2.1加速版双图图生图｜高效图像编辑出图_2108450269943132161.json, 图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json, 图片生成/文生图/文生图Qwen Image 2.1 PE加速版，角色设计文生图高质量方案_2106832611799814145.json, 图片生成/文生图/文生图Qwen_Image_2.1_PE加速版，角色设计文生图高质量方案_2110543311986577410.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_193

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 PE模特换装超清放大版，图生图高清画质提升工作流_2102856922788622338.json、图片生成/图生图/Qwen Image 2.1图片编辑加角色定妆照，图生图角色一致性设计方案_2103556787147460610.json、图片生成/图生图/Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514.json、图片生成/图生图/qwen image2.1加速版三图图生图 多张输入精准改图_2108703420906565633.json、图片生成/图生图/qwen image2.1加速版三图图生图｜多图编辑高效出图_2108440932126380034.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `QwenPERewriteT8` —— 8/9 个有
- `SeedVR2LoadDiTModel` —— 8/9 个有
- `SeedVR2LoadVAEModel` —— 8/9 个有
- `SeedVR2VideoUpscaler` —— 8/9 个有
- `孤海注释` —— 7/9 个有
- `CR Prompt Text` —— 6/9 个有
- `ComfySwitchNode` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `INTConstant` —— 6/9 个有
- `LoadImage` —— 6/9 个有
- `ResolutionSelector` —— 6/9 个有
- `easy cleanGpuUsed` —— 6/9 个有
- `ResizeAndPadImage` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `Any Switch (rgthree)` —— 2/9 个有
- `EmptyImage` —— 2/9 个有
- `Int` —— 2/9 个有
- `MuyeTextEditOutput` —— 2/9 个有
- `ImageStitch` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
