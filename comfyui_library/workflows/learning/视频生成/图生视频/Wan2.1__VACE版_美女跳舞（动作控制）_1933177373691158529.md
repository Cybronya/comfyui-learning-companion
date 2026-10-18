---
key: 视频生成/图生视频/Wan2.1__VACE版_美女跳舞（动作控制）_1933177373691158529.json
name: Wan2.1__VACE版_美女跳舞（动作控制）_1933177373691158529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1__VACE版_美女跳舞（动作控制）_1933177373691158529.json
hash: c352bcfa488e8f12
coverage: 0.84
learned_at: 2026-10-15 22:30:13
nodes: [easy showAnything, ImageUpscaleWithModel, UpscaleModelLoader, PreviewImage, WanVideoDecode, RIFE VFI, PlaySound|pysssss, PlaySound|pysssss, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoTeaCache, WanVideoSampler, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTextEncode, GetImageSizeAndCount, WanVideoVAELoader, easy anythingIndexSwitch, easy showAnything, MimicMotionGetPoses, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVACEEncode, easy showAnything, easy showAnything, SimpleMath+, SimpleMath+, ImageResizeKJv2, WanVideoVACEModelSelect, Text Concatenate, ShowText|pysssss, RH_Captioner, JWInteger, JWInteger, ImageScale, RH_Translator, easy showAnything, ImageResizeKJv2, OpenposePreprocessor, LoadImage, JWInteger, SimpleMath+, JWInteger, JWInteger, SimpleMath+, VHS_LoadVideo, easy showAnything]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1__VACE版_美女跳舞（动作控制）_1933177373691158529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1933177373691158529.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `easy showAnything`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `PreviewImage`
- `WanVideoDecode`
- `RIFE VFI`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `MimicMotionGetPoses`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVACEEncode`
- `easy showAnything`
- `easy showAnything`
- `SimpleMath+`
- `SimpleMath+`
- `ImageResizeKJv2`
- `WanVideoVACEModelSelect`
- `Text Concatenate`
- `ShowText|pysssss`
- `RH_Captioner`
- `JWInteger`
- `JWInteger`
- `ImageScale`
- `RH_Translator`
- `easy showAnything`
- `ImageResizeKJv2`
- `OpenposePreprocessor`
- `LoadImage`
- `JWInteger`
- `SimpleMath+`
- `JWInteger`
- `JWInteger`
- `SimpleMath+`
- `VHS_LoadVideo`
- `easy showAnything`

## 知识

覆盖率 **84%**（42/50）

**有卡**：`ImageUpscaleWithModel`、`UpscaleModelLoader`、`WanVideoDecode`、`RIFE VFI`、`PlaySound|pysssss`、`VHS_VideoCombine`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`easy anythingIndexSwitch`、`MimicMotionGetPoses`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVACEEncode`、`SimpleMath+`、`ImageResizeKJv2`、`WanVideoVACEModelSelect`、`Text Concatenate`、`RH_Captioner`、`JWInteger`、`ImageScale`、`RH_Translator`、`OpenposePreprocessor`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、OpenposePreprocessor、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
