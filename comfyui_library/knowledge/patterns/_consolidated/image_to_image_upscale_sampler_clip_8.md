---
name: image_to_image_upscale_sampler_clip_8
type: Image To Image
frequency: 16
level: moderate
coverage: 0.757812
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageScaleBy, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/zimage双K洗图放大_2010944842016235521.json, 图片生成/图生图/【加密版】图片去除Ai感工作流： Z_image反推洗图重绘+SeedVR放大工作流-B站UP主@好奇漫步_2065781622254956545.json, 图片生成/图生图/图片去除Ai感重绘放大工作流_2049669122480455682.json, 图片生成/图生图/图片反推洗图工作流，去同质化保健康分_2072580610752860161.json, 图片生成/图生图/最强还原人物真实度、去AI感_2077790045355995137.json, 图片生成/图生图/最强还原人物真实度、去AI感_2092808030168637441.json, 图片生成/图生图/最强还原人物真实度、去AI感_2093497000145805314.json, 图片生成/图生图/最强还原人物真实度、去AI感_2096456819844673537.json, 图片生成/图生图/最强还原人物真实度、去AI感_2111073643794100225.json, 图片生成/图生图/最强还原人物真实度去AI感自然修图工作流_2083006885749411842.json, 图片生成/图生图/最强还原人物真实度去AI感自然修图工作流_2083022220804321281.json, 图片生成/图生图/黄哥13期专用_2091511337003343874.json, 图片生成/文生图/Z-Image最新模型 洗图+去除ai感 「24G」可用_2010631129069522946.json, 图片生成/文生图/zimage二次元转真人，双K洗图放大_2006226308195426306.json, 图片生成/文生图/图片去除Ai感工作流+全节点注释_2056746160630616066.json, 视频生成/图生视频/洗图加生视频_2070330640096120833.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/zimage双K洗图放大_2010944842016235521.json、图片生成/图生图/【加密版】图片去除Ai感工作流： Z_image反推洗图重绘+SeedVR放大工作流-B站UP主@好奇漫步_2065781622254956545.json、图片生成/图生图/图片去除Ai感重绘放大工作流_2049669122480455682.json、图片生成/图生图/图片反推洗图工作流，去同质化保健康分_2072580610752860161.json、图片生成/图生图/最强还原人物真实度、去AI感_2077790045355995137.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageScaleBy`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 14/16 个有
- `LayerUtility: PurgeVRAM` —— 12/16 个有
- `Fast Groups Bypasser (rgthree)` —— 11/16 个有
- `Image Comparer (rgthree)` —— 10/16 个有
- `LoraLoaderModelOnly` —— 8/16 个有
- `CR Text` —— 3/16 个有
- `easy cleanGpuUsed` —— 3/16 个有
- `LayerUtility: PurgeVRAM V2` —— 2/16 个有
- `easy clearCacheAll` —— 2/16 个有
- `AILab_QwenVL` —— 1/16 个有
- `HAIGC_SaveImagesToZip` —— 1/16 个有
- `JWFloat` —— 1/16 个有
- `Latent Noise Injection` —— 1/16 个有
- `PrimitiveFloat` —— 1/16 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 1/16 个有
- `SaveVideo` —— 1/16 个有
- `TT_img_enc` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 5 - 10 | 16 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.6 | 16 | 82% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 0.7 | 0.1 - 1 | 16 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 5 - 10，16 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.6，16 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.1 - 1，16 个样本
