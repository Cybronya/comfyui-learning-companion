---
name: unknown_workflow_sampler_vae_48
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.924143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3融合底模 参考图一键生成环绕运镜视频（刻晴演示）_2103328135499567105.json, 视频生成/图生视频/MiniMax H3音画同步参考工作流_2091481322647805954.json, 视频生成/图生视频/MiniMax+H3+H25  多参8步视频生成_2090783049813413889.json, 视频生成/图生视频/MiniMax+H3+H25+Hybrid+多参8步最优实现_2114636999469649922.json, 视频生成/文生视频/10ErosMax+test4多参考_2087899966655262721.json, 视频生成/文生视频/MiniMax H3 H25 Hybrid 多参8步最优对比测试_2088184113558806529.json, 视频生成/文生视频/MiniMax+H3+H25+Hybrid+多参8步最优实现_2088303974402318338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_48

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3融合底模 参考图一键生成环绕运镜视频（刻晴演示）_2103328135499567105.json、视频生成/图生视频/MiniMax H3音画同步参考工作流_2091481322647805954.json、视频生成/图生视频/MiniMax+H3+H25  多参8步视频生成_2090783049813413889.json、视频生成/图生视频/MiniMax+H3+H25+Hybrid+多参8步最优实现_2114636999469649922.json、视频生成/文生视频/10ErosMax+test4多参考_2087899966655262721.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/7 个有
- `MiniMaxH3SigmaShift` —— 6/7 个有
- `PathchSageAttentionKJ` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `TrimAudioDuration` —— 5/7 个有
- `GetVideoComponents` —— 4/7 个有
- `LoadVideo` —— 4/7 个有
- `MiniMaxH3HybridLoader` —— 4/7 个有
- `UNETLoader` —— 4/7 个有
- `Video Slice` —— 4/7 个有
- `AddLabel` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `Anything Everywhere` —— 1/7 个有
- `H3SLAAttention` —— 1/7 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `SpectrumSDXLBatch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
