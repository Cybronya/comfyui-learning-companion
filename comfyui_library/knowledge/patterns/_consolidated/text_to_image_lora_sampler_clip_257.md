---
name: text_to_image_lora_sampler_clip_257
type: Text To Image
frequency: 8
level: weak
coverage: 0.867125
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json, 图片生成/图生图/换脸 Face+Swap++Qwen-Image-2.1模特换头+换脸 klein_2104029720345137153.json, 图片生成/图生图/换脸+Face+Swap+ 模特换头+换脸+klein_2109808922092724226.json, 图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json, 图片生成/文生图/Qwen Image 2.1加Flux2 Klein人像换脸换头与换脸双分支图生图方案_2106166383640924161.json, 图片生成/文生图/Qwen Image 2.1图像编辑工作流，图生图处理高质量方案_2105774125573828610.json, 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json, 平台全量/Qwen Image 2.1一键换装｜图片服装替换自动完成｜电商模特好帮手_2102295912205869058.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_257

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json、图片生成/图生图/换脸 Face+Swap++Qwen-Image-2.1模特换头+换脸 klein_2104029720345137153.json、图片生成/图生图/换脸+Face+Swap+ 模特换头+换脸+klein_2109808922092724226.json、图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json、图片生成/文生图/Qwen Image 2.1加Flux2 Klein人像换脸换头与换脸双分支图生图方案_2106166383640924161.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `BatchImagesNode` —— 5/8 个有
- `EmptyFlux2LatentImage` —— 5/8 个有
- `ImageResizeKJv2` —— 5/8 个有
- `ReferenceLatent` —— 5/8 个有
- `TextGenerateLTX2Prompt` —— 5/8 个有
- `VAEEncode` —— 5/8 个有
- `solarL_SaveImagesToZip` —— 4/8 个有
- `孤海注释` —— 4/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 8 | 36% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 80 - 1024 | 8 | 32% |
| 高度 | 1024 | 80 - 1024 | 8 | 32% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 32%
- 高度 中位数 1024，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 32%
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
