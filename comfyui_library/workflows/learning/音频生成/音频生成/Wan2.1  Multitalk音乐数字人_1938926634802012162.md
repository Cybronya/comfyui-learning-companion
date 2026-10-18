---
key: 音频生成/音频生成/Wan2.1  Multitalk音乐数字人_1938926634802012162.json
name: Wan2.1  Multitalk音乐数字人_1938926634802012162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Wan2.1  Multitalk音乐数字人_1938926634802012162.json
hash: e2ae9268202e01f8
coverage: 0.8375
learned_at: 2026-10-18 01:24:03
nodes: [WanVideoTorchCompileSettings, ImageResizeKJv2, WanVideoVAELoader, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoBlockSwap, RH_Captioner, easy showAnything, Text Concatenate, RH_Translator, easy imageSize, PreviewImage, JWInteger, WanVideoImageToVideoEncode, easy showAnything, easy showAnything, easy compare, easy ifElse, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, easy showAnything, easy showAnything, easy showAnything, MultiTalkModelLoader, easy showAnything, easy imageScaleDownToSize, PlaySound|pysssss, easy showAnything, PlaySound|pysssss, easy showAnything, SimpleMath+, ImageScale, WanVideoTextEncode, AudioSeparation, RIFE VFI, MathExpression|pysssss, SimpleMath+, WanVideoSampler, AudioCrop, DownloadAndLoadWav2VecModel, ImageUpscaleWithModel, UpscaleModelLoader, easy showAnything, JWIntegerToString, JWIntegerToString, ImageResizeKJv2, INTConstant, easy anythingIndexSwitch, ImageResizeKJv2, easy anythingIndexSwitch, easy anythingIndexSwitch, VHS_VideoCombine, JWInteger, VHS_LoadVideo, JWInteger, JWInteger, JWInteger, JWInteger, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, WanVideoSLG, easy anythingIndexSwitch, WanVideoEncode, WanVideoUni3C_ControlnetLoader, VHS_LoadVideo, SimpleMath+, VHS_VideoCombine, LoadAudio, WanVideoClipVisionEncode, JWInteger, CR Text, JWInteger, VHS_DuplicateImages, WanVideoModelLoader, WanVideoUni3C_embeds, WanVideoDecode, MultiTalkWav2VecEmbeds, WanVideoContextOptions, WanVideoLoraSelect, LoadImage]
patterns: []
missing: []
---

# 音频生成/音频生成/Wan2.1  Multitalk音乐数字人_1938926634802012162.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Wan2.1  Multitalk音乐数字人_1938926634802012162.json`

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
- `easy imageSize`
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
- `easy showAnything`
- `PlaySound|pysssss`
- `easy showAnything`
- `SimpleMath+`
- `ImageScale`
- `WanVideoTextEncode`
- `AudioSeparation`
- `RIFE VFI`
- `MathExpression|pysssss`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `easy showAnything`
- `JWIntegerToString`
- `JWIntegerToString`
- `ImageResizeKJv2`
- `INTConstant`
- `easy anythingIndexSwitch`
- `ImageResizeKJv2`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `VHS_VideoCombine`
- `JWInteger`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `easy anythingIndexSwitch`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_LoadVideo`
- `SimpleMath+`
- `VHS_VideoCombine`
- `LoadAudio`
- `WanVideoClipVisionEncode`
- `JWInteger`
- `CR Text`
- `JWInteger`
- `VHS_DuplicateImages`
- `WanVideoModelLoader`
- `WanVideoUni3C_embeds`
- `WanVideoDecode`
- `MultiTalkWav2VecEmbeds`
- `WanVideoContextOptions`
- `WanVideoLoraSelect`
- `LoadImage`

## 知识

覆盖率 **84%**（67/80）

**有卡**：`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`RH_Captioner`、`Text Concatenate`、`RH_Translator`、`easy imageSize`、`JWInteger`、`WanVideoImageToVideoEncode`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`MultiTalkModelLoader`、`easy imageScaleDownToSize`、`PlaySound|pysssss`、`SimpleMath+`、`ImageScale`、`WanVideoTextEncode`、`AudioSeparation`、`RIFE VFI`、`MathExpression|pysssss`、`WanVideoSampler`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`JWIntegerToString`、`INTConstant`、`easy anythingIndexSwitch`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`LoadAudio`、`WanVideoClipVisionEncode`、`CR Text`、`VHS_DuplicateImages`、`WanVideoModelLoader`、`WanVideoUni3C_embeds`、`WanVideoDecode`、`MultiTalkWav2VecEmbeds`、`WanVideoContextOptions`、`WanVideoLoraSelect`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
