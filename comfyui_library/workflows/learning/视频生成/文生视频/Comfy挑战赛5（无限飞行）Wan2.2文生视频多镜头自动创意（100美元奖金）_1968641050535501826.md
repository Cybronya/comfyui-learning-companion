---
key: 视频生成/文生视频/Comfy挑战赛5（无限飞行）Wan2.2文生视频多镜头自动创意（100美元奖金）_1968641050535501826.json
name: Comfy挑战赛5（无限飞行）Wan2.2文生视频多镜头自动创意（100美元奖金）_1968641050535501826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Comfy挑战赛5（无限飞行）Wan2.2文生视频多镜头自动创意（100美元奖金）_1968641050535501826.json
hash: 109700b2375f6880
coverage: 0.858824
learned_at: 2026-10-15 22:43:46
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, INTConstant, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoVAELoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSampler, ShowText|pysssss, WanVideoLoraSelect, INTConstant, GetImageSizeAndCount, Note, Note, Note, CLIPLoader, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, WanVideoModelLoader, easy showAnything, VHS_VideoCombine, ModelSamplingAuraFlow, Note, SaveLatent, WanVideoSampler, Note _O, Note _O, Note _O, VAELoader, TextConcat, easy showAnything, KSampler, VAEDecode, EmptySD3LatentImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, RH_Captioner, easy showAnything, easy showAnything, TextConcat, JWStringConcat, RH_LLMAPI_NODE, TextConcat, CR Prompt Text, JWInteger, VAELoader, SaveLatent, VAEEncode, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch+, LayerUtility: PurgeVRAM, HunyuanVideoFoley, LoadAudio, JWInteger, PrimitiveNode, Note, Note, CR Prompt Text, WanVideoBlockSwap, CR Prompt Text, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Prompt Text, RH_LLMAPI_NODE, Wan22PromptSelector, CR Prompt Text, CR Prompt Text, CLIPTextEncode, UNETLoader, SaveImage, VHS_VideoCombine, CR Prompt Text, CR Prompt Text, CR Prompt Text, WanVideoTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 133655084073801, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Comfy挑战赛5（无限飞行）Wan2.2文生视频多镜头自动创意（100美元奖金）_1968641050535501826.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968641050535501826.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `ShowText|pysssss`
- `WanVideoLoraSelect`
- `INTConstant`
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoModelLoader`
- `easy showAnything`
- `VHS_VideoCombine`
- `ModelSamplingAuraFlow`
- `Note`
- `SaveLatent`
- `WanVideoSampler` ★核心
- `Note _O`
- `Note _O`
- `Note _O`
- `VAELoader`
- `TextConcat`
- `easy showAnything`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `RH_Captioner`
- `easy showAnything`
- `easy showAnything`
- `TextConcat`
- `JWStringConcat`
- `RH_LLMAPI_NODE`
- `TextConcat`
- `CR Prompt Text`
- `JWInteger`
- `VAELoader`
- `SaveLatent`
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `HunyuanVideoFoley`
- `LoadAudio`
- `JWInteger`
- `PrimitiveNode`
- `Note`
- `Note`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `Wan22PromptSelector`
- `CR Prompt Text`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `WanVideoTextEncode`

## 关键参数

- `seed` = `133655084073801`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **86%**（73/85）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoLoraSelect`、`GetImageSizeAndCount`、`CLIPLoader`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`ModelSamplingAuraFlow`、`SaveLatent`、`Note _O`、`VAELoader`、`TextConcat`、`KSampler`、`VAEDecode`、`EmptySD3LatentImage`、`RH_Captioner`、`JWStringConcat`、`RH_LLMAPI_NODE`、`CR Prompt Text`、`JWInteger`、`VAEEncode`、`ImageFromBatch+`、`HunyuanVideoFoley`、`LoadAudio`、`WanVideoBlockSwap`、`LoraLoaderModelOnly`、`Wan22PromptSelector`、`UNETLoader`、`SaveImage`、`WanVideoTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanVideoSampler

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
