---
key: 视频生成/图生视频/创意首尾帧视频制作 WAN2.2-LightX2V-I2V_1981037704194441217.json
name: 创意首尾帧视频制作 WAN2.2-LightX2V-I2V_1981037704194441217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981037704194441217.json
hash: 7bec3df09c77665a
coverage: 0.8
learned_at: 2026-10-15 22:32:36
nodes: [GetNode, KSamplerAdvanced, WanFirstLastFrameToVideo, VAEDecode, CLIPTextEncode, CLIPTextEncode, GetNode, JWInteger, JWInteger, UNETLoader, CLIPLoader, ModelPatchTorchSettings, wanBlockSwap, ModelSamplingSD3, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, SetNode, SetNode, SetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, wanBlockSwap, PathchSageAttentionKJ, VAELoader, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, GetNode, GetNode, MathExpression|pysssss, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, RH_LLMAPI_NODE, ImageConcanate, ImageResizeKJ, CLIPVisionEncode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSamplerAdvanced, easy showAnything, ImpactSwitch, Note, CR Text, VHS_VideoCombine, VHS_VideoCombine, CR Text, CR Text, CR Text, VHS_VideoCombine, LoadImage, RH_Nano_Banana_Image2Image, CR Text, PreviewImage, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/创意首尾帧视频制作 WAN2.2-LightX2V-I2V_1981037704194441217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981037704194441217.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `GetNode`
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `RH_LLMAPI_NODE`
- `ImageConcanate`
- `ImageResizeKJ`
- `CLIPVisionEncode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `ImpactSwitch`
- `Note`
- `CR Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Text`
- `CR Text`
- `CR Text`
- `VHS_VideoCombine`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `CR Text`
- `PreviewImage`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（48/60）

**有卡**：`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPTextEncode`、`JWInteger`、`UNETLoader`、`CLIPLoader`、`ModelPatchTorchSettings`、`wanBlockSwap`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoader`、`MathExpression|pysssss`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`RH_LLMAPI_NODE`、`ImageConcanate`、`ImageResizeKJ`、`LoadImage`、`CR Text`、`VHS_VideoCombine`、`RH_Nano_Banana_Image2Image`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
