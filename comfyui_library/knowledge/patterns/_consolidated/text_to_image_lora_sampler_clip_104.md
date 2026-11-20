---
name: text_to_image_lora_sampler_clip_104
type: Text To Image
frequency: 13
level: strong
coverage: 0.851077
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 PE模特换装超清放大版，图生图高清画质提升工作流_2102856922788622338.json, 图片生成/图生图/Qwen Image 2.1图片编辑神器｜配饰配件随心换_2103041179548995585.json, 图片生成/图生图/Qwen Image 2.1图片编辑配件可用，帽子等配饰换装图生图工具_2103195052028813313.json, 图片生成/图生图/Qwen Image 2.1配件编辑实测｜换配饰改道具轻松搞定_2103083517977645057.json, 图片生成/图生图/Qwen Image2.1角色资产4格详图 SEEDVR2高清放大处理工具_2113048870426075138.json, 图片生成/图生图/Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514.json, 图片生成/图生图/qwen image2.1加速版三图图生图 多张输入精准改图_2108703420906565633.json, 图片生成/图生图/qwen image2.1加速版三图图生图｜多图编辑高效出图_2108440932126380034.json, 图片生成/图生图/qwen image2.1加速版双图图生图｜高效图像编辑出图_2108450269943132161.json, 图片生成/图生图/角色资产4格详图制作Qwen Image 2.1工作流，图生图其它图片处理工具_2107887078867558401.json, 图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json, 图片生成/文生图/文生图Qwen Image 2.1 PE加速版，角色设计文生图高质量方案_2106832611799814145.json, 图片生成/文生图/文生图Qwen_Image_2.1_PE加速版，角色设计文生图高质量方案_2110543311986577410.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 PE模特换装超清放大版，图生图高清画质提升工作流_2102856922788622338.json、图片生成/图生图/Qwen Image 2.1图片编辑神器｜配饰配件随心换_2103041179548995585.json、图片生成/图生图/Qwen Image 2.1图片编辑配件可用，帽子等配饰换装图生图工具_2103195052028813313.json、图片生成/图生图/Qwen Image 2.1配件编辑实测｜换配饰改道具轻松搞定_2103083517977645057.json、图片生成/图生图/Qwen Image2.1角色资产4格详图 SEEDVR2高清放大处理工具_2113048870426075138.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
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
- `孤海注释` —— 11/13 个有
- `ComfySwitchNode` —— 10/13 个有
- `ImageScaleToTotalPixels` —— 10/13 个有
- `LoadImage` —— 10/13 个有
- `PreviewImage` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `SeedVR2LoadDiTModel` —— 10/13 个有
- `SeedVR2LoadVAEModel` —— 10/13 个有
- `SeedVR2VideoUpscaler` —— 10/13 个有
- `Fast Groups Bypasser (rgthree)` —— 8/13 个有
- `QwenPERewriteT8` —— 8/13 个有
- `CR Prompt Text` —— 6/13 个有
- `INTConstant` —— 6/13 个有
- `easy cleanGpuUsed` —— 6/13 个有
- `easy showAnything` —— 6/13 个有
- `QwenImage21PromptEnhancerT8` —— 3/13 个有
- `ResizeAndPadImage` —— 3/13 个有
- `Any Switch (rgthree)` —— 2/13 个有
- `EmptyImage` —— 2/13 个有
- `Int` —— 2/13 个有
- `MuyeTextEditOutput` —— 2/13 个有
- `PrimitiveBoolean` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
