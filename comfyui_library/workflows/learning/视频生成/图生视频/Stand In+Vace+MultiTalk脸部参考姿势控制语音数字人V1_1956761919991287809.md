---
key: 视频生成/图生视频/Stand In+Vace+MultiTalk脸部参考姿势控制语音数字人V1_1956761919991287809.json
name: Stand In+Vace+MultiTalk脸部参考姿势控制语音数字人V1_1956761919991287809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Stand In+Vace+MultiTalk脸部参考姿势控制语音数字人V1_1956761919991287809.json
hash: e1c78f9d7f2c52c3
coverage: 0.869565
learned_at: 2026-10-15 22:31:15
nodes: [WanVideoLoraSelect, WanVideoDecode, JWInteger, VHS_VideoInfo, ApplyFaceProcessor, DWPreprocessor, VHS_VideoCombine, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, WanVideoVACEModelSelect, WanVideoVAELoader, Note, Note, Note, CR Text, easy showAnything, ImageResizeKJv2, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, WanVideoEncode, WanVideoVACEStartToEndFrame, WanVideoVACEEncode, AudioSeparation, DownloadAndLoadWav2VecModel, LayerUtility: PurgeVRAM, MultiTalkWav2VecEmbeds, WanVideoAddStandInLatent, PreviewImage, WanVideoTextEncode, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, PreviewAudio, LayerUtility: PurgeVRAM, WanVideoSampler, VHS_VideoCombine, LoadImage, VHS_LoadVideo, WanVideoBlockSwap, FaceProcessorLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Stand In+Vace+MultiTalk脸部参考姿势控制语音数字人V1_1956761919991287809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956761919991287809.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `JWInteger`
- `VHS_VideoInfo`
- `ApplyFaceProcessor`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `Note`
- `Note`
- `Note`
- `CR Text`
- `easy showAnything`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `WanVideoEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEEncode`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: PurgeVRAM`
- `MultiTalkWav2VecEmbeds`
- `WanVideoAddStandInLatent`
- `PreviewImage`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PreviewAudio`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `FaceProcessorLoader`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`WanVideoLoraSelect`、`WanVideoDecode`、`JWInteger`、`VHS_VideoInfo`、`ApplyFaceProcessor`、`DWPreprocessor`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`MultiTalkModelLoader`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`CR Text`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoEncode`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`LayerUtility: PurgeVRAM`、`MultiTalkWav2VecEmbeds`、`WanVideoAddStandInLatent`、`WanVideoTextEncode`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`PreviewAudio`、`WanVideoSampler`、`LoadImage`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`FaceProcessorLoader`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
