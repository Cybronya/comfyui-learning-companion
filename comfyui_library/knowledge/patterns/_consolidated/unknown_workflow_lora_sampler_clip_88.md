---
name: unknown_workflow_lora_sampler_clip_88
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.933857
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApplySimple, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/无需提示词，图生IP三视图_1911780889070895106.json, 图片生成/图生图/照片一键转绘 全能图片G-4o 吉卜力风格_1913046305365553153.json, 图片生成/图生图/美式喜剧风格插画_全能图片G4o(同款)_1909846224130797569.json, 平台全量/F.1 复古风格头像_1889917217784602625.json, 平台全量/Flux一键像素风头像_1866030337162637314.json, 平台全量/【转吉卜力风格】全能图片G-4o版吉卜力风格_1908754978499141634.json, 平台全量/超女superwoman_1867824818929418242.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/无需提示词，图生IP三视图_1911780889070895106.json、图片生成/图生图/照片一键转绘 全能图片G-4o 吉卜力风格_1913046305365553153.json、图片生成/图生图/美式喜剧风格插画_全能图片G4o(同款)_1909846224130797569.json、平台全量/F.1 复古风格头像_1889917217784602625.json、平台全量/Flux一键像素风头像_1866030337162637314.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApplySimple`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 6/7 个有
- `PulidEvaClipLoader` —— 6/7 个有
- `PulidFluxModelLoader` —— 6/7 个有
- `PulidInsightFaceLoader` —— 6/7 个有
- `ModelSamplingFlux` —— 5/7 个有
- `EmptySD3LatentImage` —— 4/7 个有
- `PreviewImage` —— 2/7 个有
- `VAEEncode` —— 2/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `ControlNetApplySD3` —— 1/7 个有
- `ControlNetLoader` —— 1/7 个有
- `DF_Get_image_size` —— 1/7 个有
- `EmptyLatentImage` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageResizeKJ` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy promptConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 1 | 100% |
| 宽度 | 1536 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
