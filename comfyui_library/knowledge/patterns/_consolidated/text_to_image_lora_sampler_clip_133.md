---
name: text_to_image_lora_sampler_clip_133
type: Text To Image
frequency: 7
level: strong
coverage: 0.630857
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, FB_Qwen3TTSVoiceDesign, Fast Groups Bypasser (rgthree), GetNode, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, RegexExtract, SaveAudio, SaveImage, SetNode, StringConcatenate, StringReplace, UNETLoader, VAEDecode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/资产生成短剧拍档V16.1 Qwen2.1可编辑版，文生图图生图短剧资产工具_2106108165623468034.json, 音频生成/音频生成/Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474.json, 音频生成/音频生成/场景角色双支持｜短剧拍档V12.2继承版资产生成_2091795341573181442.json, 音频生成/音频生成/短剧拍档V12.1重置版｜资产生成文生图音频_2092888610189176834.json, 音频生成/音频生成/短剧拍档V13.1预览编辑版 资产生成与角色管理_2098292808837849090.json, 音频生成/音频生成/短剧拍档V13.1预览编辑版 资产生成与角色管理工具_2098705139308777473.json, 音频生成/音频生成/短剧拍档资产生成｜V12.1重置版文生图音频_2091793261215178753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_133

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/资产生成短剧拍档V16.1 Qwen2.1可编辑版，文生图图生图短剧资产工具_2106108165623468034.json、音频生成/音频生成/Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474.json、音频生成/音频生成/场景角色双支持｜短剧拍档V12.2继承版资产生成_2091795341573181442.json、音频生成/音频生成/短剧拍档V12.1重置版｜资产生成文生图音频_2092888610189176834.json、音频生成/音频生成/短剧拍档V13.1预览编辑版 资产生成与角色管理_2098292808837849090.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `FB_Qwen3TTSVoiceDesign`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RegexExtract`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `YUAN_TXTReplace` —— 6/7 个有
- `BasicScheduler` —— 5/7 个有
- `KSamplerSelect` —— 5/7 个有
- `PrimitiveBoolean` —— 5/7 个有
- `RandomNoise` —— 5/7 个有
- `SamplerCustomAdvanced` —— 5/7 个有
- `BasicGuider` —— 4/7 个有
- `YUAN_TXTPreviewContent` —— 4/7 个有
- `CFGGuider` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `CustomCombo` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `ResolutionSelector` —— 2/7 个有
- `TextEncodeQwenImage21` —— 2/7 个有
- `VAEEncode` —— 2/7 个有
- `YuanCustomCombo` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
