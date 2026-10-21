---
name: unknown_workflow_lora_sampler_unet_3
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.5848
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAEEncodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-H3-二采多图参考（4步加速_官方节点版）_2090604828555825154.json, 视频生成/文生视频/H3 LightX2V 二采高清图_文生视频_2087548123051806721.json, 视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json, 视频生成/文生视频/MiniMax H3 多图参考双采短剧视频生成工作流_2104589979459612673.json, 视频生成/文生视频/MiniMax H3超级多合一工作流_2089374116016119810.json, 视频生成/文生视频/MiniMax H3超级多合一工作流（加速rola+二采）_2087353258498158593.json, 视频生成/文生视频/MiniMax+H3超级多合_2086713203135967234.json, 视频生成/文生视频/MiniMax+H3超级多合一工作流-官方版V2_2088289193456922626.json, 视频生成/文生视频/MiniMaxH3官方版超级多合一工作流ENG+ENG_2087111558542479361.json, 视频生成/文生视频/Minimax-H3 多图参考_产品介绍视频_2090089362729033729.json, 视频生成/文生视频/Minimax-H3-4步加速-单图参考（二次采样_官方节点版）_2090043814345007105.json, 视频生成/文生视频/李哈哈自用3_2087402730037014530.json, 视频生成/文生视频/自用测试-超级多合一_2092461754998673409.json, 视频生成/文生视频/🐳【傲雪AIGC】MiniMax+H3短剧双采工作流_2093005569190875138.json, 视频生成/文生视频/🐳【傲雪AIGC】MiniMax+H3短剧双采工作流_2108512240256249857.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_3

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3-二采多图参考（4步加速_官方节点版）_2090604828555825154.json、视频生成/文生视频/H3 LightX2V 二采高清图_文生视频_2087548123051806721.json、视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json、视频生成/文生视频/MiniMax H3 多图参考双采短剧视频生成工作流_2104589979459612673.json、视频生成/文生视频/MiniMax H3超级多合一工作流_2089374116016119810.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 14/15 个有
- `Text` —— 14/15 个有
- `VAEDecodeAudio` —— 12/15 个有
- `GetNode` —— 11/15 个有
- `LoadAudio` —— 11/15 个有
- `SetNode` —— 11/15 个有
- `VHS_LoadVideo` —— 11/15 个有
- `VHS_VideoCombine` —— 11/15 个有
- `Fast Groups Bypasser (rgthree)` —— 10/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/15 个有
- `PT_H3ConcatAVLatent` —— 10/15 个有
- `PreviewImage` —— 10/15 个有
- `easy cleanGpuUsed` —— 9/15 个有
- `ModelAttentionBackend` —— 8/15 个有
- `MiniMaxH3ImageToVideo` —— 7/15 个有
- `孤海注释` —— 7/15 个有
- `LTXVConcatAVLatent` —— 5/15 个有
- `RunningHub Deepcleaner` —— 5/15 个有
- `SaveVideo` —— 5/15 个有
- `CreateVideo` —— 4/15 个有
- `Float` —— 4/15 个有
- `EasyCache` —— 3/15 个有
- `MiniMaxH3AVDecodeT8` —— 3/15 个有
- `RTXVideoSuperResolution` —— 3/15 个有
- `VRAMReserver` —— 3/15 个有
- `easy clearCacheAll` —— 3/15 个有
- `PlaySound|pysssss` —— 2/15 个有
- `MuyeLoadImage` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
