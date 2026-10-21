---
name: unknown_workflow_sampler_unet_vae_22
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.82525
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/电商产品展示 图片参考生视频 minimax h3_2085356615661875201.json, 视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2085731924324216833.json, 视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2087164469729386498.json, 视频生成/文生视频/MiniMax H3  文生视频工作流_2084912279681851394.json, 视频生成/文生视频/MiniMax H3 文生视频_2084544656423088130.json, 视频生成/文生视频/MiniMax H3 首尾帧图生视频_2084850865038520322.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086459494866968577.json, 视频生成/文生视频/MiniMax H3图生视频6倍加速24GB通用版_2086411696771522561.json, 视频生成/文生视频/MiniMax H3图生视频6倍加速48GB高配版_2086411679377743873.json, 视频生成/文生视频/MiniMax H3图生视频6倍加速80GB满配版_2086411651821170689.json, 视频生成/文生视频/MiniMax+H3+多图参考+官方提示词模板+提速40%无劣化+真人短剧剧情演绎_2095730598064250881.json, 视频生成/文生视频/MiniMax+H3+首帧图生视频_2084850825154875394.json, 视频生成/文生视频/Minimax H3多参视频生成+全节点注释_2084873538615472129.json, 视频生成/文生视频/MinimaxH3参考8步生成视频工作流_2087040392687611906.json, 视频生成/文生视频/video_minimax_h3_r2v_fast_2094242970009694209.json, 视频生成/文生视频/【V-zion】Minimax-H3【文生视频_首尾帧_首帧_尾帧】附加提示词模板_2084613485291462658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_22

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/电商产品展示 图片参考生视频 minimax h3_2085356615661875201.json、视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2085731924324216833.json、视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2087164469729386498.json、视频生成/文生视频/MiniMax H3  文生视频工作流_2084912279681851394.json、视频生成/文生视频/MiniMax H3 文生视频_2084544656423088130.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 15/16 个有
- `EasyCache` —— 14/16 个有
- `LoadImage` —— 14/16 个有
- `CreateVideo` —— 11/16 个有
- `PrimitiveStringMultiline` —— 11/16 个有
- `SaveVideo` —— 11/16 个有
- `MiniMaxH3ImageToVideo` —— 10/16 个有
- `MiniMaxH3ReferenceToVideo` —— 7/16 个有
- `SolAttnPatch` —— 7/16 个有
- `ImageResizeKJv2` —— 6/16 个有
- `VHS_VideoCombine` —— 6/16 个有
- `LoraLoaderModelOnly` —— 5/16 个有
- `JjkText` —— 4/16 个有
- `LoadAudio` —— 3/16 个有
- `PreviewAny` —— 3/16 个有
- `ImageScaleToTotalPixels` —— 2/16 个有
- `RH_Translator` —— 2/16 个有
- `DF_Float` —— 1/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `PainterVRAM` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
