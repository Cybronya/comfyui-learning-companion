---
key: 图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072539419097264129.json
name: MiniCPM4.5视频反推提示词_2072539419097264129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072539419097264129.json
hash: 77d91dc4c93c1c31
coverage: 0.844156
learned_at: 2026-10-26 01:45:40
nodes: [LoadVideo, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImageResizeKJv2, VHS_VideoCombine, WanVideoBlockSwap, CLIPVisionLoader, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, LoadImage, VHS_VideoCombine, WanVideoClipVisionEncode, GetImageSizeAndCount, PrimitiveInt, MarkdownNote, PrimitiveInt, CR Text, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, WanVideoEmptyEmbeds, WanVideoTorchCompileSettings, ShowText|pysssss, easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoLoraSelect, PrimitiveInt, CR Text, WanVideoTextEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageFromBatch+, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, INTConstant, VHS_VideoCombine, Wan_video_prompt_generator, MarkdownNote, MarkdownNote, PrimitiveInt, MarkdownNote, ShellAgentPluginOutputText, ShowText|pysssss, Fast Groups Bypasser (rgthree), AILab_MiniCPM_4_V_Advanced, LoadImage, SaveImage, MarkdownNote]
patterns: []
missing: []
---

# 图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072539419097264129.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072539419097264129.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（77 个）：
- `LoadVideo`
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
- `WanVideoClipVisionEncode`
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
- `Fast Groups Bypasser (rgthree)`
- `AILab_MiniCPM_4_V_Advanced`
- `LoadImage`
- `SaveImage`
- `MarkdownNote`

## 知识

覆盖率 **84%**（65/77）

**有卡**：`LoadVideo`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSampler`、`LoadImage`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`CR Text`、`WanVideoEmptyEmbeds`、`ImageFromBatch+`、`INTConstant`、`Wan_video_prompt_generator`、`ShellAgentPluginOutputText`、`AILab_MiniCPM_4_V_Advanced`、`SaveImage`

**用到的条目**：SaveImage、LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
