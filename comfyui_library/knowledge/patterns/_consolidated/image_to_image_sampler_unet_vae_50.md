---
name: image_to_image_sampler_unet_vae_50
type: Image To Image
frequency: 3
level: strong
coverage: 0.521
common_nodes: [CLIPLoader, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, FB_Qwen3TTSVoiceDesign, Fast Groups Bypasser (rgthree), GetNode, KSampler, LoadImage, PrimitiveInt, PrimitiveStringMultiline, RegexExtract, ResolutionSelector, SaveAudio, SaveImage, SetNode, StringConcatenate, StringReplace, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, YUAN_TXTPreviewContent, YUAN_TXTReplace, YuanCustomCombo]
problems: []
missing: []
members: [图片生成/图生图/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2114636164119490562.json, 图片生成/文生图/资产生成-短剧拍档V16.1(Qwen2.1可编辑版)_2105476566175277057.json, 音频生成/音频生成/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2110643506917240834.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_50

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2114636164119490562.json、图片生成/文生图/资产生成-短剧拍档V16.1(Qwen2.1可编辑版)_2105476566175277057.json、音频生成/音频生成/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2110643506917240834.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `FB_Qwen3TTSVoiceDesign`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `ResolutionSelector`
- `SaveAudio`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `StringReplace`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YUAN_TXTConvertAny`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTPreviewContent`
- `YUAN_TXTReplace`
- `YuanCustomCombo`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1088 | 1088 - 1088 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1088，观测区间 1088 - 1088，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
