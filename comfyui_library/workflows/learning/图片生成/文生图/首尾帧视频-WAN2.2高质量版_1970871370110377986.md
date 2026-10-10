---
key: 首尾帧视频-WAN2.2高质量版_1970871370110377986.json
name: 首尾帧视频-WAN2.2高质量版_1970871370110377986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/首尾帧视频-WAN2.2高质量版_1970871370110377986.json
hash: cab9d69a4ea0a3f9
coverage: 0.864865
learned_at: 2026-10-10 21:00:00
nodes: [ImageResize+, ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveNode, JWInteger, WanVideoTextEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, INTConstant, LoadWanVideoClipTextEncoder, WanVideoBlockSwap, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoImageToVideoEncode, SimpleMath+, JWInteger, WanVideoSampler, VHS_VideoCombine, WanVideoDecode, easy cleanGpuUsed, BasicScheduler, RandomNoise, KSamplerSelect, RepeatLatentBatch, FluxGuidance, SamplerCustomAdvanced, EmptyLatentImage, LoraLoader, LoraLoader, Fast Groups Bypasser (rgthree), LoraLoader, DualCLIPLoader, CLIPTextEncode, VAELoader, UNETLoader, BasicScheduler, RandomNoise, KSamplerSelect, RepeatLatentBatch, BasicGuider, FluxGuidance, SamplerCustomAdvanced, SaveImage, EmptyLatentImage, LoraLoader, LoraLoader, Fast Groups Bypasser (rgthree), LoraLoader, DualCLIPLoader, CLIPTextEncode, VAELoader, UNETLoader, LoadImage, BasicGuider, SaveImage, VAEDecode, VAEDecode, LoadImage, RH_Translator, RH_Translator, CR Prompt Text, JWInteger, JWInteger]
patterns: [lora]
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SimpleMath+, easy cleanGpuUsed, CR Prompt Text, ImageResize+, ImageResize+]
parameters: {"batch_size": 1, "height": 1024, "lora_name": "flux-lora-大家电场景图.safetensors", "strength_clip": 0.6000000000000001, "strength_model": 0.6000000000000001, "width": 768}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 首尾帧视频-WAN2.2高质量版_1970871370110377986.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/首尾帧视频-WAN2.2高质量版_1970871370110377986.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `ImageResize+`
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `JWInteger`
- `WanVideoTextEncode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `JWInteger`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `RepeatLatentBatch`
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoraLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `RepeatLatentBatch`
- `BasicGuider`
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoraLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `BasicGuider`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `RH_Translator`
- `RH_Translator`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`

**识别到的模式**：lora

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `flux-lora-大家电场景图.safetensors`
- `strength_model` = `0.6000000000000001`
- `strength_clip` = `0.6000000000000001`

## 知识

覆盖率 **86%**（64/74）

**有卡**：`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`WanVideoTextEncode`、`INTConstant`、`LoadWanVideoClipTextEncoder`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`WanVideoDecode`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`RepeatLatentBatch`、`FluxGuidance`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`LoraLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`BasicGuider`、`SaveImage`、`LoadImage`、`VAEDecode`、`RH_Translator`

**缺卡**（7）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`easy cleanGpuUsed`、`CR Prompt Text`、`ImageResize+`、`ImageResize+`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
