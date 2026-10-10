---
key: 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧视频（高动态+自动提示词）_1986071453768568834.json
name: Wan2.2 Smooth Mix首尾帧视频（高动态+自动提示词）_1986071453768568834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix首尾帧视频（高动态+自动提示词）_1986071453768568834.json
hash: 33fdc5c3f70223c7
coverage: 0.698113
learned_at: 2026-10-11 02:45:02
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, RIFE VFI, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, UNETLoader, UNETLoader, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, SeedVR2GGUF, CLIPVisionEncode, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, ImageConcanate, ImageConcanate, CLIPLoader, SetNode, VAELoader, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ImageResizeKJ, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, VHS_VideoCombine, GetNode, easy showAnything, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, CR Text, ImpactSwitch, Note, ImageConcanate, RH_LLMAPI_NODE]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, RIFE VFI]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧视频（高动态+自动提示词）_1986071453768568834.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix首尾帧视频（高动态+自动提示词）_1986071453768568834.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（53 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VHS_VideoCombine`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `SeedVR2GGUF`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImageResizeKJ`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `GetNode`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `ImpactSwitch`
- `Note`
- `ImageConcanate`
- `RH_LLMAPI_NODE`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **70%**（37/53）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`SeedVR2GGUF`、`CLIPVisionEncode`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`VAEDecode`、`ImageConcanate`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResizeKJ`、`JWInteger`、`LoadImage`、`RH_LLMAPI_NODE`

**缺卡**（4）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、SeedVR2BlockSwap

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
