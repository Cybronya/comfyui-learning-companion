---
name: text_to_image_sampler_clip_unet_62
type: Text To Image
frequency: 10
level: strong
coverage: 0.7424
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DeepTranslatorTextNode, EmptyLatentImage, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy saveText]
problems: []
missing: []
members: [图片生成/图生图/Z-image-turbo-图生图-图片反推（开源之王）_1997492114353242114.json, 图片生成/图生图/Z-image最强真实人物模型生成_1994716674047811586.json, 图片生成/图生图/Z-image最强真实人物细节_2065062994622640130.json, 图片生成/图生图/图片反推+Z-image最强真实人物细节生成_1994020375361241089.json, 图片生成/图生图/图片反推洗图+Z-image最强真实人物细节多场景生成_2089635395637174274.json, 图片生成/文生图/Z-image 平替Flux2 图片反推+文生图  最强真实人物细节多场景生成 Z-image_1993908699964047361.json, 图片生成/文生图/Z-imageTurbo 快速高清 4K 工作流_1995495345377443841.json, 图片生成/文生图/图片反推+Z-image最强真实人物细节多场景生成_1993853085036511234.json, 图片生成/文生图/图片反推+Z-image最强真实人物细节多场景生成_1998679334598664193.json, 图片生成/文生图/图片反推+Z-image最强真实人物细节多场景生成_2002784165995114497.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_62

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Z-image-turbo-图生图-图片反推（开源之王）_1997492114353242114.json、图片生成/图生图/Z-image最强真实人物模型生成_1994716674047811586.json、图片生成/图生图/Z-image最强真实人物细节_2065062994622640130.json、图片生成/图生图/图片反推+Z-image最强真实人物细节生成_1994020375361241089.json、图片生成/图生图/图片反推洗图+Z-image最强真实人物细节多场景生成_2089635395637174274.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `AspectRatio` —— 8/10 个有
- `Fast Groups Muter (rgthree)` —— 8/10 个有
- `PreviewImage` —— 5/10 个有
- `easy promptList` —— 5/10 个有
- `LatentCombine` —— 2/10 个有
- `VAEEncode` —— 2/10 个有
- `GetNode` —— 1/10 个有
- `SetNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1000 - 1920 | 10 | 77% |
| 高度 | 1080 | 1080 - 1920 | 10 | 78% |
| 采样步数 | 10 | 10 - 10 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1920，观测区间 1000 - 1920，10 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，10 个样本
- 采样步数 中位数 10，观测区间 10 - 10，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
