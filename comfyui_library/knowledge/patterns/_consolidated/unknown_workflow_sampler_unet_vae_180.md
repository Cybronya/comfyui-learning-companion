---
name: unknown_workflow_sampler_unet_vae_180
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.877429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, ImageFromBatch, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy imageConcat]
problems: []
missing: []
members: [图片生成/反推提示词/图片人物替换-MiniMax H3图像编辑_2116089881633058817.json, 图片生成/图生图/人物替换-minimax图像编辑API版_2115622056388812802.json, 图片生成/图生图/人物替换-minimax图像编辑API版_2115669277599686658.json, 图片生成/图生图/人物迁移-minimax图像编辑（API版）_2102450365731008514.json, 图片生成/图生图/人物迁移-minimax图像编辑（免费版）_2104550573549903874.json, 图片生成/图生图/服装迁移-超高一致性-h3图像编辑_2106818747007852545.json, 平台全量/人物替换-minimax图像编辑（API版）_2117193297327382530.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_180

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/图片人物替换-MiniMax H3图像编辑_2116089881633058817.json、图片生成/图生图/人物替换-minimax图像编辑API版_2115622056388812802.json、图片生成/图生图/人物替换-minimax图像编辑API版_2115669277599686658.json、图片生成/图生图/人物迁移-minimax图像编辑（API版）_2102450365731008514.json、图片生成/图生图/人物迁移-minimax图像编辑（免费版）_2104550573549903874.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `ImageFromBatch`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
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

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 6/7 个有
- `GetImageSize` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 6/7 个有
- `LoraLoader` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `easy imageInsetCrop` —— 6/7 个有
- `RHLLMChatNode` —— 5/7 个有
- `MiniMaxH3UnifiedToVideo` —— 4/7 个有
- `MiniMaxH3ReferenceToVideo` —— 3/7 个有
- `Qwen3VL_Chat` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageScaleBy` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有
- `VAEDecodeAudio` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
