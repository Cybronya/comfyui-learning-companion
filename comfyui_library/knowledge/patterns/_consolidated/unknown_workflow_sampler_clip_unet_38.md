---
name: unknown_workflow_sampler_clip_unet_38
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.548417
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, GetNode, KSamplerSelect, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RegexExtract, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter]
problems: []
missing: []
members: [图片生成/文生图/Krea2_短剧场景＆角色-资产生成_2089612313283350530.json, 图片生成/文生图/Krea2版 短剧拍档支持场景和角色生成文生图_2088934511211012098.json, 图片生成/文生图/Krea2版 短剧拍档支持场景和角色生成文生图_2088960690924122114.json, 图片生成/文生图/Krea2版 短剧拍档支持场景和角色生成文生图_2093638279458545666.json, 图片生成/文生图/【傲雪AIGC】MiniMax+H3短剧角色+场景+道具多合一工作流_2093254371827077121.json, 图片生成/文生图/短剧场景V10(真实电影场景)_2090815269898899457.json, 图片生成/文生图/短剧拍档支持场景和角色V9.0(Krea2版) 加lora_2090724606184353793.json, 图片生成/文生图/短剧拍档支持场景和角色V9.0(Krea2版)_修复_2089636684685201409.json, 图片生成/文生图/短剧自动场景和角色V2.0_2087854471954128897.json, 数字人/数字人/短剧声音和场景_道具_角色V10(美国建模)_2090815289637298178.json, 音频生成/音频生成/短剧拍档支持场景和角色V12.2(V11继承版)_2087664915262824449.json, 音频生成/音频生成/资产生成-短剧拍档V13.1（预览编辑版）_2091445990522974210.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_38

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Krea2_短剧场景＆角色-资产生成_2089612313283350530.json、图片生成/文生图/Krea2版 短剧拍档支持场景和角色生成文生图_2088934511211012098.json、图片生成/文生图/Krea2版 短剧拍档支持场景和角色生成文生图_2088960690924122114.json、图片生成/文生图/Krea2版 短剧拍档支持场景和角色生成文生图_2093638279458545666.json、图片生成/文生图/【傲雪AIGC】MiniMax+H3短剧角色+场景+道具多合一工作流_2093254371827077121.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `GetNode`
- `KSamplerSelect`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RegexExtract`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YUAN_TXTConvertAny`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTParagraphSplitter`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 11/12 个有
- `ShowText|pysssss` —— 11/12 个有
- `Fast Groups Bypasser (rgthree)` —— 9/12 个有
- `easy positive` —— 7/12 个有
- `ComfyMathExpression` —— 5/12 个有
- `FB_Qwen3TTSVoiceDesign` —— 5/12 个有
- `LoraLoaderModelOnly` —— 5/12 个有
- `SaveAudio` —— 5/12 个有
- `StringConcatenate` —— 5/12 个有
- `StringReplace` —— 5/12 个有
- `ModelAttentionBackend` —— 3/12 个有
- `BasicGuider` —— 1/12 个有
- `LoadImage` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `YUAN_TXTPreviewContent` —— 1/12 个有
- `YUAN_TXTReplace` —— 1/12 个有
- `孤海注释` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1920 | 12 | 74% |
| 高度 | 1920 | 1080 - 1920 | 12 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1920，12 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，12 个样本，取值集中（一致性 83%）
