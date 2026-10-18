---
key: 视频生成/图生视频/提取爆款视频文案 一键生成LTX2.3图生视频提示词_2082120400535900161.json
name: 提取爆款视频文案 一键生成LTX2.3图生视频提示词_2082120400535900161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/提取爆款视频文案 一键生成LTX2.3图生视频提示词_2082120400535900161.json
hash: e8528b4d11288276
coverage: 0.769231
learned_at: 2026-10-15 22:42:27
nodes: [LoadImage, CR Text, ShellAgentPluginOutputText, AudioSeparation, CR Text Concatenate, Audio To Text (mtb), CR Text, easy showAnything, easy saveText, Qwen3ASRLoader, LoadAudio, ShowText|pysssss, LayerUtility: PurgeVRAM V2, easy saveText, RH_LLMAPI_Pro_Node, easy showAnything, CR Text, SaveImage, LoadImage, Qwen3ASRTranscribe, Note, MarkdownNote, Note, LoadVideo, Load Whisper (mtb), GetVideoComponents]
patterns: []
missing: []
---

# 视频生成/图生视频/提取爆款视频文案 一键生成LTX2.3图生视频提示词_2082120400535900161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082120400535900161.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（26 个）：
- `LoadImage`
- `CR Text`
- `ShellAgentPluginOutputText`
- `AudioSeparation`
- `CR Text Concatenate`
- `Audio To Text (mtb)`
- `CR Text`
- `easy showAnything`
- `easy saveText`
- `Qwen3ASRLoader`
- `LoadAudio`
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM V2`
- `easy saveText`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `CR Text`
- `SaveImage`
- `LoadImage`
- `Qwen3ASRTranscribe`
- `Note`
- `MarkdownNote`
- `Note`
- `LoadVideo`
- `Load Whisper (mtb)`
- `GetVideoComponents`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`LoadImage`、`CR Text`、`ShellAgentPluginOutputText`、`AudioSeparation`、`CR Text Concatenate`、`Audio To Text (mtb)`、`easy saveText`、`Qwen3ASRLoader`、`LoadAudio`、`LayerUtility: PurgeVRAM V2`、`RH_LLMAPI_Pro_Node`、`SaveImage`、`Qwen3ASRTranscribe`、`LoadVideo`、`Load Whisper (mtb)`、`GetVideoComponents`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、easy saveText、GetVideoComponents、LoadAudio、LoadVideo、RH_LLMAPI_Pro_Node
