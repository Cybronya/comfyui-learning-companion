---
key: （自用）QwenEdit AIO V7.1文生图_1985324572306194434.json
name: （自用）QwenEdit AIO V7.1文生图_1985324572306194434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（自用）QwenEdit AIO V7.1文生图_1985324572306194434.json
hash: 00d70c7b5dd6cbee
coverage: 0.8125
learned_at: 2026-10-10 21:00:01
nodes: [Int, EmptyLatentImage, KSampler, Int, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEDecode, TT_img_enc, Int, Text Multiline, SaveImage, SaveImage, CR Prompt Text, PrimitiveInt, CheckpointLoaderSimple, TT_img_enc_v2]
patterns: []
missing: [Text Multiline, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v7.1.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 134261077877488, "steps": 8, "width": 512}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# （自用）QwenEdit AIO V7.1文生图_1985324572306194434.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（自用）QwenEdit AIO V7.1文生图_1985324572306194434.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `Int`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `Int`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `TT_img_enc`
- `Int`
- `Text Multiline`
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`
- `PrimitiveInt`
- `CheckpointLoaderSimple` ★核心
- `TT_img_enc_v2`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `134261077877488`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v7.1.safetensors`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`Int`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`TT_img_enc`、`SaveImage`、`CheckpointLoaderSimple`、`TT_img_enc_v2`

**缺卡**（2）：`Text Multiline`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、EmptyLatentImage、TextEncodeQwenImageEditPlus、SaveImage、Int、TT_img_enc

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
