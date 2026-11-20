---
name: image_to_image_sampler_clip_unet_118
type: Image To Image
frequency: 4
level: strong
coverage: 0.94775
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image Base 洗图_2016353054697725954.json, 图片生成/图生图/Z-image-Base-基础洗图_2017239330523189249.json, 图片生成/图生图/Z-image-base-洗图_2016877440781524993.json, 图片生成/图生图/qwen_image图生图支持中文_1953775268991303681.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_118

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z-image Base 洗图_2016353054697725954.json、图片生成/图生图/Z-image-Base-基础洗图_2017239330523189249.json、图片生成/图生图/Z-image-base-洗图_2016877440781524993.json、图片生成/图生图/qwen_image图生图支持中文_1953775268991303681.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `AILab_QwenVL` —— 2/4 个有
- `Float` —— 1/4 个有
- `Int` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 25 - 30 | 4 | 92% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 3.5 | 4 | 84% |
| 采样算法 | res_multistep | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.6 - 1 | 4 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 25 - 30，4 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 3.5，4 个样本，取值集中（一致性 84%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，4 个样本，取值集中（一致性 81%）
