---
name: text_to_image_lora_sampler_clip_423
type: Text To Image
frequency: 5
level: weak
coverage: 0.5768
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, FB_Qwen3TTSVoiceDesign, Fast Groups Bypasser (rgthree), GetNode, KSampler, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, RegexExtract, ResolutionSelector, SaveAudio, SaveImage, SetNode, StringConcatenate, StringReplace, UNETLoader, VAEDecode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, YUAN_TXTPreviewContent, YUAN_TXTReplace]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/短剧拍档支持场景和角色V12.2(V11继承版)_2115626843268280322.json, 图片生成/文生图/短剧拍档支持场景和角色V12.2(V11继承版)_2115672455384748033.json, 图片生成/文生图/资产生成-短剧拍档V17.2(Moss版)_2116454911205535746.json, 图片生成/文生图/资产生成短剧拍档V16.1 Qwen2.1可编辑版，文生图图生图短剧资产工具_2106108165623468034.json, 音频生成/音频生成/Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_423

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/短剧拍档支持场景和角色V12.2(V11继承版)_2115626843268280322.json、图片生成/文生图/短剧拍档支持场景和角色V12.2(V11继承版)_2115672455384748033.json、图片生成/文生图/资产生成-短剧拍档V17.2(Moss版)_2116454911205535746.json、图片生成/文生图/资产生成短剧拍档V16.1 Qwen2.1可编辑版，文生图图生图短剧资产工具_2106108165623468034.json、音频生成/音频生成/Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `FB_Qwen3TTSVoiceDesign`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `ResolutionSelector`
- `SaveAudio`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YUAN_TXTConvertAny`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTPreviewContent`
- `YUAN_TXTReplace`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `ModelAttentionBackend` —— 3/5 个有
- `TextEncodeQwenImage21` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `YuanCustomCombo` —— 3/5 个有
- `YuanPrimitive` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `solarL_SaveImagesToZip` —— 2/5 个有
- `孤海注释` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1088 | 80 - 1088 | 5 | 28% |
| 高度 | 1920 | 80 - 1920 | 5 | 24% |
| 采样步数 | 8 | 4 - 12 | 5 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 5 | 29% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1088，观测区间 80 - 1088，5 个样本，取值分散，一致性仅 28%
- 高度 中位数 1920，观测区间 80 - 1920，5 个样本，取值分散，一致性仅 24%
- 采样步数 中位数 8，观测区间 4 - 12，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
