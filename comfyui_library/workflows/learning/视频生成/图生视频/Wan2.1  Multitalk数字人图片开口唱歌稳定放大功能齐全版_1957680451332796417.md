---
key: 视频生成/图生视频/Wan2.1  Multitalk数字人图片开口唱歌稳定放大功能齐全版_1957680451332796417.json
name: Wan2.1  Multitalk数字人图片开口唱歌稳定放大功能齐全版_1957680451332796417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1  Multitalk数字人图片开口唱歌稳定放大功能齐全版_1957680451332796417.json
hash: 42eff53fda150ded
coverage: 0.8375
learned_at: 2026-10-15 22:31:17
nodes: [WanVideoTorchCompileSettings, ImageResizeKJv2, WanVideoVAELoader, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoBlockSwap, RH_Captioner, easy showAnything, Text Concatenate, RH_Translator, PreviewImage, JWInteger, WanVideoImageToVideoEncode, easy showAnything, easy showAnything, easy compare, easy ifElse, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, easy showAnything, easy showAnything, easy showAnything, MultiTalkModelLoader, easy showAnything, easy imageScaleDownToSize, PlaySound|pysssss, ImageScale, WanVideoTextEncode, AudioSeparation, WanVideoSampler, AudioCrop, DownloadAndLoadWav2VecModel, ImageUpscaleWithModel, easy showAnything, JWIntegerToString, JWIntegerToString, ImageResizeKJv2, easy anythingIndexSwitch, VHS_VideoCombine, JWInteger, JWInteger, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoEncode, WanVideoUni3C_ControlnetLoader, VHS_VideoCombine, LoadAudio, WanVideoClipVisionEncode, WanVideoModelLoader, WanVideoUni3C_embeds, WanVideoDecode, MultiTalkWav2VecEmbeds, WanVideoContextOptions, WanVideoLoraSelect, easy anythingIndexSwitch, VHS_DuplicateImages, MathExpression|pysssss, INTConstant, SimpleMath+, VHS_LoadVideo, LoadImage, CR Text, JWInteger, JWInteger, JWInteger, JWInteger, UpscaleModelLoader, SimpleMath+, SimpleMath+, easy showAnything, RIFE VFI, PlaySound|pysssss, easy showAnything, JWInteger, VHS_LoadVideo, easy imageSize, ImageResizeKJv2, easy anythingIndexSwitch, easy anythingIndexSwitch]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1  Multitalk数字人图片开口唱歌稳定放大功能齐全版_1957680451332796417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957680451332796417.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（80 个）：
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `RH_Captioner`
- `easy showAnything`
- `Text Concatenate`
- `RH_Translator`
- `PreviewImage`
- `JWInteger`
- `WanVideoImageToVideoEncode`
- `easy showAnything`
- `easy showAnything`
- `easy compare`
- `easy ifElse`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `MultiTalkModelLoader`
- `easy showAnything`
- `easy imageScaleDownToSize`
- `PlaySound|pysssss`
- `ImageScale`
- `WanVideoTextEncode`
- `AudioSeparation`
- `WanVideoSampler` ★核心
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `ImageUpscaleWithModel`
- `easy showAnything`
- `JWIntegerToString`
- `JWIntegerToString`
- `ImageResizeKJv2`
- `easy anythingIndexSwitch`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_VideoCombine`
- `LoadAudio`
- `WanVideoClipVisionEncode`
- `WanVideoModelLoader`
- `WanVideoUni3C_embeds`
- `WanVideoDecode`
- `MultiTalkWav2VecEmbeds`
- `WanVideoContextOptions`
- `WanVideoLoraSelect`
- `easy anythingIndexSwitch`
- `VHS_DuplicateImages`
- `MathExpression|pysssss`
- `INTConstant`
- `SimpleMath+`
- `VHS_LoadVideo`
- `LoadImage`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `UpscaleModelLoader`
- `SimpleMath+`
- `SimpleMath+`
- `easy showAnything`
- `RIFE VFI`
- `PlaySound|pysssss`
- `easy showAnything`
- `JWInteger`
- `VHS_LoadVideo`
- `easy imageSize`
- `ImageResizeKJv2`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`

## 知识

覆盖率 **84%**（67/80）

**有卡**：`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`RH_Captioner`、`Text Concatenate`、`RH_Translator`、`JWInteger`、`WanVideoImageToVideoEncode`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`MultiTalkModelLoader`、`easy imageScaleDownToSize`、`PlaySound|pysssss`、`ImageScale`、`WanVideoTextEncode`、`AudioSeparation`、`WanVideoSampler`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`ImageUpscaleWithModel`、`JWIntegerToString`、`easy anythingIndexSwitch`、`VHS_VideoCombine`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`LoadAudio`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoUni3C_embeds`、`WanVideoDecode`、`MultiTalkWav2VecEmbeds`、`WanVideoContextOptions`、`WanVideoLoraSelect`、`VHS_DuplicateImages`、`MathExpression|pysssss`、`INTConstant`、`SimpleMath+`、`VHS_LoadVideo`、`LoadImage`、`CR Text`、`UpscaleModelLoader`、`RIFE VFI`、`easy imageSize`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
