---
name: unknown_workflow_sampler_unet_vae_6
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.809304
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3参考生视频，动作迁移_2084614442729426945.json, 视频生成/图生视频/Minimax H3图生视频_2084833087787192322.json, 视频生成/图生视频/Minimax H3多参视频生成_2084926235125305346.json, 视频生成/图生视频/Minimax H3多图参考视频生成+全节点注释_2099072693512531970.json, 视频生成/图生视频/Minimax H3开源版参考图生视频高质量加速版_2086456184978108417.json, 视频生成/图生视频/Minimax H3高质量融合模型10Eros-多参生视频BF16加速_2086859051593457665.json, 视频生成/图生视频/Minimax-H3-R2V 开源版本 多参考生视频_2084285644305682434.json, 视频生成/图生视频/Minimax-H3-单_双图生视频-sage+cache双重提速-平均3分半钟出5秒！_2084572403178500098.json, 视频生成/图生视频/Minimax-H3-单_双图生视频BF16高质量768P-双重加速（T8-cache）_2085387593134469122.json, 视频生成/图生视频/Minimax-H3-多参生视频BF16高质量768P-双重加速（T8-cache）_2085387583219126274.json, 视频生成/图生视频/Minimax-H3-多模态参考生视频-sage+cache双重提速_2084572409679671298.json, 视频生成/图生视频/MinimaxH3 ref2va全能多参工作流_2084512370860318722.json, 视频生成/图生视频/Minimax_H3多图参考视频生成+全节点注释_2099778923717550082.json, 视频生成/图生视频/Minimax_H3多图参考视频生成+全节点注释_2100038725966319618.json, 视频生成/图生视频/Minimax_h3_r2v图生视频_2084277716307767297.json, 视频生成/图生视频/Minimax参考生视频 高质量 加速版_2086430508090744833.json, 视频生成/图生视频/minimaxH3多参考视频工作流_2084285648122499073.json, 视频生成/图生视频/minimax_h3_全能参考（参考视频输入）_2085193849571463169.json, 视频生成/图生视频/加速版Minimax多参生视频BF16高质量-sage+Block Cache (T8)_2085374592817909762.json, 视频生成/图生视频/多种参考生视频-MiniMax_h3_r2v-视频音频图片参考_2084132425894031361.json, 视频生成/图生视频/开源版Minimax-h3 多模态全能参考版_2084936517058912257.json, 视频生成/文生视频/多参生视频-MiniMax_h3_r2v-视频音频图片参考-智能提示词_2084694636374872065.json, 视频生成/文生视频/智能提示词-多参生视频-MiniMax_h3_r2v-视频音频图片参考_2084262166823268354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/Minimax H3参考生视频，动作迁移_2084614442729426945.json、视频生成/图生视频/Minimax H3图生视频_2084833087787192322.json、视频生成/图生视频/Minimax H3多参视频生成_2084926235125305346.json、视频生成/图生视频/Minimax H3多图参考视频生成+全节点注释_2099072693512531970.json、视频生成/图生视频/Minimax H3开源版参考图生视频高质量加速版_2086456184978108417.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 22/23 个有
- `ResolutionSelector` —— 22/23 个有
- `PrimitiveStringMultiline` —— 21/23 个有
- `MiniMaxH3ReferenceToVideo` —— 20/23 个有
- `PathchSageAttentionKJ` —— 15/23 个有
- `LoadAudio` —— 10/23 个有
- `EasyCache` —— 8/23 个有
- `VHS_LoadVideo` —— 8/23 个有
- `MiniMaxH3BlockCacheT8` —— 6/23 个有
- `AudioCrop` —— 5/23 个有
- `ImageScaleToTotalPixels` —— 5/23 个有
- `孤海注释` —— 5/23 个有
- `MiniMaxH3ImageToVideo` —— 3/23 个有
- `PrimitiveInt` —— 3/23 个有
- `easy anythingIndexSwitch` —— 3/23 个有
- `easy showAnything` —— 3/23 个有
- `CR Prompt Text` —— 2/23 个有
- `LoadVideo` —— 2/23 个有
- `RH_LLMAPI_Pro_Node` —— 2/23 个有
- `Any To String (mtb)` —— 1/23 个有
- `CR Text` —— 1/23 个有
- `ImageResizeKJv2` —— 1/23 个有
- `Note Plus (mtb)` —— 1/23 个有
- `PreviewAudio` —— 1/23 个有
- `RH_GetAudioDuration` —— 1/23 个有
- `VHS_VideoInfo` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
