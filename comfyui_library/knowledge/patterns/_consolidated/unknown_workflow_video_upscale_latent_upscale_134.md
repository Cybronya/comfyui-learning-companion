---
name: unknown_workflow_video_upscale_latent_upscale_134
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8155
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRAM_Debug, easy float, 孤海注释, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3｜单人高质量数字人｜音频驱动多图参考 MV_2096969226736193537.json, 视频生成/文生视频/MiniMax H3｜批量生素材图片｜支持文生图 图生图_2097230672099368962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_134

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3｜单人高质量数字人｜音频驱动多图参考 MV_2096969226736193537.json、视频生成/文生视频/MiniMax H3｜批量生素材图片｜支持文生图 图生图_2097230672099368962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `easy float`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `ExtractStoryboards_xuhuan1024` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `SaveAudioAdvanced` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/2 个有
- `ZML_AnyTypeSwitch` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
