---
name: unknown_workflow_video_lora_sampler_354
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8455
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CreateCFGScheduleFloatList, Float, INTConstant, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, ModelSamplingSD3, UNETLoader, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2011420423543590914.json, 视频生成/图生视频/2011638158131208193.json, 视频生成/图生视频/1981064285088518146.json, 视频生成/图生视频/1984548034874916865.json, 视频生成/图生视频/2073241002395136001.json, 视频生成/图生视频/2013465829291073537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_354

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2011420423543590914.json、视频生成/图生视频/2011638158131208193.json、视频生成/图生视频/1981064285088518146.json、视频生成/图生视频/1984548034874916865.json、视频生成/图生视频/2073241002395136001.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CreateCFGScheduleFloatList`
- `Float`
- `INTConstant`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 5/6 个有
- `ColorMatch` —— 5/6 个有
- `GetImageSizeAndCount` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `ImageScaleBy` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `Pick From Batch (mtb)` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `Seed (rgthree)` —— 5/6 个有
- `VAEDecode` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `RunningHub Deepcleaner` —— 4/6 个有
- `AddLabel` —— 3/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `VAEDecodeTiled` —— 3/6 个有
- `WanVideoSetBlockSwap` —— 3/6 个有
- `WanVideoSetLoRAs` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `KSampler` —— 1/6 个有
- `ModelPatchTorchSettings` —— 1/6 个有
- `PDIMAGE_LongerSize` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `Wan22ImageToVideoLatent` —— 1/6 个有
- `mxSlider2D` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 7 | 5 - 8 | 6 | 82% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 7，观测区间 5 - 8，6 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 83%
