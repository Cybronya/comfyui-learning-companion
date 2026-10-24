---
name: unknown_workflow_sampler_unet_vae_15
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.818905
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3参考生视频，动作迁移_2084614442729426945.json, 视频生成/图生视频/Minimax H3图生视频_2084833087787192322.json, 视频生成/图生视频/Minimax H3多参视频生成_2084926235125305346.json, 视频生成/图生视频/Minimax H3多图参考视频生成+全节点注释_2099072693512531970.json, 视频生成/图生视频/Minimax H3开源版参考图生视频高质量加速版_2086456184978108417.json, 视频生成/图生视频/Minimax H3首尾帧生视频-In8加速版_2084502270833676289.json, 视频生成/图生视频/Minimax H3高质量融合模型10Eros-多参生视频BF16加速_2086859051593457665.json, 视频生成/图生视频/Minimax-H3-R2V 开源版本 多参考生视频_2084285644305682434.json, 视频生成/图生视频/Minimax-H3-单_双图生视频BF16高质量768P-双重加速（T8-cache）_2085387593134469122.json, 视频生成/图生视频/Minimax-H3-多参生视频BF16高质量768P-双重加速（T8-cache）_2085387583219126274.json, 视频生成/图生视频/Minimax-H3-多模态参考生视频-sage+cache双重提速_2084572409679671298.json, 视频生成/图生视频/MinimaxH3参考生成视频工作流_2084154580937564162.json, 视频生成/图生视频/Minimax_H3多图参考视频生成+全节点注释_2099778923717550082.json, 视频生成/图生视频/Minimax_H3多图参考视频生成+全节点注释_2100038725966319618.json, 视频生成/图生视频/Minimax_h3_r2v图生视频_2084277716307767297.json, 视频生成/图生视频/minimaxH3多参考视频工作流_2084285648122499073.json, 视频生成/图生视频/minimax_h3 多参考图+视频参考+sage加速_2084192560171536385.json, 视频生成/图生视频/加速版Minimax多参生视频BF16高质量-sage+Block Cache (T8)_2085374592817909762.json, 视频生成/图生视频/多种参考生视频-MiniMax_h3_r2v-视频音频图片参考_2084132425894031361.json, 视频生成/图生视频/超级融合模型-高质量(10Eros-Max)Minimax BF16参考生视频-加速版-TEST3版_2086762633667108866.json, 视频生成/文生视频/MiniMax H3 真实电影质感｜全能参考_2099697903618056193.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_15

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/Minimax H3参考生视频，动作迁移_2084614442729426945.json、视频生成/图生视频/Minimax H3图生视频_2084833087787192322.json、视频生成/图生视频/Minimax H3多参视频生成_2084926235125305346.json、视频生成/图生视频/Minimax H3多图参考视频生成+全节点注释_2099072693512531970.json、视频生成/图生视频/Minimax H3开源版参考图生视频高质量加速版_2086456184978108417.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 20/21 个有
- `PrimitiveStringMultiline` —— 20/21 个有
- `MiniMaxH3ReferenceToVideo` —— 18/21 个有
- `PathchSageAttentionKJ` —— 15/21 个有
- `LoadAudio` —— 8/21 个有
- `EasyCache` —— 7/21 个有
- `MiniMaxH3BlockCacheT8` —— 7/21 个有
- `VHS_LoadVideo` —— 7/21 个有
- `ImageScaleToTotalPixels` —— 4/21 个有
- `孤海注释` —— 4/21 个有
- `MiniMaxH3ImageToVideo` —— 3/21 个有
- `easy anythingIndexSwitch` —— 2/21 个有
- `easy showAnything` —— 2/21 个有
- `AudioCrop` —— 1/21 个有
- `CR Prompt Text` —— 1/21 个有
- `DisableNoise` —— 1/21 个有
- `H3SigmaRefiner` —— 1/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/21 个有
- `LoraLoaderModelOnly` —— 1/21 个有
- `PrimitiveInt` —— 1/21 个有
- `RHHiddenNodes` —— 1/21 个有
- `SplitSigmas` —— 1/21 个有
- `VHS_VideoInfo` —— 1/21 个有
- `VideoInfoLoaded` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
