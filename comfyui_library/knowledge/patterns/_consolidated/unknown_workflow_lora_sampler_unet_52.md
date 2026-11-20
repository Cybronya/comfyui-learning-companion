---
name: unknown_workflow_lora_sampler_unet_52
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.632182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-H3-二采多图参考（4步加速_官方节点版）_2090604828555825154.json, 视频生成/文生视频/H3 LightX2V 二采高清图_文生视频_2087548123051806721.json, 视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json, 视频生成/文生视频/MiniMax H3 多图参考双采短剧视频生成工作流_2104589979459612673.json, 视频生成/文生视频/MiniMax H3超级多合一工作流_2089374116016119810.json, 视频生成/文生视频/Minimax-H3 多图参考_产品介绍视频_2090089362729033729.json, 视频生成/文生视频/Minimax-H3-4步加速-单图参考（二次采样_官方节点版）_2090043814345007105.json, 视频生成/文生视频/心然·寻源-Minimax H3 多模态参考生视频（双采加速版）_2087734113288679426.json, 视频生成/文生视频/自用测试-超级多合一_2092461754998673409.json, 视频生成/文生视频/🐳【傲雪AIGC】MiniMax+H3短剧双采工作流_2093005569190875138.json, 视频生成/文生视频/🐳【傲雪AIGC】MiniMax+H3短剧双采工作流_2108512240256249857.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_52

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3-二采多图参考（4步加速_官方节点版）_2090604828555825154.json、视频生成/文生视频/H3 LightX2V 二采高清图_文生视频_2087548123051806721.json、视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json、视频生成/文生视频/MiniMax H3 多图参考双采短剧视频生成工作流_2104589979459612673.json、视频生成/文生视频/MiniMax H3超级多合一工作流_2089374116016119810.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/11 个有
- `MiniMaxH3ReferenceToVideo` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `ModelAttentionBackend` —— 9/11 个有
- `Text` —— 9/11 个有
- `GetNode` —— 7/11 个有
- `LoadAudio` —— 7/11 个有
- `SetNode` —— 7/11 个有
- `VHS_LoadVideo` —— 7/11 个有
- `VHS_VideoCombine` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 6/11 个有
- `PT_H3ConcatAVLatent` —— 6/11 个有
- `LTXVConcatAVLatent` —— 5/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `SaveVideo` —— 5/11 个有
- `CreateVideo` —— 4/11 个有
- `Float` —— 4/11 个有
- `EasyCache` —— 3/11 个有
- `MiniMaxH3ImageToVideo` —— 3/11 个有
- `RTXVideoSuperResolution` —— 3/11 个有
- `VRAMReserver` —— 3/11 个有
- `easy clearCacheAll` —— 3/11 个有
- `PlaySound|pysssss` —— 2/11 个有
- `孤海注释` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
