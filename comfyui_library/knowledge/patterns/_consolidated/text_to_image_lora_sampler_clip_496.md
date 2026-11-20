---
name: text_to_image_lora_sampler_clip_496
type: Text To Image
frequency: 4
level: strong
coverage: 0.911
common_nodes: [AILab_QwenVL, AddLabel, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, ImageConcatMulti, ImagesConcanateToGrid, KSampler, Label (rgthree), LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, ResolutionSelector, SaveImage, Seed (rgthree), StringConcatenate, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy cleanGpuUsed, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy showAnything, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS -Image - Beauty -LoRA (适合人像)_2117016899681873922.json, 图片生成/文生图/MOSS Image工作流合集_2113152333101232129.json, 图片生成/文生图/MOSS Image工作流合集_2115641057986830338.json, 视频生成/图生视频/MOSS_Image工作流合集_2115251783256858625.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_496

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/MOSS -Image - Beauty -LoRA (适合人像)_2117016899681873922.json、图片生成/文生图/MOSS Image工作流合集_2113152333101232129.json、图片生成/文生图/MOSS Image工作流合集_2115641057986830338.json、视频生成/图生视频/MOSS_Image工作流合集_2115251783256858625.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageConcatMulti`
- `ImagesConcanateToGrid`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `StringConcatenate`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 50 | 50 - 50 | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 50 - 50，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
