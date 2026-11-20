---
name: unknown_workflow_sampler_unet_vae_42
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.878235
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, EasyCache, KSamplerSelect, LoadImage, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【开源】MiniMax_H3 单图编辑_2086008079639998465.json, 图片生成/文生图/MiniMax H3 R2V-01：多图参考_2084544634998575105.json, 图片生成/文生图/MiniMax H3 R2V-04：人物图＋独立音频_2084544649284378626.json, 图片生成/文生图/MiniMax H3 R2V-05：人物图＋视频＋视频配套音轨_2084608990058733569.json, 图片生成/文生图/MiniMax H3 尾帧图生视频_2084544642758037506.json, 平台全量/AI Video Studio PR插件VIP专用视频一键消除_2090341509672554498.json, 平台全量/MiniMax+H3+R2V-03：人物图＋动作视频_2113630864541315074.json, 平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用一句话特效_2090357874504589313.json, 平台全量/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用首尾帧转场_2089331713825660929.json, 视频生成/图生视频/MiniMax H3 极速首尾帧图生视频_2087539459008057345.json, 视频生成/图生视频/MiniMax+H3+首帧图生视频_2113618062388846594.json, 视频生成/图生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用多图参考生成视频_2089356847248666626.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086411670364184577.json, 视频生成/文生视频/MiniMax+H3+R2V-02：纯视频参考_2084850819463208962.json, 视频生成/文生视频/MiniMax+H3+R2V-03：人物图＋动作视频_2084850873976578049.json, 视频生成/文生视频/R2V-06：人物图＋动作视频＋新音频_2084910702598381569.json, 视频生成/文生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用图生视频、文生视频_2089147200021553154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_42

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/【开源】MiniMax_H3 单图编辑_2086008079639998465.json、图片生成/文生图/MiniMax H3 R2V-01：多图参考_2084544634998575105.json、图片生成/文生图/MiniMax H3 R2V-04：人物图＋独立音频_2084544649284378626.json、图片生成/文生图/MiniMax H3 R2V-05：人物图＋视频＋视频配套音轨_2084608990058733569.json、图片生成/文生图/MiniMax H3 尾帧图生视频_2084544642758037506.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `EasyCache`
- `KSamplerSelect`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 16/17 个有
- `ResolutionSelector` —— 16/17 个有
- `SaveVideo` —— 16/17 个有
- `VAEDecodeAudio` —— 16/17 个有
- `MiniMaxH3ReferenceToVideo` —— 14/17 个有
- `PrimitiveStringMultiline` —— 12/17 个有
- `ImageResizeKJv2` —— 11/17 个有
- `SolAttnPatch` —— 11/17 个有
- `GetVideoComponents` —— 8/17 个有
- `LoadAudio` —— 8/17 个有
- `LoadVideo` —— 8/17 个有
- `TrimAudioDuration` —— 8/17 个有
- `Video Slice` —— 6/17 个有
- `CR Prompt Text` —— 5/17 个有
- `ImageUpscaleWithModel` —— 5/17 个有
- `UpscaleModelLoader` —— 5/17 个有
- `MiniMaxH3ImageToVideo` —— 3/17 个有
- `Image Comparer (rgthree)` —— 1/17 个有
- `LoraLoaderModelOnly` —— 1/17 个有
- `PrimitiveInt` —— 1/17 个有
- `SaveImage` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
