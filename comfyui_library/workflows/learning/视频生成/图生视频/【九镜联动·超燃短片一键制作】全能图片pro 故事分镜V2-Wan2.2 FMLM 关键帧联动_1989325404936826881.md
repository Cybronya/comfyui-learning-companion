---
key: 视频生成/图生视频/【九镜联动·超燃短片一键制作】全能图片pro 故事分镜V2-Wan2.2 FMLM 关键帧联动_1989325404936826881.json
name: 【九镜联动·超燃短片一键制作】全能图片pro 故事分镜V2-Wan2.2 FMLM 关键帧联动_1989325404936826881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【九镜联动·超燃短片一键制作】全能图片pro 故事分镜V2-Wan2.2 FMLM 关键帧联动_1989325404936826881.json
hash: b23c521881d62b4a
coverage: 0.767123
learned_at: 2026-10-15 22:33:06
nodes: [Compare, GetImageSize, LayerUtility: PurgeVRAM, ImageResize+, ImageResize+, SetNode, SetNode, CLIPLoader, UNETLoader, ModelSamplingSD3, VAELoader, WanFirstMiddleLastFrameToVideo, GetNode, GetNode, GetNode, GetNode, easy imageListToImageBatch, PathchSageAttentionKJ, wanBlockSwap, GetNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPTextEncode, GetNode, PathchSageAttentionKJ, GetNode, LayerUtility: PurgeVRAM, GetNode, CLIPTextEncode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, LoadImage, ModelSamplingSD3, WanFirstMiddleLastFrameToVideo, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, VAEDecode, VAEDecode, VAEDecode, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, PreviewImage, VHS_Unbatch, RHHiddenNodes, GetImageSize, KSamplerAdvanced, KSamplerAdvanced, easy batchAnything, wanBlockSwap, VHS_VideoCombine, easy batchAnything, KSamplerAdvanced, RHHiddenNodes, WanFirstMiddleLastFrameToVideo, WanFirstMiddleLastFrameToVideo, Int, Int, Note, JWInteger, Note, easy batchAnything, Note, easy ifElse, ShowText|pysssss, RH_Nano_Banana2_Image2Image]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/【九镜联动·超燃短片一键制作】全能图片pro 故事分镜V2-Wan2.2 FMLM 关键帧联动_1989325404936826881.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989325404936826881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `Compare`
- `GetImageSize`
- `LayerUtility: PurgeVRAM`
- `ImageResize+`
- `ImageResize+`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `WanFirstMiddleLastFrameToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy imageListToImageBatch`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ModelSamplingSD3`
- `WanFirstMiddleLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `VHS_Unbatch`
- `RHHiddenNodes`
- `GetImageSize`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy batchAnything`
- `wanBlockSwap`
- `VHS_VideoCombine`
- `easy batchAnything`
- `KSamplerAdvanced` ★核心
- `RHHiddenNodes`
- `WanFirstMiddleLastFrameToVideo`
- `WanFirstMiddleLastFrameToVideo`
- `Int`
- `Int`
- `Note`
- `JWInteger`
- `Note`
- `easy batchAnything`
- `Note`
- `easy ifElse`
- `ShowText|pysssss`
- `RH_Nano_Banana2_Image2Image`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（56/73）

**有卡**：`Compare`、`GetImageSize`、`LayerUtility: PurgeVRAM`、`ImageResize+`、`CLIPLoader`、`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`WanFirstMiddleLastFrameToVideo`、`easy imageListToImageBatch`、`PathchSageAttentionKJ`、`wanBlockSwap`、`CLIPTextEncode`、`easy cleanGpuUsed`、`LoadImage`、`LoraLoaderModelOnly`、`VAEDecode`、`KSamplerAdvanced`、`VHS_Unbatch`、`RHHiddenNodes`、`easy batchAnything`、`VHS_VideoCombine`、`Int`、`JWInteger`、`RH_Nano_Banana2_Image2Image`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
