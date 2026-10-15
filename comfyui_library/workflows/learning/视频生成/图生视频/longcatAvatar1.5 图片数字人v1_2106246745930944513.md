---
key: 视频生成/图生视频/longcatAvatar1.5 图片数字人v1_2106246745930944513.json
name: longcatAvatar1.5 图片数字人v1_2106246745930944513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/longcatAvatar1.5 图片数字人v1_2106246745930944513.json
hash: 27fe8bada34c6d24
coverage: 1
learned_at: 2026-10-15 22:42:58
nodes: [WanVideoSetBlockSwap, LongCatAvatarWhisperEmbeds, WanVideoModelLoader, WanVideoLoraSelect, WhisperModelLoader, LoadWanVideoT5TextEncoder, WanVideoDecode, VHS_VideoCombine, FloatConstant, WanVideoBlockSwap, WanVideoVAELoader, INTConstant, INTConstant, WanVideoLongCatAvatarExtendEmbeds, ImageResizeKJv2, WanVideoEncode, WanVideoSampler, TrimAudioDuration, ComfyNumberConvert, ComfyMathExpression, LoadImage, LoadAudio, WanVideoTextEncode, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/longcatAvatar1.5 图片数字人v1_2106246745930944513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/longcatAvatar1.5 图片数字人v1_2106246745930944513.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（24 个）：
- `WanVideoSetBlockSwap`
- `LongCatAvatarWhisperEmbeds`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WhisperModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `FloatConstant`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `INTConstant`
- `INTConstant`
- `WanVideoLongCatAvatarExtendEmbeds`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `TrimAudioDuration`
- `ComfyNumberConvert`
- `ComfyMathExpression`
- `LoadImage`
- `LoadAudio`
- `WanVideoTextEncode`
- `CR Text`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`WanVideoSetBlockSwap`、`LongCatAvatarWhisperEmbeds`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WhisperModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`VHS_VideoCombine`、`FloatConstant`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`INTConstant`、`WanVideoLongCatAvatarExtendEmbeds`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoSampler`、`TrimAudioDuration`、`ComfyNumberConvert`、`ComfyMathExpression`、`LoadImage`、`LoadAudio`、`WanVideoTextEncode`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
