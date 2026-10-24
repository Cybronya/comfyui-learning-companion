---
name: unknown_workflow_sampler_clip_unet_176
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.858
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Deepseek-janus-Pro精准反推图生图FLUX (1)_1896094012430811138.json, 图片生成/图生图/FLUX_图生图_赛博朋克风格V1.0_1922702310974308353.json, 图片生成/图生图/Flux 一键洗图_1920407438544277505.json, 图片生成/图生图/flux_吉卜力风格_图生图_1922695650230812674.json, 图片生成/图生图/修图重绘-常用_2006036350398631937.json, 图片生成/图生图/修图重绘_1939903917381881857.json, 图片生成/文生图/flux图生图-在线生图_1995862598363099137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_176

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Deepseek-janus-Pro精准反推图生图FLUX (1)_1896094012430811138.json、图片生成/图生图/FLUX_图生图_赛博朋克风格V1.0_1922702310974308353.json、图片生成/图生图/Flux 一键洗图_1920407438544277505.json、图片生成/图生图/flux_吉卜力风格_图生图_1922695650230812674.json、图片生成/图生图/修图重绘-常用_2006036350398631937.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 6/7 个有
- `CR Latent Batch Size` —— 5/7 个有
- `Florence2ModelLoader` —— 5/7 个有
- `Florence2Run` —— 5/7 个有
- `ImageResize+` —— 5/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `CR Text Concatenate` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `TextInput_` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `JanusImageUnderstanding` —— 2/7 个有
- `JanusModelLoader` —— 2/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `ttN advPlot images` —— 1/7 个有
- `ttN advanced xyPlot` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 6 | 78% |
| LoRA 文本强度 | 1 | 1 - 10.48 | 6 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，6 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 10.48，6 个样本，取值分散，一致性仅 0%
