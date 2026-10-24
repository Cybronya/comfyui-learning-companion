---
name: image_to_image_lora_sampler_unet_38
type: Image To Image
frequency: 13
level: strong
coverage: 0.985
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图(一生三图版)_2039549230775279618.json, 图片生成/图生图/图生图111_2039507362217730050.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2093239766459437058.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2096233939248701441.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2096414871079444482.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2109487018899234818.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2109491082986868738.json, 图片生成/图生图/图生图—转手绘线条水彩风格_2086717758758281217.json, 图片生成/图生图/图转粗线条水彩_2027575355669745666.json, 图片生成/图生图/图转速写线稿_2019680136496418817.json, 图片生成/图生图/手动调整角度工作流_2064900917597659137.json, 图片生成/图生图/角度调节_2102280831946547201.json, 视频生成/图生视频/qwen2511图转速手绘线条水彩风格_2088151301396975617.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_38

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/图生图(一生三图版)_2039549230775279618.json、图片生成/图生图/图生图111_2039507362217730050.json、图片生成/图生图/图生图—一键转手绘线条水彩风_2093239766459437058.json、图片生成/图生图/图生图—一键转手绘线条水彩风_2096233939248701441.json、图片生成/图生图/图生图—一键转手绘线条水彩风_2096414871079444482.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 9/13 个有
- `ReferenceLatent` —— 9/13 个有
- `ResizeImagesByLongerEdge` —— 7/13 个有
- `QwenMultiangleCameraNode` —— 4/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/13 个有
- `CFGNorm` —— 2/13 个有
- `KepStringList` —— 2/13 个有
- `Anything Everywhere3` —— 1/13 个有
- `Image Comparer (rgthree)` —— 1/13 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/13 个有
- `ResizeShortestToNode` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 12 | 13 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | beta | - | 13 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 12，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
