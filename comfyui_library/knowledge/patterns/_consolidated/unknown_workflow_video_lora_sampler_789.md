---
name: unknown_workflow_video_lora_sampler_789
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.789
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ExtractStoryboards_xuhuan1024, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveBoolean, PrimitiveFloat, ResolutionSelector, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, VRAM_Debug, ZML_AnyTypeSwitch, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, 孤海注释, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3｜批量生高清素材图片｜Self Lift双采加速_2100983955179786241.json, 视频生成/文生视频/MiniMax H3｜批量生素材图片｜支持文生图 图生图_2097230672099368962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_789

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/MiniMax H3｜批量生高清素材图片｜Self Lift双采加速_2100983955179786241.json、视频生成/文生视频/MiniMax H3｜批量生素材图片｜支持文生图 图生图_2097230672099368962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ExtractStoryboards_xuhuan1024`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `ZML_AnyTypeSwitch`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LTXVConcatAVLatent` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `MinimaxH3LatentUpscaler3D` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `SelfLiftAvatarH3Sampler` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
