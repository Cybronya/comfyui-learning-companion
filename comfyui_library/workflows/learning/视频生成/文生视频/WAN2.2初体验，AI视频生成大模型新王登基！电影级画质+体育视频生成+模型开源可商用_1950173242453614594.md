---
key: 视频生成/文生视频/WAN2.2初体验，AI视频生成大模型新王登基！电影级画质+体育视频生成+模型开源可商用_1950173242453614594.json
name: WAN2.2初体验，AI视频生成大模型新王登基！电影级画质+体育视频生成+模型开源可商用_1950173242453614594.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950173242453614594.json
hash: 910424729be4d63d
coverage: 0.938596
learned_at: 2026-10-15 22:43:34
nodes: [CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, UNETLoader, UNETLoader, CreateVideo, CLIPLoader, VAELoader, VAEDecode, CreateVideo, SaveVideo, Wan22ImageToVideoLatent, CLIPTextEncode, MarkdownNote, KSampler, CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, SaveVideo, UNETLoader, UNETLoader, MarkdownNote, CreateVideo, EmptyHunyuanLatentVideo, Label (rgthree), Label (rgthree), CLIPLoader, VAELoader, VAEDecode, CreateVideo, SaveVideo, Wan22ImageToVideoLatent, CLIPTextEncode, MarkdownNote, ModelSamplingSD3, KSampler, Label (rgthree), Note, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, Label (rgthree), ImageResizeKJv2, WanVideoVAELoader, WanVideoLoraSelect, WanVideoImageToVideoEncode, UNETLoader, Note, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoVAELoader, Label (rgthree), WanImageToVideo, WanVideoEmptyEmbeds, UNETLoader, ModelSamplingSD3, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, INTConstant, INTConstant, Label (rgthree), Label (rgthree), Label (rgthree), Fast Groups Bypasser (rgthree), CLIPTextEncode, LoadImage, CLIPTextEncode, CLIPTextEncode, LoadImage, CLIPTextEncode, SaveVideo, WanVideoTextEncode, INTConstant, INTConstant, WanVideoModelLoader, VHS_VideoCombine, LoadImage, WanVideoTextEncode, VHS_VideoCombine, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 910656015066797, "steps": 20}
---

# 视频生成/文生视频/WAN2.2初体验，AI视频生成大模型新王登基！电影级画质+体育视频生成+模型开源可商用_1950173242453614594.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950173242453614594.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（114 个）：
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CreateVideo`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `Wan22ImageToVideoLatent`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `KSampler` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `CreateVideo`
- `EmptyHunyuanLatentVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `Wan22ImageToVideoLatent`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `Label (rgthree)`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `Label (rgthree)`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `UNETLoader` ★核心
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `Label (rgthree)`
- `WanImageToVideo`
- `WanVideoEmptyEmbeds`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `INTConstant`
- `INTConstant`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `WanVideoTextEncode`
- `INTConstant`
- `INTConstant`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `Label (rgthree)`

## 关键参数

- `seed` = `910656015066797`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（107/114）

**有卡**：`CLIPLoader`、`KSamplerAdvanced`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`CreateVideo`、`SaveVideo`、`Wan22ImageToVideoLatent`、`KSampler`、`EmptyHunyuanLatentVideo`、`Label (rgthree)`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoImageToVideoEncode`、`WanImageToVideo`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`、`INTConstant`、`LoadImage`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
