---
name: unknown_workflow_sampler_vae_24
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.894455
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3融合底模 参考图一键生成环绕运镜视频（刻晴演示）_2103328135499567105.json, 视频生成/图生视频/MiniMax H3音画同步参考工作流_2091481322647805954.json, 视频生成/图生视频/MiniMax+H3+H25  多参8步视频生成_2090783049813413889.json, 视频生成/文生视频/10ErosMax+test4多参考_2087899966655262721.json, 视频生成/文生视频/MiniMax H3 H25 Hybrid 多参8步最优对比测试_2088184113558806529.json, 视频生成/文生视频/MiniMax H3全能参考工作流_2084202154499338242.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086411670364184577.json, 视频生成/文生视频/MiniMax+H3+H25+Hybrid+多参8步最优实现_2088303974402318338.json, 视频生成/文生视频/MiniMax+H3+R2V-02：纯视频参考_2084850819463208962.json, 视频生成/文生视频/MiniMax+H3+R2V-03：人物图＋动作视频_2084850873976578049.json, 视频生成/文生视频/R2V-06：人物图＋动作视频＋新音频_2084910702598381569.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3融合底模 参考图一键生成环绕运镜视频（刻晴演示）_2103328135499567105.json、视频生成/图生视频/MiniMax H3音画同步参考工作流_2091481322647805954.json、视频生成/图生视频/MiniMax+H3+H25  多参8步视频生成_2090783049813413889.json、视频生成/文生视频/10ErosMax+test4多参考_2087899966655262721.json、视频生成/文生视频/MiniMax H3 H25 Hybrid 多参8步最优对比测试_2088184113558806529.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 10/11 个有
- `PathchSageAttentionKJ` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `UNETLoader` —— 9/11 个有
- `GetVideoComponents` —— 8/11 个有
- `LoadVideo` —— 8/11 个有
- `TrimAudioDuration` —— 8/11 个有
- `Video Slice` —— 8/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `MiniMaxH3SigmaShift` —— 5/11 个有
- `EasyCache` —— 4/11 个有
- `ImageResizeKJv2` —— 4/11 个有
- `AddLabel` —— 3/11 个有
- `ImageScaleToTotalPixels` —— 3/11 个有
- `MiniMaxH3HybridLoader` —— 3/11 个有
- `SolAttnPatch` —— 3/11 个有
- `ModelPatchTorchSettings` —— 2/11 个有
- `SpectrumSDXLBatch` —— 2/11 个有
- `H3SLAAttention` —— 1/11 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
