---
name: text_to_image_lora_sampler_clip_171
type: Text To Image
frequency: 10
level: strong
coverage: 0.8632
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MotionContext, MiniMaxH3ReferenceToVideo, PreviewAny, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Text Multiline, Text To Image (mtb), UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy batchAnything, easy cleanGpuUsed, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy promptConcat, easy saveVideo, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图直出｜Minimax H3全自动小短片智能生成_2089824260796801025.json, 视频生成/图生视频/Minimax H3全自动一键小短片图生视频生成_2088180357941260289.json, 视频生成/图生视频/一键MV视频生成 图生视频快速创作处理工具_2099908541107752961.json, 视频生成/图生视频/一键MV音乐视频制作图生视频处理生成工具包_2101377930248146945.json, 视频生成/图生视频/一键MV音乐视频生成｜图生视频自动剪辑制作_2096300169238241282.json, 视频生成/图生视频/一键出MV大片｜图生视频音乐短片自动生成_2096563753335746561.json, 视频生成/图生视频/全自动小短片直出｜MiniMax H3一键生成成片_2089768190795669506.json, 视频生成/图生视频/图生视频｜一键生成专属MV大片，音乐视频零门槛搞定_2099851688155897857.json, 视频生成/文生视频/1分钟短片全自动｜MiniMax H3动漫短剧自动循环延长_2089814390295064578.json, 视频生成/文生视频/动漫短剧全自动V5｜海螺MinimaxH3自动循环延长直出_2089781259865255938.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_171

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/文生图直出｜Minimax H3全自动小短片智能生成_2089824260796801025.json、视频生成/图生视频/Minimax H3全自动一键小短片图生视频生成_2088180357941260289.json、视频生成/图生视频/一键MV视频生成 图生视频快速创作处理工具_2099908541107752961.json、视频生成/图生视频/一键MV音乐视频制作图生视频处理生成工具包_2101377930248146945.json、视频生成/图生视频/一键MV音乐视频生成｜图生视频自动剪辑制作_2096300169238241282.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MotionContext`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `Text To Image (mtb)`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy promptConcat`
- `easy saveVideo`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `MiniMaxH3MotionContextTrim` —— 8/10 个有
- `Text String Truncate` —— 6/10 个有
- `ACE_AudioCrop` —— 5/10 个有
- `ASRMW` —— 5/10 个有
- `CR Text Concatenate` —— 5/10 个有
- `DF_Float` —— 5/10 个有
- `ExtractLinesByIndex` —— 5/10 个有
- `GetAudioDurationFromAudio` —— 5/10 个有
- `Int Literal` —— 5/10 个有
- `PreviewAudio` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `RH_LLMAPI_Pro_Node` —— 5/10 个有
- `ShowText|pysssss` —— 5/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 5/10 个有
- `easy clearCacheAll` —— 5/10 个有
- `ttN concat` —— 5/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `RHHiddenNodes` —— 2/10 个有
- `easy MiniMaxH3MotionContextHard` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
