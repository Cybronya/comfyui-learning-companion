---
name: image_to_image_lora_sampler_unet_134
type: Image To Image
frequency: 5
level: strong
coverage: 0.6678
common_nodes: [CLIPLoader, GetNode, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, RH_LLMAPI_NODE, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/三宫格写真-分镜图像制作8步出图-Qwen Edit2509 Next Scene_1982985349662158849.json, 图片生成/图生图/效果炸裂的九宫格个人写真，超越闭源模型，分图和九宫格图分开保存_1984858088886976513.json, 图片生成/图生图/自动反推-分镜图像制作8步出图-Qwen Edit2509 Next Scene_1981989626938310657.json, 图片生成/图生图/豆包抖音三宫格文艺写真照_1984233042329878530.json, 视频生成/图生视频/视频版抖音三宫格写真-分镜视频制作-Qwen Edit2509 Next Scene+wan2.2_1983726049295015938.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_134

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/三宫格写真-分镜图像制作8步出图-Qwen Edit2509 Next Scene_1982985349662158849.json、图片生成/图生图/效果炸裂的九宫格个人写真，超越闭源模型，分图和九宫格图分开保存_1984858088886976513.json、图片生成/图生图/自动反推-分镜图像制作8步出图-Qwen Edit2509 Next Scene_1981989626938310657.json、图片生成/图生图/豆包抖音三宫格文艺写真照_1984233042329878530.json、视频生成/图生视频/视频版抖音三宫格写真-分镜视频制作-Qwen Edit2509 Next Scene+wan2.2_1983726049295015938.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 4/5 个有
- `CR Prompt Text` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `ImageFromBatch` —— 4/5 个有
- `Int` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `CR Overlay Text` —— 3/5 个有
- `DeepTranslatorTextNode` —— 3/5 个有
- `ImageListToImageBatch` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `Text` —— 3/5 个有
- `easy promptConcat` —— 3/5 个有
- `easy imageListToImageBatch` —— 2/5 个有
- `CLIPTextEncode` —— 1/5 个有
- `CLIPVisionEncode` —— 1/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Float` —— 1/5 个有
- `ImagePadForOutpaint` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `ModelSamplingSD3` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `SDVM Image List Repeat` —— 1/5 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/5 个有
- `VHS_VideoCombine` —— 1/5 个有
- `WanImageToVideo` —— 1/5 个有
- `easy imageBatchToImageList` —— 1/5 个有
- `wanBlockSwap` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
