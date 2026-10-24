---
name: image_to_image_sampler_clip_unet_82
type: Image To Image
frequency: 6
level: strong
coverage: 0.912667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片黑白渲染变成彩色_1979817875533893634.json, 图片生成/图生图/手办模型_1961814911435345921.json, 图片生成/图生图/手办模型盲盒_2047665313591857154.json, 图片生成/图生图/手办模型盲盒_2063493693570633730.json, 图片生成/图生图/矢量插画风格-一键转绘_1969793417184243714.json, 图片生成/图生图/自动溶图_Kontext_1950812344156880897.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_82

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/图片黑白渲染变成彩色_1979817875533893634.json、图片生成/图生图/手办模型_1961814911435345921.json、图片生成/图生图/手办模型盲盒_2047665313591857154.json、图片生成/图生图/手办模型盲盒_2063493693570633730.json、图片生成/图生图/矢量插画风格-一键转绘_1969793417184243714.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 5/6 个有
- `FluxKontextImageScale` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `ACE_TextGoogleTranslate` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `JoinStrings` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `String` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
