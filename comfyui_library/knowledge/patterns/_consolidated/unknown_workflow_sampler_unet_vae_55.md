---
name: unknown_workflow_sampler_unet_vae_55
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.836727
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/minimax_h3_t2v文生视频_2084177287007784961.json, 视频生成/文生视频/minimax_h3_文生_图生视频_2084261498850988033.json, 视频生成/文生视频/minimax_h3_文生视频4步加速_2084135777386192898.json, 视频生成/文生视频/minimax_h3_文生视频_2084110685591654402.json, 视频生成/文生视频/minimax_h3_文生视频_8步加速_2084159928788410370.json, 视频生成/文生视频/minimax_h3文生视频 图生视频 首尾帧+sage加速_2084126972392857602.json, 视频生成/文生视频/minimax_h3文生视频 图生视频 首尾帧+sage加速_2085982926470213634.json, 视频生成/文生视频/minimax文字出视频_2084271438885904386.json, 视频生成/文生视频/video_minimax_h3_r2v多参考生视频_2084510984789647362.json, 视频生成/文生视频/video_minimax_h3_t2v_2084126777605181442.json, 视频生成/文生视频/video_minimax_h3_t2v_i2v_r2v_rv2v_2091314256494022658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_55

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/minimax_h3_t2v文生视频_2084177287007784961.json、视频生成/文生视频/minimax_h3_文生_图生视频_2084261498850988033.json、视频生成/文生视频/minimax_h3_文生视频4步加速_2084135777386192898.json、视频生成/文生视频/minimax_h3_文生视频_2084110685591654402.json、视频生成/文生视频/minimax_h3_文生视频_8步加速_2084159928788410370.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/11 个有
- `MiniMaxH3ImageToVideo` —— 10/11 个有
- `SaveVideo` —— 10/11 个有
- `LoadImage` —— 6/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/11 个有
- `GetImageSize` —— 4/11 个有
- `ImageScaleToTotalPixels` —— 4/11 个有
- `PathchSageAttentionKJ` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `EasyCache` —— 2/11 个有
- `MiniMaxH3ReferenceToVideo` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `MiniMaxChunkFeedForward` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `VHS_VideoCombine` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
