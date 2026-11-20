---
name: image_to_image_sampler_unet_vae_2
type: Image To Image
frequency: 30
level: weak
coverage: 0.840133
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2509 基础工作流_1971613466534539266.json, 图片生成/图生图/Qwen-Image-Edit-2511 多角度摄像控制_2009091314398269441.json, 图片生成/图生图/Qwen-Image-Edit-2511_2004929074399248386.json, 图片生成/图生图/Qwen-Image-Edit-2511多角度摄像_2016392343011725313.json, 图片生成/图生图/Qwen-Image可视化多角度人物调整_2010558787219890178.json, 图片生成/图生图/QwenEdit2511图片编辑 多角度生成工作流-B站UP主@好奇漫步_2065257036354506754.json, 图片生成/图生图/九个视角 人物道具 场景视角 加速版_2034191846393520129.json, 图片生成/图生图/人物场景多视图一键生成_2014235660437164034.json, 图片生成/图生图/全方位多视角调节图片_2077676206090182658.json, 图片生成/图生图/千问多角度控制lora_2013230266269044737.json, 图片生成/图生图/千问多角度控制lora_2016779041151393794.json, 图片生成/图生图/千问多角度控制lora，手动控制_2013226905612324866.json, 图片生成/图生图/千问多角度控制lora，手动控制_2033440618382364673.json, 图片生成/图生图/可视化摄像机角度调节，一键生成图像多视角_2004504081580388354.json, 图片生成/图生图/图像转角度｜单张（一致性LoRA + 多角度LoRA）Qwen Edit 2511_2100019431236784130.json, 图片生成/图生图/场景多视角_2016036160287543298.json, 图片生成/图生图/场景多视角镜头_2010978287455051777.json, 图片生成/图生图/多视角多角度人物道具场景视角加速版（九视角版本）已配置好（更多视角到工作流）_2009830651888930818.json, 图片生成/图生图/多视角（十视角）加速版，人物场景道具通用_2010525695197323265.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2011997466366844929.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2013597857110036482.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2016506996190617602.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2018227314567417857.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2020891798947762178.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2025792054508396546.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2071518519048630273.json, 图片生成/图生图/对镜自拍Qwen2511-multiple-angles多角度工作流+全节点注释_2041417500948172801.json, 图片生成/图生图/电商商品多角度自由控制角度【手动控制】_2018287831155744770.json, 图片生成/图生图/角度切换_自由切换_2071542576972386306.json, 视频生成/图生视频/图像转角度｜单张一致性LoRA_+_多角度LoRAQwen_Edit_2511_2100191664584351746.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2509 基础工作流_1971613466534539266.json、图片生成/图生图/Qwen-Image-Edit-2511 多角度摄像控制_2009091314398269441.json、图片生成/图生图/Qwen-Image-Edit-2511_2004929074399248386.json、图片生成/图生图/Qwen-Image-Edit-2511多角度摄像_2016392343011725313.json、图片生成/图生图/Qwen-Image可视化多角度人物调整_2010558787219890178.json…）

- **类型**：Image To Image
- **样本数**：30
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 30 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 29/30 个有
- `LoraLoaderModelOnly` —— 29/30 个有
- `ImageScaleToTotalPixels` —— 27/30 个有
- `QwenMultiangleCameraNode` —— 27/30 个有
- `easy promptList` —— 24/30 个有
- `PreviewAny` —— 20/30 个有
- `FluxKontextImageScale` —— 5/30 个有
- `ShowText|pysssss` —— 5/30 个有
- `easy imageSize` —— 2/30 个有
- `CR Text Concatenate` —— 1/30 个有
- `EmptyImage` —— 1/30 个有
- `LayerUtility: ImageReel` —— 1/30 个有
- `LayerUtility: ImageReelComposit` —— 1/30 个有
- `PreviewImage` —— 1/30 个有
- `PrimitiveStringMultiline` —— 1/30 个有
- `RH_Translator` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 30 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 30 | 38% |
| 采样算法 | euler | - | 30 | 97% |
| 调度器 | simple | - | 30 | 97% |
| 重绘幅度 | 1 | 1 - 1 | 30 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/30 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，30 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，30 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，30 个样本，一致性 97%
- 调度器 最常用 simple，30 个样本，一致性 97%
- 重绘幅度 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 高发问题（28/30 个样本）：Steps较低可能导致细节不足
