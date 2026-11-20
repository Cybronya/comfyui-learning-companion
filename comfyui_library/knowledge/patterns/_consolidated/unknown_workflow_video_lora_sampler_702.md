---
name: unknown_workflow_video_lora_sampler_702
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8285
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/视频多人物替换加速版 1080p minimax H3_2087436526853648385.json, 视频生成/图生视频/H3二采工作流_2107807033440428033.json, 视频生成/图生视频/MiniMax H3 多图参考+二采+高清放大+去噪点+两倍提速_2090100666210537473.json, 视频生成/图生视频/MiniMax_H3_去油腻_TwoPass_Ref2VA_2114214100938092545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_702

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/视频多人物替换加速版 1080p minimax H3_2087436526853648385.json、视频生成/图生视频/H3二采工作流_2107807033440428033.json、视频生成/图生视频/MiniMax H3 多图参考+二采+高清放大+去噪点+两倍提速_2090100666210537473.json、视频生成/图生视频/MiniMax_H3_去油腻_TwoPass_Ref2VA_2114214100938092545.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 3/4 个有
- `LTXVSeparateAVLatent` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `MinimaxH3LatentUpscaler3D` —— 3/4 个有
- `BasicGuider` —— 2/4 个有
- `CFGGuider` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `DisableNoise` —— 1/4 个有
- `FlashVSRNode` —— 1/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有
- `easy float` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
