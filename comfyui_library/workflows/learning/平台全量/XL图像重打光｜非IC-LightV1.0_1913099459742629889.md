---
key: 平台全量/XL图像重打光｜非IC-LightV1.0_1913099459742629889.json
name: XL图像重打光｜非IC-LightV1.0_1913099459742629889
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/XL图像重打光｜非IC-LightV1.0_1913099459742629889.json
hash: 8719952dcfa7162a
coverage: 0.853659
learned_at: 2026-11-14 01:07:35
nodes: [EcomIDFaceAnalysis, LayerUtility: PurgeVRAM, JanusModelLoader, ShowText|pysssss, LoadImage, CLIPTextEncode, CLIPTextEncode, ControlNetApplyAdvanced, LayerUtility: ImageScaleByAspectRatio V2, PulidEvaClipLoader, EcomID_PulidModelLoader, ApplyEcomIDAdvanced, VAEDecode, IPAdapterUnifiedLoader, Florence2Run, LayerMask: BiRefNetUltraV2, LoadImage, ImitationHueNode, PreviewImage, ttN concat, EmptyLatentImage, PreviewImage, Image Comparer (rgthree), LayerMask: LoadBiRefNetModelV2, ShowText|pysssss, ShowText|pysssss, IPAdapter, ControlNetApplyAdvanced, ControlNetApplyAdvanced, KSampler, CheckpointLoaderSimple, ControlNetLoader, ControlNetLoader, ControlNetLoader, ControlNetLoader, Florence2ModelLoader, InstantIDModelLoader, JanusImageUnderstanding, CR Text, easy imageDetailTransfer, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "juggernautXL_v9-Lightning_4S_V9 + RDPhoto 2.safetensors", "controlnet_strength": 0.45, "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 564535539469445, "steps": 10, "width": 1024}
---

# 平台全量/XL图像重打光｜非IC-LightV1.0_1913099459742629889.json

> 来源文件 `comfyui_library/workflows/平台全量/XL图像重打光｜非IC-LightV1.0_1913099459742629889.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `EcomIDFaceAnalysis`
- `LayerUtility: PurgeVRAM`
- `JanusModelLoader`
- `ShowText|pysssss`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PulidEvaClipLoader`
- `EcomID_PulidModelLoader`
- `ApplyEcomIDAdvanced`
- `VAEDecode` ★核心
- `IPAdapterUnifiedLoader`
- `Florence2Run`
- `LayerMask: BiRefNetUltraV2`
- `LoadImage`
- `ImitationHueNode`
- `PreviewImage`
- `ttN concat`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerMask: LoadBiRefNetModelV2`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `IPAdapter`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `Florence2ModelLoader`
- `InstantIDModelLoader`
- `JanusImageUnderstanding`
- `CR Text`
- `easy imageDetailTransfer`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `0.45`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `564535539469445`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `juggernautXL_v9-Lightning_4S_V9 + RDPhoto 2.safetensors`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`EcomIDFaceAnalysis`、`LayerUtility: PurgeVRAM`、`JanusModelLoader`、`LoadImage`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`PulidEvaClipLoader`、`EcomID_PulidModelLoader`、`ApplyEcomIDAdvanced`、`VAEDecode`、`IPAdapterUnifiedLoader`、`Florence2Run`、`LayerMask: BiRefNetUltraV2`、`ImitationHueNode`、`ttN concat`、`EmptyLatentImage`、`LayerMask: LoadBiRefNetModelV2`、`IPAdapter`、`KSampler`、`CheckpointLoaderSimple`、`ControlNetLoader`、`Florence2ModelLoader`、`InstantIDModelLoader`、`JanusImageUnderstanding`、`CR Text`、`easy imageDetailTransfer`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
