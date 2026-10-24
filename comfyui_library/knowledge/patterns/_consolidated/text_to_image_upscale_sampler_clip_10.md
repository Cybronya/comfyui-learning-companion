---
name: text_to_image_upscale_sampler_clip_10
type: Text To Image
frequency: 9
level: strong
coverage: 0.650556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, JoinStrings, KSampler, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SomethingToString, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Anima3_动漫图生图_Qwen3反推工作流_2043988078615863297.json, 图片生成/图生图/Anima动漫图像模型—全自动图像反推生图_2047319224565108737.json, 图片生成/文生图/Anima3_动漫文生图+Qwen3工作流_2043942915990360065.json, 图片生成/文生图/Anima动漫图像模型—全自动图像反推生图_2018204687069089793.json, 图片生成/文生图/Anima动漫图像模型—全自动文生图_2018013665781354497.json, 图片生成/文生图/Anima动漫图像模型：全自动图像反推生图工作流_2034605359565901825.json, 图片生成/文生图/Anima动漫文生图+Qwen3工作流_2019122223247794178.json, 图片生成/文生图/Anima动漫文生图-角色图像反推（支持二次元热门手游角色）_2019429862456434689.json, 图片生成/文生图/【02.01】ANIMA动漫生图模型+二次放大_2060402251050610689.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Anima3_动漫图生图_Qwen3反推工作流_2043988078615863297.json、图片生成/图生图/Anima动漫图像模型—全自动图像反推生图_2047319224565108737.json、图片生成/文生图/Anima3_动漫文生图+Qwen3工作流_2043942915990360065.json、图片生成/文生图/Anima动漫图像模型—全自动图像反推生图_2018204687069089793.json、图片生成/文生图/Anima动漫图像模型—全自动文生图_2018013665781354497.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `JoinStrings`
- `KSampler`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SomethingToString`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/9 个有
- `LoadImage` —— 6/9 个有
- `GetNode` —— 5/9 个有
- `INTConstant` —— 5/9 个有
- `ModelSamplingAuraFlow` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `LayerUtility: ImageReel` —— 4/9 个有
- `LayerUtility: ImageReelComposit` —— 4/9 个有
- `PreviewAny` —— 4/9 个有
- `Image Comparer (rgthree)` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 9 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 896 - 1024 | 9 | 93% |
| 高度 | 1024 | 1024 - 1152 | 9 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 896 - 1024，9 个样本，取值集中（一致性 93%）
- 高度 中位数 1024，观测区间 1024 - 1152，9 个样本，取值集中（一致性 94%）
