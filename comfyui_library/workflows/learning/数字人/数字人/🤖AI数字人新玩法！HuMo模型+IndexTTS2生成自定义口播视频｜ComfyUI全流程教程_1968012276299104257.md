---
key: 数字人/数字人/🤖AI数字人新玩法！HuMo模型+IndexTTS2生成自定义口播视频｜ComfyUI全流程教程_1968012276299104257.json
name: 🤖AI数字人新玩法！HuMo模型+IndexTTS2生成自定义口播视频｜ComfyUI全流程教程_1968012276299104257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/🤖AI数字人新玩法！HuMo模型+IndexTTS2生成自定义口播视频｜ComfyUI全流程教程_1968012276299104257.json
hash: 5ea323f51dcdcd35
coverage: 0.767442
learned_at: 2026-10-26 02:06:20
nodes: [Note, WanVideoSetBlockSwap, ImageResizeKJv2, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoVAELoader, CreateCFGScheduleFloatList, MelBandRoFormerSampler, NormalizeAudioLoudness, WhisperModelLoader, SetNode, GetNode, MarkdownNote, Note, Note, WanVideoTorchCompileSettings, PreviewImage, Note, ImageBatchMulti, PreviewAudio, NormalizeAudioLoudness, MelBandRoFormerSampler, MelBandRoFormerModelLoader, Note, IndexTTS2Run, PreviewAudio, SaveAudio, PrimitiveString, ttN text, LoadAudio, WanVideoModelLoader, WanVideoLoraSelect, MelBandRoFormerModelLoader, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, HuMoEmbeds, INTConstant, INTConstant, WanVideoTextEncodeCached, LoadAudio, LoadImage, Label (rgthree)]
patterns: []
missing: []
---

# 数字人/数字人/🤖AI数字人新玩法！HuMo模型+IndexTTS2生成自定义口播视频｜ComfyUI全流程教程_1968012276299104257.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/🤖AI数字人新玩法！HuMo模型+IndexTTS2生成自定义口播视频｜ComfyUI全流程教程_1968012276299104257.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `CreateCFGScheduleFloatList`
- `MelBandRoFormerSampler` ★核心
- `NormalizeAudioLoudness`
- `WhisperModelLoader`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `PreviewImage`
- `Note`
- `ImageBatchMulti`
- `PreviewAudio`
- `NormalizeAudioLoudness`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `Note`
- `IndexTTS2Run`
- `PreviewAudio`
- `SaveAudio`
- `PrimitiveString`
- `ttN text`
- `LoadAudio`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MelBandRoFormerModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `HuMoEmbeds`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `LoadAudio`
- `LoadImage`
- `Label (rgthree)`

## 知识

覆盖率 **77%**（33/43）

**有卡**：`WanVideoSetBlockSwap`、`ImageResizeKJv2`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`WhisperModelLoader`、`WanVideoTorchCompileSettings`、`ImageBatchMulti`、`PreviewAudio`、`MelBandRoFormerModelLoader`、`IndexTTS2Run`、`SaveAudio`、`ttN text`、`LoadAudio`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`HuMoEmbeds`、`INTConstant`、`WanVideoTextEncodeCached`、`LoadImage`、`Label (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、MelBandRoFormerSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect
