---
key: 视频生成/图生视频/（自用）HunyuanVideo 1.5 720P 20步优化版图生视频_1992838013717901313.json
name: （自用）HunyuanVideo 1.5 720P 20步优化版图生视频_1992838013717901313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1992838013717901313.json
hash: 95ee0ae70d9713ab
coverage: 0.866667
learned_at: 2026-10-15 22:33:17
nodes: [CLIPVisionLoader, DualCLIPLoader, VAELoader, MarkdownNote, EasyCache, Note, MarkdownNote, MarkdownNote, RandomNoise, KSamplerSelect, HunyuanVideo15ImageToVideo, ModelSamplingSD3, CLIPTextEncode, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VAEDecodeTiled, RunningHub Deepcleaner, SaveImage, SaveImage, VAEDecode, SamplerCustomAdvanced, BasicScheduler, TT_img_enc_v2, TT_img_enc, LoadImage, CLIPTextEncode, CFGGuider, UNETLoader, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/（自用）HunyuanVideo 1.5 720P 20步优化版图生视频_1992838013717901313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992838013717901313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `EasyCache`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `HunyuanVideo15ImageToVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VAEDecodeTiled` ★核心
- `RunningHub Deepcleaner`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `TT_img_enc_v2`
- `TT_img_enc`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `UNETLoader` ★核心
- `CR Prompt Text`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`VAELoader`、`EasyCache`、`RandomNoise`、`KSamplerSelect`、`HunyuanVideo15ImageToVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`VAEDecodeTiled`、`RunningHub Deepcleaner`、`SaveImage`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicScheduler`、`TT_img_enc_v2`、`TT_img_enc`、`LoadImage`、`CFGGuider`、`UNETLoader`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
