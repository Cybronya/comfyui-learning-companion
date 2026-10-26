---
name: text_to_image_lora_sampler_clip_215
type: Text To Image
frequency: 9
level: weak
coverage: 0.873222
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json, 图片生成/图生图/换脸 Face+Swap++Qwen-Image-2.1模特换头+换脸 klein_2104029720345137153.json, 图片生成/图生图/换脸+Face+Swap+ 模特换头+换脸+klein_2109808922092724226.json, 图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json, 图片生成/图生图/模特换头换脸神器｜Face+Swap++Qwen-Image-2.1 电商出图必备_2105513776450723842.json, 图片生成/文生图/Qwen Image 2.1加Flux2 Klein人像换脸换头与换脸双分支图生图方案_2106166383640924161.json, 图片生成/文生图/Qwen Image 2.1图像编辑工作流，图生图处理高质量方案_2105774125573828610.json, 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json, 视频生成/图生视频/qwen_image_2.1编辑工作流｜文生图图生图双支持｜日常改图必备款_2102310384794427394.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_215

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json、图片生成/图生图/换脸 Face+Swap++Qwen-Image-2.1模特换头+换脸 klein_2104029720345137153.json、图片生成/图生图/换脸+Face+Swap+ 模特换头+换脸+klein_2109808922092724226.json、图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json、图片生成/图生图/模特换头换脸神器｜Face+Swap++Qwen-Image-2.1 电商出图必备_2105513776450723842.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 8/9 个有
- `BatchImagesNode` —— 6/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `TextGenerateLTX2Prompt` —— 6/9 个有
- `EmptyFlux2LatentImage` —— 5/9 个有
- `ImageResizeKJv2` —— 5/9 个有
- `ReferenceLatent` —— 5/9 个有
- `VAEEncode` —— 5/9 个有
- `solarL_SaveImagesToZip` —— 5/9 个有
- `孤海注释` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `Any Switch (rgthree)` —— 1/9 个有
- `EmptyImage` —— 1/9 个有
- `ImageScaleBy` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 9 | 41% |
| 采样算法 | er_sde | - | 9 | 56% |
| 调度器 | beta | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 1024 | 9 | 6% |
| 高度 | 80 | 80 - 1024 | 9 | 6% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 er_sde，9 个样本，一致性 56%
- 调度器 最常用 beta，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 6%
- 高度 中位数 80，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 6%
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
