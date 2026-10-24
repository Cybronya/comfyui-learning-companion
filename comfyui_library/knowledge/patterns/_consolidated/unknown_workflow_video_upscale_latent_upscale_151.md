---
name: unknown_workflow_video_upscale_latent_upscale_151
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7225
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, Fast Groups Bypasser (rgthree), GoohaiAnyExists, H3SigmaRefiner, IfInnerExecute, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxH3EasySecondPassConditioning, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, PDIMAGE_LongerSize, PreviewImage, PrimitiveInt, RH_DLSS5Enhance, RandomNoise, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3大全 + 自动高清 VOSR + DLSS_2098255923381882882.json, 视频生成/文生视频/海螺H3！ 多模型合一！ 自动高清 VOSR + DLSS！_2098290326447415298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_151

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3大全 + 自动高清 VOSR + DLSS_2098255923381882882.json、视频生成/文生视频/海螺H3！ 多模型合一！ 自动高清 VOSR + DLSS！_2098290326447415298.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GoohaiAnyExists`
- `H3SigmaRefiner`
- `IfInnerExecute`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3EasySecondPassConditioning`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `PDIMAGE_LongerSize`
- `PreviewImage`
- `PrimitiveInt`
- `RH_DLSS5Enhance`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`
- `忽略多组孤海`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
