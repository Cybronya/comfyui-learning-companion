---
name: unknown_workflow_controlnet_video_lora_43
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8975
common_nodes: [AudioCrop, AudioSeparation, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CreateCFGScheduleFloatList, DownloadAndLoadWav2VecModel, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, GetImageSize, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingFlux, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, RH_Translator, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/取衣去人跳舞(去人留衣)_1991388491707953154.json, 视频生成/图生视频/Flux-Kontext去人取衣跳舞+运镜参考_1940396618250170369.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_43

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/取衣去人跳舞(去人留衣)_1991388491707953154.json、视频生成/图生视频/Flux-Kontext去人取衣跳舞+运镜参考_1940396618250170369.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadWav2VecModel`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingFlux`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `RH_Translator`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
