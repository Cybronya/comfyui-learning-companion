---
key: 视频生成/文生视频/MiniCPM4.5视频反推+图生视频+文生视频_2003004980099465217.json
name: MiniCPM4.5视频反推+图生视频+文生视频_2003004980099465217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniCPM4.5视频反推+图生视频+文生视频_2003004980099465217.json
hash: 265ebf224d9b1729
coverage: 0.855263
learned_at: 2026-10-15 22:45:27
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImageResizeKJv2, VHS_VideoCombine, WanVideoBlockSwap, CLIPVisionLoader, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, LoadImage, VHS_VideoCombine, GetImageSizeAndCount, PrimitiveInt, MarkdownNote, PrimitiveInt, CR Text, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, WanVideoEmptyEmbeds, WanVideoTorchCompileSettings, ShowText|pysssss, easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoLoraSelect, PrimitiveInt, CR Text, WanVideoTextEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageFromBatch+, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, INTConstant, VHS_VideoCombine, Wan_video_prompt_generator, MarkdownNote, MarkdownNote, PrimitiveInt, MarkdownNote, ShellAgentPluginOutputText, ShowText|pysssss, AILab_MiniCPM_4_V_Advanced, LoadImage, WanVideoClipVisionEncode, LoadVideo, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniCPM4.5视频反推+图生视频+文生视频_2003004980099465217.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniCPM4.5视频反推+图生视频+文生视频_2003004980099465217.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（76 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `PrimitiveInt`
- `MarkdownNote`
- `PrimitiveInt`
- `CR Text`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoEmptyEmbeds`
- `WanVideoTorchCompileSettings`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `PrimitiveInt`
- `CR Text`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageFromBatch+`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `VHS_VideoCombine`
- `Wan_video_prompt_generator`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveInt`
- `MarkdownNote`
- `ShellAgentPluginOutputText`
- `ShowText|pysssss`
- `AILab_MiniCPM_4_V_Advanced`
- `LoadImage`
- `WanVideoClipVisionEncode`
- `LoadVideo`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **86%**（65/76）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSampler`、`LoadImage`、`GetImageSizeAndCount`、`CR Text`、`WanVideoEmptyEmbeds`、`ImageFromBatch+`、`INTConstant`、`Wan_video_prompt_generator`、`ShellAgentPluginOutputText`、`AILab_MiniCPM_4_V_Advanced`、`WanVideoClipVisionEncode`、`LoadVideo`、`SaveImage`

**用到的条目**：SaveImage、LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
