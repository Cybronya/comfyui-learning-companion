---
key: 视频生成/文生视频/MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090.json
name: MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090.json
hash: feadb315639d873e
coverage: 0.916667
learned_at: 2026-10-15 22:45:45
nodes: [VAELoader, VAELoader, UNETLoader, MarkdownNote, ResolutionSelector, PrimitiveFloat, LoraLoaderModelOnly, CLIPLoader, BasicGuider, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, CreateVideo, PlaySound|pysssss, ComfyMathExpression, KSamplerSelect, SaveVideo, MiniMaxH3ImageToVideo, LoadImage, ResizeImagesByLongerEdge, LoadImage, ResizeImagesByLongerEdge, RandomNoise, BasicScheduler]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `ResolutionSelector`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `PlaySound|pysssss`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `SaveVideo`
- `MiniMaxH3ImageToVideo`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `RandomNoise`
- `BasicScheduler`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`VAELoader`、`UNETLoader`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPLoader`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`PlaySound|pysssss`、`ComfyMathExpression`、`KSamplerSelect`、`SaveVideo`、`MiniMaxH3ImageToVideo`、`LoadImage`、`ResizeImagesByLongerEdge`、`RandomNoise`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
