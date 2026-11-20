---
key: 平台全量/视角转换 摄影机角度变换 手动改变图片角度和镜头！Multiple angles Qwen edit_2056180055499386882.json
name: 视角转换 摄影机角度变换 手动改变图片角度和镜头！Multiple angles Qwen edit_2056180055499386882
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/视角转换 摄影机角度变换 手动改变图片角度和镜头！Multiple angles Qwen edit_2056180055499386882.json
hash: ad9497a945cbc702
coverage: 0.913043
learned_at: 2026-11-14 02:33:55
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, FluxKontextMultiReferenceLatentMethod, VAEEncode, TextEncodeQwenImageEditPlus, easy promptList, ModelSamplingAuraFlow, INTConstant, CFGNorm, FluxKontextMultiReferenceLatentMethod, UNETLoader, easy showAnything, CLIPLoader, VAELoader, KSampler, VAEDecode, QwenMultiangleCameraNode, LoadImage, easy showAnything, SaveImage, VNCCS_VisualPositionControl, LayerUtility: ImageScaleByAspectRatio V2]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 729234902716570, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/视角转换 摄影机角度变换 手动改变图片角度和镜头！Multiple angles Qwen edit_2056180055499386882.json

> 来源文件 `comfyui_library/workflows/平台全量/视角转换 摄影机角度变换 手动改变图片角度和镜头！Multiple angles Qwen edit_2056180055499386882.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `easy promptList`
- `ModelSamplingAuraFlow`
- `INTConstant`
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `UNETLoader` ★核心
- `easy showAnything`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `QwenMultiangleCameraNode`
- `LoadImage`
- `easy showAnything`
- `SaveImage`
- `VNCCS_VisualPositionControl`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `729234902716570`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`easy promptList`、`ModelSamplingAuraFlow`、`INTConstant`、`CFGNorm`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`QwenMultiangleCameraNode`、`LoadImage`、`SaveImage`、`VNCCS_VisualPositionControl`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
