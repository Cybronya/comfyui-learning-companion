---
key: 视频生成/文生视频/MiniMax H3全能导演台手动版视频生成处理工具V3.1_2101004935784648706.json
name: MiniMax H3全能导演台手动版视频生成处理工具V3.1_2101004935784648706
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3全能导演台手动版视频生成处理工具V3.1_2101004935784648706.json
hash: bfbed34fd12fff65
coverage: 0.92
learned_at: 2026-10-15 22:45:48
nodes: [BasicGuider, UNETLoader, VAELoader, VAELoader, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy minimaxH3ToVideo, ComfyMathExpression, SamplerCustomAdvanced, RandomNoise, MiniMaxH3MultiRateSamplerEXPT8, CLIPLoader, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, easy matchLine, easy promptLine, easy multiTrackEditor, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax H3全能导演台手动版视频生成处理工具V3.1_2101004935784648706.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3全能导演台手动版视频生成处理工具V3.1_2101004935784648706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（50 个）：
- `BasicGuider`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy minimaxH3ToVideo`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `CLIPLoader`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3AVDecodeT8`
- `easy matchLine`
- `easy promptLine`
- `easy multiTrackEditor`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（46/50）

**有卡**：`BasicGuider`、`UNETLoader`、`VAELoader`、`easy multiTrackInfoOutput`、`easy multiTrackTaskOutput`、`easy minimaxH3ToVideo`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`RandomNoise`、`MiniMaxH3MultiRateSamplerEXPT8`、`CLIPLoader`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`MiniMaxH3AVDecodeT8`、`easy matchLine`、`easy promptLine`、`easy multiTrackEditor`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
