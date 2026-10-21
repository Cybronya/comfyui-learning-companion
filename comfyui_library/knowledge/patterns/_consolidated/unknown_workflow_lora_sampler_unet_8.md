---
name: unknown_workflow_lora_sampler_unet_8
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.878833
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100787039317876737.json, 视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100884384172830721.json, 视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100928696604520449.json, 视频生成/图生视频/MiniMax H3双采参考生视频-低显存版本_2104091652603338754.json, 视频生成/图生视频/Minimax H3 参考生视频 ｜不油、不崩脸、真实感强｜Hybird V1 + Sla 4步加速_2091946357614534657.json, 视频生成/图生视频/尾帧生视频_2099041242926632962.json, 视频生成/图生视频/银河系小王参考生视频-自用_2094346923468738561.json, 视频生成/图生视频/银河系小王图生视频-自用_2094273549614800897.json, 视频生成/图生视频/首帧生视频_2099038054504812545.json, 视频生成/图生视频/（Minimax H3）Remix版文戏工作流_2096586271111081985.json, 视频生成/文生视频/(最佳动态)MiniMax H3参考生视频（dasiwa的模型和加速lora）_2093873787371606017.json, 视频生成/文生视频/10Eros Beta5 + FL2VA_Ref2VA小脸去油二采精修流_2101605881900261377.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_8

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100787039317876737.json、视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100884384172830721.json、视频生成/图生视频/(低显存-时间分块+前馈分块)MiniMax H3双采参考生视频_2100928696604520449.json、视频生成/图生视频/MiniMax H3双采参考生视频-低显存版本_2104091652603338754.json、视频生成/图生视频/Minimax H3 参考生视频 ｜不油、不崩脸、真实感强｜Hybird V1 + Sla 4步加速_2091946357614534657.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
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
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 11/12 个有
- `PrimitiveFloat` —— 8/12 个有
- `VHS_VideoCombine` —— 8/12 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 7/12 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 7/12 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 7/12 个有
- `CreateVideo` —— 5/12 个有
- `SaveVideo` —— 5/12 个有
- `easy cleanGpuUsed` —— 5/12 个有
- `JWFloat` —— 4/12 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 4/12 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 4/12 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 4/12 个有
- `PreviewAny` —— 4/12 个有
- `LoadAudio` —— 3/12 个有
- `AudioCrop` —— 1/12 个有
- `ConcatTextOfUtils` —— 1/12 个有
- `GetVideoComponents` —— 1/12 个有
- `LoadVideo` —— 1/12 个有
- `LoraLoaderModelOnly` —— 1/12 个有
- `Video Slice` —— 1/12 个有
- `easy clearCacheAll` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
