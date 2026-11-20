---
name: image_to_image_controlnet_ipadapter_upscale_3
type: Image To Image
frequency: 4
level: strong
coverage: 0.88375
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, IPAdapterAdvanced, IPAdapterModelLoader, KSampler, KSamplerSelect, LoadImage, OpenposePreprocessor, PreviewImage, RandomNoise, SDXLEmptyLatentSizePicker+, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux 人物一致性，多视角人物_1915228748579540994.json, 图片生成/图生图/flux人物多视角一键生成_1917156480104206337.json, 平台全量/Flux Consistent Character Sheet_1868838232778752001.json, 平台全量/人物设计图 Flux refine_1820866898295984129.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux 人物一致性，多视角人物_1915228748579540994.json、图片生成/图生图/flux人物多视角一键生成_1917156480104206337.json、平台全量/Flux Consistent Character Sheet_1868838232778752001.json、平台全量/人物设计图 Flux refine_1820866898295984129.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `OpenposePreprocessor`
- `PreviewImage`
- `RandomNoise`
- `SDXLEmptyLatentSizePicker+`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Save` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `TextWildcardList_AS` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1216x832 (1.46) | - | 4 | 75% |
| 高度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 4 | 4 - 5 | 4 | 90% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 4 | 100% |
| 采样算法 | dpmpp_sde | - | 4 | 75% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 最常用 1216x832 (1.46)，4 个样本，一致性 75%
- 高度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 5，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，4 个样本，一致性 75%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
