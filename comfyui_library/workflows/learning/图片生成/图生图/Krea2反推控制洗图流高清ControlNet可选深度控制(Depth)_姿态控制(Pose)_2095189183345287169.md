---
key: 图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2095189183345287169.json
name: Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2095189183345287169
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2095189183345287169.json
hash: 95663a11dc4a992b
coverage: 0.962264
learned_at: 2026-10-21 00:41:12
nodes: [PathchSageAttentionKJ, ConditioningKrea2Rebalance, CLIPLoader, VAEDecode, LoraLoaderModelOnly, UpscaleModelLoader, LoraLoaderModelOnly, VAEEncode, VAELoader, CR Image Input Switch, llama_cpp_parameters, llama_cpp_model_loader, Krea2T-Enhancer-Advanced, FluxKontextMultiReferenceLatentMethod, 图像缩放V2_孤海, GetImageSize, VAEDecode, Krea2ControlImageEncode, Krea2ControlApply, UNETLoader, CR Model Input Switch, ConditioningZeroOut, VAELoader, EmptyLatentImage, KSampler, LoraLoaderModelOnly, KSampler, 图像缩放V2_孤海, SDPoseKeypointExtractor, AIO_Preprocessor, ImageUpscaleWithModel, TextEncodeKrea2OstrisEdit, Float, CLIPTextEncode, CheckpointLoaderSimple, INTConstant, INTConstant, Krea2OstrisEditModelPatch, Krea2ControlLoRALoader, LoadImage, 图像缩放V2_孤海, easy imageConcat, SaveImage, SaveImage, ShowText|pysssss, 图像缩放V2_孤海, BodyRatioMapperSDPoseRender, llama_cpp_instruct_adv, DisTorchPurgeVRAMV2, Reroute, RHHiddenNodes, CR Text, CR Text Concatenate]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 0.6, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 449595168623398, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2095189183345287169.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea2反推控制洗图流高清ControlNet可选深度控制(Depth)_姿态控制(Pose)_2095189183345287169.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `PathchSageAttentionKJ`
- `ConditioningKrea2Rebalance`
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `CR Image Input Switch`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Krea2T-Enhancer-Advanced`
- `FluxKontextMultiReferenceLatentMethod`
- `图像缩放V2_孤海`
- `GetImageSize`
- `VAEDecode` ★核心
- `Krea2ControlImageEncode`
- `Krea2ControlApply`
- `UNETLoader` ★核心
- `CR Model Input Switch`
- `ConditioningZeroOut`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `图像缩放V2_孤海`
- `SDPoseKeypointExtractor`
- `AIO_Preprocessor`
- `ImageUpscaleWithModel`
- `TextEncodeKrea2OstrisEdit`
- `Float`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `INTConstant`
- `INTConstant`
- `Krea2OstrisEditModelPatch`
- `Krea2ControlLoRALoader` ★核心
- `LoadImage`
- `图像缩放V2_孤海`
- `easy imageConcat`
- `SaveImage`
- `SaveImage`
- `ShowText|pysssss`
- `图像缩放V2_孤海`
- `BodyRatioMapperSDPoseRender`
- `llama_cpp_instruct_adv`
- `DisTorchPurgeVRAMV2`
- `Reroute`
- `RHHiddenNodes`
- `CR Text`
- `CR Text Concatenate`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `449595168623398`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6`
- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **96%**（51/53）

**有卡**：`PathchSageAttentionKJ`、`ConditioningKrea2Rebalance`、`CLIPLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`VAEEncode`、`VAELoader`、`CR Image Input Switch`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`Krea2T-Enhancer-Advanced`、`FluxKontextMultiReferenceLatentMethod`、`图像缩放V2_孤海`、`GetImageSize`、`Krea2ControlImageEncode`、`Krea2ControlApply`、`UNETLoader`、`CR Model Input Switch`、`ConditioningZeroOut`、`EmptyLatentImage`、`KSampler`、`SDPoseKeypointExtractor`、`AIO_Preprocessor`、`ImageUpscaleWithModel`、`TextEncodeKrea2OstrisEdit`、`Float`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`INTConstant`、`Krea2OstrisEditModelPatch`、`Krea2ControlLoRALoader`、`LoadImage`、`easy imageConcat`、`SaveImage`、`BodyRatioMapperSDPoseRender`、`llama_cpp_instruct_adv`、`DisTorchPurgeVRAMV2`、`RHHiddenNodes`、`CR Text`、`CR Text Concatenate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
