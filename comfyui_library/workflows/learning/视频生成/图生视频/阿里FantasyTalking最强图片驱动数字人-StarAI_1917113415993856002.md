---
key: 视频生成/图生视频/阿里FantasyTalking最强图片驱动数字人-StarAI_1917113415993856002.json
name: 阿里FantasyTalking最强图片驱动数字人-StarAI_1917113415993856002.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1917113415993856002.json
hash: a9b648776be32acf
coverage: 0.941176
learned_at: 2026-10-15 22:29:39
nodes: [WanVideoImageToVideoEncode, FantasyTalkingWav2VecEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, CLIPVisionLoader, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoBlockSwap, WanVideoDecode, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, IndexTTSNode, CR Text, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, ImpactSwitch, Int, WanVideoTextEncode, Note, WanVideoVAELoader, Note Plus (mtb), CR Text, VHS_VideoCombine, Int, LoadImage, WanVideoTeaCache, WanVideoModelLoader, LoadAudio, WanVideoSampler, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/阿里FantasyTalking最强图片驱动数字人-StarAI_1917113415993856002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917113415993856002.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `WanVideoImageToVideoEncode`
- `FantasyTalkingWav2VecEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `IndexTTSNode`
- `CR Text`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactSwitch`
- `Int`
- `WanVideoTextEncode`
- `Note`
- `WanVideoVAELoader`
- `Note Plus (mtb)`
- `CR Text`
- `VHS_VideoCombine`
- `Int`
- `LoadImage`
- `WanVideoTeaCache`
- `WanVideoModelLoader`
- `LoadAudio`
- `WanVideoSampler` ★核心
- `Int`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`WanVideoImageToVideoEncode`、`FantasyTalkingWav2VecEmbeds`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`easy cleanGpuUsed`、`WanVideoBlockSwap`、`WanVideoDecode`、`DownloadAndLoadWav2VecModel`、`FantasyTalkingModelLoader`、`IndexTTSNode`、`CR Text`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`WanVideoTextEncode`、`WanVideoVAELoader`、`Note Plus (mtb)`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTeaCache`、`WanVideoModelLoader`、`LoadAudio`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
