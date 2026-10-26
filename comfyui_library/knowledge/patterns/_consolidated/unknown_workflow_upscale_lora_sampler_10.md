---
name: unknown_workflow_upscale_lora_sampler_10
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.929625
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Model Input Switch, EmptyLatentImage, FluxGuidance, GetImageSize, ImageResizeKJ, ImageUpscaleWithModel, KSamplerSelect, LoadImage, ModelSamplingFlux, Number to Int, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RH_Captioner, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, Text to Number, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/reduxV2-反推洗图万能流_2049374493121974273.json, 图片生成/反推提示词/反推洗图万能流_2066494855731310593.json, 图片生成/图生图/reduxV2-反推洗图万能流_1932236006693437441.json, 图片生成/图生图/reduxV2-反推洗图万能流_1957731194199965697.json, 图片生成/图生图/reduxV2-反推洗图万能流_2039339997765050369.json, 图片生成/图生图/reduxV2-反推洗图万能流_2039350395746656257.json, 图片生成/图生图/reduxV2-反推洗图万能流_2082016128121004033.json, 图片生成/图生图/reduxV2-反推洗图万能流_2086653747555561474.json, 图片生成/图生图/reduxV2-反推洗图万能流_2090263579768483841.json, 图片生成/图生图/reduxV2-反推洗图万能流_2104757049266622466.json, 图片生成/图生图/反推洗图万能流---eduxV2_2068061825878548482.json, 图片生成/图生图/反推洗图万能流---eduxV2_2068179172471693314.json, 图片生成/图生图/洗图反推图片工作流_2046057407863857154.json, 图片生成/图生图/超好用🔥图片反推工作流，风格画作-看上什么画风直接截图_2046487806398173186.json, 数字人/数字人/reduxV2-反推洗图万能流_2041584997311717377.json, 视频生成/图生视频/3.0最新反推洗图万能流_2066082702180311041.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/反推提示词/reduxV2-反推洗图万能流_2049374493121974273.json、图片生成/反推提示词/反推洗图万能流_2066494855731310593.json、图片生成/图生图/reduxV2-反推洗图万能流_1932236006693437441.json、图片生成/图生图/reduxV2-反推洗图万能流_1957731194199965697.json、图片生成/图生图/reduxV2-反推洗图万能流_2039339997765050369.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Model Input Switch`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetImageSize`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `Number to Int`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RH_Captioner`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `Text to Number`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 15/16 个有
- `Image Comparer (rgthree)` —— 2/16 个有
- `Get Image Size` —— 1/16 个有
- `ImageScale` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 16 | 100% |
| 高度 | 512 | 512 - 512 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，16 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，16 个样本，取值集中（一致性 100%）
