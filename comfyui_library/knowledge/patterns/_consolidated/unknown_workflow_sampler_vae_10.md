---
name: unknown_workflow_sampler_vae_10
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.887182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json, 图片生成/文生图/MiniMax H3 FL2VA开源版-人物参考_2084833557930926081.json, 图片生成/文生图/MiniMax H3 R2V-01：多图参考_2084544634998575105.json, 图片生成/文生图/MiniMax H3 R2V-04：人物图＋独立音频_2084544649284378626.json, 图片生成/文生图/MiniMax H3 R2V-05：人物图＋视频＋视频配套音轨_2084608990058733569.json, 图片生成/文生图/MiniMax H3 加速版-文生视频_2084834194160701441.json, 图片生成/文生图/MiniMax H3 尾帧图生视频_2084544642758037506.json, 数字人/数字人/MiniMax H3 R2V-8步 comfyorg_2087907718676959234.json, 数字人/数字人/MiniMax+H3参考生视频6倍加速80GB满配版_2086471377510559745.json, 视频生成/图生视频/MiniMax H3 多图生视频+音频+视频接入_2090198237796982786.json, 视频生成/图生视频/MiniMax H3 极速首尾帧图生视频_2087539459008057345.json, 视频生成/图生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086446949431078914.json, 视频生成/图生视频/MiniMax H3参考生视频6倍加速48GB高配版_2087554038731722753.json, 视频生成/图生视频/MiniMax H3参考生视频6倍加速48GB高配版_2087554175612841985.json, 视频生成/图生视频/MiniMax+H3+H25  多参8步视频生成_2090783049813413889.json, 视频生成/文生视频/10ErosMax+test4多参考_2087899966655262721.json, 视频生成/文生视频/MiniMax H3 H25 Hybrid 多参8步最优对比测试_2088184113558806529.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086411670364184577.json, 视频生成/文生视频/MiniMax+H3+H25+Hybrid+多参8步最优实现_2088303974402318338.json, 视频生成/文生视频/MiniMax+H3+R2V-02：纯视频参考_2084850819463208962.json, 视频生成/文生视频/MiniMax+H3+R2V-03：人物图＋动作视频_2084850873976578049.json, 视频生成/文生视频/R2V-06：人物图＋动作视频＋新音频_2084910702598381569.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_10

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json、图片生成/文生图/MiniMax H3 FL2VA开源版-人物参考_2084833557930926081.json、图片生成/文生图/MiniMax H3 R2V-01：多图参考_2084544634998575105.json、图片生成/文生图/MiniMax H3 R2V-04：人物图＋独立音频_2084544649284378626.json、图片生成/文生图/MiniMax H3 R2V-05：人物图＋视频＋视频配套音轨_2084608990058733569.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 22 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 21/22 个有
- `ResolutionSelector` —— 21/22 个有
- `MiniMaxH3ReferenceToVideo` —— 20/22 个有
- `UNETLoader` —— 20/22 个有
- `PathchSageAttentionKJ` —— 17/22 个有
- `LoadAudio` —— 16/22 个有
- `EasyCache` —— 13/22 个有
- `ImageResizeKJv2` —— 13/22 个有
- `LoraLoaderModelOnly` —— 11/22 个有
- `TrimAudioDuration` —— 11/22 个有
- `GetVideoComponents` —— 10/22 个有
- `LoadVideo` —— 10/22 个有
- `Video Slice` —— 9/22 个有
- `SolAttnPatch` —— 8/22 个有
- `MiniMaxH3SigmaShift` —— 4/22 个有
- `AddLabel` —— 3/22 个有
- `ImageScaleToTotalPixels` —— 3/22 个有
- `MiniMaxH3HybridLoader` —— 3/22 个有
- `JjkText` —— 2/22 个有
- `MiniMaxH3ImageToVideo` —— 2/22 个有
- `LoadVideoNode` —— 1/22 个有
- `VHS_LoadVideo` —— 1/22 个有
- `孤海注释` —— 1/22 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
