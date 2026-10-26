---
name: text_to_image_lora_sampler_clip_159
type: Text To Image
frequency: 11
level: strong
coverage: 0.857455
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MotionContext, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图直出｜Minimax H3全自动小短片智能生成_2089824260796801025.json, 视频生成/图生视频/MiniMax H3连续衔接插件Motion Context REF无限循环，长视频不断片_2114478187416735745.json, 视频生成/图生视频/Minimax H3全自动一键小短片图生视频生成_2088180357941260289.json, 视频生成/图生视频/一键MV视频生成 图生视频快速创作处理工具_2099908541107752961.json, 视频生成/图生视频/一键MV音乐视频制作图生视频处理生成工具包_2101377930248146945.json, 视频生成/图生视频/一键MV音乐视频生成｜图生视频自动剪辑制作_2096300169238241282.json, 视频生成/图生视频/一键出MV大片｜图生视频音乐短片自动生成_2096563753335746561.json, 视频生成/图生视频/全自动小短片直出｜MiniMax H3一键生成成片_2089768190795669506.json, 视频生成/图生视频/图生视频｜一键生成专属MV大片，音乐视频零门槛搞定_2099851688155897857.json, 视频生成/文生视频/1分钟短片全自动｜MiniMax H3动漫短剧自动循环延长_2089814390295064578.json, 视频生成/文生视频/动漫短剧全自动V5｜海螺MinimaxH3自动循环延长直出_2089781259865255938.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_159

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/文生图直出｜Minimax H3全自动小短片智能生成_2089824260796801025.json、视频生成/图生视频/MiniMax H3连续衔接插件Motion Context REF无限循环，长视频不断片_2114478187416735745.json、视频生成/图生视频/Minimax H3全自动一键小短片图生视频生成_2088180357941260289.json、视频生成/图生视频/一键MV视频生成 图生视频快速创作处理工具_2099908541107752961.json、视频生成/图生视频/一键MV音乐视频制作图生视频处理生成工具包_2101377930248146945.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
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
- `MiniMaxH3MotionContext`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 10/11 个有
- `PreviewAny` —— 10/11 个有
- `Text Multiline` —— 10/11 个有
- `Text To Image (mtb)` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `easy convertAnything` —— 10/11 个有
- `easy promptConcat` —— 10/11 个有
- `easy saveVideo` —— 10/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/11 个有
- `MiniMaxH3MotionContextTrim` —— 9/11 个有
- `PrimitiveStringMultiline` —— 6/11 个有
- `ShowText|pysssss` —— 6/11 个有
- `Text String Truncate` —— 6/11 个有
- `ACE_AudioCrop` —— 5/11 个有
- `ASRMW` —— 5/11 个有
- `CR Text Concatenate` —— 5/11 个有
- `DF_Float` —— 5/11 个有
- `ExtractLinesByIndex` —— 5/11 个有
- `GetAudioDurationFromAudio` —— 5/11 个有
- `Int Literal` —— 5/11 个有
- `PreviewAudio` —— 5/11 个有
- `RH_LLMAPI_Pro_Node` —— 5/11 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 5/11 个有
- `easy clearCacheAll` —— 5/11 个有
- `ttN concat` —— 5/11 个有
- `ModelAttentionBackend` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `CreateVideo` —— 1/11 个有
- `GoohaiAnySwitch` —— 1/11 个有
- `MiniMaxH3MotionContextLoadLatent` —— 1/11 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/11 个有
- `SaveVideo` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `easy MiniMaxH3MotionContextHard` —— 1/11 个有
- `easy ifElse` —— 1/11 个有
- `easy textIndexSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
