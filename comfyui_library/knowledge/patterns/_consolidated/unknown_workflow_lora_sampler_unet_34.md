---
name: unknown_workflow_lora_sampler_unet_34
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.676786
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, KSamplerSelect, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Minimax文生视频T2V_2114255990785921025.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-单图生成视频-工作流_2093578786934710274.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-尾帧视频-工作流_2093527771631931393.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧生成视频-工作流-v2版本_2092500053683433474.json, 视频生成/图生视频/MiniMax H3：图生视频_2095788026013249538.json, 视频生成/图生视频/Minimax H3 单张参考图生视频标准版_2102224374689517569.json, 视频生成/图生视频/Minimax H3 首尾帧图生视频标准版_2102237236300435457.json, 视频生成/图生视频/Minimax_H3_单张参考图生视频标准版_2102317605854990338.json, 视频生成/图生视频/Minimax_H3_首尾帧图生视频标准版_2104053564233568257.json, 视频生成/图生视频/Minimax图生视频I2V_2099170083997315073.json, 视频生成/图生视频/Minmax多参考生成视频R2V_2084668436755599362.json, 视频生成/图生视频/minimax_h3_i2v_accel_2096897727664836609.json, 视频生成/图生视频/minimax_h3_i2v官方首尾帧_2114194060029292545.json, 视频生成/文生视频/Minimax文生视频T2V_2098449873984122882.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_34

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Minimax文生视频T2V_2114255990785921025.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-单图生成视频-工作流_2093578786934710274.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-尾帧视频-工作流_2093527771631931393.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧生成视频-工作流-v2版本_2092500053683433474.json、视频生成/图生视频/MiniMax H3：图生视频_2095788026013249538.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 13/14 个有
- `MiniMaxH3ImageToVideo` —— 13/14 个有
- `GetImageSize` —— 11/14 个有
- `ImageScaleToTotalPixels` —— 8/14 个有
- `ResolutionSelector` —— 7/14 个有
- `AudioCrop` —— 4/14 个有
- `GetNode` —— 4/14 个有
- `LoadAudio` —— 4/14 个有
- `SetNode` —— 4/14 个有
- `easy minimaxH3AudioLock` —— 4/14 个有
- `CR Text` —— 3/14 个有
- `ImageScale` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `EmptyImage` —— 2/14 个有
- `LTXVSeparateAVLatent` —— 1/14 个有
- `MiniMaxH3ReferenceToVideo` —— 1/14 个有
- `MiniMaxH3SaveLatent` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `SaveLatent` —— 1/14 个有
- `VHS_LoadVideo` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
