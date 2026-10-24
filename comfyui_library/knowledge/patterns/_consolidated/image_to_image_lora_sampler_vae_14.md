---
name: image_to_image_lora_sampler_vae_14
type: Image To Image
frequency: 5
level: strong
coverage: 0.855
common_nodes: [ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511视角转换_2011479861298208770.json, 图片生成/图生图/251225001.005.QwenEdit2511一图多角度_2004204630026448898.json, 图片生成/图生图/LH-DMT版本-2.生图片类-045.QwenEdit2511一图多角度_2016524860691845122.json, 图片生成/图生图/QwenEdit2511产品多角度_2009334297819353089.json, 图片生成/文生图/Gemini3.5 笔记本手账生成+全节点注释_2058861210543673345.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_14

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2511视角转换_2011479861298208770.json、图片生成/图生图/251225001.005.QwenEdit2511一图多角度_2004204630026448898.json、图片生成/图生图/LH-DMT版本-2.生图片类-045.QwenEdit2511一图多角度_2016524860691845122.json、图片生成/图生图/QwenEdit2511产品多角度_2009334297819353089.json、图片生成/文生图/Gemini3.5 笔记本手账生成+全节点注释_2058861210543673345.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/5 个有
- `VAELoader` —— 4/5 个有
- `UnetLoaderGGUF` —— 3/5 个有
- `easy promptLine` —— 3/5 个有
- `Text` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `QwenMultiangleCameraNode` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `UNETLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
