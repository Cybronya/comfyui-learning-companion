---
name: unknown_workflow_video_upscale_latent_upscale_127
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.785333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, Fast Groups Bypasser (rgthree), H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxH3EasySecondPassConditioning, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3大全 + 自动高清 VOSR + DLSS_2098255923381882882.json, 视频生成/文生视频/最强去油全模式精简流+独立双采样 MINIMAXH3_2094672915202662401.json, 视频生成/文生视频/海螺H3！ 多模型合一！ 自动高清 VOSR + DLSS！_2098290326447415298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_127

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3大全 + 自动高清 VOSR + DLSS_2098255923381882882.json、视频生成/文生视频/最强去油全模式精简流+独立双采样 MINIMAXH3_2094672915202662401.json、视频生成/文生视频/海螺H3！ 多模型合一！ 自动高清 VOSR + DLSS！_2098290326447415298.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3EasySecondPassConditioning`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GoohaiAnyExists` —— 2/3 个有
- `IfInnerExecute` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PDIMAGE_LongerSize` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `RH_DLSS5Enhance` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `VOSR2ModelLoader` —— 2/3 个有
- `VOSR2Upscale` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `忽略多组孤海` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
