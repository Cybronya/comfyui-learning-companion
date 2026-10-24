---
name: unknown_workflow_controlnet_lora_sampler_8
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6658
common_nodes: [CR Prompt Text, CheckpointLoaderSimple, DWPreprocessor, INTConstant, JWStringConcat, LayerColor: AutoAdjustV2, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, QwenImageControlNetIntegratedLoader, QwenImageIntegratedKSampler, SaveImage, Text Multiline, easy promptLine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Qwen-AIO大合集 支持单图编辑，姿势迁移，人物换装，多场景分镜_2004199516708503554.json, 图片生成/图生图/qwen aio 大全_2045218618383802369.json, 图片生成/图生图/单图编辑_2110712248527319042.json, 图片生成/图生图/大合集 支持单图编辑，姿势迁移，人物换装，多场景分镜_2056018251020292098.json, 视频生成/图生视频/Qwen-AIO全能图像大合集｜单图编辑_姿势迁移_人物换装_2109096922601582593.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_8

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-AIO大合集 支持单图编辑，姿势迁移，人物换装，多场景分镜_2004199516708503554.json、图片生成/图生图/qwen aio 大全_2045218618383802369.json、图片生成/图生图/单图编辑_2110712248527319042.json、图片生成/图生图/大合集 支持单图编辑，姿势迁移，人物换装，多场景分镜_2056018251020292098.json、视频生成/图生视频/Qwen-AIO全能图像大合集｜单图编辑_姿势迁移_人物换装_2109096922601582593.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 5 个 workflow 都包含：
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `DWPreprocessor`
- `INTConstant`
- `JWStringConcat`
- `LayerColor: AutoAdjustV2`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `QwenImageControlNetIntegratedLoader`
- `QwenImageIntegratedKSampler`
- `SaveImage`
- `Text Multiline`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `Anything Everywhere3` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | 512 | 512 - 512 | 5 | 100% |
| 调度器 | 768 | 768 - 768 | 5 | 100% |
| 重绘幅度 | 6.36025e+14 | 3.07854e+14 - 9.90455e+14 | 5 | 62% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 调度器 中位数 768，观测区间 768 - 768，5 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 6.36025e+14，观测区间 3.07854e+14 - 9.90455e+14，5 个样本
- 风险：重绘幅度 观测到 9.90455e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
