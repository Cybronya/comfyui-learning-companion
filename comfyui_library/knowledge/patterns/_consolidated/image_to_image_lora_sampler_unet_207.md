---
name: image_to_image_lora_sampler_unet_207
type: Image To Image
frequency: 3
level: moderate
coverage: 0.620333
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json, 图片生成/文生图/面料印花提取工作流｜Qwen Image Edit+花纹LoRA，去褶皱去背景全注释+全节点注释_2060980136811520002.json, 数字人/数字人/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版_2042627893414596610.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_207

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json、图片生成/文生图/面料印花提取工作流｜Qwen Image Edit+花纹LoRA，去褶皱去背景全注释+全节点注释_2060980136811520002.json、数字人/数字人/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版_2042627893414596610.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 2/3 个有
- `Int` —— 2/3 个有
- `TextEncodeQwenImageEdit` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Float` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `QwenMultiangleCameraNode` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
