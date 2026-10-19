---
name: unknown_workflow_sampler_unet_vae_19
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.839471
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [数字人/数字人/海螺H3(minimax H3)图生视频（图生视频&首尾帧）加速开源版_2084181324272852993.json, 视频生成/图生视频/Minimax H3 -图生视频工作流_2084907599123804162.json, 视频生成/图生视频/Minimax H3 单图视频_2084186710258315266.json, 视频生成/图生视频/Minimax H3 图生视频_2084260606722527233.json, 视频生成/图生视频/Minimax H3 图生视频_2084647272570245121.json, 视频生成/图生视频/Minimax H3 首尾帧图生视频_2084915506569633793.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084176815941308418.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084449411379326978.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084464401641467905.json, 视频生成/图生视频/Minimax H3-i2v 官方版图生视频_2084552805813149698.json, 视频生成/图生视频/Minimax H3视频模型图生视频_2084132239176192002.json, 视频生成/图生视频/Minimax-H3+图生视频-官流_2095734200711340034.json, 视频生成/图生视频/Minimax-H3-T2V 开源版本 图生视频_2084262714964275202.json, 视频生成/图生视频/MinimaxH3视频人物替换_2095672328909836290.json, 视频生成/图生视频/MinimaxH3视频人物替换_2109569066229919746.json, 视频生成/图生视频/Minimax_H3_图生视频_2084193867901005825.json, 视频生成/图生视频/雷霆运镜Minimax H3 最强视频参考，动作迁移，人物替换_2090101579029504002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_19

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（数字人/数字人/海螺H3(minimax H3)图生视频（图生视频&首尾帧）加速开源版_2084181324272852993.json、视频生成/图生视频/Minimax H3 -图生视频工作流_2084907599123804162.json、视频生成/图生视频/Minimax H3 单图视频_2084186710258315266.json、视频生成/图生视频/Minimax H3 图生视频_2084260606722527233.json、视频生成/图生视频/Minimax H3 图生视频_2084647272570245121.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 15/17 个有
- `GetImageSize` —— 15/17 个有
- `PrimitiveFloat` —— 15/17 个有
- `MiniMaxH3ImageToVideo` —— 14/17 个有
- `CreateVideo` —— 12/17 个有
- `ImageScaleToTotalPixels` —— 12/17 个有
- `SaveVideo` —— 12/17 个有
- `ResolutionSelector` —— 10/17 个有
- `PathchSageAttentionKJ` —— 9/17 个有
- `VHS_VideoCombine` —— 8/17 个有
- `PrimitiveStringMultiline` —— 5/17 个有
- `SimpleMath+` —— 5/17 个有
- `ImageResizeKJv2` —— 4/17 个有
- `CR Text` —— 3/17 个有
- `ImageConcanate` —— 3/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/17 个有
- `MiniMaxH3ReferenceToVideo` —— 3/17 个有
- `PainterVRAM` —— 3/17 个有
- `PrimitiveInt` —— 3/17 个有
- `VHS_LoadVideo` —— 3/17 个有
- `VHS_VideoInfo` —— 3/17 个有
- `EasyCache` —— 2/17 个有
- `INTConstant` —— 2/17 个有
- `Label (rgthree)` —— 2/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
