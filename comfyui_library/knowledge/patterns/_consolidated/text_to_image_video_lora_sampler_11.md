---
name: text_to_image_video_lora_sampler_11
type: Text To Image
frequency: 29
level: weak
coverage: 0.876931
common_nodes: [BerniniConditioning, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, EnhancedLoadDiffusionModel, FluxKontextMultiReferenceLatentMethod, ImageResizeKJv2, ImageScaleToTotalPixels, Int, JWInteger, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewImage, RandomInt, Split String by Commas, StringReplace, Text, TextConcatenate_UTK, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy indexAnything, easy mathInt, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Bernini自动分镜视频发布版工作流，图生视频自动分镜创作工具_2105754352567808002.json, 视频生成/图生视频/Bernini自动多参Gemm4开源版图生视频工具_2099918410950991873.json, 视频生成/图生视频/bernini gemm4开源版自动多参图生视频工作流_2087336969197154305.json, 视频生成/图生视频/2076951801567465474.json, 视频生成/图生视频/2080213506917486594.json, 视频生成/图生视频/2080461814877474818.json, 视频生成/图生视频/2077014017478053890.json, 视频生成/图生视频/2077052662113202177.json, 视频生成/图生视频/bernini自动分镜视频发布版_2076843690617827330.json, 视频生成/图生视频/bernini自动分镜视频发布版｜图生视频自动化_2097924760024993794.json, 视频生成/图生视频/2077031752845058050.json, 视频生成/图生视频/bernini自动分镜｜视频发布版图生视频一键生成_2094472948609544194.json, 视频生成/图生视频/bernini自动多参gemm4开源发布版_2083445043389620226.json, 视频生成/图生视频/bernini自动多参gemm4开源版_2083434109308850177.json, 视频生成/图生视频/bernini自动多参gemm4开源版_2100052975162056705.json, 视频生成/图生视频/bernini自动多参gemm4开源版_2100133559137816577.json, 视频生成/图生视频/bernini自动多参gemm4开源版｜图生视频生成_2095206435062894594.json, 视频生成/图生视频/bernini自动多参｜gemm4开源版图生视频，参数自由配_2099910395120144386.json, 视频生成/图生视频/gemm4漫剧自动扩展提示词多参视频TEST1_2083810470955413506.json, 视频生成/图生视频/gemm4漫剧自动扩展提示词多参视频TEST2_2083813813098475521.json, 视频生成/图生视频/gemm4漫剧自动扩展提示词多参视频TEST3_2083815602338230273.json, 视频生成/图生视频/叮叮给你一个甜甜的笑容_2083454015727296513.json, 视频生成/图生视频/她给了你一个飞吻_2083822231435694081.json, 视频生成/图生视频/2077415348361588737.json, 视频生成/图生视频/2075772423257018370.json, 视频生成/图生视频/2075555368637394946.json, 视频生成/图生视频/2075874925533024258.json, 视频生成/图生视频/2076876646682021890.json, 视频生成/图生视频/自动多参图生视频｜bernini gemm4开源版_2095483112770859010.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/Bernini自动分镜视频发布版工作流，图生视频自动分镜创作工具_2105754352567808002.json、视频生成/图生视频/Bernini自动多参Gemm4开源版图生视频工具_2099918410950991873.json、视频生成/图生视频/bernini gemm4开源版自动多参图生视频工作流_2087336969197154305.json、视频生成/图生视频/2076951801567465474.json、视频生成/图生视频/2080213506917486594.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 29 个 workflow 都包含：
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `Int`
- `JWInteger`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RandomInt`
- `Split String by Commas`
- `StringReplace`
- `Text`
- `TextConcatenate_UTK`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy indexAnything`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `HunyuanVideoFoley` —— 26/29 个有
- `Any To Any` —— 25/29 个有
- `CR Prompt Text` —— 25/29 个有
- `Float` —— 25/29 个有
- `Qwen3_VQA` —— 25/29 个有
- `RHHiddenNodes` —— 25/29 个有
- `VHS_SelectFilename` —— 25/29 个有
- `easy cleanGpuUsed` —— 25/29 个有
- `RH_Captioner` —— 15/29 个有
- `JDCN_StringToList` —— 14/29 个有
- `llama_cpp_instruct_adv` —— 14/29 个有
- `llama_cpp_model_loader` —— 14/29 个有
- `llama_cpp_parameters` —— 14/29 个有
- `JjkText` —— 8/29 个有
- `solarL_SaveImagesToZip` —— 8/29 个有
- `孤海注释` —— 8/29 个有
- `BatchImagesNode` —— 4/29 个有
- `BerniniPromptEnhancer` —— 4/29 个有
- `LoadAudio` —— 4/29 个有
- `RHLLMChatNode` —— 4/29 个有
- `SaveImage` —— 2/29 个有
- `DF_Integer` —— 1/29 个有
- `FL_RIFE` —— 1/29 个有
- `PreviewAny` —— 1/29 个有
- `easy imageConcat` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 29 | 31% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 高度 | 720 | 80 - 960 | 29 | 46% |
| 采样算法 | euler | - | 29 | 59% |
| 调度器 | simple | - | 29 | 59% |
| 采样步数 | 8 | 4 - 8 | 25 | 72% |
| 宽度 | 1280 | 80 - 1280 | 29 | 42% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 38/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，29 个样本，取值分散，一致性仅 31%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 80 - 960，29 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，29 个样本，一致性 59%
- 调度器 最常用 simple，29 个样本，一致性 59%
- 采样步数 中位数 8，观测区间 4 - 8，25 个样本
- 宽度 中位数 1280，观测区间 80 - 1280，29 个样本，取值分散，一致性仅 42%
- 高发问题（38/29 个样本）：Steps较低可能导致细节不足
