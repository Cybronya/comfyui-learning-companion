---
key: 视频生成/图生视频/minimax_h3_r2v_complex_camera_motion_2094372650780028929.json
name: minimax_h3_r2v_complex_camera_motion_2094372650780028929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax_h3_r2v_complex_camera_motion_2094372650780028929.json
hash: 034e519221729c56
coverage: 0.875
learned_at: 2026-10-17 00:02:47
nodes: [VAELoader, VAELoader, ManualSigmas, VAEDecode, VAEDecodeAudio, LTXVConcatAVLatent, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, SplitSigmas, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, BasicScheduler, BasicGuider, BasicGuider, ManualSigmas, MiniMaxH3SigmaShift, RandomNoise, ModelAttentionBackend, LTXVSeparateAVLatent, MinimaxH3LatentUpscaler3D, UNETLoader, VAEDecode, VAEDecodeAudio, ResolutionSelector, ResolutionSelector, ImageResizeKJv2, MarkdownNote, ComfyMathExpression, PrimitiveNode, VHS_VideoCombine, VHS_LoadVideo, PrimitiveFloat, LoadImage, MarkdownNote, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax_h3_r2v_complex_camera_motion_2094372650780028929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax_h3_r2v_complex_camera_motion_2094372650780028929.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（40 个）：
- `VAELoader`
- `VAELoader`
- `ManualSigmas`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LTXVConcatAVLatent`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
- `SplitSigmas`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `BasicScheduler`
- `BasicGuider`
- `BasicGuider`
- `ManualSigmas`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `ModelAttentionBackend`
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ResolutionSelector`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `MarkdownNote`
- `ComfyMathExpression`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`VAELoader`、`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`LTXVConcatAVLatent`、`MiniMaxH3ReferenceToVideo`、`ModelPreviewOverrideKJ`、`SplitSigmas`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`MiniMaxH3SigmaShift`、`RandomNoise`、`ModelAttentionBackend`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscaler3D`、`UNETLoader`、`ResolutionSelector`、`ImageResizeKJv2`、`ComfyMathExpression`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
