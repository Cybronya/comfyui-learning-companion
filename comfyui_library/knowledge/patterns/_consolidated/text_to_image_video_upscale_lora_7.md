---
name: text_to_image_video_upscale_lora_7
type: Text To Image
frequency: 2
level: weak
coverage: 0.79
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, CR Text Replace, ColorMatch, ConditioningZeroOut, EmptyLatentImage, FlashVSRNode, GetImageRangeFromBatch, GetImageSize, GetNode, ImageBatchSplitter //Inspire, ImageConcatMulti, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactInt, Int, JDCN_StringToList, JWInteger, JjkText, JoinStrings, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, MuyeTextEditOutput, PathchSageAttentionKJ, PreviewImage, ProcessString, Qwen3VL_Chat, Qwen3_VQA, RH_Captioner_Pro, RH_LLMAPI_NODE, SaveImage, Seed (rgthree), SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetNode, ShellAgentPluginOutputText, ShowText|pysssss, Text Concatenate, TextEncodeQwenImageEditPlus, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VHS_Unbatch, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo, easy batchAnything, easy cleanGpuUsed, easy imageListToImageBatch, easy promptLine, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1997586587758301186.json, 视频生成/图生视频/1995678393033166849.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1997586587758301186.json、视频生成/图生视频/1995678393033166849.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `CR Text Replace`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FlashVSRNode`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetNode`
- `ImageBatchSplitter //Inspire`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `Int`
- `JDCN_StringToList`
- `JWInteger`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `MuyeTextEditOutput`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `ProcessString`
- `Qwen3VL_Chat`
- `Qwen3_VQA`
- `RH_Captioner_Pro`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetNode`
- `ShellAgentPluginOutputText`
- `ShowText|pysssss`
- `Text Concatenate`
- `TextEncodeQwenImageEditPlus`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_Unbatch`
- `VHS_VideoCombine`
- `WanFirstMiddleLastFrameToVideo`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy imageListToImageBatch`
- `easy promptLine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImpactConditionalBranch` —— 1/2 个有
- `SDXLEmptyLatentSizePicker+` —— 1/2 个有
- `easy boolean` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | beta57 | - | 2 | 100% |
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 960.5 | - | 2 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 beta57，2 个样本，一致性 100%
- 高度 中位数 960.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
