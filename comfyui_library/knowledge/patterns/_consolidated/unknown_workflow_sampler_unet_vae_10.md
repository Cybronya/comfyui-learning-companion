---
name: unknown_workflow_sampler_unet_vae_10
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8425
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Minimax_H3_图生视频_2088655826771861505.json, 数字人/数字人/海螺H3(minimax H3)图生视频（图生视频&首尾帧）加速开源版_2084181324272852993.json, 视频生成/图生视频/Minimax H3 -图生视频工作流_2084907599123804162.json, 视频生成/图生视频/Minimax H3 I2V图生视频_首尾帧_2084485077328814081.json, 视频生成/图生视频/Minimax H3 I2v_尾帧参考_2085634658221510658.json, 视频生成/图生视频/Minimax H3 I2v_尾帧参考_竖屏_2090355202326097921.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_2084148989418622977.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_both_2085634176757362689.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_both_竖屏_2090357898231767042.json, 视频生成/图生视频/Minimax H3 I2v_首帧参考_2084900505624600577.json, 视频生成/图生视频/Minimax H3 I2v_首帧参考_竖屏_2090353004041031682.json, 视频生成/图生视频/Minimax H3 单图视频_2084186710258315266.json, 视频生成/图生视频/Minimax H3 图生视频_2084260606722527233.json, 视频生成/图生视频/Minimax H3 图生视频_2084647272570245121.json, 视频生成/图生视频/Minimax H3 首尾帧图生视频_2084915506569633793.json, 视频生成/图生视频/Minimax H3视频模型图生视频_2084132239176192002.json, 视频生成/图生视频/Minimax-H3+图生视频-官流_2095734200711340034.json, 视频生成/图生视频/Minimax-H3-单_双图生视频-sage+cache双重提速-平均3分半钟出5秒！_2084572403178500098.json, 视频生成/图生视频/MinimaxH3图生视频&首尾帧 量化加速版_2084545071873093633.json, 视频生成/图生视频/Minimax_H3_图生视频_2084193867901005825.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Minimax_H3_图生视频_2088655826771861505.json、数字人/数字人/海螺H3(minimax H3)图生视频（图生视频&首尾帧）加速开源版_2084181324272852993.json、视频生成/图生视频/Minimax H3 -图生视频工作流_2084907599123804162.json、视频生成/图生视频/Minimax H3 I2V图生视频_首尾帧_2084485077328814081.json、视频生成/图生视频/Minimax H3 I2v_尾帧参考_2085634658221510658.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 18/20 个有
- `ComfyMathExpression` —— 17/20 个有
- `GetImageSize` —— 17/20 个有
- `PathchSageAttentionKJ` —— 17/20 个有
- `PrimitiveFloat` —— 17/20 个有
- `ResolutionSelector` —— 15/20 个有
- `CreateVideo` —— 14/20 个有
- `LoadImage` —— 14/20 个有
- `SaveVideo` —— 14/20 个有
- `EasyCache` —— 12/20 个有
- `PrimitiveStringMultiline` —— 8/20 个有
- `SDVN Load Image Url` —— 6/20 个有
- `VHS_VideoCombine` —— 6/20 个有
- `CR Text` —— 4/20 个有
- `PainterVRAM` —— 4/20 个有
- `INTConstant` —— 3/20 个有
- `SimpleMath+` —— 3/20 个有
- `CR Prompt Text` —— 2/20 个有
- `ImageResizeKJv2` —— 2/20 个有
- `Label (rgthree)` —— 2/20 个有
- `AnyBooleanSwitch` —— 1/20 个有
- `Float` —— 1/20 个有
- `PrimitiveBoolean` —— 1/20 个有
- `RTXVideoSuperResolution` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
