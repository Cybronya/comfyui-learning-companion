---
name: unknown_workflow_face_detailer_lora_sampler
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.728333
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, DifferentialDiffusion, FaceDetailer, HighRes-Fix Script, KSampler (Efficient), LoraLoader, PrimitiveStringMultiline, SAMLoader, SaveImage, Seed Everywhere, StringFunction|pysssss, UltralyticsDetectorProvider]
problems: []
missing: [HighRes-Fix Script, StringFunction|pysssss, KSampler (Efficient), SDXLEmptyLatentSizePicker+, Seed Everywhere]
members: [图片生成/文生图/1959080276469166081.json, 图片生成/文生图/illustrious-3D-CG风格YunY_2065363292136501248.json, 图片生成/文生图/illustrious-yunying-3d_2083898984397099009.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_lora_sampler

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1959080276469166081.json、图片生成/文生图/illustrious-3D-CG风格YunY_2065363292136501248.json、图片生成/文生图/illustrious-yunying-3d_2083898984397099009.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DifferentialDiffusion`
- `FaceDetailer`
- `HighRes-Fix Script`
- `KSampler (Efficient)`
- `LoraLoader`
- `PrimitiveStringMultiline`
- `SAMLoader`
- `SaveImage`
- `Seed Everywhere`
- `StringFunction|pysssss`
- `UltralyticsDetectorProvider`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `SDXLEmptyLatentSizePicker+` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `UltimateSDUpscale` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LoadImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 28 | 3 | 95% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 864 | - | 2 | 100% |
| 高度 | 1536 | 1 - 1536 | 3 | 29% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 3 | 89% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 28，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 864，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1 - 1536，3 个样本，取值分散，一致性仅 29%
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，3 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：HighRes-Fix Script、StringFunction|pysssss、KSampler (Efficient)、SDXLEmptyLatentSizePicker+、Seed Everywhere
