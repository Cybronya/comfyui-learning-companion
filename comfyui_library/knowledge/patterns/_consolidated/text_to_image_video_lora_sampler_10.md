---
name: text_to_image_video_lora_sampler_10
type: Text To Image
frequency: 34
level: weak
coverage: 0.846471
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLTXVLatentVideo, EmptyLatentImage, INTConstant, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LoraLoaderModelOnly, LowVRAMCheckpointLoader, ManualSigmas, PreviewImage, RandomNoise, SamplerCustomAdvanced, Text, VAEDecode, VAELoader, VHS_VideoCombine, easy indexAnything, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Gemma4开源版2｜LTX-2.3_MSR V2视频处理生成_2095064005294514177.json, 图片生成/图生图/LTX 2.3 MSR V2 Gemma4开源版2工作流，其它视频处理方案_2106454518350307330.json, 图片生成/图生图/LTX-2.3 MSR V2 Gemma4开源版2-其它视频处理工作流_2087338246153003009.json, 图片生成/图生图/LTX-2.3 MSR V2 Gemma4开源版2｜视频处理新选择_2106259370370748417.json, 图片生成/图生图/LTX-2.3 MSR V2 Gemma4开源版2｜视频处理长镜头稳定不掉帧_2099122238648832002.json, 图片生成/图生图/LTX-2.3_MSR+V2漫剧自动多参分镜_2083110121860849666.json, 图片生成/图生图/MSR V2 Gemma4开源版｜LTX-2.3视频处理直出_2090880480139898882.json, 图片生成/图生图/开源Gemma4加持｜LTX-2.3 MSR V2参考图生视频处理_2091158499739914241.json, 视频生成/图生视频/3分镜图生视频｜image2+LTX-MSR多参运镜，出片更有戏_2099909158635139074.json, 视频生成/图生视频/3分镜多参图生视频｜image2+LTX-MSR组合生成_2095484514092015618.json, 视频生成/图生视频/Image2加LTX多参数三分镜图生视频 多角色分镜创作_2099916907792130050.json, 视频生成/图生视频/LTX-2.3_MSR V2 Gemma4开源版_2083136188516491265.json, 视频生成/图生视频/LTX-2.3_MSR V2多参分镜自动扩展提示词1_2079756676873408513.json, 视频生成/图生视频/LTX-2.3_MSR V2多参漫剧长镜头1_2083106849519398914.json, 视频生成/图生视频/LTX-2.3_MSR V2漫剧短剧自动多参分镜图生视频_2080241011628007425.json, 视频生成/图生视频/LTX-2.3_MSR V2漫剧短剧自动多参分镜图生视频_2081010266782912513.json, 视频生成/图生视频/LTX-2.3_MSR V2漫剧自动多参分镜_2079758603824750594.json, 视频生成/图生视频/LTX-2.3_MSR V2漫剧自动多参分镜_2080572501062672386.json, 视频生成/图生视频/LTX-2.3_MSR+V2漫剧自动多参分镜_2095747117393473538.json, 视频生成/图生视频/LTX-MSR多参3分镜图生视频image2_2087478149268459522.json, 视频生成/图生视频/MRS自动分镜提示词1_2079459174697754625.json, 视频生成/图生视频/ltx23-mrsv2自动多分镜视频_2080283230909063170.json, 视频生成/图生视频/ltx漫剧多参_2072609363512094721.json, 视频生成/图生视频/最新版 LTX 无API漫剧多参视频漫剧电商服装分镜真人_2072967530607632385.json, 视频生成/图生视频/最新版LTX多参图生视频漫剧分镜电商服装1_2074307864331636737.json, 视频生成/图生视频/最新版LTX多参图生视频漫剧分镜电商服装2_2074307850519797761.json, 视频生成/图生视频/最新版LTX多参图生视频漫剧分镜电商服装3_2074345334553268226.json, 视频生成/图生视频/最新版LTX多参图生视频漫剧分镜电商服装_2074181237513744385.json, 视频生成/图生视频/最新版LTX多参图生视频漫剧电商服装分镜真人_2074184483884064769.json, 视频生成/图生视频/最新版LTX漫剧多参视频无API版漫剧_2074365914375614466.json, 视频生成/图生视频/最新版LTX漫剧多参视频无API版漫剧电商服装分镜真人_2072600045387599874.json, 视频生成/图生视频/最新版LTX漫剧多参视频无API版漫剧电商服装分镜真人_2074366376860545025.json, 视频生成/图生视频/漫剧场景缤纷世界_2079795396607565825.json, 视频生成/图生视频/漫剧多参分镜自动扩展提示词1_2079483993136918530.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 34 个 workflow 归纳得出（图片生成/图生图/Gemma4开源版2｜LTX-2.3_MSR V2视频处理生成_2095064005294514177.json、图片生成/图生图/LTX 2.3 MSR V2 Gemma4开源版2工作流，其它视频处理方案_2106454518350307330.json、图片生成/图生图/LTX-2.3 MSR V2 Gemma4开源版2-其它视频处理工作流_2087338246153003009.json、图片生成/图生图/LTX-2.3 MSR V2 Gemma4开源版2｜视频处理新选择_2106259370370748417.json、图片生成/图生图/LTX-2.3 MSR V2 Gemma4开源版2｜视频处理长镜头稳定不掉帧_2099122238648832002.json…）

