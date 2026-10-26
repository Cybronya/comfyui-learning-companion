---
name: text_to_image_lora_sampler_clip_465
type: Text To Image
frequency: 4
level: moderate
coverage: 0.855
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Alan测试-文生图_图生图_Klein+Zimage 双采样_极致真实感_2042969313996447745.json, 图片生成/文生图/alan测-文生图_图生图_Klein+Zimage 双采样_极致真实感_2042970533716824066.json, 图片生成/文生图/文生图_图生图_Klein+Zimage 双采样_极致真实感_2014477964599107585.json, 图片生成/文生图/生图_洗图_极致细节_Qwen-image+Klein_2031714866574139394.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_465

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Alan测试-文生图_图生图_Klein+Zimage 双采样_极致真实感_2042969313996447745.json、图片生成/文生图/alan测-文生图_图生图_Klein+Zimage 双采样_极致真实感_2042970533716824066.json、图片生成/文生图/文生图_图生图_Klein+Zimage 双采样_极致真实感_2014477964599107585.json、图片生成/文生图/生图_洗图_极致细节_Qwen-image+Klein_2031714866574139394.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 3/4 个有
- `workflow>自定义采样器` —— 3/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageSharpen` —— 1/4 个有
- `PainterFluxImageEdit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 15 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 4 | 65% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 75% |
| 重绘幅度 | 0.7 | 0.7 - 1 | 4 | 83% |
| 宽度 | 768 | 768 - 1080 | 4 | 84% |
| 高度 | 1080 | 1080 - 1960 | 4 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 15，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 1，4 个样本，取值集中（一致性 83%）
- 宽度 中位数 768，观测区间 768 - 1080，4 个样本，取值集中（一致性 84%）
- 高度 中位数 1080，观测区间 1080 - 1960，4 个样本
