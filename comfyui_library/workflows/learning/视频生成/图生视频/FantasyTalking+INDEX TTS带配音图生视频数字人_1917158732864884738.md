---
key: 视频生成/图生视频/FantasyTalking+INDEX TTS带配音图生视频数字人_1917158732864884738.json
name: FantasyTalking+INDEX TTS带配音图生视频数字人_1917158732864884738.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/FantasyTalking+INDEX TTS带配音图生视频数字人_1917158732864884738.json
hash: 7f64bffc9870fbbf
coverage: 0.942857
learned_at: 2026-10-15 22:29:39
nodes: [WanVideoTextEncode, WanVideoModelLoader, WanVideoDecode, VHS_VideoCombine, WanVideoVAELoader, WanVideoBlockSwap, WanVideoTeaCache, LoadImage, CLIPVisionLoader, WanVideoClipVisionEncode, FantasyTalkingModelLoader, WanVideoSampler, DownloadAndLoadWav2VecModel, FantasyTalkingWav2VecEmbeds, ImageResizeKJ, ImageConcanate, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Text Multiline, Reroute, UpscaleModelLoader, ImageUpscaleWithModel, LayerUtility: PurgeVRAM, Note Plus (mtb), VHS_VideoCombine, PreviewAudio, easy cleanGpuUsed, Note, IndexTTSNode, LoadAudio, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/FantasyTalking+INDEX TTS带配音图生视频数字人_1917158732864884738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917158732864884738.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoTeaCache`
- `LoadImage`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `FantasyTalkingModelLoader`
- `WanVideoSampler` ★核心
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingWav2VecEmbeds`
- `ImageResizeKJ`
- `ImageConcanate`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `Reroute`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM`
- `Note Plus (mtb)`
- `VHS_VideoCombine`
- `PreviewAudio`
- `easy cleanGpuUsed`
- `Note`
- `IndexTTSNode`
- `LoadAudio`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `INTConstant`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTeaCache`、`LoadImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`FantasyTalkingModelLoader`、`WanVideoSampler`、`DownloadAndLoadWav2VecModel`、`FantasyTalkingWav2VecEmbeds`、`ImageResizeKJ`、`ImageConcanate`、`Primitive integer [Crystools]`、`Text Multiline`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LayerUtility: PurgeVRAM`、`Note Plus (mtb)`、`PreviewAudio`、`easy cleanGpuUsed`、`IndexTTSNode`、`LoadAudio`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
