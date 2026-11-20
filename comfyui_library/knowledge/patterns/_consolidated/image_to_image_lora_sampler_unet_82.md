---
name: image_to_image_lora_sampler_unet_82
type: Image To Image
frequency: 7
level: strong
coverage: 0.840143
common_nodes: [CFGNorm, CLIPLoader, CR Overlay Text, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, String Literal, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王027.手动提示词三宫格人物写真_2034926160143978497.json, 图片生成/图生图/002.Qwen编辑之王028.小红书自动三宫格一致性写真_2034926180758986754.json, 图片生成/图生图/250110004.手动提示词三宫格人物写真_2011256969578942466.json, 图片生成/图生图/260110003.小红书三宫格一致性写真_2011257341500465154.json, 图片生成/图生图/三宫格写真，人物不改，文字不崩，美学升级！解密版本，全自动，除参考图外无任何输入_1983088387672436737.json, 图片生成/图生图/三格时光——爆款三宫格写真情绪递进版_1987497714176995330.json, 图片生成/文生图/最近爆火的三宫格全自动写真（提示词自动优化+自动字幕）_1985867106191323137.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_82

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王027.手动提示词三宫格人物写真_2034926160143978497.json、图片生成/图生图/002.Qwen编辑之王028.小红书自动三宫格一致性写真_2034926180758986754.json、图片生成/图生图/250110004.手动提示词三宫格人物写真_2011256969578942466.json、图片生成/图生图/260110003.小红书三宫格一致性写真_2011257341500465154.json、图片生成/图生图/三宫格写真，人物不改，文字不崩，美学升级！解密版本，全自动，除参考图外无任何输入_1983088387672436737.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Overlay Text`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `String Literal`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `ImageFromBatch` —— 6/7 个有
- `ImageListToImageBatch` —— 6/7 个有
- `RH_LLMAPI_NODE` —— 6/7 个有
- `Text` —— 6/7 个有
- `CR Text Concatenate` —— 5/7 个有
- `DeepTranslatorTextNode` —— 5/7 个有
- `GODMT_ListSlice` —— 5/7 个有
- `ImageConcatMulti` —— 5/7 个有
- `JDCN_ListToString` —— 5/7 个有
- `TextListSplit` —— 5/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `easy promptList` —— 4/7 个有
- `ImageBatchMultiple+` —— 2/7 个有
- `ImageConcatFromBatch` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `Text Concatenate` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `ShowText` —— 1/7 个有
- `ttN seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 71% |
| 调度器 | beta57 | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 71%
- 调度器 最常用 beta57，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（13/7 个样本）：Steps较低可能导致细节不足
