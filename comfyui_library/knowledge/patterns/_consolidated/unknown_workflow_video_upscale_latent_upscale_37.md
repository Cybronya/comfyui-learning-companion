---
name: unknown_workflow_video_upscale_latent_upscale_37
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6082
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 多参考双采｜5秒一致性版_2098723223021113346.json, 视频生成/图生视频/H3 角色替换_2085882691152605185.json, 视频生成/图生视频/H3_动作迁移 + 深度视频参考_2090034137221648385.json, 视频生成/图生视频/H3短剧生成新模型_2102294100425920514.json, 视频生成/图生视频/MiniMax H3-图生视频_2103135562264834050.json, 视频生成/图生视频/MiniMax H3-多参考生视频 快速高质量_2098739556991455233.json, 视频生成/图生视频/MiniMax H3-多参考生视频-720p_2094616194417516546.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2094397865706737666.json, 视频生成/图生视频/MiniMax H3-多参考生视频-自用_2099876679551377409.json, 视频生成/文生视频/视频生成API_2099703467815292929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_37

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/H3 多参考双采｜5秒一致性版_2098723223021113346.json、视频生成/图生视频/H3 角色替换_2085882691152605185.json、视频生成/图生视频/H3_动作迁移 + 深度视频参考_2090034137221648385.json、视频生成/图生视频/H3短剧生成新模型_2102294100425920514.json、视频生成/图生视频/MiniMax H3-图生视频_2103135562264834050.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `SplitSigmas` —— 9/10 个有
- `Text` —— 9/10 个有
- `VHS_LoadVideo` —— 9/10 个有
- `easy float` —— 8/10 个有
- `GetNode` —— 7/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `LoadAudio` —— 6/10 个有
- `忽略多组孤海` —— 6/10 个有
- `ModelAttentionBackend` —— 4/10 个有
- `Lora Loader Stack (rgthree)` —— 3/10 个有
- `SolAttnMiniMax` —— 3/10 个有
- `llama_cpp_instruct_adv` —— 2/10 个有
- `llama_cpp_model_loader` —— 2/10 个有
- `llama_cpp_parameters` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `FlashVSRNode` —— 1/10 个有
- `H3SigmaRefiner` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `MiniMaxLowVRAMAttention` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `Sleep` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
