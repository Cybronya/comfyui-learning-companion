---
name: text_to_image_lora_sampler_clip_293
type: Text To Image
frequency: 3
level: strong
coverage: 0.911333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CLIPVisionEncode, CLIPVisionLoader, CR Text, DF_Text_Box, DetailDaemonSamplerNode, DualCLIPLoader, EmptyLatentImage, Image Comparer (rgthree), JWImageResizeByLongerSide, Joy_caption_two, Joy_caption_two_load, KSampler, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StyleModelApplySimple, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/文生图/1985668347650088962.json, 图片生成/文生图/工作流项目篇10-萌宠合影趣味写真照(内含洗图工作流)_2016702922922397697.json, 图片生成/文生图/萌宠合影趣味写真（含洗图）_2061367052845281281.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_293

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1985668347650088962.json、图片生成/文生图/工作流项目篇10-萌宠合影趣味写真照(内含洗图工作流)_2016702922922397697.json、图片生成/文生图/萌宠合影趣味写真（含洗图）_2061367052845281281.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `DF_Text_Box`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JWImageResizeByLongerSide`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelApplySimple`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 896 - 896 | 3 | 100% |
| 高度 | 1152 | 1152 - 1152 | 3 | 100% |
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 896 - 896，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，观测区间 1152 - 1152，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
