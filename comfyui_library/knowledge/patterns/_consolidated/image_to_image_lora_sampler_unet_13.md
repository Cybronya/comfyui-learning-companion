---
name: image_to_image_lora_sampler_unet_13
type: Image To Image
frequency: 23
level: strong
coverage: 0.852609
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像转HDR ｜可调整曝光、恢复更多细节｜Qwen Image Edit 2511_2048131777956417538.json, 图片生成/图生图/图像转角度｜单张（一致性LoRA + 多角度LoRA）Qwen Edit 2511_2100019431236784130.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2009533490206871553.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2083366341913960449.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2083375355112550402.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2091742231643381762.json, 图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2101961996269871105.json, 图片生成/图生图/场景多角度分镜4.0((九视角）制作镜头qwen2511风格一致性分镜加速版4.0_2018924258122010625.json, 图片生成/图生图/多场景 多角度 分镜制作 qwen2511 风格一致性 分镜加速版3.0_2046210559363780610.json, 图片生成/图生图/多视角多角度人物道具场景视角加速版（九视角版本）已配置好（更多视角到工作流）_2009830651888930818.json, 图片生成/图生图/多视角影视人物多视角加速版（常用视角）_2009573649203863554.json, 图片生成/图生图/多视角（十视角）加速版，人物场景道具通用_2010525695197323265.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2011997466366844929.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2013597857110036482.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2016506996190617602.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2018227314567417857.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2020891798947762178.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2025792054508396546.json, 图片生成/图生图/多角度【手动控制】更精准-自由切换选择·高质量·快速出图_2071518519048630273.json, 图片生成/图生图/多角度分镜-qwen edit 2511_2009893386551037953.json, 图片生成/图生图/电商商品多角度自由控制角度【手动控制】_2018287831155744770.json, 图片生成/图生图/角度切换_自由切换_2071542576972386306.json, 视频生成/图生视频/图像转角度｜单张一致性LoRA_+_多角度LoRAQwen_Edit_2511_2100191664584351746.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/图像转HDR ｜可调整曝光、恢复更多细节｜Qwen Image Edit 2511_2048131777956417538.json、图片生成/图生图/图像转角度｜单张（一致性LoRA + 多角度LoRA）Qwen Edit 2511_2100019431236784130.json、图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2009533490206871553.json、图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2083366341913960449.json、图片生成/图生图/场景多角度分镜3.0制作镜头qwen2511风格一致性分镜加速版3.0qwenedit2511加速版_2083375355112550402.json…）

- **类型**：Image To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 23 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 21/23 个有
- `ImageScaleToTotalPixels` —— 13/23 个有
- `QwenMultiangleCameraNode` —— 13/23 个有
- `FluxKontextImageScale` —— 11/23 个有
- `easy promptList` —— 11/23 个有
- `CR Prompt List` —— 9/23 个有
- `Text Multiline` —— 9/23 个有
- `easy imageSize` —— 2/23 个有
- `Anything Everywhere3` —— 1/23 个有
- `EmptyImage` —— 1/23 个有
- `GearColorGrade` —— 1/23 个有
- `GearLogC3DecodeSaveEXR` —— 1/23 个有
- `PreviewImage` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 23 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 23 | 90% |
| 采样算法 | euler | - | 23 | 96% |
| 调度器 | simple | - | 23 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，23 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，23 个样本，取值集中（一致性 90%）
- 采样算法 最常用 euler，23 个样本，一致性 96%
- 调度器 最常用 simple，23 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（23/23 个样本）：Steps较低可能导致细节不足
