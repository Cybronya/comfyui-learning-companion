---
name: unknown_workflow_video_lora_sampler_716
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6755
common_nodes: [AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, INTConstant, ImageResizeKJv2, Int, JoinStrings, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PainterI2V, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, ShowText|pysssss, SimpleMath+, SoundFlow_GetLength, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [数字人/数字人/For循环+旅行提示词-图生视频-V2V-Infinitetalk高动态数字人_1990794516057759745.json, 视频生成/图生视频/1990442232287301633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_716

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/For循环+旅行提示词-图生视频-V2V-Infinitetalk高动态数字人_1990794516057759745.json、视频生成/图生视频/1990442232287301633.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `INTConstant`
- `ImageResizeKJv2`
- `Int`
- `JoinStrings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `CRTFirstLastFrameSelector` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `Float to Int` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Getter` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `Setter` —— 1/2 个有
- `Text Load Line From File` —— 1/2 个有
- `WanMoeKSampler` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy convertAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 12 | - | 2 | 33% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 1 | 100% |
| 重绘幅度 | euler | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
