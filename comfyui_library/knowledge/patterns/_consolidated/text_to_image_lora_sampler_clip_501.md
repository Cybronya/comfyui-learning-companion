---
name: text_to_image_lora_sampler_clip_501
type: Text To Image
frequency: 3
level: strong
coverage: 0.836
common_nodes: [AudioSeparation, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, MultiTextConcatenate, PreviewAudio, PrimitiveBoolean, RH_LLMAPI_Pro_Node, RH_RhartVideoSparkvideo20MiniMultimodalVideo, SaveImage, SaveVideoNode, Text, UNETLoader, VAEDecode, VAELoader, easy getAudioFromVideo, easy ifElse, easy saveText, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/定制爆款视频复刻｜自定义提示词随意改 背景音色也能换_2097506459964760066.json, 图片生成/反推提示词/爆款视频复刻定制专用｜自定义提示词背景配音视频生成_2097110047389216770.json, 图片生成/反推提示词/爆款视频复刻定制工作流｜自定义提示词背景音色视频生成_2097389230640160769.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_501

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/定制爆款视频复刻｜自定义提示词随意改 背景音色也能换_2097506459964760066.json、图片生成/反推提示词/爆款视频复刻定制专用｜自定义提示词背景配音视频生成_2097110047389216770.json、图片生成/反推提示词/爆款视频复刻定制工作流｜自定义提示词背景音色视频生成_2097389230640160769.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MultiTextConcatenate`
- `PreviewAudio`
- `PrimitiveBoolean`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartVideoSparkvideo20MiniMultimodalVideo`
- `SaveImage`
- `SaveVideoNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getAudioFromVideo`
- `easy ifElse`
- `easy saveText`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `忽略多组孤海` —— 2/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `OmniVoiceVoiceCloneTTS` —— 1/3 个有
- `Qwen3ASRLoader` —— 1/3 个有
- `Qwen3ASRTranscribe` —— 1/3 个有
- `RH_GetAudioDuration` —— 1/3 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
