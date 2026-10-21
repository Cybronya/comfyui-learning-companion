---
name: text_to_image_upscale_sampler_clip_13
type: Text To Image
frequency: 5
level: strong
coverage: 0.6278
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, JoinStrings, KSampler, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SomethingToString, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima动漫图像模型—全自动图像反推生图_2018204687069089793.json, 图片生成/文生图/Anima动漫图像模型—全自动文生图_2018013665781354497.json, 图片生成/文生图/Anima动漫文生图+Qwen3工作流_2019122223247794178.json, 图片生成/文生图/Anima动漫文生图-角色图像反推（支持二次元热门手游角色）_2019429862456434689.json, 图片生成/文生图/【02.01】ANIMA动漫生图模型+二次放大_2060402251050610689.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Anima动漫图像模型—全自动图像反推生图_2018204687069089793.json、图片生成/文生图/Anima动漫图像模型—全自动文生图_2018013665781354497.json、图片生成/文生图/Anima动漫文生图+Qwen3工作流_2019122223247794178.json、图片生成/文生图/Anima动漫文生图-角色图像反推（支持二次元热门手游角色）_2019429862456434689.json、图片生成/文生图/【02.01】ANIMA动漫生图模型+二次放大_2060402251050610689.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CR Text` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 896 - 1024 | 5 | 94% |
| 高度 | 1024 | 1024 - 1152 | 5 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 896 - 1024，5 个样本，取值集中（一致性 94%）
- 高度 中位数 1024，观测区间 1024 - 1152，5 个样本，取值集中（一致性 94%）
