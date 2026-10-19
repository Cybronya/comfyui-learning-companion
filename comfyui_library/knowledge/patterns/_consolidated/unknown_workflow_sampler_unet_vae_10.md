---
name: unknown_workflow_sampler_unet_vae_10
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.81381
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100787039317876737.json, 视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100884384172830721.json, 视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100928696604520449.json, 视频生成/图生视频/MiniMax H3双采参考生视频-低显存版本_2104091652603338754.json, 视频生成/图生视频/Minimax H3 参考生视频 ｜不油、不崩脸、真实感强｜Hybird V1 + Sla 4步加速_2091946357614534657.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2090687227016863745.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091039164530778113.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2094625265921126401.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090690174513664001.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090981502527037441.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090280306870931457.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090767546290106369.json, 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2093200891477319681.json, 视频生成/图生视频/Minimax H3横版文生视频Lantent Upscaler2_2091776496015863809.json, 视频生成/图生视频/Minimax+H3+Zs05+双采+加速+Lantent+Upscaler参考生视频_2092271863945846785.json, 视频生成/图生视频/【MiniMax H3】多图参考视频-T8双采样加速_2104070548694331394.json, 视频生成/图生视频/【MiniMax H3】首帧生视频-T8双采样加速_2099383411554209793.json, 视频生成/图生视频/人像口播丨MiniMax H3丨参考生音视频_2099787278662070274.json, 视频生成/图生视频/双参战斗版 MiniMax H3开源 参考生视频_2095814447255347202.json, 视频生成/图生视频/尾帧生视频_2099041242926632962.json, 视频生成/图生视频/电影质感 _ 文武双修 H3 多参双采高清V3_2099337469803192321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100787039317876737.json、视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100884384172830721.json、视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100928696604520449.json、视频生成/图生视频/MiniMax H3双采参考生视频-低显存版本_2104091652603338754.json、视频生成/图生视频/Minimax H3 参考生视频 ｜不油、不崩脸、真实感强｜Hybird V1 + Sla 4步加速_2091946357614534657.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 20/21 个有
- `LoraLoaderBypassModelOnly` —— 19/21 个有
- `PrimitiveFloat` —— 17/21 个有
- `VHS_VideoCombine` —— 17/21 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 16/21 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 16/21 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 16/21 个有
- `easy cleanGpuUsed` —— 6/21 个有
- `PreviewAny` —— 5/21 个有
- `CreateVideo` —— 4/21 个有
- `JWFloat` —— 4/21 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 4/21 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 4/21 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 4/21 个有
- `SaveVideo` —— 4/21 个有
- `GetNode` —— 3/21 个有
- `SetNode` —— 3/21 个有
- `LoraLoaderModelOnly` —— 2/21 个有
- `ConcatTextOfUtils` —— 1/21 个有
- `Float` —— 1/21 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/21 个有
- `RH_Translator` —— 1/21 个有
- `VantageImagesOrNone` —— 1/21 个有
- `easy anythingIndexSwitch` —— 1/21 个有
- `easy clearCacheAll` —— 1/21 个有
- `easy saveText` —— 1/21 个有
- `easy showAnything` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
