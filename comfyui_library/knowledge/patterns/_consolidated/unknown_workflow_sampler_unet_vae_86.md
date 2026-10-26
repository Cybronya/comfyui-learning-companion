---
name: unknown_workflow_sampler_unet_vae_86
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.879545
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 开源版 多图参考生视频 加速版_2086403186247688193.json, 视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速24GB通用版_2086411688710066177.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086411670364184577.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086459494866968577.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速80GB满配版_2086411609148313601.json, 视频生成/文生视频/MiniMax+H3+R2V-02：纯视频参考_2084850819463208962.json, 视频生成/文生视频/MiniMax+H3+R2V-03：人物图＋动作视频_2084850873976578049.json, 视频生成/文生视频/Minimax H3 多模态--综合应用流_2085249742157729793.json, 视频生成/文生视频/R2V-06：人物图＋动作视频＋新音频_2084910702598381569.json, 视频生成/文生视频/【5】全能多模态--多参视频生成（真正平替seedance）--ref2va模型_2087209584539820034.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_86

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 开源版 多图参考生视频 加速版_2086403186247688193.json、视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json、视频生成/文生视频/MiniMax H3参考生视频6倍加速24GB通用版_2086411688710066177.json、视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086411670364184577.json、视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086459494866968577.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `CreateVideo` —— 9/11 个有
- `LoadAudio` —— 9/11 个有
- `SaveVideo` —— 9/11 个有
- `GetVideoComponents` —— 8/11 个有
- `ImageResizeKJv2` —— 8/11 个有
- `LoadVideo` —— 8/11 个有
- `PathchSageAttentionKJ` —— 8/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `TrimAudioDuration` —— 4/11 个有
- `Video Slice` —— 4/11 个有
- `SolAttnPatch` —— 3/11 个有
- `Label (rgthree)` —— 2/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `VHS_VideoCombine` —— 2/11 个有
- `DF_Int_to_Float` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
