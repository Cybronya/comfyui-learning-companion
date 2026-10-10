---
key: wan2.2低频超真实+批量文生图（自动提示词）V3_1950771546711351297.json
name: wan2.2低频超真实+批量文生图（自动提示词）V3_1950771546711351297
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2低频超真实+批量文生图（自动提示词）V3_1950771546711351297.json
hash: 31f17dda8fc825de
coverage: 0.791667
learned_at: 2026-10-10 20:59:27
nodes: [LoraLoader, CLIPTextEncode, CLIPLoader, VAELoader, CFGZeroStarAndInit, CR Text Concatenate, JWInteger, KSampler, VAEDecode, RH_LLMAPI_NODE, ShowText|pysssss, UNETLoader, ShowText|pysssss, LoraLoader, CLIPTextEncode, LoraLoader, RHHiddenNodes, RHHiddenNodes, Wan_video_prompt_generator, SaveImage, Text Multiline, JWInteger, EmptyLatentImage, Note]
patterns: [text_to_image, lora]
missing: [CR Text Concatenate, Text Multiline]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 512, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 162542999044562, "steps": 8, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001, "width": 512}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# wan2.2低频超真实+批量文生图（自动提示词）V3_1950771546711351297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2低频超真实+批量文生图（自动提示词）V3_1950771546711351297.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGZeroStarAndInit`
- `CR Text Concatenate`
- `JWInteger`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Wan_video_prompt_generator`
- `SaveImage`
- `Text Multiline`
- `JWInteger`
- `EmptyLatentImage` ★核心
- `Note`

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `162542999044562`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `4`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`LoraLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`CFGZeroStarAndInit`、`JWInteger`、`KSampler`、`VAEDecode`、`RH_LLMAPI_NODE`、`UNETLoader`、`RHHiddenNodes`、`Wan_video_prompt_generator`、`SaveImage`、`EmptyLatentImage`

**缺卡**（2）：`CR Text Concatenate`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CFGZeroStarAndInit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
