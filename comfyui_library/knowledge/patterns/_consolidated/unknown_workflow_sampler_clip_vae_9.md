---
name: unknown_workflow_sampler_clip_vae_9
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.805929
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, INTConstant, JWString, KSamplerSelect, LoadAudio, PreviewAny, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveAudio, SaveImage, ScriptJSONParser, ShowText|pysssss, TDQwen3TTSBatchGenerateSpeaker, TDQwen3TTSDefineSpeaker, TDQwen3TTSModelLoader, TDQwen3TTSMultiDialog, VAEDecode, VAEEncode, parse_json_node]
problems: []
missing: []
members: [图片生成/图生图/解说漫自动分镜+语音生成_2018000318780416002.json, 图片生成/文生图/2030655855456165889.json, 图片生成/文生图/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2017634082175324161.json, 图片生成/文生图/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2018154162223058946.json, 图片生成/文生图/【100%全自动版】有声小说+分镜图一条龙直出 林耀_2017439134444429313.json, 图片生成/文生图/分镜头图片生成+AI漫剧+小说+短剧+自动配音_2018288054846361602.json, 图片生成/文生图/短剧自动配音+分镜_2018625997012213762.json, 视频生成/图生视频/原版解说类 -短剧自动配音+分镜_2041960740780777474.json, 视频生成/文生视频/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2070634252647096321.json, 视频生成/文生视频/短剧+小说＋自动配音ai生成动画_2018483381134172161.json, 音频生成/音频生成/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2017966660707164161.json, 音频生成/音频生成/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2043573314668466178.json, 音频生成/音频生成/【真全自动版】全自动有声小说+分镜图一条龙_2016070253796659201.json, 音频生成/音频生成/原版解说类 -短剧自动配音+分镜_2049180878814846977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_9

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/解说漫自动分镜+语音生成_2018000318780416002.json、图片生成/文生图/2030655855456165889.json、图片生成/文生图/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2017634082175324161.json、图片生成/文生图/AI小说、短剧、漫剧自动配音+分镜Flux2+Qwen3TTS自定义语音_2018154162223058946.json、图片生成/文生图/【100%全自动版】有声小说+分镜图一条龙直出 林耀_2017439134444429313.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 14 个 workflow 都包含：
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
- `Fast Groups Muter (rgthree)` —— 11/14 个有
- `RHHiddenNodes` —— 11/14 个有
- `WujiCleaner` —— 11/14 个有
- `easy promptConcat` —— 11/14 个有
- `CLIPLoader` —— 10/14 个有
- `UNETLoader` —— 10/14 个有
- `VAELoader` —— 10/14 个有
- `BatchImageSelector` —— 7/14 个有
- `WujiBatchImageSelector` —— 5/14 个有
- `CheckpointLoaderSimple` —— 4/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `GetNode` —— 3/14 个有
- `RH_LLMAPI_Pro_Node` —— 3/14 个有
- `SetNode` —— 3/14 个有
- `LayerUtility: BatchSelector` —— 2/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