- **类型**：Text To Image
- **样本数**：34
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 34 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `INTConstant`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy indexAnything`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `TextConcatenate_UTK` —— 31/34 个有
- `ConditioningZeroOut` —— 30/34 个有
- `EnhancedLoadDiffusionModel` —— 30/34 个有
- `FluxKontextMultiReferenceLatentMethod` —— 30/34 个有
- `Int` —— 30/34 个有
- `LayerUtility: PurgeVRAM V2` —— 30/34 个有
- `RH_Captioner` —— 30/34 个有
- `RandomInt` —— 30/34 个有
- `StringReplace` —— 30/34 个有
- `TextEncodeQwenImageEditPlus` —— 30/34 个有
- `easy batchAnything` —— 30/34 个有
- `easy forLoopEnd` —— 30/34 个有
- `easy forLoopStart` —— 30/34 个有
- `Split String by Commas` —— 26/34 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 25/34 个有
- `ImageConcatenate_UTK` —— 24/34 个有
- `CR Float To Integer` —— 20/34 个有
- `CR Prompt Text` —— 20/34 个有
- `FloatConstant` —— 20/34 个有
- `LTX2_NAG` —— 20/34 个有
- `PromptRelayEncode` —— 20/34 个有
- `SimpleMath+` —— 20/34 个有
- `JjkText` —— 11/34 个有
- `UNETLoader` —— 11/34 个有
- `solarL_SaveImagesToZip` —— 11/34 个有
- `孤海注释` —— 11/34 个有
- `llama_cpp_instruct_adv` —— 8/34 个有
- `llama_cpp_model_loader` —— 8/34 个有
- `llama_cpp_parameters` —— 8/34 个有
- `ImageScaleToTotalPixels` —— 4/34 个有
- `RHHiddenNodes` —— 4/34 个有
- `RH_RhartImageG2ImageToImage` —— 4/34 个有
- `SetNode` —— 4/34 个有
- `easy imageSplitGrid` —— 4/34 个有
- `SaveImage` —— 2/34 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 34 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 34 | 23% |
| 采样算法 | euler | - | 34 | 68% |
| 调度器 | simple | - | 34 | 68% |
| 重绘幅度 | 1 | 1 - 1 | 34 | 100% |
| 宽度 | 241 | 80 - 1280 | 34 | 0% |
| 高度 | 80 | 50 - 720 | 34 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 41/34 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，34 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，34 个样本，取值分散，一致性仅 23%
- 采样算法 最常用 euler，34 个样本，一致性 68%
- 调度器 最常用 simple，34 个样本，一致性 68%
- 重绘幅度 中位数 1，观测区间 1 - 1，34 个样本，取值集中（一致性 100%）
- 宽度 中位数 241，观测区间 80 - 1280，34 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 50 - 720，34 个样本，取值分散，一致性仅 0%
- 高发问题（41/34 个样本）：Steps较低可能导致细节不足
