---
name: unknown_workflow_sampler_unet_vae_4
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.862962
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Minimax_H3_图生视频_2088655826771861505.json, 数字人/数字人/海螺H3(minimax H3)图生视频（图生视频&首尾帧）加速开源版_2084181324272852993.json, 视频生成/图生视频/Minimax H3 -图生视频工作流_2084907599123804162.json, 视频生成/图生视频/Minimax H3 I2V图生视频_首尾帧_2084485077328814081.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧_2084148989418622977.json, 视频生成/图生视频/Minimax H3 单图视频_2084186710258315266.json, 视频生成/图生视频/Minimax H3 图生视频_2084260606722527233.json, 视频生成/图生视频/Minimax H3 图生视频_2084647272570245121.json, 视频生成/图生视频/Minimax H3 首尾帧图生视频_2084915506569633793.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084176815941308418.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084449411379326978.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084464401641467905.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084552805813149698.json, 视频生成/图生视频/Minimax H3视频模型图生视频_2084132239176192002.json, 视频生成/图生视频/Minimax-H3+图生视频-官流_2095734200711340034.json, 视频生成/图生视频/Minimax-H3-T2V 开源版本 图生视频_2084262714964275202.json, 视频生成/图生视频/Minimax-h3图生视频版_2084511817468039169.json, 视频生成/图生视频/Minimax_H3_图生视频_2084193867901005825.json, 视频生成/图生视频/Minimax_h3_超级加速图生视频_2084162376542281729.json, 视频生成/图生视频/Minimax_h3_超级加速首尾帧图生视频_2084842867264155649.json, 视频生成/图生视频/【2】图生视频（首帧图生视频）video_minimax_h3_i2v_2087199971459289090.json, 视频生成/图生视频/【3】图生视频（尾帧图生视频）video_minimax_h3_i2v_2087202435805827073.json, 视频生成/图生视频/【4】图生视频（首尾帧模式）video_minimax_h3_i2v_2087205422599073793.json, 视频生成/图生视频/地表最强Minimax-h3图生视频版_2084422222730588162.json, 视频生成/图生视频/地表最强Minimax-h3完美首尾帧版_2084469809009483778.json, 视频生成/文生视频/地表最强开源视频！Minimax-h3 文生丨图生视频版 26-08-03_2084186070467567618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/Minimax_H3_图生视频_2088655826771861505.json、数字人/数字人/海螺H3(minimax H3)图生视频（图生视频&首尾帧）加速开源版_2084181324272852993.json、视频生成/图生视频/Minimax H3 -图生视频工作流_2084907599123804162.json、视频生成/图生视频/Minimax H3 I2V图生视频_首尾帧_2084485077328814081.json、视频生成/图生视频/Minimax H3 I2v_首尾帧_2084148989418622977.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 26 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 24/26 个有
- `ResolutionSelector` —— 22/26 个有
- `ComfyMathExpression` —— 21/26 个有
- `PrimitiveFloat` —— 21/26 个有
- `GetImageSize` —— 20/26 个有
- `CreateVideo` —— 18/26 个有
- `SaveVideo` —— 18/26 个有
- `PathchSageAttentionKJ` —— 12/26 个有
- `CR Text` —— 10/26 个有
- `EasyCache` —— 8/26 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/26 个有
- `VHS_VideoCombine` —— 8/26 个有
- `PainterVRAM` —— 6/26 个有
- `INTConstant` —— 5/26 个有
- `Label (rgthree)` —— 5/26 个有
- `LoraLoaderModelOnly` —— 5/26 个有
- `PrimitiveStringMultiline` —— 5/26 个有
- `SimpleMath+` —— 5/26 个有
- `ImageCrop+` —— 4/26 个有
- `孤海注释` —— 4/26 个有
- `LayerUtility: PurgeVRAM V2` —— 3/26 个有
- `Note Plus (mtb)` —— 3/26 个有
- `ImageResizeKJv2` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
