---
key: 图片生成/文生图/Anima3 动漫文生图 qwen3.5提示词优化，可指定画师风格_2045768388223438850.json
name: Anima3 动漫文生图 qwen3.5提示词优化，可指定画师风格_2045768388223438850
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima3 动漫文生图 qwen3.5提示词优化，可指定画师风格_2045768388223438850.json
hash: ce545cda19ffb34a
coverage: 0.833333
learned_at: 2026-10-21 02:51:24
nodes: [UNETLoader, CLIPLoader, VAELoader, llama_cpp_parameters, llama_cpp_model_loader, PreviewAny, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, VAEDecode, CLIPTextEncode, CLIPTextEncode, llama_cpp_instruct_adv, SeedVR2VideoUpscaler, Note, Note, EmptyLatentImage, Int, ImpactSwitch, ZML_AnyTypeSwitchFive, Int, Int, SaveImage, CR Text, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1152, "sampler_name": "er_sde", "scheduler": "beta57", "seed": 503681619231263, "steps": 35, "width": 896}
---

# 图片生成/文生图/Anima3 动漫文生图 qwen3.5提示词优化，可指定画师风格_2045768388223438850.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima3 动漫文生图 qwen3.5提示词优化，可指定画师风格_2045768388223438850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `PreviewAny`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `SeedVR2VideoUpscaler`
- `Note`
- `Note`
- `EmptyLatentImage` ★核心
- `Int`
- `ImpactSwitch`
- `ZML_AnyTypeSwitchFive`
- `Int`
- `Int`
- `SaveImage`
- `CR Text`
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `896`
- `height` = `1152`
- `batch_size` = `1`
- `seed` = `503681619231263`
- `steps` = `35`
- `cfg` = `4`
- `sampler_name` = `er_sde`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`VAEDecode`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`SeedVR2VideoUpscaler`、`EmptyLatentImage`、`Int`、`ZML_AnyTypeSwitchFive`、`SaveImage`、`CR Text`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SeedVR2LoadDiTModel
