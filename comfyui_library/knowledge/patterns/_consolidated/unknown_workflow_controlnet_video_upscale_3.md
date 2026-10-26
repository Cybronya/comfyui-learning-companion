---
name: unknown_workflow_controlnet_video_upscale_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.838
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, INTConstant, ImageResizeKJv2, ImageScale, ImageUpscaleWithModel, JWInteger, JWIntegerToString, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PlaySound|pysssss, PreviewImage, RH_Captioner, RH_Translator, RIFE VFI, SimpleMath+, Text Concatenate, UpscaleModelLoader, VHS_DuplicateImages, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy anythingIndexSwitch, easy compare, easy ifElse, easy imageScaleDownToSize, easy imageSize, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1  Multitalk数字人图片开口唱歌稳定放大功能齐全版_1957680451332796417.json, 音频生成/音频生成/Wan2.1  Multitalk音乐数字人_1938926634802012162.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_upscale_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.1  Multitalk数字人图片开口唱歌稳定放大功能齐全版_1957680451332796417.json、音频生成/音频生成/Wan2.1  Multitalk音乐数字人_1938926634802012162.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageUpscaleWithModel`
- `JWInteger`
- `JWIntegerToString`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PlaySound|pysssss`
- `PreviewImage`
- `RH_Captioner`
- `RH_Translator`
- `RIFE VFI`
- `SimpleMath+`
- `Text Concatenate`
- `UpscaleModelLoader`
- `VHS_DuplicateImages`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy compare`
- `easy ifElse`
- `easy imageScaleDownToSize`
- `easy imageSize`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
