---
name: unknown_workflow_sampler_unet_vae_18
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.797722
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100206617605267458.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100585354809139202.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2101121504195997698.json, 视频生成/图生视频/Minimax H3 - 多参视频生成_2086482284911357953.json, 视频生成/图生视频/Minimax H3 Full2k视频超分_2084940898219151362.json, 视频生成/图生视频/Minimax H3 I2v-首帧参考-横板15秒_2093106411722076162.json, 视频生成/图生视频/Minimax H3 I2v-首帧参考-横板5秒-图生视频_2103293623193399298.json, 视频生成/图生视频/Minimax H3 I2v_尾帧参考_2085634658221510658.json, 视频生成/图生视频/Minimax H3 I2v_尾帧参考_竖屏_2090355202326097921.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧 (加速版，去动态噪点）_2084495129297121281.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_both_2085634176757362689.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_both_竖屏_2090357898231767042.json, 视频生成/图生视频/Minimax H3 I2v_首帧参考_2084900505624600577.json, 视频生成/图生视频/Minimax H3 I2v_首帧参考_竖屏_2090353004041031682.json, 视频生成/图生视频/Minimax H3 图生视频_首尾帧 (加速版，去高动态噪点）_2088505534927433729.json, 视频生成/图生视频/Minimax+H3+I2v_首尾帧+(加速版，去动态噪点）_2089185922914021377.json, 视频生成/图生视频/minimax图出视频_2084274641455112193.json, 视频生成/文生视频/MiniMax-H3全能参考工作流-金水1987_2084528401230159874.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_18

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100206617605267458.json、视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100585354809139202.json、视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2101121504195997698.json、视频生成/图生视频/Minimax H3 - 多参视频生成_2086482284911357953.json、视频生成/图生视频/Minimax H3 Full2k视频超分_2084940898219151362.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
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
- `MiniMaxH3ImageToVideo` —— 16/18 个有
- `LoadImage` —— 12/18 个有
- `PathchSageAttentionKJ` —— 12/18 个有
- `EasyCache` —— 11/18 个有
- `PrimitiveStringMultiline` —— 11/18 个有
- `GetImageSize` —— 10/18 个有
- `ImageScaleToTotalPixels` —— 10/18 个有
- `SDVN Load Image Url` —— 6/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/18 个有
- `ImageScale` —— 3/18 个有
- `JjkText` —— 3/18 个有
- `LayerUtility: TextBox` —— 3/18 个有
- `MiniMaxH3ReferenceToVideo` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `EmptyImage` —— 1/18 个有
- `ExtendIntermediateSigmas` —— 1/18 个有
- `H3SigmaRefiner` —— 1/18 个有
- `LoraLoaderModelOnly` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
