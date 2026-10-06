---
key: 图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json
name: Qwen2.1-单图编辑_2106941936392294401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json
hash: e4fa0c02348ce8eb
coverage: 1
learned_at: 2026-10-07 02:41:29
nodes: [SaveImageAdvanced, VAEDecode, BasicGuider, QwenImage21FunPDDLoader, SamplerCustomAdvanced, RandomNoise, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `BasicGuider`
- `QwenImage21FunPDDLoader`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `LoadImage`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`SaveImageAdvanced`、`VAEDecode`、`BasicGuider`、`QwenImage21FunPDDLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SaveImageAdvanced
