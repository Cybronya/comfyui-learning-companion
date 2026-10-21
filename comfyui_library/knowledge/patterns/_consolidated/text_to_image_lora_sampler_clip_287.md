---
name: text_to_image_lora_sampler_clip_287
type: Text To Image
frequency: 3
level: strong
coverage: 0.87
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ComfyMathExpression, EmptyLatentImage, ImageFromBatch, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy imageConcat, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物迁移MiniMax图像编辑API版工作流，局部重绘角色一致性图生图方案_2107254089863229441.json, 图片生成/图生图/人物迁移MiniMax图像编辑免费版工作流，局部重绘角色一致性图生图方案_2107251066072035329.json, 图片生成/图生图/服装迁移超高一致性H3图像编辑工作流，风格迁移图生图图案迁移工具_2107222093061513218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_287

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人物迁移MiniMax图像编辑API版工作流，局部重绘角色一致性图生图方案_2107254089863229441.json、图片生成/图生图/人物迁移MiniMax图像编辑免费版工作流，局部重绘角色一致性图生图方案_2107251066072035329.json、图片生成/图生图/服装迁移超高一致性H3图像编辑工作流，风格迁移图生图图案迁移工具_2107222093061513218.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ImageFromBatch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `MiniMaxH3UnifiedToVideo` —— 2/3 个有
- `RHLLMChatNode` —— 2/3 个有
- `easy imageInsetCrop` —— 2/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `Qwen3VL_Chat` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `VAEDecodeAudio` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
