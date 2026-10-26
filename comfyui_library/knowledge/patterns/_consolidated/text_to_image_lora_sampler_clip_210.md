---
name: text_to_image_lora_sampler_clip_210
type: Text To Image
frequency: 9
level: strong
coverage: 0.828111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Turbo八步极速图像编辑 高效精准改图必备方案_2110370961915727874.json, 图片生成/图生图/Qwen Image 2.1 Turbo图像编辑工作流，指令式修图快速精准出图_2114565422858194945.json, 图片生成/图生图/Qwen Image 2.1 Turbo图像编辑，图生图局部重绘快人一步_2110788994064805889.json, 图片生成/图生图/Qwen Image 2.1 Turbo图像编辑｜图生图智能修图高效又省心_2114171798861475842.json, 图片生成/图生图/Qwen Image 2.1 Turbo多参考图加速版，文生图图生图高效出图_2114500964400066561.json, 图片生成/图生图/Qwen Image 2.1图像编辑二版｜局部重绘人物出图利器_2108074166527291393.json, 图片生成/图生图/image_qwen_image_2_1_turbo_多参考图加速版｜文生图图生图提速_2114311183372210178.json, 图片生成/图生图/林茜数字人Qwen 2.1换脸流｜图生图换脸数字人两不误_2112925117058736129.json, 图片生成/文生图/Qwen Image 2.1 Turbo文生图，创意形象快速直出_2110829189711622145.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_210

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Turbo八步极速图像编辑 高效精准改图必备方案_2110370961915727874.json、图片生成/图生图/Qwen Image 2.1 Turbo图像编辑工作流，指令式修图快速精准出图_2114565422858194945.json、图片生成/图生图/Qwen Image 2.1 Turbo图像编辑，图生图局部重绘快人一步_2110788994064805889.json、图片生成/图生图/Qwen Image 2.1 Turbo图像编辑｜图生图智能修图高效又省心_2114171798861475842.json、图片生成/图生图/Qwen Image 2.1 Turbo多参考图加速版，文生图图生图高效出图_2114500964400066561.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 8/9 个有
- `KSamplerSelect` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `ManualSigmas` —— 8/9 个有
- `CFGGuider` —— 7/9 个有
- `RandomNoise` —— 7/9 个有
- `SamplerCustomAdvanced` —— 7/9 个有
- `PreviewAny` —— 6/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `TextGenerate` —— 6/9 个有
- `BatchImagesNode` —— 5/9 个有
- `SaveImageAdvanced` —— 5/9 个有
- `GetNode` —— 2/9 个有
- `Image Comparer (rgthree)` —— 2/9 个有
- `ImageCompare` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `Int` —— 1/9 个有
- `ResolutionSelector` —— 1/9 个有
- `SamplerCustom` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
