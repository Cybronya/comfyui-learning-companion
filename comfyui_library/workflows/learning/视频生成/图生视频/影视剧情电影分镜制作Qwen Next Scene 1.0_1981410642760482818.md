---
key: 视频生成/图生视频/影视剧情电影分镜制作Qwen Next Scene 1.0_1981410642760482818.json
name: 影视剧情电影分镜制作Qwen Next Scene 1.0_1981410642760482818.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/影视剧情电影分镜制作Qwen Next Scene 1.0_1981410642760482818.json
hash: 43051bc4fe61c400
coverage: 0.857143
learned_at: 2026-10-15 22:32:37
nodes: [UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, VAEDecode, KSampler, SaveImage, RH_LLMAPI_NODE, Int, easy promptLine, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ShellAgentPluginOutputText, ProcessString, easy showAnything, LoadImage, Note, JjkText]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "simple", "seed": 95727195000278, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/影视剧情电影分镜制作Qwen Next Scene 1.0_1981410642760482818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981410642760482818.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `RH_LLMAPI_NODE`
- `Int`
- `easy promptLine`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ShellAgentPluginOutputText`
- `ProcessString`
- `easy showAnything`
- `LoadImage`
- `Note`
- `JjkText`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `95727195000278`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`VAEDecode`、`KSampler`、`SaveImage`、`RH_LLMAPI_NODE`、`Int`、`easy promptLine`、`TextEncodeQwenImageEditPlus`、`ShellAgentPluginOutputText`、`ProcessString`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、SaveImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
