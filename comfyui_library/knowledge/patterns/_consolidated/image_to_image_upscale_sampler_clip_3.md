---
name: image_to_image_upscale_sampler_clip_3
type: Image To Image
frequency: 27
level: moderate
coverage: 0.699
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImpactInt, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/反推洗图工作流，图片去同质化免扣健康分2_2102430336633364482.json, 图片生成/图生图/图像去除Ai感肤色真实感极佳_2063521747957272578.json, 图片生成/图生图/图像去除Ai感，肤色真实感极佳_2058561035572961282.json, 图片生成/图生图/图像去除Ai感，肤色真实感极佳_2059092954777735170.json, 图片生成/图生图/图片image去除Ai感肤色真实感极佳_2064506351417651202.json, 图片生成/图生图/图片去除Ai感_2066524004466384897.json, 图片生成/图生图/图片去除Ai感工作流： Z_image反推洗图重绘+SeedVR放大对比工作流-B站UP主@好奇漫步_2032440095235641345.json, 图片生成/图生图/图片去除Ai感工作流： Z_image反推洗图重绘+SeedVR放大对比工作流_2070411857244024834.json, 图片生成/图生图/图片去除Ai感工作流： Z_image反推洗图重绘+SeedVR放大对比工作流_2073575059603673090.json, 图片生成/图生图/小而美图像模型：自动反推洗图_1995813733429555201.json, 图片生成/图生图/最强Z-Image反推洗图重绘：二次元动漫转真人_2011458593912000513.json, 图片生成/图生图/超好用🔥图片去除Ai感-自然_2066455395455033345.json, 图片生成/图生图/超真实图片去除Ai感+ Z_image反推洗图重绘_2052653389753921537.json, 图片生成/图生图/（ET）Z-Image：图片去除Ai感工作流_2050155551664943106.json, 图片生成/文生图/Z-IMAGE：图反推关键词+生图+高清放大_1995435685152796674.json, 图片生成/文生图/Z-IMAGE：小而美图像模型：自动反推洗图_1993918755539451906.json, 图片生成/文生图/Z-Image：图片去除Ai感工作流_1999383021906259970.json, 图片生成/文生图/Z-Image：图片去除Ai感工作流_2056552554821148673.json, 图片生成/文生图/Z-Image：图片去除Ai感工作流_2057006038511079425.json, 图片生成/文生图/Z-Image：图片去除Ai感工作流_2061617318295330817.json, 图片生成/文生图/Z-Image：图片去除Ai感工作流_2069967256154628097.json, 图片生成/文生图/qwen3反推Krea2洗图重绘去除Ai感+SeedVR放大_2089514888220725249.json, 图片生成/文生图/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2112459958427144193.json, 图片生成/文生图/qwen3反推提示词并生图_2057289354837581825.json, 图片生成/文生图/qwen3反推提示词并生图_2057720195904532481.json, 图片生成/文生图/图片AI感消失 Z-Image：工作流_1999400749585006593.json, 图片生成/文生图/图片去除Ai感工作流-邻家AI大女孩_2042209886397800450.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/反推洗图工作流，图片去同质化免扣健康分2_2102430336633364482.json、图片生成/图生图/图像去除Ai感肤色真实感极佳_2063521747957272578.json、图片生成/图生图/图像去除Ai感，肤色真实感极佳_2058561035572961282.json、图片生成/图生图/图像去除Ai感，肤色真实感极佳_2059092954777735170.json、图片生成/图生图/图片image去除Ai感肤色真实感极佳_2064506351417651202.json…）

- **类型**：Image To Image
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 27 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImpactInt`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 25/27 个有
- `PreviewImage` —— 25/27 个有
- `ShowText|pysssss` —— 25/27 个有
- `LayerUtility: ImageReel` —— 23/27 个有
- `LayerUtility: ImageReelComposit` —— 23/27 个有
- `Image Comparer (rgthree)` —— 22/27 个有
- `Fast Groups Bypasser (rgthree)` —— 21/27 个有
- `LayerUtility: PurgeVRAM` —— 21/27 个有
- `easy imageConcat` —— 16/27 个有
- `LoraLoaderModelOnly` —— 6/27 个有
- `GetNode` —— 5/27 个有
- `SetNode` —— 5/27 个有
- `孤海注释` —— 4/27 个有
- `Float` —— 2/27 个有
- `MemoryCleaner` —— 2/27 个有
- `easy saveText` —— 2/27 个有
- `CR Text` —— 1/27 个有
- `PrimitiveFloat` —— 1/27 个有
- `RHUploadZip` —— 1/27 个有
- `忽略多组孤海` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 40 | 27 | 49% |
| Prompt 约束强度(CFG) | 1 | 0.9 - 2 | 27 | 75% |
| 采样算法 | euler | - | 27 | 93% |
| 调度器 | simple | - | 27 | 96% |
| 重绘幅度 | 0.7 | 0.1 - 0.7 | 27 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 40，27 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.9 - 2，27 个样本
- 采样算法 最常用 euler，27 个样本，一致性 93%
- 调度器 最常用 simple，27 个样本，一致性 96%
- 重绘幅度 中位数 0.7，观测区间 0.1 - 0.7，27 个样本
- 风险：Prompt 约束强度(CFG) 观测到 0.9，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
