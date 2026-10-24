---
name: unknown_workflow_sampler_unet_vae_24
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.818474
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100206617605267458.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100585354809139202.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2101121504195997698.json, 视频生成/图生视频/Minimax H3 - 多参视频生成_2086482284911357953.json, 视频生成/图生视频/Minimax H3 Full2k视频超分_2084940898219151362.json, 视频生成/图生视频/Minimax H3 I2v-首帧参考-横板15秒_2093106411722076162.json, 视频生成/图生视频/Minimax H3 I2v-首帧参考-横板5秒-图生视频_2103293623193399298.json, 视频生成/图生视频/Minimax H3 I2v_尾帧参考_2085634658221510658.json, 视频生成/图生视频/Minimax H3 I2v_尾帧参考_竖屏_2090355202326097921.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_both_2085634176757362689.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_both_竖屏_2090357898231767042.json, 视频生成/图生视频/Minimax H3 I2v_首帧参考_2084900505624600577.json, 视频生成/图生视频/Minimax H3 I2v_首帧参考_竖屏_2090353004041031682.json, 视频生成/图生视频/Minimax H3 图生视频 高质量加速版_2085666960783794177.json, 视频生成/图生视频/Minimax H3 多参生视频 量化加速版_2084444583718641665.json, 视频生成/图生视频/Minimax H3 多参生视频_2084365914140659713.json, 视频生成/图生视频/MinimaxI2V_2084500141607841794.json, 视频生成/图生视频/minimax h3多图参考视频工作流（int8底模+8步提速方案）_2087813787285020674.json, 视频生成/图生视频/video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_24

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100206617605267458.json、视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2100585354809139202.json、视频生成/图生视频/MiniMax_H3_图生视频_首尾帧控制_原生音频_两张图变一段电影_2101121504195997698.json、视频生成/图生视频/Minimax H3 - 多参视频生成_2086482284911357953.json、视频生成/图生视频/Minimax H3 Full2k视频超分_2084940898219151362.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 19 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo` —— 15/19 个有
- `PrimitiveStringMultiline` —— 14/19 个有
- `LoadImage` —— 13/19 个有
- `PathchSageAttentionKJ` —— 13/19 个有
- `EasyCache` —— 12/19 个有
- `GetImageSize` —— 7/19 个有
- `ImageScaleToTotalPixels` —— 7/19 个有
- `SDVN Load Image Url` —— 6/19 个有
- `JjkText` —— 5/19 个有
- `MiniMaxH3ReferenceToVideo` —— 4/19 个有
- `LoadAudio` —— 2/19 个有
- `AudioCrop` —— 1/19 个有
- `EmptyImage` —— 1/19 个有
- `LoadVideo` —— 1/19 个有
- `LoraLoaderModelOnly` —— 1/19 个有
- `MiniMaxH3BlockCacheT8` —— 1/19 个有
- `PreviewImage` —— 1/19 个有
- `孤海注释` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
