---
key: FLUX-ControlNet Union Pro_1988619898043719681.json
name: FLUX-ControlNet Union Pro_1988619898043719681
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX-ControlNet Union Pro_1988619898043719681.json
hash: ebe13c3834a1bd3b
coverage: 0.791667
learned_at: 2026-10-10 20:58:32
nodes: [SetUnionControlNetType, AIO_Preprocessor, PreviewImage, KSampler, VAEDecode, SaveImage, EmptyLatentImage, PreviewImage, ControlNetApplySD3, ConditioningZeroOut, LayerUtility: LoadJoyCaptionBeta1Model, DualCLIPLoader, ImageResize+, UNETLoader, CLIPTextEncode, LoraLoader, LoraLoader, LoraLoader, LoraLoader, ControlNetLoader, VAELoader, LayerUtility: JoyCaptionBeta1, LoadImage, LoraLoader]
patterns: [text_to_image, lora]
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, ImageResize+]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.52, "denoise": 1, "height": 1024, "lora_name": "言灵ru-F.1绫波丽.safetensors", "sampler_name": "uni_pc", "scheduler": "sgm_uniform", "seed": 893885822912594, "steps": 25, "strength_clip": 0.30000000000000004, "strength_model": 1.0000000000000002, "width": 1536}
discoveries: [次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# FLUX-ControlNet Union Pro_1988619898043719681.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX-ControlNet Union Pro_1988619898043719681.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `ControlNetApplySD3` ★核心
- `ConditioningZeroOut`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `DualCLIPLoader`
- `ImageResize+`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `ControlNetLoader`
- `VAELoader`
- `LayerUtility: JoyCaptionBeta1`
- `LoadImage`
- `LoraLoader` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `893885822912594`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1536`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.52`
- `lora_name` = `言灵ru-F.1绫波丽.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `0.30000000000000004`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`SetUnionControlNetType`、`AIO_Preprocessor`、`KSampler`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`ControlNetApplySD3`、`ConditioningZeroOut`、`DualCLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`LoraLoader`、`ControlNetLoader`、`VAELoader`、`LoadImage`

**缺卡**（3）：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`ImageResize+`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、UNETLoader

## 学习发现

- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
