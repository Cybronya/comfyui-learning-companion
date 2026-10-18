---
key: 视频生成/图生视频/longcat avartart 1.5-single_2061466076168409089.json
name: longcat avartart 1.5-single_2061466076168409089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/longcat avartart 1.5-single_2061466076168409089.json
hash: 62e4671bc2b3697b
coverage: 0.52381
learned_at: 2026-10-15 22:38:54
nodes: [WanAnimatePlus BlockSwap, SetNode, SetNode, SetNode, WanVideoVAELoader, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, ComfyMathExpression, GetNode, PreviewAny, WanVideoModelLoader, WanVideoLoraSelect, SetNode, WanVideoSchedulerv2, LoadImage, ImageResizeKJv2, GetNode, GetNode, SetNode, INTConstant, INTConstant, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, LoadAudio, TrimAudioDuration, GetNode, FloatConstant, WhisperModelLoader, LongCatAvatarWhisperEmbeds, WanVideoTextEncodeCached, ComfyMathExpression, GetNode, WanVideoSamplerv2, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/longcat avartart 1.5-single_2061466076168409089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061466076168409089.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `WanAnimatePlus BlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `PreviewAny`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `SetNode`
- `WanVideoSchedulerv2`
- `LoadImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `LoadAudio`
- `TrimAudioDuration`
- `GetNode`
- `FloatConstant`
- `WhisperModelLoader`
- `LongCatAvatarWhisperEmbeds`
- `WanVideoTextEncodeCached`
- `ComfyMathExpression`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoDecode`

## 知识

覆盖率 **52%**（22/42）

**有卡**：`WanAnimatePlus BlockSwap`、`WanVideoVAELoader`、`VHS_VideoCombine`、`ComfyMathExpression`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSchedulerv2`、`LoadImage`、`ImageResizeKJv2`、`INTConstant`、`WanVideoEncode`、`WanVideoLongCatAvatarExtendEmbeds`、`LoadAudio`、`TrimAudioDuration`、`FloatConstant`、`WhisperModelLoader`、`LongCatAvatarWhisperEmbeds`、`WanVideoTextEncodeCached`、`WanVideoSamplerv2`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、ImageResizeKJv2
