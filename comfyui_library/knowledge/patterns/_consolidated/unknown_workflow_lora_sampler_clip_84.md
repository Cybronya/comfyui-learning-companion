---
name: unknown_workflow_lora_sampler_clip_84
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.523667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, FB_Qwen3TTSVoiceDesign, Fast Groups Bypasser (rgthree), GetNode, KSamplerSelect, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RegexExtract, SamplerCustomAdvanced, SaveAudio, SaveImage, SetNode, StringConcatenate, StringReplace, UNETLoader, VAEDecode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter]
problems: []
missing: []
members: [数字人/数字人/短剧声音和场景_道具_角色V10(美国建模)_2090815289637298178.json, 音频生成/音频生成/短剧拍档支持场景和角色V12.2(V11继承版)_2087664915262824449.json, 音频生成/音频生成/资产生成-短剧拍档V13.1（预览编辑版）_2091445990522974210.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/短剧声音和场景_道具_角色V10(美国建模)_2090815289637298178.json、音频生成/音频生成/短剧拍档支持场景和角色V12.2(V11继承版)_2087664915262824449.json、音频生成/音频生成/资产生成-短剧拍档V13.1（预览编辑版）_2091445990522974210.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `FB_Qwen3TTSVoiceDesign`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RegexExtract`
- `SamplerCustomAdvanced`
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

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `YUAN_TXTPreviewContent` —— 1/3 个有
- `YUAN_TXTReplace` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1088 | 1080 - 1920 | 3 | 71% |
| 高度 | 1920 | 1088 - 1920 | 3 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1088，观测区间 1080 - 1920，3 个样本
- 高度 中位数 1920，观测区间 1088 - 1920，3 个样本
