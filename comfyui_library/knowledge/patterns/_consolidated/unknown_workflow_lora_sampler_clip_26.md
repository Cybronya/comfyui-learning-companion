---
name: unknown_workflow_lora_sampler_clip_26
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.925154
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/10秒一键漫画感工作流_1889889417681838082.json, 图片生成/图生图/flux-redux-创意迁移-logo设计_1950208575371173889.json, 图片生成/图生图/全能图片G 同款吉卜力风格_1909795874137145345.json, 图片生成/图生图/全能图片G-4o版吉卜力风格_1912018910508711937.json, 图片生成/图生图/全能图片G-4o版吉卜力风格_1914282497189052417.json, 图片生成/图生图/全能图片G4o同款一键定制吊卡公仔_1911777214587961345.json, 图片生成/图生图/抖音同款_治愈系儿童绘本_1914188492946010114.json, 图片生成/图生图/涂鸦手绘风格-图生图转绘_1943146154374946818.json, 图片生成/图生图/真人照片改漫画_1888207245665001474.json, 平台全量/人物转涂鸦-Flux_1959320906428526594.json, 平台全量/动漫形象_1868962191436324865.json, 平台全量/手绘新年涂鸦形象_1869302388795547650.json, 平台全量/梦幻油画风格形象_1871848089949503490.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/10秒一键漫画感工作流_1889889417681838082.json、图片生成/图生图/flux-redux-创意迁移-logo设计_1950208575371173889.json、图片生成/图生图/全能图片G 同款吉卜力风格_1909795874137145345.json、图片生成/图生图/全能图片G-4o版吉卜力风格_1912018910508711937.json、图片生成/图生图/全能图片G-4o版吉卜力风格_1914282497189052417.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 12/13 个有
- `CLIPVisionEncode` —— 12/13 个有
- `PulidEvaClipLoader` —— 12/13 个有
- `PulidFluxModelLoader` —— 12/13 个有
- `PulidInsightFaceLoader` —— 12/13 个有
- `StyleModelApplySimple` —— 12/13 个有
- `EmptyLatentImage` —— 9/13 个有
- `JjkText` —— 8/13 个有
- `TextCombinerTwo` —— 8/13 个有
- `FluxResolutionNode` —— 7/13 个有
- `RH_Captioner` —— 7/13 个有
- `ShowText|pysssss` —— 6/13 个有
- `Label (rgthree)` —— 4/13 个有
- `LayerColor: Brightness & Contrast` —— 4/13 个有
- `ImageResizeKJ` —— 3/13 个有
- `VAEEncode` —— 3/13 个有
- `Anything Everywhere` —— 1/13 个有
- `CR Text Replace` —— 1/13 个有
- `ChinesePrompt_Mix` —— 1/13 个有
- `DF_Get_image_size` —— 1/13 个有
- `EmptySD3LatentImage` —— 1/13 个有
- `ModelSamplingFlux` —— 1/13 个有
- `RH_Prompter` —— 1/13 个有
- `TextCombinerSix` —— 1/13 个有
- `YC_LG_Redux` —— 1/13 个有
- `workflow/展示文本` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 9 | 83% |
| 高度 | 1280 | 512 - 1280 | 9 | 79% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，9 个样本，取值集中（一致性 83%）
- 高度 中位数 1280，观测区间 512 - 1280，9 个样本
