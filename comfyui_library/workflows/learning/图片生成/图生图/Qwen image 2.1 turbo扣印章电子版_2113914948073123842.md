---
key: 图片生成/图生图/Qwen image 2.1 turbo扣印章电子版_2113914948073123842.json
name: Qwen image 2.1 turbo扣印章电子版_2113914948073123842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 turbo扣印章电子版_2113914948073123842.json
hash: 75af4e0dccfb2033
coverage: 0.944444
learned_at: 2026-10-26 22:03:09
nodes: [BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, SamplerCustom, ManualSigmas, FluxKontextImageScale, SaveImage, VAEDecode, SaveImageAdvanced, UNETLoader, CLIPLoader, VAELoader, LoadImage, KSamplerSelect, TextEncodeQwenImage21, easy showAnything, easy promptConcat, CR Text, CR Text]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen image 2.1 turbo扣印章电子版_2113914948073123842.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 turbo扣印章电子版_2113914948073123842.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `SamplerCustom` ★核心
- `ManualSigmas`
- `FluxKontextImageScale`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `KSamplerSelect` ★核心
- `TextEncodeQwenImage21`
- `easy showAnything`
- `easy promptConcat`
- `CR Text`
- `CR Text`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`BRIA_RMBG_ModelLoader_Zho`、`BRIA_RMBG_Zho`、`SamplerCustom`、`ManualSigmas`、`FluxKontextImageScale`、`SaveImage`、`VAEDecode`、`SaveImageAdvanced`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`KSamplerSelect`、`TextEncodeQwenImage21`、`easy promptConcat`、`CR Text`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、UNETLoader、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom
