---
name: image_to_image_lora_sampler_unet_35
type: Image To Image
frequency: 13
level: strong
coverage: 0.851
common_nodes: [CFGNorm, CLIPLoader, CR Text, ImageFromBatch, ImageListToImageBatch, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy forLoopEnd]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 2509-3格图写真_1986445446946189313.json, 图片生成/图生图/Qwen-Image-Edit 2509-模特一致性不同姿势生成_1987432389506961410.json, 图片生成/图生图/Qwen-Image-Edit 2509：三宫格写真，人物不变，文字不崩_1986562399908069377.json, 图片生成/图生图/Qwen-Image-Edit 2511：超越豆包即梦！三宫格写真，人物不改，文字不崩，美学升级~_1982330896986578946.json, 图片生成/图生图/Qwen-Image-Edit+2509： 三宫格写真，人物不改，文字不崩 文生图、图像编辑_1987433825141723137.json, 图片生成/图生图/QwenImageEdit2509三宫格人物一致+中英文字幕_1982590455202357249.json, 图片生成/图生图/三宫格写真美学升级（自动文字+qwen2511）_2010262859984408578.json, 图片生成/图生图/三宫格写真，人物不改，文字不崩，美学升级！_1983140058943397890.json, 图片生成/图生图/图片人物生成氛围三宫格图_1983088377362849794.json, 图片生成/文生图/Qwen-Image-Edit 2509：超越豆包即梦！三宫格写真，人物不改，文字不崩，美学升级~_1992845023530078209.json, 图片生成/文生图/Qwen-Image-Edit 2509：超越豆包即梦！三宫格写真，人物不改，文字不崩，美学升级！111_1982644350511390722.json, 图片生成/文生图/文字生成三宫格写真，人物一致性_1983150926611554306.json, 图片生成/文生图/文字生成图片三宫格_1983145644221210625.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_35

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 2509-3格图写真_1986445446946189313.json、图片生成/图生图/Qwen-Image-Edit 2509-模特一致性不同姿势生成_1987432389506961410.json、图片生成/图生图/Qwen-Image-Edit 2509：三宫格写真，人物不变，文字不崩_1986562399908069377.json、图片生成/图生图/Qwen-Image-Edit 2511：超越豆包即梦！三宫格写真，人物不改，文字不崩，美学升级~_1982330896986578946.json、图片生成/图生图/Qwen-Image-Edit+2509： 三宫格写真，人物不改，文字不崩 文生图、图像编辑_1987433825141723137.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ImageFromBatch`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`

**可变部分**（部分 workflow 才有）：
- `CR Overlay Text` —— 12/13 个有
- `ImageConcatFromBatch` —— 12/13 个有
- `SDVM Image List Repeat` —— 12/13 个有
- `String Literal` —— 12/13 个有
- `Text` —— 12/13 个有
- `RHHiddenNodes` —— 8/13 个有
- `ImpactImageBatchToImageList` —— 7/13 个有
- `easy forLoopStart` —— 7/13 个有
- `RH_Translator` —— 6/13 个有
- `ttN text7BOX_concat` —— 6/13 个有
- `Multi Text Merge` —— 5/13 个有
- `PreviewAny` —— 5/13 个有
- `ProcessString` —— 5/13 个有
- `RH_LLMAPI_NODE` —— 5/13 个有
- `SimpleMath+` —— 5/13 个有
- `Text Load Line From File` —— 5/13 个有
- `easy showAnything` —— 5/13 个有
- `ReplaceText` —— 3/13 个有
- `Anything Everywhere3` —— 2/13 个有
- `JjkText` —— 2/13 个有
- `easy promptConcat` —— 2/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 13 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，13 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
