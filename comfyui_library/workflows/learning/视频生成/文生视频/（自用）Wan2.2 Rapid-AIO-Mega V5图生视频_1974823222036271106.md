---
key: 视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V5图生视频_1974823222036271106.json
name: （自用）Wan2.2 Rapid-AIO-Mega V5图生视频_1974823222036271106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V5图生视频_1974823222036271106.json
hash: 6a4640d422c413a9
coverage: 0.761905
learned_at: 2026-10-10 23:14:42
nodes: [ModelSamplingSD3, CLIPTextEncode, WanVaceToVideo, Note, WanVideoVACEStartToEndFrame, ApplySageAttention, Note, Note, CLIPTextEncode, LoadImage, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, KSampler, JWInteger, VAEDecode, TT_img_enc, SaveImage, CheckpointLoaderSimple, CR Prompt Text, LoadImage, SaveImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v5.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 839910138451575, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V5图生视频_1974823222036271106.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V5图生视频_1974823222036271106.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `Note`
- `WanVideoVACEStartToEndFrame`
- `ApplySageAttention`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `JWInteger`
- `VAEDecode` ★核心
- `TT_img_enc`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `CR Prompt Text`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `839910138451575`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v5.safetensors`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`ApplySageAttention`、`LoadImage`、`JWInteger`、`KSampler`、`VAEDecode`、`TT_img_enc`、`SaveImage`、`CheckpointLoaderSimple`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveImage、ModelSamplingSD3、JWInteger

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
