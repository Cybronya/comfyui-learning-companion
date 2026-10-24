---
name: text_to_image_lora_sampler_clip_225
type: Text To Image
frequency: 8
level: strong
coverage: 0.886125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ComfyMathExpression, EmptyLatentImage, ImageFromBatch, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy imageConcat, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Minimax图像编辑API版｜图生图换人角色一致稳定输出_2110678895354793985.json, 图片生成/图生图/Minimax图像编辑免费版｜局部重绘人物替换角色一致性不崩_2110677343311327233.json, 图片生成/图生图/minimax图像编辑API版人物替换，局部重绘角色一致_2110835438633181185.json, 图片生成/图生图/人物迁移MiniMax图像编辑API版工作流，局部重绘角色一致性图生图方案_2107254089863229441.json, 图片生成/图生图/人物迁移MiniMax图像编辑免费版工作流，局部重绘角色一致性图生图方案_2107251066072035329.json, 图片生成/图生图/人物迁移minimax图像编辑API版｜局部重绘角色一致性_2107008432187461634.json, 图片生成/图生图/人物迁移minimax图像编辑免费版｜局部重绘角色一致性_2106999934523371522.json, 图片生成/图生图/服装迁移超高一致性H3图像编辑工作流，风格迁移图生图图案迁移工具_2107222093061513218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_225

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Minimax图像编辑API版｜图生图换人角色一致稳定输出_2110678895354793985.json、图片生成/图生图/Minimax图像编辑免费版｜局部重绘人物替换角色一致性不崩_2110677343311327233.json、图片生成/图生图/minimax图像编辑API版人物替换，局部重绘角色一致_2110835438633181185.json、图片生成/图生图/人物迁移MiniMax图像编辑API版工作流，局部重绘角色一致性图生图方案_2107254089863229441.json、图片生成/图生图/人物迁移MiniMax图像编辑免费版工作流，局部重绘角色一致性图生图方案_2107251066072035329.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
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
- `Fast Groups Muter (rgthree)` —— 7/8 个有
- `GetImageSize` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 7/8 个有
- `LoraLoader` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `MiniMaxH3UnifiedToVideo` —— 7/8 个有
- `easy imageInsetCrop` —— 7/8 个有
- `RHLLMChatNode` —— 5/8 个有
- `Qwen3VL_Chat` —— 3/8 个有
- `ImageScaleBy` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `MiniMaxH3ReferenceToVideo` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有
- `VAEDecodeAudio` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
