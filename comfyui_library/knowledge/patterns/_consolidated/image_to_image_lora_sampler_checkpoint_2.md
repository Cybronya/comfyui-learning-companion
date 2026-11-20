---
name: image_to_image_lora_sampler_checkpoint_2
type: Image To Image
frequency: 7
level: strong
coverage: 0.679143
common_nodes: [CFGNorm, CLIPLoader, CR Prompt Text, CheckpointLoaderSimple, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ProcessString, Qwen3_VQA, ReferenceLatent, SaveImage, ShowText|pysssss, SomethingToString, Text Concatenate, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN-2511-AIO大合集_2004817156992888833.json, 图片生成/图生图/QWEN-2511-AIO大合集_2016044601487921153.json, 图片生成/图生图/Qwen-2511-AIO单图+双图+三图大合集_2010162036935761921.json, 图片生成/图生图/【推荐】QWEN-2511-AIO大合集，换装编辑多分镜姿势_2008165144609693697.json, 图片生成/图生图/图片分镜_2008923449892282369.json, 平台全量/QWEN-2511-AI0 单图双图三图大合集，单图出分镜图_2056701432866369538.json, 视频生成/图生视频/QWEN-2511-AIOV18版本大合集_2004947430074449922.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/QWEN-2511-AIO大合集_2004817156992888833.json、图片生成/图生图/QWEN-2511-AIO大合集_2016044601487921153.json、图片生成/图生图/Qwen-2511-AIO单图+双图+三图大合集_2010162036935761921.json、图片生成/图生图/【推荐】QWEN-2511-AIO大合集，换装编辑多分镜姿势_2008165144609693697.json、图片生成/图生图/图片分镜_2008923449892282369.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `Qwen3_VQA`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `SomethingToString`
- `Text Concatenate`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 6/7 个有
- `EmptyLatentImage` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `GetImageSizeAndCount` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 6/7 个有
- `LayerUtility: ImageReel` —— 6/7 个有
- `LayerUtility: ImageReelComposit` —— 6/7 个有
- `PlaySound|pysssss` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `SeedVR2LoadDiTModel` —— 1/7 个有
- `SeedVR2LoadVAEModel` —— 1/7 个有
- `SeedVR2VideoUpscaler` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1280 - 1920 | 6 | 80% |
| 高度 | 1920 | 1280 - 1920 | 6 | 82% |
| 采样步数 | 6 | 4 - 6 | 7 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler_ancestral | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1280 - 1920，6 个样本
- 高度 中位数 1920，观测区间 1280 - 1920，6 个样本，取值集中（一致性 82%）
- 采样步数 中位数 6，观测区间 4 - 6，7 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（25/7 个样本）：Steps较低可能导致细节不足
