---
key: 图片生成/图生图/【遇见AI】flex2-preview 控制pose，depth，canny_2053036057029033985.json
name: 【遇见AI】flex2-preview 控制pose，depth，canny_2053036057029033985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】flex2-preview 控制pose，depth，canny_2053036057029033985.json
hash: 6e530c4cfe909806
coverage: 0.8125
learned_at: 2026-10-23 11:52:16
nodes: [VAEDecode, SaveImage, KSampler, VAELoader, DualCLIPLoader, ConditioningZeroOut, UNETLoader, Flex2Conditioner, CLIPTextEncode, LoadImage, MarkdownNote, PreviewImage, MarkdownNote, LoadImage, AIO_Preprocessor, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 990573975754499, "steps": 28}
---

# 图片生成/图生图/【遇见AI】flex2-preview 控制pose，depth，canny_2053036057029033985.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】flex2-preview 控制pose，depth，canny_2053036057029033985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `Flex2Conditioner`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `MarkdownNote`
- `PreviewImage`
- `MarkdownNote`
- `LoadImage`
- `AIO_Preprocessor`
- `LoadImage`

## 关键参数

- `seed` = `990573975754499`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`VAEDecode`、`SaveImage`、`KSampler`、`VAELoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`UNETLoader`、`Flex2Conditioner`、`CLIPTextEncode`、`LoadImage`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、SaveImage
