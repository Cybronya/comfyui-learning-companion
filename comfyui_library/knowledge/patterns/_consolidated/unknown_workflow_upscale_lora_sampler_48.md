---
name: unknown_workflow_upscale_lora_sampler_48
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.831
common_nodes: [CFGNorm, CLIPLoader, CR Text, EmptyLatentImage, GetImageSize, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImitationHueNode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageScaleDownBy]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一张图生成多姿势（qwen2509）_1974767448341745666.json, 图片生成/图生图/人物姿势完美迁移+人物变清晰（千问plus2509）_1974682142280167425.json, 图片生成/图生图/骨骼姿态控制 人物一致性 一张图生成多姿势 写真图片 9月最新升级+全节点注释_2054198133206331394.json, 视频生成/图生视频/骨骼姿态控制 人物一致性 一张图生成多姿势 写真图片 9月最新升级_1986387692915224577.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一张图生成多姿势（qwen2509）_1974767448341745666.json、图片生成/图生图/人物姿势完美迁移+人物变清晰（千问plus2509）_1974682142280167425.json、图片生成/图生图/骨骼姿态控制 人物一致性 一张图生成多姿势 写真图片 9月最新升级+全节点注释_2054198133206331394.json、视频生成/图生视频/骨骼姿态控制 人物一致性 一张图生成多姿势 写真图片 9月最新升级_1986387692915224577.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImitationHueNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageScaleDownBy`

**可变部分**（部分 workflow 才有）：
- `ImageConcatFromBatch` —— 3/4 个有
- `ImageFromBatch` —— 3/4 个有
- `ImpactMakeImageBatch` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `easy batchAnything` —— 3/4 个有
- `easy forLoopEnd` —— 3/4 个有
- `easy forLoopStart` —— 3/4 个有
- `easy imageCount` —— 3/4 个有
- `DWPreprocessor` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2m | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
