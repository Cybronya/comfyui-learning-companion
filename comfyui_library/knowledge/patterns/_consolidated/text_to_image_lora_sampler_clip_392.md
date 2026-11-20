---
name: text_to_image_lora_sampler_clip_392
type: Text To Image
frequency: 5
level: strong
coverage: 0.8238
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image2.1姿势迁移 人物姿态精准控制_2108663641737351170.json, 图片生成/图生图/Qwen2.1 Image图片编辑工作流，指令式修图快速精准高效出图_2115012462922780674.json, 图片生成/图生图/Qwen_Image2.1姿势迁移，局部重绘动作迁移图生图_2111949159719849985.json, 图片生成/图生图/换姿势QwenImage2.1原生controlNet 姿态精准控制_2108672987565223937.json, 图片生成/文生图/AI换装Qwen Image 2.1双图试穿智能提示词 服装展示方案_2108655915309289474.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_392

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image2.1姿势迁移 人物姿态精准控制_2108663641737351170.json、图片生成/图生图/Qwen2.1 Image图片编辑工作流，指令式修图快速精准高效出图_2115012462922780674.json、图片生成/图生图/Qwen_Image2.1姿势迁移，局部重绘动作迁移图生图_2111949159719849985.json、图片生成/图生图/换姿势QwenImage2.1原生controlNet 姿态精准控制_2108672987565223937.json、图片生成/文生图/AI换装Qwen Image 2.1双图试穿智能提示词 服装展示方案_2108655915309289474.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 4/5 个有
- `QwenImage21Cache` —— 4/5 个有
- `CR Text Concatenate` —— 3/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `Int` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `OpenposePreprocessor` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `kkGetImage` —— 3/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `JsonExtractString` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
