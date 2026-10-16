---
key: 视频生成/图生视频/KTV歌后音乐生成器1.0_1967011405411049474.json
name: KTV歌后音乐生成器1.0_1967011405411049474.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967011405411049474.json
hash: 4d167fbfd879f931
coverage: 0.933333
learned_at: 2026-10-15 22:31:40
nodes: [GetTextFromJson, GetTextFromJson, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoSampler, WanVideoTorchCompileSettings, DownloadAndLoadWav2VecModel, Text Concatenate, LoadWanVideoT5TextEncoder, WanVideoVAELoader, MultiTalkWav2VecEmbeds, WanVideoTextEncode, WanVideoImageToVideoEncode, CreateCFGScheduleFloatList, RH_Captioner, easy showAnything, ImageResizeKJv2, WanVideoBlockSwap, Fast Groups Bypasser (rgthree), SaveAudio, MathExpression|pysssss, INTConstant, VHS_DuplicateImages, ImageResizeKJv2, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoDecode, WanVideoModelLoader, WanVideoLoraSelect, AudioSeparation, SaveAudio, Text Concatenate, LoadJsonFromText, ReplaceText, ReplaceText, RH_LLMAPI_NODE, ShowText, ShowText, Primitive integer [Crystools], Primitive integer [Crystools], SongGeneration_Stage2, SongGeneration_Sampler, Text Multiline, Primitive integer [Crystools], AudioCrop, RandomInt, StringReplace, easy showAnything, Text Multiline, SongGeneration_Stage1, ShowText, Save Text File, MultiTalkModelLoader, VHS_VideoCombine, VHS_LoadVideo, LoadImage, Text Multiline, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/KTV歌后音乐生成器1.0_1967011405411049474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967011405411049474.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（60 个）：
- `GetTextFromJson`
- `GetTextFromJson`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `DownloadAndLoadWav2VecModel`
- `Text Concatenate`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `MultiTalkWav2VecEmbeds`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `CreateCFGScheduleFloatList`
- `RH_Captioner`
- `easy showAnything`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `Fast Groups Bypasser (rgthree)`
- `SaveAudio`
- `MathExpression|pysssss`
- `INTConstant`
- `VHS_DuplicateImages`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `AudioSeparation`
- `SaveAudio`
- `Text Concatenate`
- `LoadJsonFromText`
- `ReplaceText`
- `ReplaceText`
- `RH_LLMAPI_NODE`
- `ShowText`
- `ShowText`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `SongGeneration_Stage2`
- `SongGeneration_Sampler` ★核心
- `Text Multiline`
- `Primitive integer [Crystools]`
- `AudioCrop`
- `RandomInt`
- `StringReplace`
- `easy showAnything`
- `Text Multiline`
- `SongGeneration_Stage1`
- `ShowText`
- `Save Text File`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `Text Multiline`
- `Note`

## 知识

覆盖率 **93%**（56/60）

**有卡**：`GetTextFromJson`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`DownloadAndLoadWav2VecModel`、`Text Concatenate`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`MultiTalkWav2VecEmbeds`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`RH_Captioner`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`SaveAudio`、`MathExpression|pysssss`、`INTConstant`、`VHS_DuplicateImages`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`AudioSeparation`、`LoadJsonFromText`、`ReplaceText`、`RH_LLMAPI_NODE`、`ShowText`、`Primitive integer [Crystools]`、`SongGeneration_Stage2`、`SongGeneration_Sampler`、`Text Multiline`、`AudioCrop`、`RandomInt`、`StringReplace`、`SongGeneration_Stage1`、`Save Text File`、`MultiTalkModelLoader`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、CreateCFGScheduleFloatList、SongGeneration_Sampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
