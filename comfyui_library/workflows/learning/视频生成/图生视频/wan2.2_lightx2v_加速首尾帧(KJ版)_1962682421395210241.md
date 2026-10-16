---
key: 视频生成/图生视频/wan2.2_lightx2v_加速首尾帧(KJ版)_1962682421395210241.json
name: wan2.2_lightx2v_加速首尾帧(KJ版)_1962682421395210241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962682421395210241.json
hash: 2a73f579d948b7d1
coverage: 0.984848
learned_at: 2026-10-15 22:31:31
nodes: [easy setNode, easy setNode, easy setNode, easy seed, easy setNode, easy setNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy setNode, easy setNode, easy setNode, easy setNode, easy setNode, easy setNode, WanVideoClipVisionEncode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, easy setNode, WanVideoSetLoRAs, easy getNode, easy getNode, easy getNode, easy getNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, easy getNode, Fast Groups Muter (rgthree), easy setNode, easy getNode, easy getNode, WanVideoDecode, easy getNode, ImageConcanate, easy getNode, easy setNode, VHS_VideoCombine, easy getNode, VHS_VideoCombine, ImageConcatMulti, EmptyImage, easy getNode, WanVideoSampler, LoadImage, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, CreateCFGScheduleFloatList, easy positive, LoadImage, easy int, easy int, easy int, easy int, easy float, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2_lightx2v_加速首尾帧(KJ版)_1962682421395210241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962682421395210241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（66 个）：
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy seed`
- `easy setNode`
- `easy setNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `WanVideoClipVisionEncode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `easy setNode`
- `WanVideoSetLoRAs`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `easy getNode`
- `Fast Groups Muter (rgthree)`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `WanVideoDecode`
- `easy getNode`
- `ImageConcanate`
- `easy getNode`
- `easy setNode`
- `VHS_VideoCombine`
- `easy getNode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `EmptyImage`
- `easy getNode`
- `WanVideoSampler` ★核心
- `LoadImage`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `CreateCFGScheduleFloatList`
- `easy positive`
- `LoadImage`
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `easy float`
- `WanVideoBlockSwap`

## 知识

覆盖率 **98%**（65/66）

**有卡**：`easy setNode`、`easy seed`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoClipVisionEncode`、`easy getNode`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`、`VHS_VideoCombine`、`ImageConcatMulti`、`EmptyImage`、`LoadImage`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`CreateCFGScheduleFloatList`、`easy positive`、`easy int`、`easy float`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoClipTextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
