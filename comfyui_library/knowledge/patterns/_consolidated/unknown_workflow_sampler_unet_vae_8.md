---
name: unknown_workflow_sampler_unet_vae_8
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.836381
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [数字人/数字人/图生视频教学工作流_2091871574247952386.json, 数字人/数字人/首尾帧逻辑_2087967441874931713.json, 视频生成/图生视频/(0713)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088910957308370946.json, 视频生成/图生视频/(0715)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088947852180545538.json, 视频生成/图生视频/(10Eros-Max V3)Minimax参考生视频BF16高质量加速版V3_2086185973813174274.json, 视频生成/图生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V3_2086166525018464258.json, 视频生成/图生视频/(10Eros-Max)MinimaxH3开源版 图生视频BF16高质量加速版_2085691291077271554.json, 视频生成/图生视频/(10Eros-Max)Minimax图生视频BF16高质量加速版V2_2085552878504206337.json, 视频生成/图生视频/(10Eros-Max)Minimax图生视频BF16高质量加速版V2_2086152176455475202.json, 视频生成/图生视频/(2倍速！量化加速版)Minimax多参生视频V2_2086292322022682625.json, 视频生成/图生视频/(2倍速！量化加速版)Minimax多参生视频V5_2084169961978814466.json, 视频生成/图生视频/(768P)Minimax多参生视频BF16高质量加速版V2_2085001617933422594.json, 视频生成/图生视频/(768P)Minimax多参生视频BF16高质量加速版V2_2085610026936397825.json, 视频生成/图生视频/(768P)Minimax多参生视频BF16高质量加速版V3_2084908126750461954.json, 视频生成/图生视频/(fl)Minimax-H3官方8步极速工作流-V1正式版_2087281024626683906.json, 视频生成/图生视频/(fl)Minimax-H3官方8步极速工作流-V1正式版（自动反推版）_2087275070858289153.json, 视频生成/图生视频/(ref)Minimax-H3官方8步极速工作流-V1正式版(自动反推版)_2087167230646775810.json, 视频生成/图生视频/(ref)Minimax-H3官方8步极速工作流-V1正式版_2087271938422038530.json, 视频生成/图生视频/MiniMax H3 多参考生视频 8步加速版_2084190473446580225.json, 视频生成/文生视频/Minimax H3-多功能工作流 _自动_手动提示词切换版_2085177847324438530.json, 视频生成/文生视频/minimax H3-FL2VA单模型_int8_高清重绘_9图3视频3音频版 (1)_2089990413913518082.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（数字人/数字人/图生视频教学工作流_2091871574247952386.json、数字人/数字人/首尾帧逻辑_2087967441874931713.json、视频生成/图生视频/(0713)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088910957308370946.json、视频生成/图生视频/(0715)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088947852180545538.json、视频生成/图生视频/(10Eros-Max V3)Minimax参考生视频BF16高质量加速版V3_2086185973813174274.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 21 个 workflow 都包含：
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
- `PrimitiveStringMultiline` —— 19/21 个有
- `MiniMaxH3ReferenceToVideo` —— 15/21 个有
- `MiniMaxH3BlockCacheT8` —— 13/21 个有
- `PathchSageAttentionKJ` —— 13/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/21 个有
- `LoraLoaderModelOnly` —— 8/21 个有
- `LoadAudio` —— 7/21 个有
- `MiniMaxH3ImageToVideo` —— 7/21 个有
- `VHS_LoadVideo` —— 7/21 个有
- `UniBlockSwap` —— 6/21 个有
- `RHLLMChatNode` —— 5/21 个有
- `StringFunction|pysssss` —— 4/21 个有
- `VRAMReserver` —— 4/21 个有
- `easy showAnything` —— 4/21 个有
- `ImageResizeKJv2` —— 3/21 个有
- `ModelAttentionBackend` —— 3/21 个有
- `SolAttnMiniMax` —— 3/21 个有
- `Any Switch (rgthree)` —— 2/21 个有
- `ComfyMiniMaxH3Director` —— 2/21 个有
- `EasyCache` —— 2/21 个有
- `Fast Groups Bypasser (rgthree)` —— 2/21 个有
- `GetImageRangeFromBatch` —— 2/21 个有
- `MiniMaxH3SigmaShift` —— 2/21 个有
- `INTConstant` —— 1/21 个有
- `LoraLoaderBypassModelOnly` —— 1/21 个有
- `PT_H3ConcatAVLatent` —— 1/21 个有
- `PreviewAny` —— 1/21 个有
- `SolAttnPatch` —— 1/21 个有
- `VAEEncode` —— 1/21 个有
- `VAEEncodeAudio` —— 1/21 个有
- `VHS_VideoCombine` —— 1/21 个有
- `easy clearCacheAll` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
