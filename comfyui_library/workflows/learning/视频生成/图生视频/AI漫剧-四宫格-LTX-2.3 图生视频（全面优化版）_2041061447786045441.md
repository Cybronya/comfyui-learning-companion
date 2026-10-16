---
key: 视频生成/图生视频/AI漫剧-四宫格-LTX-2.3 图生视频（全面优化版）_2041061447786045441.json
name: AI漫剧-四宫格-LTX-2.3 图生视频（全面优化版）_2041061447786045441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041061447786045441.json
hash: 1e26b8050fe3f548
coverage: 0.639175
learned_at: 2026-10-15 22:36:17
nodes: [GetNode, easy cleanGpuUsed, RH_LLMAPI_Pro_Node, easy showAnything, Fast Groups Bypasser (rgthree), PrimitiveNode, Fast Groups Bypasser (rgthree), SetNode, DualCLIPLoader, SetNode, LatentUpscaleModelLoader, SetNode, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, RandomNoise, VHS_VideoCombine, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVCropGuides, LTXVAudioVAEDecode, GetNode, GetNode, VAEDecodeTiled, easy cleanGpuUsed, GetNode, PrimitiveFloat, INTConstant, SimpleMath+, SetNode, SetNode, VAELoader, UNETLoader, LTXVAddGuideMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, CR Float To Integer, LoadImage, ImageConcanate, ImageConcanate, TTResolutionSelector, 孤海-图像添加水印, 孤海-图像添加水印, 孤海-图像添加水印, 孤海-图像添加水印, LTXVConditioning, GetNode, CLIPTextEncode, CLIPTextEncode, LoadImage, LoadImage, LoadImage, SaveImage, RH_Nano_Banana2_Gemini31Flash, CR Text, Fast Groups Bypasser (rgthree), GuHaiAutoImageSplit, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, LoadImage, LoadImage, LoadImage, ImageConcanate, LoadImage, PreviewImage, easy showAnything, Text, LoadImage, Text, UNETLoader, RH_LLMAPI_Pro_Node, RHHiddenNodes]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/AI漫剧-四宫格-LTX-2.3 图生视频（全面优化版）_2041061447786045441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041061447786045441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `GetNode`
- `easy cleanGpuUsed`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveNode`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `RandomNoise`
- `VHS_VideoCombine`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `PrimitiveFloat`
- `INTConstant`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `VAELoader`
- `UNETLoader` ★核心
- `LTXVAddGuideMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `CR Float To Integer`
- `LoadImage`
- `ImageConcanate`
- `ImageConcanate`
- `TTResolutionSelector`
- `孤海-图像添加水印`
- `孤海-图像添加水印`
- `孤海-图像添加水印`
- `孤海-图像添加水印`
- `LTXVConditioning`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageConcanate`
- `LoadImage`
- `PreviewImage`
- `easy showAnything`
- `Text`
- `LoadImage`
- `Text`
- `UNETLoader` ★核心
- `RH_LLMAPI_Pro_Node`
- `RHHiddenNodes`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **64%**（62/97）

**有卡**：`easy cleanGpuUsed`、`RH_LLMAPI_Pro_Node`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`ImageResizeKJv2`、`RandomNoise`、`VHS_VideoCombine`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`INTConstant`、`SimpleMath+`、`VAELoader`、`UNETLoader`、`LTXVAddGuideMulti`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`CR Float To Integer`、`LoadImage`、`ImageConcanate`、`TTResolutionSelector`、`孤海-图像添加水印`、`LTXVConditioning`、`CLIPTextEncode`、`SaveImage`、`RH_Nano_Banana2_Gemini31Flash`、`CR Text`、`GuHaiAutoImageSplit`、`ImageFromBatch+`、`Text`、`RHHiddenNodes`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
