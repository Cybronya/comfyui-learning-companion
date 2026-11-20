---
name: image_to_image_sampler_unet_vae_3
type: Image To Image
frequency: 30
level: moderate
coverage: 0.839533
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【楚心钟陌】Qwen三次元转二次元_1999336961653473281.json, 图片生成/图生图/【遇见AI】longcat image edit turbo 图片编辑_2059223215184105473.json, 图片生成/图生图/人物国风风格化_2110252503370653697.json, 图片生成/图生图/修复光斑--修复曝光LORA---Qwen-Edit-2509_1987219668211576834.json, 图片生成/图生图/全方位多视角调节图片_2077676206090182658.json, 图片生成/图生图/全量qwen edit 2512单图多角度编辑工作流_2068339692986265601.json, 图片生成/图生图/全量qwen edit 2512多图编辑工作流_2068333416139026434.json, 图片生成/图生图/千问Qwen-多图融合1.0_2012857063315087361.json, 图片生成/图生图/千问多角度控制lora_2013230266269044737.json, 图片生成/图生图/千问多角度控制lora_2016779041151393794.json, 图片生成/图生图/千问多角度控制lora，手动控制_2013226905612324866.json, 图片生成/图生图/千问多角度控制lora，手动控制_2033440618382364673.json, 图片生成/图生图/图像转角度｜单张（一致性LoRA + 多角度LoRA）Qwen Edit 2511_2100019431236784130.json, 图片生成/图生图/多视角多角度人物道具场景视角加速版（九视角版本）已配置好（更多视角到工作流）_2009830651888930818.json, 图片生成/图生图/多视角（十视角）加速版，人物场景道具通用_2010525695197323265.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2011997466366844929.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2013597857110036482.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2016506996190617602.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2018227314567417857.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2020891798947762178.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2025792054508396546.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2071518519048630273.json, 图片生成/图生图/对镜自拍Qwen2511-multiple-angles多角度工作流+全节点注释_2041417500948172801.json, 图片生成/图生图/电商商品多角度自由控制角度【手动控制】_2018287831155744770.json, 图片生成/图生图/角度切换_自由切换_2071542576972386306.json, 图片生成/图生图/👾怪獸-人物道具场景多视角加速版👾_2058103710215131137.json, 平台全量/图像转角度_2069958648004177921.json, 平台全量/图像转角度｜单张（一致性LoRA + 多角度LoRA）Qwen Edit 2511_2044389320160714754.json, 平台全量/多角度精准控制工作流（内部教学）_2034211985302233089.json, 视频生成/图生视频/图像转角度｜单张一致性LoRA_+_多角度LoRAQwen_Edit_2511_2100191664584351746.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/图生图/【楚心钟陌】Qwen三次元转二次元_1999336961653473281.json、图片生成/图生图/【遇见AI】longcat image edit turbo 图片编辑_2059223215184105473.json、图片生成/图生图/人物国风风格化_2110252503370653697.json、图片生成/图生图/修复光斑--修复曝光LORA---Qwen-Edit-2509_1987219668211576834.json、图片生成/图生图/全方位多视角调节图片_2077676206090182658.json…）

- **类型**：Image To Image
- **样本数**：30
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 30 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 28/30 个有
- `ModelSamplingAuraFlow` —— 28/30 个有
- `LoraLoaderModelOnly` —— 27/30 个有
- `CFGNorm` —— 25/30 个有
- `FluxKontextMultiReferenceLatentMethod` —— 24/30 个有
- `QwenMultiangleCameraNode` —— 23/30 个有
- `easy promptList` —— 20/30 个有
- `PreviewAny` —— 19/30 个有
- `FluxKontextImageScale` —— 7/30 个有
- `easy imageSize` —— 5/30 个有
- `Image Comparer (rgthree)` —— 2/30 个有
- `EmptyImage` —— 1/30 个有
- `FluxGuidance` —— 1/30 个有
- `LoraLoaderModelOnly_Any` —— 1/30 个有
- `PreviewImage` —— 1/30 个有
- `RepeatLatentBatch` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 30 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 30 | 51% |
| 采样算法 | euler | - | 30 | 93% |
| 调度器 | simple | - | 30 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 30 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/30 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，30 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，30 个样本
- 采样算法 最常用 euler，30 个样本，一致性 93%
- 调度器 最常用 simple，30 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 高发问题（29/30 个样本）：Steps较低可能导致细节不足
