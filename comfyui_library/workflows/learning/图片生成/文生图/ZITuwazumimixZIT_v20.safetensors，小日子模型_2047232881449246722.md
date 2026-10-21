---
key: 图片生成/文生图/ZITuwazumimixZIT_v20.safetensors，小日子模型_2047232881449246722.json
name: ZITuwazumimixZIT_v20.safetensors，小日子模型_2047232881449246722
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ZITuwazumimixZIT_v20.safetensors，小日子模型_2047232881449246722.json
hash: 41dc9d3e7c18c4d0
coverage: 0.826087
learned_at: 2026-10-19 22:45:54
nodes: [easy int, easy int, CLIPLoaderGGUF, CLIPTextEncode, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, easy int, VAEDecode, ModelSamplingAuraFlow, ProcessString, DeepTranslatorTextNode, UNETLoader, Note, LoraLoaderModelOnly, Note, Note, MarkdownNote, LoraLoaderModelOnly, SaveImage, LoraLoaderModelOnly, CR Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 67102370488848, "steps": 30, "width": 512}
---

# 图片生成/文生图/ZITuwazumimixZIT_v20.safetensors，小日子模型_2047232881449246722.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ZITuwazumimixZIT_v20.safetensors，小日子模型_2047232881449246722.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `easy int`
- `easy int`
- `CLIPLoaderGGUF`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `easy int`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `ProcessString`
- `DeepTranslatorTextNode`
- `UNETLoader` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CR Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `67102370488848`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`easy int`、`CLIPLoaderGGUF`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`ModelSamplingAuraFlow`、`ProcessString`、`DeepTranslatorTextNode`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、UNETLoader、CLIPLoaderGGUF
