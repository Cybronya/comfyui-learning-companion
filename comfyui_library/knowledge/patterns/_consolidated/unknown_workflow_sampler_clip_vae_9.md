---
name: unknown_workflow_sampler_clip_vae_9
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.831571
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, INTConstant, JWString, KSamplerSelect, LoadAudio, PreviewAny, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveAudio, SaveImage, ScriptJSONParser, ShowText|pysssss, TDQwen3TTSBatchGenerateSpeaker, TDQwen3TTSDefineSpeaker, TDQwen3TTSModelLoader, TDQwen3TTSMultiDialog, VAEDecode, VAEEncode, parse_json_node]
problems: []
missing: []
members: [视频生成/图生视频/2041960740780777474.json, 视频生成/文生视频/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2070634252647096321.json, 视频生成/文生视频/短剧+小说＋自动配音ai生成动画_2018483381134172161.json, 音频生成/音频生成/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2017966660707164161.json, 音频生成/音频生成/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2043573314668466178.json, 音频生成/音频生成/【真全自动版】全自动有声小说+分镜图一条龙_2016070253796659201.json, 音频生成/音频生成/原版解说类 -短剧自动配音+分镜_2049180878814846977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_9

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2041960740780777474.json、视频生成/文生视频/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2070634252647096321.json、视频生成/文生视频/短剧+小说＋自动配音ai生成动画_2018483381134172161.json、音频生成/音频生成/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2017966660707164161.json、音频生成/音频生成/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2043573314668466178.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `INTConstant`
- `JWString`
- `KSamplerSelect`
- `LoadAudio`
- `PreviewAny`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveAudio`
- `SaveImage`
- `ScriptJSONParser`
- `ShowText|pysssss`
- `TDQwen3TTSBatchGenerateSpeaker`
- `TDQwen3TTSDefineSpeaker`
- `TDQwen3TTSModelLoader`
- `TDQwen3TTSMultiDialog`
- `VAEDecode`
- `VAEEncode`
- `parse_json_node`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 6/7 个有
- `RHHiddenNodes` —— 6/7 个有
- `WujiCleaner` —— 6/7 个有
- `easy promptConcat` —— 6/7 个有
- `CLIPLoader` —— 4/7 个有
- `UNETLoader` —— 4/7 个有
- `VAELoader` —— 4/7 个有
- `CheckpointLoaderSimple` —— 3/7 个有
- `WujiBatchImageSelector` —— 3/7 个有
- `BatchImageSelector` —— 2/7 个有
- `LayerUtility: BatchSelector` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
