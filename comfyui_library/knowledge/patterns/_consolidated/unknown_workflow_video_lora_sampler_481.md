---
name: unknown_workflow_video_lora_sampler_481
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8222
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ColorMatch, CreateCFGScheduleFloatList, Float, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, ImageScaleBy, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, RH_LLMAPI_NODE, SaveImage, Seed (rgthree), UNETLoader, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Dasiwa V9 Vs Anisoxa v3 Vs Anime-U V3动漫视频对比_2011420423543590914.json, 视频生成/图生视频/Dasiwa V9 Vs V8动漫视频对比_2011638158131208193.json, 视频生成/图生视频/Lightx2v 1022 VS Smooth Mix图生视频对比工作流V1_1981064285088518146.json, 视频生成/图生视频/Lightx2v 1030 VS 1022 VS Smooth Mix图生视频对比工作流V1_1984548034874916865.json, 视频生成/图生视频/Smooth V2 Vs Dasiwa V9 Vs V8动漫视频对比工作流 浮云1.20_2013465829291073537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_481

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Dasiwa V9 Vs Anisoxa v3 Vs Anime-U V3动漫视频对比_2011420423543590914.json、视频生成/图生视频/Dasiwa V9 Vs V8动漫视频对比_2011638158131208193.json、视频生成/图生视频/Lightx2v 1022 VS Smooth Mix图生视频对比工作流V1_1981064285088518146.json、视频生成/图生视频/Lightx2v 1030 VS 1022 VS Smooth Mix图生视频对比工作流V1_1984548034874916865.json、视频生成/图生视频/Smooth V2 Vs Dasiwa V9 Vs V8动漫视频对比工作流 浮云1.20_2013465829291073537.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ColorMatch`
- `CreateCFGScheduleFloatList`
- `Float`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `Seed (rgthree)`
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
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RunningHub Deepcleaner` —— 4/5 个有
- `VAEDecode` —— 4/5 个有
- `AddLabel` —— 3/5 个有
- `CR Prompt Text` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `VAEDecodeTiled` —— 3/5 个有
- `ImageConcanate` —— 2/5 个有
- `WanVideoSetBlockSwap` —— 2/5 个有
- `WanVideoSetLoRAs` —— 2/5 个有
- `KSampler` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `PDIMAGE_LongerSize` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `Wan22ImageToVideoLatent` —— 1/5 个有
- `mxSlider2D` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 6 | 5 - 8 | 5 | 82% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 6，观测区间 5 - 8，5 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 80%
