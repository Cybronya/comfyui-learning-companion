---
name: image_to_image_sampler_unet_vae_40
type: Image To Image
frequency: 7
level: strong
coverage: 0.524857
common_nodes: [CLIPLoader, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, FB_Qwen3TTSVoiceDesign, Fast Groups Bypasser (rgthree), GetNode, KSampler, LoadImage, PrimitiveInt, PrimitiveStringMultiline, RegexExtract, ResolutionSelector, SaveAudio, SaveImage, SetNode, StringConcatenate, StringReplace, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, YUAN_TXTPreviewContent, YUAN_TXTReplace, YuanCustomCombo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2114636164119490562.json, 图片生成/图生图/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2115295015625904130.json, 图片生成/图生图/资产生成-短剧拍档V16.1(Qwen2.1可编辑版)_2115262450584088577.json, 图片生成/图生图/资产生成-短剧拍档V16.1(Qwen2.1可编辑版)_2115274622412353537.json, 图片生成/图生图/资产生成-短剧拍档V17.1(Qwen2.1可编辑版)_2116688348361351169.json, 图片生成/文生图/资产生成-短剧拍档V16.1(Qwen2.1可编辑版)_2105476566175277057.json, 音频生成/音频生成/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2110643506917240834.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_40

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2114636164119490562.json、图片生成/图生图/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2115295015625904130.json、图片生成/图生图/资产生成-短剧拍档V16.1(Qwen2.1可编辑版)_2115262450584088577.json、图片生成/图生图/资产生成-短剧拍档V16.1(Qwen2.1可编辑版)_2115274622412353537.json、图片生成/图生图/资产生成-短剧拍档V17.1(Qwen2.1可编辑版)_2116688348361351169.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 7 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 1/7 个有
- `YuanPrimitive` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1088 | 1088 - 1088 | 7 | 100% |
| 高度 | 1920 | 1920 - 1920 | 7 | 100% |
| 采样步数 | 25 | 8 - 25 | 7 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1088，观测区间 1088 - 1088，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 8 - 25，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
