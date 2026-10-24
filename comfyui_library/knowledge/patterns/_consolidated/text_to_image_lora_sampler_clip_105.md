---
name: text_to_image_lora_sampler_clip_105
type: Text To Image
frequency: 13
level: weak
coverage: 0.846077
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json, 图片生成/图生图/换脸 Face+Swap++Qwen-Image-2.1模特换头+换脸 klein_2104029720345137153.json, 图片生成/图生图/换脸+Face+Swap+ 模特换头+换脸+klein_2109808922092724226.json, 图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json, 图片生成/图生图/模特换头换脸神器｜Face+Swap++Qwen-Image-2.1 电商出图必备_2105513776450723842.json, 图片生成/文生图/AI换装Qwen Image 2.1双图试穿智能提示词 服装展示方案_2108655915309289474.json, 图片生成/文生图/Qwen 2.1洗图工作流，文生图反推提示词处理工具_2108319840565030913.json, 图片生成/文生图/Qwen Image 2.1加Flux2 Klein人像换脸换头与换脸双分支图生图方案_2106166383640924161.json, 图片生成/文生图/Qwen Image 2.1多功能官方流，文生图图生图多场景覆盖方案_2106450449720238081.json, 图片生成/文生图/Qwen Image 2.1官流文生图｜多图编辑一站式搞定_2106637714182459393.json, 图片生成/文生图/qwen image2.1 turbo二合一工作流 文生图图生图二合一_2109732642299142146.json, 图片生成/文生图/qwen-image2.1-turbo in 极速版 文生图图生图二合一_2110357009353756673.json, 图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_105

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json、图片生成/图生图/换脸 Face+Swap++Qwen-Image-2.1模特换头+换脸 klein_2104029720345137153.json、图片生成/图生图/换脸+Face+Swap+ 模特换头+换脸+klein_2109808922092724226.json、图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json、图片生成/图生图/模特换头换脸神器｜Face+Swap++Qwen-Image-2.1 电商出图必备_2105513776450723842.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `ComfySwitchNode` —— 12/13 个有
- `BatchImagesNode` —— 10/13 个有
- `Fast Groups Bypasser (rgthree)` —— 10/13 个有
- `Image Comparer (rgthree)` —— 9/13 个有
- `ImageResizeKJv2` —— 9/13 个有
- `solarL_SaveImagesToZip` —— 9/13 个有
- `孤海注释` —— 9/13 个有
- `PrimitiveStringMultiline` —— 7/13 个有
- `TextGenerate` —— 7/13 个有
- `ImageScaleToTotalPixels` —— 6/13 个有
- `PreviewAny` —— 6/13 个有
- `VAEEncode` —— 6/13 个有
- `Any Switch (rgthree)` —— 5/13 个有
- `EmptyFlux2LatentImage` —— 5/13 个有
- `ModelAttentionBackend` —— 5/13 个有
- `PrimitiveBoolean` —— 5/13 个有
- `PrimitiveInt` —— 5/13 个有
- `ReferenceLatent` —— 5/13 个有
- `GetImageSize` —— 4/13 个有
- `TextGenerateLTX2Prompt` —— 4/13 个有
- `KSamplerSelect` —— 2/13 个有
- `ManualSigmas` —— 2/13 个有
- `SamplerCustom` —— 2/13 个有
- `SeedGenerator` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 13 | 53% |
| 采样算法 | er_sde | - | 13 | 69% |
| 调度器 | beta | - | 13 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 1024 | 13 | 0% |
| 高度 | 80 | 80 - 1024 | 13 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 69%
- 调度器 最常用 beta，13 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，13 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，13 个样本，取值分散，一致性仅 0%
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
