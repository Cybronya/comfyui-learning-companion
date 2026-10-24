---
name: image_to_image_sampler_clip_unet_31
type: Image To Image
frequency: 10
level: strong
coverage: 0.925
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, ImageScaleDownToSize, KSampler, LoadImage, SaveImage, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX-krea + LoRA 洗图｜高质量图像_1951115644588728322.json, 图片生成/图生图/FLUX-krea最新模型图生图更真实_1951086054793224194.json, 图片生成/图生图/Flux.1 Krea Dev图生图【逼真质感 无AI味】_1951177506269409281.json, 图片生成/图生图/Flux.1 Krea Dev：图生图革新，独特风格再塑！Krea去除AI感_图生图洗图_1951069893238173698.json, 图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味超细节_1951506881573498882.json, 图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味逼真质感_1950940521936125954.json, 图片生成/图生图/Flux.1-Krea-Dev图生图｜无 AI 感洗图_1951117735654793217.json, 图片生成/图生图/Flux图生图-电影感无AI味_1991140862363041793.json, 图片生成/图生图/无AI特征逼真质感生图Flux.1-Krea_1991133381247238146.json, 图片生成/文生图/FLUX-krea最新模型图生图（超级真实去AI味+自动提示词+批量）_1951085916716736514.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/FLUX-krea + LoRA 洗图｜高质量图像_1951115644588728322.json、图片生成/图生图/FLUX-krea最新模型图生图更真实_1951086054793224194.json、图片生成/图生图/Flux.1 Krea Dev图生图【逼真质感 无AI味】_1951177506269409281.json、图片生成/图生图/Flux.1 Krea Dev：图生图革新，独特风格再塑！Krea去除AI感_图生图洗图_1951069893238173698.json、图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味超细节_1951506881573498882.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `ImageScaleDownToSize`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 9/10 个有
- `RepeatLatentBatch` —— 9/10 个有
- `easy showAnything` —— 7/10 个有
- `ImageStitch` —— 6/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `RH_LLMAPI_NODE` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `Florence2ModelLoader` —— 1/10 个有
- `Florence2Run` —— 1/10 个有
- `NunchakuFluxDiTLoader` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `easy imageConcat` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 0.95 | 0.6 - 1 | 10 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 0.95，观测区间 0.6 - 1，10 个样本，取值集中（一致性 85%）
