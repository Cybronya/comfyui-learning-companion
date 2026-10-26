---
name: image_to_image_lora_sampler_unet_12
type: Image To Image
frequency: 24
level: moderate
coverage: 0.995708
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511图转手绘线条水彩风格图片风格化_2078074989806444546.json, 图片生成/图生图/qwen2511图转手绘线条水彩风格图片风格化_2078077711209291777.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2026148427746254850.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2067415744551411714.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2067446975695511554.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2072947797464276994.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2075144823752978433.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2077588149060067330.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2077666313538990082.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2079102882938445826.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2095794944433811458.json, 图片生成/图生图/qwen2511图转速手绘线条水彩风格_2096151173555380225.json, 图片生成/图生图/qwen2511真人转手绘线条画风_2089264984500035585.json, 图片生成/图生图/qwen万能lora控图_1960703410297344001.json, 图片生成/图生图/【阡陌】Qwen-Image六合一In Context Controlnet lora精准控制工作流_1960248554344361985.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2093239766459437058.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2096233939248701441.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2096414871079444482.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2109487018899234818.json, 图片生成/图生图/图生图—一键转手绘线条水彩风_2109491082986868738.json, 图片生成/图生图/图生图—转手绘线条水彩风格_2086717758758281217.json, 图片生成/图生图/图转粗线条水彩_2027575355669745666.json, 图片生成/图生图/图转速写线稿_2019680136496418817.json, 图片生成/文生图/Qwen-Image的union cn_1958888407248351234.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/qwen2511图转手绘线条水彩风格图片风格化_2078074989806444546.json、图片生成/图生图/qwen2511图转手绘线条水彩风格图片风格化_2078077711209291777.json、图片生成/图生图/qwen2511图转速手绘线条水彩风格_2026148427746254850.json、图片生成/图生图/qwen2511图转速手绘线条水彩风格_2067415744551411714.json、图片生成/图生图/qwen2511图转速手绘线条水彩风格_2067446975695511554.json…）

- **类型**：Image To Image
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 21/24 个有
- `TextEncodeQwenImageEditPlus` —— 21/24 个有
- `ResizeImagesByLongerEdge` —— 19/24 个有
- `AIO_Preprocessor` —— 3/24 个有
- `CLIPTextEncode` —— 3/24 个有
- `PreviewImage` —— 2/24 个有
- `EmptySD3LatentImage` —— 1/24 个有
- `ImageResizeKJv2` —— 1/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/24 个有
- `String Literal` —— 1/24 个有
- `TextBox` —— 1/24 个有
- `easy seed` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 30 | 24 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 24 | 72% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | beta | - | 24 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 30，24 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，24 个样本
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
