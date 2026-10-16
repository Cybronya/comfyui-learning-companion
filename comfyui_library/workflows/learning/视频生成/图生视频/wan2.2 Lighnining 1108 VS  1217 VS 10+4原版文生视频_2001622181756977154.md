---
key: 视频生成/图生视频/wan2.2 Lighnining 1108 VS  1217 VS 10+4原版文生视频_2001622181756977154.json
name: wan2.2 Lighnining 1108 VS  1217 VS 10+4原版文生视频_2001622181756977154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2001622181756977154.json
hash: 341fb4f91bb47dbc
coverage: 0.988889
learned_at: 2026-10-15 22:33:46
nodes: [PathchSageAttentionKJ, TorchCompileModel, TorchCompileModel, ModelSamplingSD3, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, TT_img_enc, SaveImage, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly, INTConstant, INTConstant, ImageSharpen, ImageFromBatch+, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, INTConstant, JWInteger, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, INTConstant, SaveImage, VAEDecode, LoraLoaderModelOnly, PathchSageAttentionKJ, KSamplerAdvanced, ModelSamplingSD3, KSamplerAdvanced, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, ImageConcanate, INTConstant, INTConstant, VHS_VideoCombine, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, ImageConcanate, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageFromBatch+, LayerUtility: PurgeVRAM, ImageFromBatch+, CLIPLoader, JWInteger, JWInteger, TT_img_enc, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, easy seed, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, easy showAnything, AddLabel, AddLabel, AddLabel, VHS_VideoCombine, VHS_VideoCombine, RH_LLMAPI_Pro_Node, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 Lighnining 1108 VS  1217 VS 10+4原版文生视频_2001622181756977154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001622181756977154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `TorchCompileModel`
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `TT_img_enc`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `ImageSharpen`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `JWInteger`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `INTConstant`
- `SaveImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `ImageConcanate`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImageConcanate`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `ImageFromBatch+`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `TT_img_enc`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy seed`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **99%**（89/90）

**有卡**：`PathchSageAttentionKJ`、`TorchCompileModel`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`VAEDecode`、`TT_img_enc`、`SaveImage`、`CLIPTextEncode`、`INTConstant`、`ImageSharpen`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`VAELoader`、`JWInteger`、`ImageConcanate`、`VHS_VideoCombine`、`UNETLoader`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`CLIPLoader`、`easy seed`、`AddLabel`、`RH_LLMAPI_Pro_Node`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、easy seed
