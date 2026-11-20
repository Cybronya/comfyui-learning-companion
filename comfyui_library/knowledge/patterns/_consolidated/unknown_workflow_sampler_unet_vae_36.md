---
name: unknown_workflow_sampler_unet_vae_36
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.81575
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_全参考ref2va_中文版_2085180698285142017.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100206617605267458.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100585354809139202.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2101121504195997698.json, 视频生成/图生视频/Minimax H3 - 多参视频生成_2086482284911357953.json, 视频生成/图生视频/Minimax H3 Full2k视频超分_2084940898219151362.json, 视频生成/图生视频/Minimax H3 图生视频 高质量加速版_2085666960783794177.json, 视频生成/图生视频/Minimax H3 数字人带货视频_2084925025257353218.json, 视频生成/图生视频/Minimax H3-t2v 多图参考生视频_2084205760405397505.json, 视频生成/图生视频/Minimax H3参考生视频，动作迁移_2084614442729426945.json, 视频生成/图生视频/Minimax H3开源版参考图生视频高质量加速版_2086456184978108417.json, 视频生成/图生视频/Minimax H3高质量融合模型10Eros-多参生视频BF16加速_2086859051593457665.json, 视频生成/图生视频/Minimax-H3-多参生视频BF16高质量768P-双重加速（T8-cache）_2085387583219126274.json, 视频生成/图生视频/Minimax-H3-多参考生成 官流_2095740048577744897.json, 视频生成/图生视频/MinimaxH3参考生成视频工作流_2084154580937564162.json, 视频生成/图生视频/minimax_h3 多参考图+视频参考+sage加速_2084192560171536385.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_36

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_全参考ref2va_中文版_2085180698285142017.json、视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100206617605267458.json、视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100585354809139202.json、视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2101121504195997698.json、视频生成/图生视频/Minimax H3 - 多参视频生成_2086482284911357953.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 13/16 个有
- `MiniMaxH3ReferenceToVideo` —— 11/16 个有
- `MiniMaxH3ImageToVideo` —— 5/16 个有
- `PathchSageAttentionKJ` —— 5/16 个有
- `MiniMaxH3BlockCacheT8` —— 4/16 个有
- `VHS_LoadVideo` —— 3/16 个有
- `ImageScaleToTotalPixels` —— 2/16 个有
- `JjkText` —— 2/16 个有
- `EmptyImage` —— 1/16 个有
- `ImageUpscaleWithModel` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `UpscaleModelLoader` —— 1/16 个有
- `VHS_VideoInfo` —— 1/16 个有
- `VideoInfoLoaded` —— 1/16 个有
- `easy showAnything` —— 1/16 个有
- `孤海注释` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
