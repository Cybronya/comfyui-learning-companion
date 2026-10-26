---
name: unknown_workflow_sampler_unet_vae_2
type: Unknown Workflow
frequency: 30
level: moderate
coverage: 0.836933
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Minimax_H3_图生视频_2088655826771861505.json, 数字人/数字人/海螺H3(minimax H3)图生视频（图生视频&首尾帧）加速开源版_2084181324272852993.json, 视频生成/图生视频/Minimax H3 -图生视频工作流_2084907599123804162.json, 视频生成/图生视频/Minimax H3 I2V图生视频_首尾帧_2084485077328814081.json, 视频生成/图生视频/Minimax H3 I2v_尾帧参考_2085634658221510658.json, 视频生成/图生视频/Minimax H3 I2v_尾帧参考_竖屏_2090355202326097921.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_2084148989418622977.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_both_2085634176757362689.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_both_竖屏_2090357898231767042.json, 视频生成/图生视频/Minimax H3 I2v_首帧参考_2084900505624600577.json, 视频生成/图生视频/Minimax H3 I2v_首帧参考_竖屏_2090353004041031682.json, 视频生成/图生视频/Minimax H3 单图视频_2084186710258315266.json, 视频生成/图生视频/Minimax H3 图生视频_2084647272570245121.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084176815941308418.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084449411379326978.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084464401641467905.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084552805813149698.json, 视频生成/图生视频/Minimax H3图生视频_2084833087787192322.json, 视频生成/图生视频/Minimax H3视频模型图生视频_2084132239176192002.json, 视频生成/图生视频/Minimax H3首尾帧生视频-In8加速版_2084502270833676289.json, 视频生成/图生视频/Minimax-H3+图生视频-官流_2095734200711340034.json, 视频生成/图生视频/Minimax-H3-T2V 开源版本 图生视频_2084262714964275202.json, 视频生成/图生视频/Minimax-H3-多模态参考生视频-sage+cache双重提速_2084572409679671298.json, 视频生成/图生视频/Minimax_H3_图生视频_2084193867901005825.json, 视频生成/图生视频/Minimax_h3_r2v图生视频_2084277716307767297.json, 视频生成/图生视频/Minimax_h3_超级加速图生视频_2084162376542281729.json, 视频生成/图生视频/Minimax_h3_超级加速首尾帧图生视频_2084842867264155649.json, 视频生成/图生视频/【2】图生视频（首帧图生视频）video_minimax_h3_i2v_2087199971459289090.json, 视频生成/图生视频/【3】图生视频（尾帧图生视频）video_minimax_h3_i2v_2087202435805827073.json, 视频生成/图生视频/【4】图生视频（首尾帧模式）video_minimax_h3_i2v_2087205422599073793.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/文生图/Minimax_H3_图生视频_2088655826771861505.json、数字人/数字人/海螺H3(minimax H3)图生视频（图生视频&首尾帧）加速开源版_2084181324272852993.json、视频生成/图生视频/Minimax H3 -图生视频工作流_2084907599123804162.json、视频生成/图生视频/Minimax H3 I2V图生视频_首尾帧_2084485077328814081.json、视频生成/图生视频/Minimax H3 I2v_尾帧参考_2085634658221510658.json…）

- **类型**：Unknown Workflow
- **样本数**：30
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 30 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 28/30 个有
- `ResolutionSelector` —— 27/30 个有
- `ImageScaleToTotalPixels` —— 26/30 个有
- `ComfyMathExpression` —— 25/30 个有
- `GetImageSize` —— 25/30 个有
- `PrimitiveFloat` —— 25/30 个有
- `LoadImage` —— 24/30 个有
- `CreateVideo` —— 23/30 个有
- `SaveVideo` —— 23/30 个有
- `EasyCache` —— 15/30 个有
- `PathchSageAttentionKJ` —— 15/30 个有
- `PrimitiveStringMultiline` —— 15/30 个有
- `VHS_VideoCombine` —— 7/30 个有
- `CR Text` —— 6/30 个有
- `PainterVRAM` —— 6/30 个有
- `SDVN Load Image Url` —— 6/30 个有
- `INTConstant` —— 5/30 个有
- `Label (rgthree)` —— 5/30 个有
- `LoraLoaderModelOnly` —— 5/30 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/30 个有
- `SimpleMath+` —— 5/30 个有
- `LayerUtility: PurgeVRAM V2` —— 3/30 个有
- `MiniMaxH3ReferenceToVideo` —— 2/30 个有
- `RHHiddenNodes` —— 1/30 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
