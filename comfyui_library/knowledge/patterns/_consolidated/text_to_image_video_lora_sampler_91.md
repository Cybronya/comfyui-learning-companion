---
name: text_to_image_video_lora_sampler_91
type: Text To Image
frequency: 8
level: strong
coverage: 0.83025
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, GetNode, JWInteger, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewImage, SamplerCustom, SetNode, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Gemma4本地自动化｜LTX2.3最新图生视频运行_2094471635867885569.json, 视频生成/图生视频/LTX2.3+Gemma4本地自动化运行 图生视频最新组合_2094201577295933442.json, 视频生成/图生视频/LTX2.3+Gemma4本地自动化运行｜图生视频新组合_2097923039580213250.json, 视频生成/图生视频/LTX2.3加Gemma4本地自动化运行工作流，图生视频高效创作方案_2105752871810719746.json, 视频生成/图生视频/Ltx2.3 Prompt Relay Smart｜VBVR 390K单图精准控制｜参考生视频稳_2104801534893711362.json, 视频生成/图生视频/Ltx2.3多镜头长时间KJ版｜时间分段剪辑加逻辑控制PromptRe｜图生视频_2099155859929649154.json, 视频生成/图生视频/ltx-bernini人物多角度参考｜最新加速图生视频生成_2097758585924182017.json, 视频生成/图生视频/ltx-bernini最新加速｜人物多角度参考视频生视频_2090346710928281601.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_91

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Gemma4本地自动化｜LTX2.3最新图生视频运行_2094471635867885569.json、视频生成/图生视频/LTX2.3+Gemma4本地自动化运行 图生视频最新组合_2094201577295933442.json、视频生成/图生视频/LTX2.3+Gemma4本地自动化运行｜图生视频新组合_2097923039580213250.json、视频生成/图生视频/LTX2.3加Gemma4本地自动化运行工作流，图生视频高效创作方案_2105752871810719746.json、视频生成/图生视频/Ltx2.3 Prompt Relay Smart｜VBVR 390K单图精准控制｜参考生视频稳_2104801534893711362.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `GetNode`
- `JWInteger`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SamplerCustom`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PromptRelayEncode` —— 7/8 个有
- `LTX2SamplingPreviewOverride` —— 6/8 个有
- `LayerUtility: PurgeVRAM V2` —— 6/8 个有
- `PreviewAny` —— 6/8 个有
- `RegexExtract` —— 6/8 个有
- `StringReplace` —— 6/8 个有
- `Text` —— 6/8 个有
- `easy mathInt` —— 6/8 个有
- `CR Prompt Text` —— 4/8 个有
- `FlashVSR_SM_KSampler` —— 4/8 个有
- `FlashVSR_SM_Model` —— 4/8 个有
- `GetImageRangeFromBatch` —— 4/8 个有
- `GetImageSize` —— 4/8 个有
- `llama_cpp_instruct_adv` —— 4/8 个有
- `llama_cpp_model_loader` —— 4/8 个有
- `llama_cpp_parameters` —— 4/8 个有
- `SaveImage` —— 3/8 个有
- `BatchImagesNode` —— 2/8 个有
- `BerniniConditioning` —— 2/8 个有
- `BerniniPromptEnhancer` —— 2/8 个有
- `CreateVideo` —— 2/8 个有
- `GetVideoComponents` —— 2/8 个有
- `ImageFromBatch` —— 2/8 个有
- `Int` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `RHLLMChatNode` —— 2/8 个有
- `RH_Captioner` —— 2/8 个有
- `SaveVideo` —— 2/8 个有
- `SplitSigmas` —— 2/8 个有
- `easy batchAnything` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `PromptRelaySmartEncode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
