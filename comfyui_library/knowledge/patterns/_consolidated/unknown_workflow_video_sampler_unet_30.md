---
name: unknown_workflow_video_sampler_unet_30
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.433727
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json, 视频生成/图生视频/H3极速测试工作流_2109473161694760961.json, 视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json, 视频生成/图生视频/MiniMax H3  15s全参_2084269888650174465.json, 视频生成/图生视频/MiniMax H3 DSW全能多参1280分辨率加速工作流_2092879864431988738.json, 视频生成/图生视频/MiniMax H3 全能多参1280分辨率3_4Harness专用_2094567538721116161.json, 视频生成/图生视频/MiniMax H3 全能多参1280分辨率加速工作流_2085980820623413250.json, 视频生成/图生视频/MiniMax H3 全能多参DSW工作流Harness专用_2095550051505491970.json, 视频生成/图生视频/MiniMax-H3-FastVideo多参极速版_2108479598177636354.json, 视频生成/图生视频/MiniMaxH38高动态加速流_2091799612456783873.json, 视频生成/文生视频/MiniMax H3官方工作流_多参考生成视频_2090004683493560321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_30

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json、视频生成/图生视频/H3极速测试工作流_2109473161694760961.json、视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json、视频生成/图生视频/MiniMax H3  15s全参_2084269888650174465.json、视频生成/图生视频/MiniMax H3 DSW全能多参1280分辨率加速工作流_2092879864431988738.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/11 个有
- `VAEDecode` —— 10/11 个有
- `VAEDecodeAudio` —— 10/11 个有
- `LoadAudio` —— 7/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `PrimitiveFloat` —— 7/11 个有
- `Text` —— 7/11 个有
- `Label (rgthree)` —— 6/11 个有
- `VHS_LoadVideo` —— 6/11 个有
- `Fast Groups Bypasser (rgthree)` —— 5/11 个有
- `ModelAttentionBackend` —— 5/11 个有
- `SigmasGraph` —— 4/11 个有
- `BlockSparseAttention` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `easy float` —— 3/11 个有
- `LoadVideo` —— 2/11 个有
- `FloatConstant` —— 1/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `MiniMaxH3AVDecodeT8` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
