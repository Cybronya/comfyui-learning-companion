---
name: unknown_workflow_face_detailer_lora_sampler_3
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78475
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, DifferentialDiffusion, FaceDetailer, HighRes-Fix Script, KSampler (Efficient), LoraLoader, PrimitiveStringMultiline, SAMLoader, SaveImage, Seed Everywhere, StringFunction|pysssss, UltralyticsDetectorProvider]
problems: []
missing: []
members: [图片生成/文生图/[T2I] 文生图-二次元_动漫人物高质量生成 （IL）_1959080276469166081.json, 图片生成/文生图/illustrious-3D-CG风格YunY-海边_2065363274876940288.json, 图片生成/文生图/illustrious-3D-CG风格YunY_2065363292136501248.json, 图片生成/文生图/illustrious-yunying-3d_2083898984397099009.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/[T2I] 文生图-二次元_动漫人物高质量生成 （IL）_1959080276469166081.json、图片生成/文生图/illustrious-3D-CG风格YunY-海边_2065363274876940288.json、图片生成/文生图/illustrious-3D-CG风格YunY_2065363292136501248.json、图片生成/文生图/illustrious-yunying-3d_2083898984397099009.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CompressImages` —— 3/4 个有
- `EmptyLatentImage` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `SDXLEmptyLatentSizePicker+` —— 3/4 个有
- `UltimateSDUpscale` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `SetNode` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 28 | 4 | 95% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 864 | 864 - 1536 | 3 | 71% |
| 高度 | 1200 | 1 - 1536 | 4 | 36% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 4 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 28，4 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 864，观测区间 864 - 1536，3 个样本
- 高度 中位数 1200，观测区间 1 - 1536，4 个样本，取值分散，一致性仅 36%
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，4 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
