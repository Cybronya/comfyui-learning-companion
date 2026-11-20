---
name: unknown_workflow_sampler_unet_vae_159
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.867286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2099794040656060418.json, 图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json, 图片生成/图生图/剧情短片丨MiniMax H3丨双图参考·有声视频_2112107687327649793.json, 图片生成/文生图/H3fast-v2全参加速_2110710299581046785.json, 视频生成/图生视频/(0713)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088910957308370946.json, 视频生成/图生视频/(0715)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088947852180545538.json, 视频生成/图生视频/minimax   h3 最强动作迁移_2089285244263424001.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_159

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2099794040656060418.json、图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json、图片生成/图生图/剧情短片丨MiniMax H3丨双图参考·有声视频_2112107687327649793.json、图片生成/文生图/H3fast-v2全参加速_2110710299581046785.json、视频生成/图生视频/(0713)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088910957308370946.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 6/7 个有
- `CreateVideo` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `ModelAttentionBackend` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `SaveVideo` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `LoadAudio` —— 3/7 个有
- `SolAttnMiniMax` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `ComfyMiniMaxH3Director` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `MiniMaxH3BlockCacheT8` —— 2/7 个有
- `MiniMaxH3SigmaShift` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `VHS_VideoCombine` —— 2/7 个有
- `BlockSparseAttention` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `MiniMaxH3AddGuide` —— 1/7 个有
- `ModelPreviewOverrideKJ` —— 1/7 个有
- `PainterVRAM` —— 1/7 个有
- `RTXVideoSuperResolution` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `UniBlockSwapTE` —— 1/7 个有
- `easy positive` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
