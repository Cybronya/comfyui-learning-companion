---
name: text_to_image_lora_sampler_clip_604
type: Text To Image
frequency: 2
level: weak
coverage: 0.732
common_nodes: [AddLabel, BatchCount+, CLIPTextEncode, CLIPTextEncodeFlux, DualCLIPLoaderGGUF, EmptyLatentImage, Fast Groups Muter (rgthree), GetNode, ImageConcanate, Joy_caption_two, Joy_caption_two_load, KSampler, LoadAndResizeImage, LoraLoaderModelOnly, MathExpression|pysssss, SaveImage, SetNode, ShowText|pysssss, Text List to Text, TextSplitByDelimiter, UnetLoaderGGUF, VAEDecode, VAELoader, easy promptList, easy rangeInt, ttN concat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/最强图片反推提示词工具 JoyCaption Beta One与Joy Caption2 对比_1944664271521239042.json, 图片生成/文生图/超全！！八大超全图片反推提示词工具集合-选择反推生图-合并_1944293508461002754.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_604

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/最强图片反推提示词工具 JoyCaption Beta One与Joy Caption2 对比_1944664271521239042.json、图片生成/文生图/超全！！八大超全图片反推提示词工具集合-选择反推生图-合并_1944293508461002754.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `BatchCount+`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `DualCLIPLoaderGGUF`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `ImageConcanate`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadAndResizeImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `Text List to Text`
- `TextSplitByDelimiter`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy promptList`
- `easy rangeInt`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `ClipInterrogator` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `JJC_JoyCaption` —— 1/2 个有
- `JanusImageUnderstanding` —— 1/2 个有
- `JanusModelLoader` —— 1/2 个有
- `LayerMask: LoadFlorence2Model` —— 1/2 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/2 个有
- `MiniCPM_VQA` —— 1/2 个有
- `Molmo7BDbnb` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
