---
name: unknown_workflow_video_lora_sampler_261
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8066
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MINIMAX H3 PIKA 双采参考生视频(生成8秒视频 3分18秒)_2117764175161290753.json, 平台全量/Mini H3-加速对比（lightx2v VS pika VS Dmad VS larryvr ）_2117588431751704578.json, 平台全量/Minima H3-视频角色换头+角色替换（双采）_2103695284973953025.json, 平台全量/Minima_H3-视频角色换头+角色替换双采_2109819443865022465.json, 平台全量/Minima_H3-视频角色换头+角色替换双采_2110558547846193153.json, 平台全量/Minimax-H3-Pika加速_2117577169277902850.json, 平台全量/参考图像音频生成口播视频-MiniMaxH3_2119983786036391937.json, 视频生成/图生视频/MiniMax_二采_selflift_急速工作流_2099671590920351746.json, 视频生成/图生视频/MiniMax_二采_selflift_急速工作流自用_2105654345877512193.json, 视频生成/图生视频/绘影-Minimax H3-参考生视频-self-lift双采-1080P-V1.2_2099315406128369665.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_261

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/MINIMAX H3 PIKA 双采参考生视频(生成8秒视频 3分18秒)_2117764175161290753.json、平台全量/Mini H3-加速对比（lightx2v VS pika VS Dmad VS larryvr ）_2117588431751704578.json、平台全量/Minima H3-视频角色换头+角色替换（双采）_2103695284973953025.json、平台全量/Minima_H3-视频角色换头+角色替换双采_2109819443865022465.json、平台全量/Minima_H3-视频角色换头+角色替换双采_2110558547846193153.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 9/10 个有
- `MiniMaxChunkFeedForward` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `MiniMaxLowVRAMAttention` —— 8/10 个有
- `ModelPreviewOverrideKJ` —— 8/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `VHS_LoadVideo` —— 6/10 个有
- `LoadAudio` —— 5/10 个有
- `BlockSparseAttention` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `INTConstant` —— 2/10 个有
- `MiniMaxH3SigmaShift` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `BasicGuider` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `RandomNoise` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
